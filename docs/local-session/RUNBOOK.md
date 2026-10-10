# Local session runbook: Workbench site + YouTube setup

> **What this is:** everything needed for the session on Joshua's computer where Claude builds the
> **Workbench** site, plus the YouTube setup around it. Part A is Joshua's to do **before** the
> session (about 45 minutes, mostly sign-ups). Part B is what Claude and Joshua do together.
> The site's full design is in [`SPEC.md`](SPEC.md).
>
> Written by Claude (Anthropic), 2026-10-10, from that day's decisions (listed at the bottom).

**To start the session:** make a folder for the two repos, open Claude Code in it, and say:
> *Clone joshluicz/mark-one and joshluicz/workbench into this folder, read
> mark-one/docs/local-session/RUNBOOK.md and SPEC.md, then run Part B with me, step by step.*

---

## Part A: before the session (Joshua)

### A1. Decide the channel name ⬜
Pick the YouTube channel name and handle (the `@name`). Check the handle is free on YouTube and,
if you might want a matching site address later, that the domain is free too. Nothing else in this
runbook depends on the name except A2 and B9, so it's fine to settle it last.

### A2. Create the shared Google account
This account owns the **YouTube channel only**. Everything technical (GitHub, Supabase, Cloudflare)
stays on your personal accounts, so nothing important is shared by accident.
1. Create a new Google account, named after the channel.
2. Turn on **2-step verification** straight away, with your phone as the second step.
3. Store the password in a password manager. Decide now who else knows it (ruled: it's shared, so
   your brother may; that's your call).
4. Don't create the channel yet. That's B9, once the name is final.

⚠️ **Your brother on camera.** He's a regular guest, so before the first upload: he agrees, and
because the channel is public, your parents know and agree too. Decide together what's off-limits
(full name, school, uniform, house exterior, anything readable on screen).

### A3. Supabase (sign-in and database): new personal organisation
1. Go to supabase.com and sign in with your **personal** account (not Renvae's).
2. Create a **new organisation** in your own name, on the **Free** plan.
3. Don't create a project yet; Claude does that in B3 so the settings are right.

Free-plan note: a free project **pauses after about a week with no activity**. Opening the site
wakes it up, but the first load after a pause can take a minute.

### A4. Cloudflare (hosting): free account
Sign up at cloudflare.com with your personal email. That's all; the site is connected in B7.

### A5. Create two empty GitHub repositories
On github.com (the cloud session couldn't create repositories for you):
1. **`workbench`** under your account. **Private**, no README, no licence (Claude pushes the first
   commit).
2. Your brother, signed in to **his** GitHub account: a repository for his notes (suggested name
   `bench-notes`). **Private**, tick "Add a README". This is "his own repo" from the 3 Oct ruling.
   He adds you as a collaborator (Settings → Collaborators) so you can help him there.

### A6. Two GitHub access tokens (so the site can save notes into the repos)
The site writes your reflections into GitHub on your behalf, so it needs a key. Use
**fine-grained** tokens: each one can touch only the repositories you pick.

**Yours** (github.com → Settings → Developer settings → Personal access tokens → Fine-grained →
Generate):
- Name: `workbench-mark-one`. Expiry: 1 year.
- Repository access: **Only select repositories** → `mark-one`.
- Permissions → Repository → **Contents: Read and write**. Nothing else.
- Copy the token somewhere safe for B5. ⛔ Never paste it into a chat or commit it.

**Your brother's** (signed in as him, same steps): name `workbench-notes`, only his notes repo,
Contents: Read and write.

> Why two tokens: a fine-grained token can only reach repositories owned by the account that made
> it, and his notes live in his account. It also means the site *can't* write his notes into your
> public repo, or yours into his.

### A7. Install on your computer
- **Git**, **Node.js 20 or later**, and **Claude Code**.
- **GitHub CLI** (`gh`), then run `gh auth login`.
- Nothing else; Claude installs the Supabase and Cloudflare command-line tools inside the project.

### A8. Have these ready when the session starts
☐ channel name · ☐ the two tokens · ☐ your brother's GitHub username and his notes repo name ·
☐ the two email addresses you'll each sign in to the site with.

---

## Part B: in the session (Claude and Joshua)

Each step lists what "done" looks like, so the session can stop at any step and resume later.

| # | Step | Done when |
|---|---|---|
| B1 | Clone `mark-one` and `workbench`; read this runbook, `SPEC.md` and `bench-apprentice-rev-b.html` (the current board, whose games get ported) | Both repos on disk |
| B2 | Scaffold the site in `workbench` exactly as `SPEC.md` § Files lays it out; credit Claude in its README | `npm run dev` shows the sign-in page locally |
| B3 | Create the Supabase project in the **new personal org** (region: Singapore). Apply the migration from `SPEC.md` § Database. **Turn off public sign-ups** | Tables and row-level security exist; sign-ups off |
| B4 | Create the two users (Joshua = `owner`, brother = `learner`) and their profile rows, with each one's repo | Both of you can sign in locally |
| B5 | Deploy the `commit-entry` edge function; store the two tokens as Supabase secrets (Joshua pastes them into the terminal prompt, never into chat) | A test study note from Joshua lands in `mark-one/study/` |
| B6 | Seed the content (`SPEC.md` § Content): both people's tracks, recall items from `curriculum/RETENTION.md`, open questions | Today page shows real items for each of you |
| B7 | Connect `workbench` to **Cloudflare Pages**: no build step, output folder `public/` | Site live on a free `*.pages.dev` address |
| B8 | Acceptance test (`SPEC.md` § Acceptance) on a phone, signed in as each person | Every box ticked |
| B9 | Create the YouTube channel on the shared Google account with the chosen name and handle; put the handle in mark-one's `STATE.md` | Channel exists, nothing uploaded yet |
| B10 | Commit, push, update `STATE.md` (site URL, what's done, what's next) | Pushed |

**Later, not in this session:** pointing one of your existing domains at the site (one DNS record
in Cloudflare), the channel's banner and first video.

---

## Decisions this rests on (2026-10-10, Joshua)
- **Address:** free `*.pages.dev` first; your own domain once the site has proven itself.
- **Reflections:** each person's writing goes to **their own repo**. Yours → `mark-one` (public:
  study notes and build logs, in your words). Your brother's → his own private notes repo.
  ⛔ Nothing about him goes into `mark-one`.
- **Builder:** Claude builds the site, credited in its README. It's a learning tool for the two of
  you, not a project for the application, so your hours stay on the bench.
- **Accounts:** Supabase under a **new personal organisation**, not Renvae's. GitHub under your
  personal account. A **shared Google account** for YouTube only.
- **Brother's role:** apprentice who knows the plan and brings ideas, credited (`../../CLAUDE.md`).
