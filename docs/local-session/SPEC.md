# Workbench: site specification

> **What it is:** a private learning site for Joshua and his brother. Quests, recall checks and
> games (the quest board, grown up), with sign-in, progress saved online, open questions to work
> through, and a writing page whose entries are committed to each person's own GitHub repo.
>
> **Who it's for:** two users. Not a product. Keep it small, cheap ($0 a month) and boring to run.
>
> Written by Claude (Anthropic), 2026-10-10. The local session builds from this; if this spec and
> mark-one's `EVIDENCE.md` disagree, **EVIDENCE.md wins**.

---

## Principles
1. **The repo is the record; the site is the pen.** Anything that belongs in mark-one's record
   (study notes, build logs, recall results) is **committed to GitHub**, in the format
   `EVIDENCE.md` already defines. The database holds only working state (progress, schedules,
   drafts) and a copy of what was sent.
2. **Contemporaneous by construction.** The server stamps every entry with today's date in
   Singapore time. There is no date field to edit, so an entry can't be backdated. Committed
   entries are never edited; a correction is a new entry (`EVIDENCE.md`: *"Nothing is rewritten
   after the fact"*).
3. **Each person writes only to their own repo.** Which repo a user writes to is stored on the
   server against their account and never sent from the browser.
4. **The site never writes words for anyone.** No AI-generated text goes into an entry. (Red line 1
   of mark-one; the brother's notes deserve the same.)
5. **No build step.** Plain HTML, CSS and ES modules, so there's nothing to break and nothing to
   update.

---

## Stack (all free tiers)
| Part | Choice | Why |
|---|---|---|
| Hosting | **Cloudflare Pages**, serving `public/` as static files | Free, fast in Singapore, custom domain later in one step |
| Sign-in + database | **Supabase** (new personal org, Singapore region): email + password auth, Postgres with row-level security | Free tier covers two users many times over |
| Writing to GitHub | One **Supabase Edge Function**, `commit-entry`, holding the two fine-grained tokens as secrets | Tokens never reach the browser |
| Client library | `@supabase/supabase-js` v2, loaded as an ES module from jsDelivr, **pinned to an exact version** | No bundler needed |

---

## Files
```
workbench/
  README.md                  what it is, how to run it, "Built by Claude (Anthropic) for Joshua and his brother"
  public/
    index.html               app shell: sign-in view + nav (Today · Tracks · Games · Questions · Write · Brother*)
    styles.css               the board's look (PCB green, copper, gold); light text on dark, phone-first
    app.js                   router, session handling, rendering
    content/joshua.js        Joshua's tracks, recall items, seed questions (see § Content)
    content/brother.js       the brother's tracks (ported from the quest board)
    games/*.js               one module per game, ported from bench-apprentice-rev-b.html
    config.js                Supabase URL + anon key (public by design; RLS protects the data)
  supabase/
    migrations/0001_init.sql the schema below
    functions/commit-entry/index.ts
  docs/DECISIONS.md          copied from RUNBOOK.md's decisions section
```
\* The *Brother* page shows only for the `owner` role (Joshua's mentor view).

---

## Database
```sql
-- Who's who. One row per user, created by hand in B4 (sign-ups are off).
create table profiles (
  id uuid primary key references auth.users on delete cascade,
  display_name text not null,
  role text not null check (role in ('owner', 'learner')),
  repo text not null,              -- 'joshluicz/mark-one' or '<brother>/<notes repo>'; server-side only
  token_secret text not null       -- name of the Supabase secret holding this user's GitHub token
);

-- A quest or curriculum item ticked off.
create table progress (
  user_id uuid references auth.users on delete cascade,
  item_id text not null,
  done_at timestamptz not null default now(),
  primary key (user_id, item_id)
);

-- Spaced recall: games and RETENTION.md items. Intervals 1, 3, 7, 14, 30, 90 days.
create table recall (
  user_id uuid references auth.users on delete cascade,
  item_id text not null,
  step int not null default 0,
  due date not null,
  last_result text check (last_result in ('clean', 'shaky', 'fail')),
  last_check date,
  primary key (user_id, item_id)
);

-- Every game played, for the progress view.
create table game_runs (
  id bigint generated always as identity primary key,
  user_id uuid references auth.users on delete cascade,
  game text not null,
  score int not null,
  lives_left int not null,
  won boolean not null,
  played_at timestamptz not null default now()
);

-- Things that need working out (mark-one's open ⬜ items, "What I didn't get", self-check questions).
create table questions (
  id bigint generated always as identity primary key,
  user_id uuid references auth.users on delete cascade,
  text text not null,
  source text,                      -- e.g. 'study/nand2tetris.md 2026-10-04'
  status text not null default 'open' check (status in ('open', 'answered')),
  answer text,
  answered_at timestamptz
);

-- What was written on the Write page, and where it went.
create table entries (
  id bigint generated always as identity primary key,
  user_id uuid references auth.users on delete cascade,
  kind text not null check (kind in ('study', 'buildlog', 'recall', 'answer', 'note')),
  payload jsonb not null,           -- the form fields, exactly as typed
  entry_date date not null,         -- set by the server, Asia/Singapore
  status text not null default 'draft' check (status in ('draft', 'committed', 'failed')),
  commit_url text,
  error text,
  created_at timestamptz not null default now()
);
```
**Row-level security, on every table:**
- Each user can select, insert, update and delete **their own rows** (`user_id = auth.uid()`).
- `profiles`: each user can read their own row; **no client writes**. `repo` and `token_secret`
  are read only by the edge function (service role). Expose `display_name` and `role` to the client
  through a view.
- **Mentor view:** a user whose role is `owner` can **select** (never write) the brother's
  `progress`, `recall`, `game_runs` and `questions`. ⛔ Not `entries`: the brother's writing is his.
  (Change this only if both of them agree.)
- `entries.status`, `commit_url` and `error` are written only by the edge function.

---

## The `commit-entry` function
`POST` with the user's session token and `{ entry_id }`. It:
1. Verifies the session; loads the entry (must belong to the caller and be a `draft`).
2. Loads the caller's profile with the service role, so `repo` and the token come from the server.
3. Builds the file change for `kind` (table below), with today's date in Asia/Singapore.
4. Writes through the GitHub Contents API (`GET` for the current file and its `sha`, then `PUT`).
   Two-file changes (a build log plus its index line) are two sequential commits.
5. Marks the entry `committed` with the commit URL, or `failed` with the error. A failed entry can
   be retried; it's never lost.

**Commit messages:** `<kind>: <title>` and a trailer line `Written on Workbench by <display name>`.

### What each kind writes
| Kind | Joshua (mark-one) | Brother (his notes repo) |
|---|---|---|
| **study** | Appends a dated section to `study/<source>.md` in `study/README.md`'s format (What I learned · What I didn't get · Want to test on the bench), ending *Written by Joshua on Workbench, YYYY-MM-DD.* New source → also a row in `curriculum/SOURCES.md` | Appends to `notes/<source>.md`, same format |
| **buildlog** | New file `projects/bench-to-flight/log/YYYY-MM-DD-<session>-<slug>.md` following `logs/TEMPLATE.md` field for field (including **What failed** and the Brother/Claude attribution lines), plus its row in `BUILD-LOG.md` and an updated total hours. The form makes **Duration**, **Hazard** and **What failed** required, and rounds hours down | Not offered (his builds come later, in his repo) |
| **recall** | Updates that item's row in `curriculum/RETENTION.md`'s recall log (Last check · Result · Next due). Result is his own ✅ / 🟡 / ❌ | Recall lives only in his database |
| **answer** | Appends to `study/questions.md`: the question, its source, his answer, the date. If the question came from a study note, also appends `> Resolved (YYYY-MM-DD): see study/questions.md` under it | Appends to `notes/questions.md` |
| **note** | A free reflection: `journal/YYYY-MM-DD.md` (append if the day's file exists) | `journal/YYYY-MM-DD.md` |

**Two new record types for mark-one:** `study/questions.md` and `journal/`. Add both to the table in
`EVIDENCE.md` § Where each record lives, in the same commit that ships the function.

⛔ Nothing about the brother is ever written to mark-one. If Joshua's build log credits his brother,
it says "my brother" as the template does, as typed by Joshua.

---

## Pages
- **Sign in:** email + password. No sign-up link.
- **Today:** recall due (games and RETENTION items), next quest per track, open-question count,
  streak, XP and rank. The first thing each person sees.
- **Tracks:** levels and quests, as on the board, with Done-when lines and links into the
  illustrated guides on GitHub.
- **Games:** every board game (Safety Check, Resistor Rush, Cap Code, Ohm's Law Blitz, Breadboard
  Detective, Series or Parallel?, Gate Guesser, Name That Gate, Bit Flipper), playable any time.
  Results feed `recall` and `game_runs`.
- **Questions:** open questions with a box to answer. Answering creates an `answer` entry.
- **Write:** choose *Study note · Build log · Reflection* (Joshua) or *Study note · Reflection*
  (brother). The form follows the template. Draft autosaves to the database. **Send to GitHub**
  commits it and shows the commit link.
- **Brother** (owner only): his rank, streak, recall due and recent games. No access to his writing.

---

## Content
### Joshua (`content/joshua.js`), from mark-one as of 2026-10-10
- **Bench to Flight, Stage 0:** S0.1–S0.11 as quests, each linking to its guide and using its
  "How you know you're done" as the Done-when.
- **Study:** Nand2Tetris Part I (projects 1–6; currently at unit 1.3) · CS50P (problem sets 0–9;
  sets 0–1 done, set 2 started) · MIT OCW Single Variable Calculus (resume by the gap protocol:
  unit problems cold, restart at the first unit he can't do; no unit list, to avoid guessing it).
- **Recall items:** exactly the rows of `curriculum/RETENTION.md`'s recall log at build time (today:
  XOR from its truth table; Python; integration by parts). Recall checks are done **on paper**; the
  site shows the task, then asks for his honest ✅ / 🟡 / ❌.
- **Seed questions:** De Morgan's law, and the distributive law (`study/nand2tetris.md`, 10-04) ·
  do 1% resistors use the same number of colour bands? (`STATE.md`) · rule on the RETENTION keep
  list · "physics 6.0001": which course did you mean? (`RETENTION.md`) · the Stage 0 self-check
  questions, each tagged with its session.

### Brother (`content/brother.js`)
Port the board's tracks, levels, quests and XP from `bench-apprentice-rev-b.html` as they are.
Progress already on his phone moves across with the board's **backup code**: the site gets an
"Import from the quest board" box that reads the `BA1:` code once.

---

## Acceptance (B8): tick every box on a phone
☐ Sign-up is impossible; both accounts sign in · ☐ Joshua's study note appears in
`mark-one/study/` with today's date and the Workbench footer · ☐ the brother's note appears in **his**
repo and **not** in mark-one · ☐ a build-log entry can't be sent without Duration, Hazard and What
failed, and lands with its index row and correct hour total · ☐ a recall result updates the right
RETENTION row · ☐ the brother's account can't read Joshua's entries, and Joshua's mentor view can't
read the brother's entries (test with the database's API, not just the UI) · ☐ the GitHub tokens
appear nowhere in the browser's network tab or page source · ☐ a game win schedules its recall ·
☐ the board's backup code imports correctly · ☐ every page works at phone width.
