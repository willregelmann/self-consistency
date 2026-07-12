---
description: "Research report — plain-English narrative of what the research accomplished, tiered by significance"
arguments:
  - name: window
    description: "Lookback window, e.g. '7d', '2w', '1mo'. Default 7d."
    required: false
  - name: program
    description: "Optional: focus on one program (directory under programs/). If omitted, cover all four."
    required: false
---

You are producing a **read-only research report** for the experimenter: a
plain-English narrative of what the *research* accomplished in the window,
tiered by significance. This is the on-demand twin of the automated weekly
`digest.yml` (which emails the same kind of report and posts it to the
"Breakthrough digest" issue) — keep the framing identical so the two never
drift. It is the **research** counterpart to `/status-report`, which covers
operational health (runs, tripwires, queue). Use this one to answer "what did
we discover / overturn / advance?"; use `/status-report` for "is the machine
healthy, what needs me?".

Default the window to **7 days** unless $ARGUMENTS specifies one. Being
interactive, you can go deeper than the headless digest: read the actual
`index.tex` sections, explorations, and PR diffs to ground and explain claims,
and follow up on any single result the experimenter asks about.

## Step 1: Gather (run in parallel)

Compute `SINCE` from the window, then:

1. **Merged work:** `gh pr list --state merged --limit 50 --json number,title,mergedAt,labels,body` filtered to `mergedAt >= SINCE`. The labels `promotion-rigorous` / `demotion` / `withdrawn` / `governance` drive Tier A; the milestone IDs in titles (`CE-2`, `FPE-4`, …) map work to programs.
2. **Queue health:** open `needs-human` (verbatim), `stuck`, and PRs awaiting quorum (`gh pr list --state open --label agent-pr`).
3. **Rigor posture:** the rigor distribution from the latest metrics snapshot (Metrics dashboard issue / newest `metrics/*.json`), as the trend baseline.
4. **Ground the claims:** for any Tier A/B item, read the relevant `programs/<p>/index.tex` section, exploration, or PR diff so the one-line description is accurate and at the correct rigor level — do not paraphrase the PR title. If `$program` is set, restrict to that program.

## Step 2: Tier the work (significance, not activity)

Mirror `digest.yml` exactly:

- **Tier A — gate-certified events:** every merged PR labeled `promotion-rigorous`, `demotion`, or `withdrawn`, plus every `governance` merge touching an `OBJECTIVES.md`. Membership is mechanical — list ALL and nothing else here, each with one sentence on what was promoted/overturned and why it matters.
- **Tier B — significant below the gate bar:** merged work meeting METHODOLOGY's significance test — *"would change a prediction or appear in the abstract"* — that is not Tier A: a new Sketch with a complete gap map, a negative result closing a direction, a notable exploration, a milestone advanced. Point at the specific labeled result or prediction; "interesting" is not a criterion.
- **Tier C:** everything else merged, one line each.

## Step 3: Write the report

Lead with the outcome. Structure:

```
# Research report — <date>, <window> window

## Headline
<One paragraph, plain English a non-physicist could follow: what materially changed.>

## Tier A — gate-certified events
<Every promotion/demotion/withdrawal/OBJECTIVES merge, one sentence each. "None this window." if empty — the expected steady state, not a failure.>

## Tier B — significant below the bar
<Significant non-gate-certified work, each pointing at the affected result/prediction. "None this window." if empty.>

## Tier C
<Everything else merged, one line each.>

## Per-program
<One line per program (or just $program if focused): what advanced, current rigor posture, what's in flight.>

## Queue health
<needs-human verbatim; stuck; PRs awaiting quorum.>
```

## Calibration rules (binding — same as digest.yml)

- **Do not inflate.** "None this window." is a valid and common Tier A line; it is the expected steady state, not a failure.
- **Never state a result above its rigor label.** Call conjectures conjectures, sketches sketches, in plain English too.
- **Demotions and withdrawals are progress**, not setbacks — report them that way (a counterexample found is a result).
- **Read-only and informational.** No recommendations about labels, verdicts, or merges; no edits, no dispatches. If something needs action, that belongs in `/status-report`, not here.
