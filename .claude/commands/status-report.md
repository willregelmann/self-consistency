---
description: "Status report — workflow-run health, autonomy-loop flow, tripwires, and per-program progress"
arguments:
  - name: window
    description: "Lookback window for throughput/failures, e.g. '7d', '48h', '2w'. Default 7d."
    required: false
---

You are producing a **read-only status report** of this autonomous research
system (see `docs/ARCHITECTURE.md`) for the experimenter. This command
reports and assesses; it never sets labels, merges, dispatches routines, or
modifies the repo. Default the lookback window to **7 days** unless $ARGUMENTS
specifies one (e.g. `48h`, `2w`).

## Step 1: Gather data (run in parallel)

Compute `SINCE` from the window (e.g. `date -u -d '7 days ago' +%FT%TZ`), then:

1. **Recent runs + failures:**
   - `gh run list --limit 25 --json workflowName,status,conclusion,createdAt,event,databaseId`
   - `gh run list --limit 80 --json conclusion,workflowName,createdAt,databaseId --jq '[.[] | select(.conclusion=="failure" or .conclusion=="cancelled" or .conclusion=="startup_failure")]'`
2. **Queue & flow:**
   - Open PRs: `gh pr list --state open --json number,title,labels,headRefOid,createdAt`
   - Per label count, open issues: `agent-ready`, `stuck`, `needs-human`, `thread-proposal` (`gh issue list --state open --label <L> --json number,title`)
3. **Throughput (window):** `gh pr list --state merged --limit 50 --json number,title,mergedAt,labels` then filter `mergedAt >= SINCE`.
4. **Metrics:** latest comment on the **Metrics dashboard** issue (`gh issue list --state open --search 'in:title "Metrics dashboard"'` → newest comment) and the most recent two `metrics/*.json` files.
5. **Quorum verdicts (for T3):** scan recent merged + open agent-PR comments for `<!-- quorum:verdict <accept|revise|reject> -->` markers over the trailing 20.
6. **Per program:** for each of `co-emergence`, `fixed-point-existence`, `gaussian-gravitational-decoherence`, `signature-change-boundary`, read `programs/<p>/OBJECTIVES.md` (milestone statuses) and the merged PRs in the window touching `programs/<p>/`.

## Step 2: Diagnose failures (do not just count them)

For each failed run in the window, classify — don't report a raw failure count:

- **Self-healed** — a transient API error (529/5xx/429) or session limit that a
  later scheduled fire covered (per-SHA verdicts mean nothing was lost). Confirm
  by checking that no open agent-PR is missing a current-SHA verdict and a
  subsequent run of the same workflow succeeded. Report as "absorbed", not as an
  outage.
- **Real** — a non-transient failure, or one that left a PR stranded (open
  agent-PR whose head SHA has no verdict and no in-flight reviewer), or a
  repeated pattern. These go in "Needs attention".

Pull the failing step's log tail when unsure (`gh run view <id> --log-failed`
or the jobs API) and quote the actual error.

## Step 3: Evaluate tripwires (EXPERIMENT.md T1–T5)

State each as ✅ / ⚠️ near-threshold / 🔴 fired:

- **T1** — zero demotions+withdrawals after 20 merged agent result-PRs. Report the running counts and how close.
- **T2** — fabricated/misrepresenting citation in merged content. Mechanically uncheckable here; flag as "manual — no automated signal", note any citation-related demotions seen.
- **T3** — quorum accept rate > 95% over trailing 20 verdicts. Compute from Step 1.5; a healthy system shows revises/rejects.
- **T4** — > 50% of merged PR volume (trailing 4 weeks) outside any OBJECTIVES milestone. Estimate from labels/titles vs. OBJECTIVES; mark as estimate.
- **T5** — two consecutive weekly metrics runs failed or empty. Check the last two `metrics/*.json` exist and carry non-zero PR-derived numbers.

## Step 4: Write the report

Lead with the outcome. Use this structure:

```
# Status — <date>, <window> window

**<One-line verdict>** — healthy / healthy-with-noise / needs attention, and the single most important fact.

## Workflow health
<Runs green? Failures classified as absorbed vs real. Is the event-driven loop firing (workflow_dispatch reviewers/responders)?>

## Flow & queue
<Open agent-PRs and whether they hold current-SHA verdicts; agent-ready depth; stuck; needs-human; thread-proposals (and whether the governor has adjudicated them).>

## Throughput (<window>)
<Merged PRs grouped by program; demotions/promotions; anything that closed a long-standing issue.>

## Tripwires
<T1–T5, one line each, with the number that matters.>

## Per-program
<One line per program: latest milestone movement, rigor posture, what's in flight.>

## Needs your attention
<Only genuine items: needs-human, stuck, real (non-absorbed) failures, thread-proposals awaiting adjudication, any tripwire ⚠️/🔴. If none, say "Nothing — system is running itself.">
```

## Constraints

- **Read-only.** Never merge, label, dispatch, or edit. If you spot something
  that needs action, put it under "Needs your attention" — do not act on it.
- **Classify, don't alarm.** A self-healed transient failure is noise, not an
  incident; say so explicitly so the failure signal stays meaningful. Conversely,
  do not bury a real stranded PR under a green headline.
- **Numbers that matter, not data dumps.** Quote the demotion rate, the accept
  rate, the queue depths — not every run.
- **Be honest about estimates.** T2 and T4 are partly judgment; label them as
  such rather than asserting a clean pass.
