# The Agent Workflow

This project is an experiment in **research-as-code**: a theoretical-physics
program run the way a software team runs a codebase, with AI agents as
first-class contributors. This document is the map of the machinery — the
roles, the lifecycle, the tooling, and the guardrails that keep agent-produced
research honest.

The physics (see the [programs](../programs/)) is the *testbed*. The
methodology is the *product*. The full normative spec lives in
[`METHODOLOGY.md`](../METHODOLOGY.md); this is the operational tour.

---

## The core model

**Agent-as-contributor, human-as-reviewer** is the default model. Agents claim
issues, work on branches, and open PRs. The human author reviews and merges.
In this mode agents have no merge authority — every change to the papers
passes through human review. This mirrors the 2025–2026 consensus that
autonomous science still needs a human in the loop for conceptual judgment,
while letting agents do the heavy lifting of derivation, search, and drafting.

**Autonomous mode** is the pre-registered exception built to test that
consensus directly: for the 90-day experiment window defined in
[`EXPERIMENT.md`](../EXPERIMENT.md), merge authority is delegated to a
mechanical gate stack and the human acts as *experimenter*, not reviewer. See
[Autonomous mode](#autonomous-mode-the-90-day-experiment) below.

## The contribution lifecycle

```
issue ──▶ branch ──▶ commits ──▶ self-check ──▶ PR ──▶ [adversarial review] ──▶ human merge
```

1. **Claim an issue.** Every PR targets a specific issue; speculative work
   proposes an issue first.
2. **Branch** as `program/issue-N-description` (or `tooling/…` for
   repo-wide infrastructure).
3. **Commit in coherent steps** — messages say what was *derived*, not "update".
4. **Self-check** before the PR: dimensional analysis, limiting cases,
   consistency, order-of-magnitude sanity — documented in the PR description.
5. **Adversarial review** (optional, human-requested) — see below.
6. **Merge.** Default mode: the human merges. Autonomous mode: GitHub
   auto-merge fires mechanically once the full gate stack passes.

## Rigor labels and the rigor lifecycle

Every result is labelled **Rigorous**, **Sketch**, or **Conjecture**, and the
label is *not permanent*. Results are promoted (Conjecture→Sketch→Rigorous) and
**demoted** (→Demoted / Conjecture→Withdrawn) as understanding changes. Each
transition is its own PR. Demotion is treated as normal maintenance, not
failure — a silently-wrong result is worse than an honestly-labelled sketch.
See [case studies](case-studies.md) for real promotions and demotions.

## Adversarial review

After self-checks, a second agent can be dispatched to critique a derivation,
in one of two modes:

- **Verification** — check every step: does the algebra follow, are cited
  results used as cited, are there sign/factor errors? Baseline for any
  Sketch→Rigorous promotion.
- **Stress testing** — actively try to *break* the result: counterexamples,
  edge cases, alternative interpretations, and explicit checks that no hidden
  time-evolution, background structure, or preferred foliation has snuck in.

## Agent teams and the debate pattern

For genuinely open questions, the project uses **agent teams** rather than a
single agent, specifically to fight anchoring. Multiple **position agents**
develop the strongest version of competing approaches *in parallel, without
seeing each other's reasoning*; a **synthesis agent** then runs adversarial
critique across all positions and reports what survives.

> **Worked example — the mass-gap debate.** Two position agents independently
> developed competing mechanisms for self-consistent mass generation
> ([`position-starobinsky-mass.md`](../programs/co-emergence/explorations/position-starobinsky-mass.md),
> [`position-measure-mass.md`](../programs/co-emergence/explorations/position-measure-mass.md)),
> and a synthesis pass
> ([`2026-03-03-mass-gap-synthesis.md`](../programs/co-emergence/explorations/2026-03-03-mass-gap-synthesis.md))
> adjudicated — killing one mechanism as background-dependent, keeping the
> trace-anomaly mechanism, and surfacing the codependence insight that
> reshaped the program. The losing position is kept in the record, not deleted.

The output of a debate is an **Exploration** — a dated artifact committed to
the program's `explorations/` directory. Explorations shape direction; they do
not edit the paper directly. (A known limitation, tracked for improvement:
position agents drawn from the same base model partially correlate, so genuine
independence benefits from varying the model/temperature across positions.)

## Autonomous mode (the 90-day experiment)

The default model keeps a human in the merge loop. The autonomous experiment
removes them and asks whether machinery alone can hold the quality bar. The
full normative spec is the constitution, [`AUTONOMY.md`](../AUTONOMY.md); the
pre-registration (hypothesis, metrics, tripwires, kill switch, live status and
incident log) is [`EXPERIMENT.md`](../EXPERIMENT.md). The operational picture:

**Seven scheduled routines** replace the human's roles, each defined in a
version-controlled, constitutionally protected file under
[`automation/routines/`](../automation/routines/): a daily **worker** (claims
one issue, works it to a PR), a twice-daily **reviewer** (adversarial quorum:
two-pass review, machine-readable verdict per head SHA), a daily **responder**
(addresses revise verdicts and CI failures), a **red-team** every three days
(stress-tests merged Rigorous results — its product is demotions), a weekly
**scout** (opens issues for OBJECTIVES milestones) and **librarian** (arXiv
watch), and a monthly **governor** (direction: updates objectives, kills and
opens research lines).

**The merge-gate stack.** A PR merges when — and only when — all required
checks pass, in four tiers:

```
PR ──▶ deterministic (pytest · pdflatex · citation existence)
   ──▶ semantic (claim-support: do load-bearing citations support their claims?)
   ──▶ quorum (reviewer verdict marker for the current head SHA; promotions
       to Rigorous additionally need an independent stress-test marker)
   ──▶ constitutional (protected paths require the experimenter's approval)
   ──▶ GitHub auto-merge
```

Verdicts are per-SHA: any push invalidates them and the gate resets. Routines
authenticate as a dedicated machine account with write (not admin) access, so
branch protection, no-self-approval, and settings immutability hold *by
construction*, not by promise.

**The human is the experimenter, not a reviewer**: kill switch, budget,
constitutional amendments, and `needs-human` escalations — agents halt and
escalate rather than improvise when they hit a contradiction, a suspect
citation in merged content, or a malfunctioning gate.

## Custom tooling (`.claude/commands/`)

Three project-specific slash commands encode the workflow:

| Command | What it does |
|---------|--------------|
| [`/work-issue`](../.claude/commands/work-issue.md) | Picks an issue (ranked by dependencies/impact) and sets up the contribution workflow. |
| [`/review-pr`](../.claude/commands/review-pr.md) | Runs the two-pass dialectical review (adversarial critic, then steelman defender) and emits a calibrated verdict table. |
| [`/restructure-paper`](../.claude/commands/restructure-paper.md) | Plans a paper reorganization — the intellectual analogue of a refactor. |

## Quality gates (hooks)

[`.claude/settings.json`](../.claude/settings.json) wires the `TeammateIdle`
and `TaskCompleted` hook events to
[`scripts/hooks/require-clean-sources.sh`](../scripts/hooks/require-clean-sources.sh),
which blocks a teammate from going idle or a task from completing while tracked
source files (papers, tooling, tests) have uncommitted changes. It fails open
on any internal error, so it can never wedge the workflow.

## CI gates

Every PR is checked by GitHub Actions — the guardrails that turn *attested*
rigor into *demonstrated* rigor:

| Workflow | Gate |
|----------|------|
| `tests` | The co-emergence numerical toy model and scaling tests pass (Python 3.10 / 3.12). |
| `build-papers` | Every paper compiles with `pdflatex`. |
| `verify-citations` | Every `\bibitem` resolves against Crossref/arXiv; the build fails on any unresolved reference. See [`tools/verify_citations.py`](../tools/verify_citations.py). |
| `semantic-review` | *Advisory.* An isolated LLM evaluator judges questions that aren't mechanically decidable — e.g. whether load-bearing citations actually **support** their claims (`.claude/tests/citation-claim-support/`). |

### Three tiers of verification

The CI gates form a deliberate hierarchy from cheap-and-certain to
judgment-and-advisory:

| Tier | Question | Mechanism | Blocking? |
|------|----------|-----------|-----------|
| **Deterministic** | Does it compile / run / resolve? | `tests`, `build-papers`, `verify-citations` | yes |
| **Semantic** | Does it overclaim / mis-cite / skip a self-check? | `semantic-review` — LLM-as-evaluator ([claude-tests](https://github.com/willregelmann/claude-tests)) | advisory in default mode; the autonomous mode's `claim-support` check is **blocking** |
| **Formal** | Is the proof actually valid? | Lean formalization (planned, issue #45) | yes, where formalized |

The semantic tier is run by an **isolated evaluator with no implementation
context** — the same anti-anchoring principle as the adversarial-review debate,
but standing and repeatable. It is deliberately *advisory*: an LLM verdict
flags an overclaim or a dubious citation for human attention, but never
certifies mathematical truth — that stays with the deterministic and formal
tiers, because an LLM judge can itself err.

## Citation discipline

Two tiers. **Paper-grade** references (anything in `thebibliography`) must be
verified to exist *and* to support the claim. **Exploratory** references in
issues/PRs may be unverified but must be flagged as such, and never committed to
a `.tex` file. Existence is now mechanically enforced by the `verify-citations`
gate; claim-support remains a human/agent responsibility. The gate has already
caught a real error — see [case studies](case-studies.md).
