# Position D: Queue runway is the binding constraint — point the scout at SCB, adopt #63 as SCB-6

**Author:** position agent D (governor debate, 2026-06-11) · **Model:** claude-fable-5

## Summary

The experiment's throughput is gated not by research difficulty but by issue-queue arithmetic: the worker drains up to 7 issues/week, the scout refills at most 2/week and exits early when the queue looks "stocked." The queue currently holds 4 issues and zero of them advance the repo's cheapest, most sharply specified milestones (SCB-2/3/4). The governor's only lever over the refill is OBJECTIVES content. This cycle's governance pass should therefore: (a) update SCB OBJECTIVES so the scout's next run files SCB issues first, (b) adopt experimenter-authored issue #63 as milestone SCB-6 so it stops being an unactionable orphan, and (c) record the SCB-1 completion that the OBJECTIVES table currently fails to reflect.

## 1. The queue is a pipeline with a structural deficit

All claims in this section are process claims grounded in the cited artifacts.

**Drain rate.** The worker runs daily and claims one `agent-ready` issue per run (`automation/routines/` role table in AUTONOMY.md). Backpressure (skip if ≥3 `agent-pr` PRs await quorum) is currently inactive: exactly one open `agent-pr` PR exists (#89). So the drain is at full rate: up to 7 issues/week.

**Refill rate.** The scout runs weekly, files **at most 2 issues per run**, and — critically — **exits without filing anything if ≥4 unclaimed `agent-ready` issues exist** (`automation/routines/scout.md`, §1 and Hard rules). The queue today is exactly 4 (#91, #66, #33, #29): if the scout ran this morning it would file nothing.

**Consequence.** Runway is ~4 days. Worst case: the scout's weekly run lands just after a no-op exit, the worker exhausts the queue by ~2026-06-15, and then idles daily until the next scout run, which adds back at most 2. The steady state of this pipeline is a near-empty queue with idle worker runs — lost throughput in a 90-day pre-registered experiment, at day T+2, when demonstrating sustained autonomous operation is the point. The scout's exit threshold and cap live in a protected path the governor cannot edit; **the only lever the governor holds is which milestones are Open, how they are annotated, and whether existing issues map to them.** OBJECTIVES is the steering wheel for the refill; this pass should use it deliberately.

**Composition problem.** None of the 4 queued issues touches SCB or GGD. Of the four, #29 (distinct Einstein–Hilbert actions across smooth structures) is a hard open-ended proof task with real `stuck`-label risk, and #33 is a numerics-explanation task. The queue is not only short; it is not load-balanced toward the milestones with the highest completion probability.

## 2. SCB-2/3/4 are the cheapest compounding milestones in the repo

**Track record.** SCB-1 produced the experiment's first fully autonomous merge: PR #78, merged 2026-06-10 (day T+1), closing #65 — a clean pass through the full gate stack. (Process claim; `gh pr view 78`.) The other merged result-PRs (#74, #90) are CE fixes; SCB is so far the only program where a full milestone went issue → PR → autonomous merge inside the experiment window.

**SCB-2 is nearly free.** The mathematical content is already stated in the program README's open-points section: ν = 1/2 is non-integer for every n, so no logarithmic solution arises even when the indicial roots {0, 1 + n/2} differ by an integer (Sketch — stated in README and seed note §5 context, not yet carried into the note as an explicit labeled statement; that gap is exactly what SCB-2 closes). The deliverable is a paragraph plus a check.

**SCB-3 is labeling, not derivation.** §§3–6 Rigorous-given-background, §7 Sketch, per the program's own review section. It brings the note into compliance with the repo-wide convention ("All results labeled" — AGENTS.md). Zero new mathematics.

**SCB-4 exercises the gate the experiment most needs to demonstrate.** The four exploratory references (Ellis et al.; Hayward; Dray–Ellis–Hellaby–Manogue; Kossowski–Kriele) must be verified or replaced. A grep of the seed note shows the "Relation to existing work" section does not currently flag these inline as unverified — README flags them, the note does not — so SCB-4 also fixes a citation-discipline hygiene defect. More importantly: METHODOLOGY calls fabricated citations "the single most serious failure mode," and the experiment's gate stack has a dedicated deterministic tier (`verify-citations`) and semantic tier (`claim-support`) for exactly this. No merged experiment PR has yet stress-exercised verification of a fresh reference list. SCB-4 is the cheapest way to put the citation machinery through a real rep early, while the cost of discovering a gate defect is still low (T+2, not T+60). (Process claim; AUTONOMY.md merge-gate stack, OBJECTIVES SCB-4 row.)

**They compound.** OBJECTIVES states "SCB-1 through SCB-4 should land before SCB-5." With SCB-1 merged, landing 2/3/4 — plausibly within one to two weeks at observed cadence — unblocks SCB-5, the index.tex port. SCB-5 touches `.github/` (CI build matrix) and therefore requires experimenter approval via constitution-guard: reaching it early gives the experiment its first planned exercise of the protected-path approval flow on a *cooperative* change, which is valuable calibration data for the audit.

**Sizing note for the scout.** SCB-2 and SCB-3 both edit the same note and are individually below sensible issue granularity; one combined issue advances both milestones without violating the scout's 2-issues-per-run cap. One scout run can therefore cover three milestones (SCB-2+3 combined, SCB-4 standalone).

## 3. Issue #63: adopt it as SCB-6, with explicit ordering

Issue #63 (open, unlabeled, experimenter-authored) proposes extending the fixed-background analysis to ds² = λ(x⁰)(dx⁰)² + a²(x⁰)dx⃗² with prescribed a > 0, and explicitly offers a milestone row (SCB-6). Today it is in a dead zone: the scout's hard rule forbids issues outside OBJECTIVES milestones and forbids it labeling anything not mapped to one, the worker only claims `agent-ready` issues, and only the governor edits OBJECTIVES. **An open, well-specified, experimenter-authored issue that no routine is permitted to act on is a standing process inconsistency, and unmapped open issues are precisely how topic drift accumulates** — the drift metric measures merged work against OBJECTIVES, so work flowing into #63 without a milestone would register as drift even though the experimenter wrote it.

The case for adopting rather than deferring:

- Its stated ordering constraint ("prefer landing after SCB-1") is now satisfied by PR #78.
- It is scope-guard compliant by construction: both λ and a prescribed, no backreaction, no self-consistency machinery — the issue body restates the README's binding scope guard verbatim.
- It is the natural research increment: the Lorentzian region of the current background is exactly Minkowski, while the framework's only exact self-consistent solution is an *expanding* spacetime (the de Sitter fixed point, Rigorous, `programs/fixed-point-existence/index.tex`). A realistic boundary adjoins an expanding region; #63 supplies the fixed-background half. (Sketch — this motivational chain is in the issue body; the de Sitter fixed point's rigor label is per the FPE paper.)
- The issue already meets the scout's quality bar (milestone row, context with file paths, concrete deliverable, acceptance criteria including the mandatory a → const limiting case, declared relations) — adoption costs the governor one OBJECTIVES row and the scout one labeling action, not a drafting cycle.
- The issue's technical expectation — indicial roots {0, 1 + n/2} survive with k² → k²/a(0)², local-but-not-global Bessel reducibility — is labeled there as expected-verify-or-refute; it stays **(Conjecture)** until the work is done, and a clean negative is an acceptable outcome per the issue's own acceptance criteria.

Order it **after SCB-2/3/4** (so the extension is built on the labeled, citation-clean note) and **independent of SCB-5** (it produces a new note; it does not touch index.tex or protected paths). It is the right "substantial" queue item to follow the three cheap ones — it keeps the worker stocked with SCB work across the gap weeks when the scout's cap binds.

## 4. Concrete proposed OBJECTIVES edit

Replace the table and trailing note in `programs/signature-change-boundary/OBJECTIVES.md` with:

```markdown
| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| SCB-1 | Odd-type profile restatement | Note restates the profile as λ ≃ −c·sgn(x⁰)·|x⁰|ⁿ and carries the two-sided (genuine signature-change) analysis through §§3–6 | **Complete (PR #78, 2026-06-10)** | #65 |
| SCB-2 | No-log strengthening | Explicit statement in §5 that ν = 1/2 excludes logarithmic solutions for every n | Open — **priority: next scout run; may share one issue with SCB-3** | — |
| SCB-3 | Rigor labels | §§3–6 labeled Rigorous (given fixed background), §7 labeled Sketch, per project convention | Open — **priority: next scout run; may share one issue with SCB-2** | — |
| SCB-4 | Citation verification | The exploratory references (Ellis et al.; Hayward; Dray–Ellis–Hellaby–Manogue; Kossowski–Kriele) verified per METHODOLOGY citation discipline, or replaced; the note's "Relation to existing work" section flags any still-unverified reference inline | Open — **priority: next scout run** | — |
| SCB-5 | Port to index.tex | `index.tex` compiles with verified bibliography; note: adding it to the CI build matrix touches `.github/` (protected path) and therefore needs experimenter approval — flag in the PR | Open | — |
| SCB-6 | Expanding Lorentzian region | §§3–6 re-derived on ds² = λ(x⁰)(dx⁰)² + a²(x⁰)dx⃗² with prescribed smooth a(x⁰) > 0; each result labeled Rigorous-given-background or explicitly demoted with the obstruction stated; a→const limit recovers the existing note exactly | Open | #63 |

SCB-2 through SCB-4 should land before SCB-5 (port a corrected note, not a
draft). SCB-6 is ordered after SCB-2/3/4 and is independent of SCB-5 (it
produces a new note and touches no protected path). Scout guidance: #63
already meets the agent-ready quality bar and needs only the label once
SCB-2/3/4 issues are filed; SCB-2 and SCB-3 are below single-issue
granularity individually and should be filed as one combined issue.
```

Two deltas beyond new rows: (1) SCB-1's status is corrected — the table still says Open although PR #78 merged, a record-hygiene defect this pass should not leave standing; (2) SCB-4's done-condition gains the inline-flagging clause, closing the note/README discrepancy noted in §2.

This edit goes out as a `governance`-labeled PR @-mentioning the experimenter, per AUTONOMY.md.

## 5. What this buys the experiment

- **Queue runway**: one scout run converts three milestones into two issues plus one labeling action, taking the SCB-specific queue from 0 to 3 and total runway from ~4 days to ~7, with SCB-6 as a multi-day anchor task behind them.
- **Gate-stack coverage**: SCB-4 gives the citation tiers their first real exercise; SCB-5 (unblocked shortly after) gives constitution-guard its first cooperative exercise. At T+2, demonstrating the machinery on cheap true positives is worth more than any single research increment.
- **Completion-rate signal**: SCB is the only program with a fully autonomous milestone merge in the window; loading the queue with its smallest remaining milestones is the highest-probability path to a string of clean merges in week 1–2, which is what the pre-registered metrics will be read against.

## Where this position is underspecified

1. **Scout timing is unknown to me.** I could not determine when the scout last ran or next runs; the "runway ≈ 4 days" arithmetic assumes full daily worker drain and a worst-case scout phase. If the scout runs tomorrow and the queue is at 4, it exits — the deficit argument holds — but the precise day the queue empties is an estimate, not a measurement.
2. **The binding-constraint claim is an inference from structure, not from observed starvation.** At T+2 no worker run has yet idled for lack of issues. I am arguing from the drain/refill asymmetry (≤2/week in, ≤7/week out, buffer capped near 4 by the scout's exit rule) before the failure manifests. A competing position could argue reviewer/quorum capacity will bind first; with only one PR currently awaiting quorum I cannot rule that out from data.
3. **The deeper fix is outside this lever.** The scout's exit threshold (≥4) and cap (2/run) structurally limit runway regardless of OBJECTIVES content. Raising either requires editing `automation/routines/scout.md` — a protected path needing experimenter approval. This position works around the constraint rather than removing it; the governor should flag the parameter mismatch to the experimenter in the governance PR, but cannot fix it.
4. **"SCB is cheapest" is a sizing judgment, not a measurement.** SCB-2/3/4 look like hours-scale tasks from the README's own review section, but #66 (FPE-1) also has a low-risk "documented obstruction" exit and I have not costed the CE issues comparably. If SCB-4 verification turns up a misrepresenting reference, the replace path could grow beyond a small task (though that discovery would itself be valuable).
5. **Portfolio concentration.** Adopting SCB-6 plus prioritizing SCB-2/3/4 makes the near-term queue SCB-heavy, and GGD currently has zero queue presence. This position deliberately optimizes completion rate and gate coverage over program balance; it does not address GGD starvation, and a synthesis weighing topic-drift and portfolio-breadth metrics may want to pair this with one GGD issue per scout cycle.
6. **SCB-6 ordering is a preference, not a dependency.** I order it after SCB-2/3/4 to build on a labeled, citation-clean note, but nothing technically blocks parallel work; if the synthesis wants maximum queue depth immediately, #63 could be labeled `agent-ready` in the same scout run with rework risk accepted.
