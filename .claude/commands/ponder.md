---
description: "Triage a probing research question — answer from the record, file an issue, or scaffold a program"
arguments:
  - name: question
    description: "The research question to ponder"
    required: true
---

You are triaging a probing research question from the experimenter. The
question is: **$ARGUMENTS**

Your job is to route it down exactly one of three paths — answer it from the
repository's record, convert it into an issue in an existing program, or
(rarely) scaffold a new program — and to do so without ever freelancing
physics. Every gate in this repository exists to keep unverified claims out of
the record; a conversational answer passes no gate, so the discipline here is
absolute: **answers may only assemble what the repo already establishes, with
rigor labels carried along. Anything beyond the artifacts is speculation and
must be fenced as such.**

## Step 1: Gather the record

In parallel:

1. Read every `programs/*/README.md` (including scope statements and the "In
   plain English" abstracts) and every `programs/*/OBJECTIVES.md`.
2. Identify 3–6 search terms from the question and grep them across
   `programs/*/index.tex`, `programs/*/explorations/*.md`, and
   `programs/*/notes/*.md`. Read the matching sections, not just the hits.
3. `gh issue list --state open --json number,title,labels,body` and skim the
   30 most recent closed issues for prior art on this exact question.

## Step 2: Attempt the answer from artifacts only

Write the best answer the record supports, structured as:

- **What the record establishes** — each claim cited to its source
  (`program §section` or exploration file) *with its rigor label carried
  along*: "(Rigorous, fixed-point-existence §3)", "(Conjecture, co-emergence
  §4)". A claim whose label you cannot find is a claim you may not make.
- **What the record does not establish** — the genuine gaps the question
  exposes, stated precisely.
- **Speculation (clearly fenced, optional)** — at most a short paragraph,
  explicitly marked, never presented as a result. External literature may be
  mentioned only with the METHODOLOGY exploratory-tier flag ("I believe X
  discusses this, but I have not verified the reference").

## Step 3: Classify

Pick exactly one:

- **`answered`** — the record fully addresses the question. The deliverable is
  Step 2's answer; no repo artifact is created. (Exception: if the answer was
  unreasonably hard to find, offer a docs issue for discoverability.)
- **`gap`** — the question is partially answered or unanswered, and it falls
  inside an existing program's scope statement or advances one of its
  OBJECTIVES milestones. The deliverable is Step 2's answer plus a draft issue.
- **`new-program`** — the question falls outside EVERY program's scope. The
  bar is high and the test is precedent: `signature-change-boundary` spun off
  only because its scope note explicitly does not fit inside `co-emergence`.
  To claim this path you must quote each program's scope statement and say why
  the question escapes it. When in doubt, it's a `gap`.

## Step 4: Confirm the path

Present the Step 2 answer, then use AskUserQuestion with your recommended path
first. For `gap`, name the target program and milestone (or note that no
milestone covers it). For `new-program`, propose the program name and scope
sentence. Always offer "answer only — file nothing" as an option.

## Step 5: Execute

**`answered`:** you are done after presenting the answer.

**`gap`:** file the issue at scout grade — a zero-context worker must be able
to start without questions:

- Milestone ID it advances, or an explicit note that it proposes a new
  milestone (the governor adopts it next cycle, or the experimenter may add it
  to OBJECTIVES directly).
- Context: what the record establishes and where (from Step 2, with paths).
- Deliverable and acceptance criteria: expected rigor labels, self-checks,
  citations to verify.
- Declared relations (`blocks` / `informs` / `contradicts` / `supersedes`).

Then ask the experimenter one more question: **label it `agent-ready` now**
(the worker fleet may claim it as early as the next daily run) **or leave it
unlabeled for discussion?**

**`new-program`:** after explicit confirmation, scaffold on a branch and open
a PR (no `agent-pr` label — this is experimenter-supervised seeding):

- `programs/<name>/README.md` — status "Early note / musings", a scope
  statement saying what is deliberately in and OUT (model it on
  `signature-change-boundary/README.md`), relationships to other programs with
  relation types, and an "In plain English" abstract per AGENTS.md.
- `programs/<name>/OBJECTIVES.md` — 2–4 seed milestones with "done ="
  conditions.
- `programs/<name>/notes/` — a dated seed note capturing the question and the
  Step 2 analysis.
- Note in the PR body that the program is excluded from the CI build matrix
  until it has an `index.tex` (adding it later touches `.github/`, a protected
  path).

## Hard rules

- Never edit a paper (`index.tex`) from this command.
- Never present unverified literature as support; never invent citations.
- Never state a claim above the rigor label the record gives it — this
  command is the experimenter's interface, which makes overclaiming here
  *more* dangerous, not less.
- One question, one path. If the question contains several questions, say so
  and triage the sharpest one first.
