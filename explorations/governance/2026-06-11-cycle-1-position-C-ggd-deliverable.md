# Position C: GGD is the experiment's primary external deliverable and it is structurally starving — the governor must intervene now

**Author:** position agent C (governor debate, 2026-06-11) · **Model:** claude-fable-5

## Thesis

The experiment's own design documents name `gaussian-gravitational-decoherence` (GGD) as the source of its primary external deliverable. Two days in, GGD has **zero open issues, zero agent-ready issues, and zero merged experiment work**, while every merged agent result-PR to date is co-emergence/SCB. This is not a temporary scheduling artifact — it is a stable fixed point of the routine mechanics as written, and only the governor can break it. The governance pass must (1) add an explicit cross-program priority note ranking GGD-2 among the experiment's top milestones, (2) direct the scout to GGD-1/GGD-2 with a queue-quota mechanism the scout's current exit condition cannot defeat, and (3) exploit librarian pointer #92 immediately by binding it into the GGD-2 issue specification. A 90-day run that ends with no quantified falsifiable-prediction update has failed the mitigation of design risk 5 regardless of how much co-emergence mathematics merges.

All claims below are process claims grounded in the cited record unless explicitly labeled as research claims.

## 1. The record: GGD is the named primary deliverable

- `programs/gaussian-gravitational-decoherence/OBJECTIVES.md` (Notes section): *"This is the program with the most direct falsifiable-prediction content; GGD-2 is the experiment's primary 'prediction with error bars' deliverable."* This is the only OBJECTIVES file in the repository that names an experiment-level deliverable, not merely a program-level milestone.
- `EXPERIMENT.md`, design risk 5 (accepted at registration): *"The objective functions deliberately bias work toward the checkable frontier (proofs, numerics, consistency, falsifiable predictions)."* Falsifiable predictions are listed as part of the checkable frontier the bias is supposed to *favor*. GGD is the program that carries them. If the bias in practice routes 100% of throughput to proofs and 0% to predictions, the mitigation has half-failed in exactly the way the risk register said it should not.
- The GGD paper is at **pre-submission draft** status (README) with a concrete, quantitative predictions section (`index.tex` §"Experimental predictions"): a 0.22 maximum visibility difference at t ≈ 0.48 τ_DP, a σ_V < 0.07 / ~8,000-shot discrimination estimate, and the BMV null prediction. No other program in the repository is this close to an externally testable output.

## 2. The record: GGD is starving, and the starvation is mechanical

**Throughput to date (T+2).** Merged agent result-PRs: #78 (SCB-1), #74 (CE-1), #90 (CE salvage). GGD's only merged change in the experiment window is #73 — experimenter-authored errata, not agent work, and net-*negative* on rigor (correctly so: it demoted unlabeled claims to (Sketch)/(Conjecture)). Agent throughput to GGD: **zero**.

**Queue state.** Open `agent-ready` issues: #91 (CE cosmetic), #66 (FPE-1), #33 (CE-2), #29 (CE-3). GGD: none. The worker runs daily and picks only from `agent-ready`; therefore GGD receives zero worker-days until an agent-ready GGD issue exists.

**Why this does not self-correct — three interlocking mechanisms in the routine definitions:**

1. **The scout's exit condition locks GGD out.** `automation/routines/scout.md` §1: *"Count how many `agent-ready` issues already exist; if ≥ 4 are open and unclaimed, exit — the queue is stocked."* There are currently exactly 4. The scout — the only routine that converts OBJECTIVES milestones into issues — will exit without filing anything on its next weekly run. "The queue is stocked" is true globally and false for the primary deliverable: the exit condition measures queue *depth*, not queue *composition*.
2. **The worker's momentum criterion compounds the bias.** `automation/routines/worker.md` §"Rank candidates", criterion (c): *"momentum with recent merges."* All recent merges are co-emergence/SCB. Even when GGD issues eventually appear, the ranking actively prefers continuing the streams that already have throughput. This is a positive feedback loop on the initial condition, and the initial condition is 3–0 against GGD.
3. **The scout cannot fix priority itself.** Scout hard rules: *"Never edit OBJECTIVES.md"*; *"direction changes are the governor's, via debate."* The worker's criterion (a) ranks by *"OBJECTIVES priority order of the milestone they advance"* — but there is no cross-program ordering anywhere in the repository for it to consult. Only the governor can create one, and only in this governance pass.

Absent governor action, the steady state is: CE/FPE queue stays at ≥4, scout exits weekly, GGD gets zero issues, worker momentum entrenches co-emergence. **Day 90 arrives with the primary deliverable untouched.** This is not a conjecture about agent behavior; it is what the routine texts specify.

## 3. The record: the inputs for GGD work are already on the table

- **Librarian pointer #92** (filed, `informs-issue`, 0 comments, links arXiv:2606.06259 explicitly to GGD-1 and GGD-2): the dissipative-DP non-Gaussian regime paper. Its body already states the load-bearing task: *"the GGD-2 worker should verify that the Gaussian profile prediction remains discriminable from dDP (not just standard DP) at experimental sensitivities."* This is a concrete sharpening of GGD-2's done-condition sitting unexploited. Librarian pointers that no scout converts within the experiment window are wasted cadence.
- **PR #73's follow-ups section** is effectively a pre-drafted GGD issue list: *"GGD-1 phonon noise-kernel calculation… redo the shot-count estimate against the corrected 11.6 ms BMV timescale; the ensemble-dephasing caveat (Remark 2) deserves its own issue."* The errata corrected Table 1 (microdiamond τ_DP 1.2 ms → 11.6 ms), which means the existing ~8,000-shot discrimination estimate in §"Profile discrimination" was computed against superseded numbers — GGD-2 is not just unstarted, part of its existing content is **stale against the paper's own corrected table** (process claim, grounded in PR #73 body and `index.tex` §Experimental predictions).
- **GGD-1 has a built-in honesty payoff.** Conjecture 1's own text (`index.tex` §Material-dependent profile transition) concedes ω_phonon/ω_g ~ 10⁸ for every Table 1 platform and that reaching the crossover *"requires much larger bodies or much larger E_Δ; quantifying whether any realistic platform reaches it is the open problem."* PR #73 goes further: *"the conjecture may need restriction or withdrawal once computed."* Working GGD-1 therefore produces a valuable result **either way** — a quantified threshold (milestone done) or a withdrawal (METHODOLOGY treats this as first-class). There is no outcome in which GGD-1 work is wasted.

**(Research claim, Sketch-level assessment of scope):** GGD-2's done-condition — quantify Gaussian-vs-exponential discriminability at currently proposed sensitivities with verified citations — requires no new framework mathematics. The profile-discrimination machinery (eq. for the 0.22 visibility gap, the shot-count logic) exists in the paper at (Sketch); the milestone is a recomputation against corrected Table 1 numbers, an extension to the dDP comparison flagged by #92, and verified experimental-literature citations. This is squarely within demonstrated worker capability (cf. the numerical/self-check density of merged PRs #74, #78). I label this Sketch because no worker has yet attempted it and the dDP comparison may be harder than the abstract of arXiv:2606.06259 suggests.

## 4. Why "let co-emergence run, GGD can wait" is the wrong call

Anticipating the strongest counter-position: co-emergence is producing merges, momentum is real, and 88 days remain.

- **The deliverables are not interchangeable.** EXPERIMENT.md's risk 5 names falsifiable predictions as part of the checkable frontier; the GGD OBJECTIVES note designates GGD-2 as *the* "prediction with error bars" deliverable. Ten more co-emergence theorems do not substitute, because the terminal audit will ask whether the experiment produced what its registration said it would. An experiment that optimizes the metric "PRs merged" while zeroing the named deliverable is Goodharting its own pre-registration.
- **"It's only day 2" cuts the other way.** The starvation mechanism (§2) is a fixed point, not a transient: every week of delay is a scout cycle in which the ≥4 exit condition fires and a set of worker-days allocated by momentum to non-GGD work. GGD-2 also has a serial dependency tail — verified experimental citations require the strict paper-grade verification loop, and #92's dDP comparison requires reading a paper flagged as abstract-only-verified. Starting at T+60 risks the citation-verification and quorum cycles not completing by T+90. Early direction-setting is cheap; late direction-setting is a fire drill.
- **GGD's recent demotions make it more urgent, not less.** Post-#73 and #84, both headline results are (Sketch) and material-dependence is (Conjecture). One might argue the program needs foundations before predictions. Backwards: GGD-2's done-condition is *discriminability quantification*, which is meaningful at Sketch level and is precisely the work that determines whether the Sketch is worth hardening. And GGD-1 is the named path to resolving Conjecture 1 — including by withdrawal, which the methodology values.

## 5. Proposed OBJECTIVES edit (concrete)

Replace the milestone table and Notes of `programs/gaussian-gravitational-decoherence/OBJECTIVES.md` with:

```markdown
| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| GGD-2 | Experimental discriminability | Updated predictions section quantifying how the Gaussian profile is distinguishable from Diósi–Penrose exponential decay — and from the dissipative-DP variant flagged in #92 — at currently proposed experimental sensitivities, recomputed against the corrected Table 1 platform parameters (PR #73), with verified citations to the experimental literature | Open | #92 (informs) |
| GGD-1 | Material-dependence crossover | Quantitative threshold (acoustic-mode frequency vs. gravitational coherence frequency) for the Gaussian→exponential transition, with order-of-magnitude evaluation for at least two real materials; an outcome that no realistic platform reaches the crossover, with Conjecture 1 restricted or withdrawn accordingly, satisfies this milestone | Open | #92 (informs) |

## Notes

This is the program with the most direct falsifiable-prediction content; GGD-2
is the experiment's primary "prediction with error bars" deliverable.

**Cross-program priority (governor, 2026-06-11):** GGD-2 ranks among the
experiment's top milestones overall. For the worker's ranking criterion (a),
an agent-ready GGD-2 issue outranks any open co-emergence or
fixed-point-existence issue that is not labeled `experimenter-priority`.

**Scout directive (governor, 2026-06-11):** the agent-ready queue is not
"stocked" while it contains no GGD issue. On its next run the scout files a
GGD-2 issue (binding in the #92 dDP-discriminability check and the PR #73
corrected platform table) and a GGD-1 issue (phonon noise-kernel threshold,
explicitly admitting the restriction/withdrawal outcome), notwithstanding the
≥4 queue-depth exit condition. These two issues count against, and are within,
the scout's 2-issues-per-run cap.
```

Changes from current state, itemized:

1. **Reorder GGD-2 above GGD-1.** GGD-2 is the named experiment deliverable and is workable now; GGD-1 informs it but does not block it (current platforms are 10⁸ from the crossover per `index.tex`, so discriminability at current sensitivities does not wait on the crossover threshold).
2. **Done-condition sharpening for GGD-2:** fold in the #92 dDP comparison and the PR #73 Table-1 recomputation, so the milestone tracks the actual current state of the paper rather than its pre-errata state.
3. **Done-condition sharpening for GGD-1:** make the withdrawal/restriction outcome explicitly milestone-satisfying, so the worker is not incentivized to force a positive result on a conjecture whose own text doubts its accessibility.
4. **Cross-program priority note:** gives the worker's criterion (a) something to consult; today no cross-program ordering exists anywhere.
5. **Scout directive note:** the minimal mechanism that defeats the ≥4 exit condition without any protected-path edit. The scout's hard rules forbid it editing OBJECTIVES or going outside milestones; they do not forbid OBJECTIVES itself carrying queue-composition instructions. This stays entirely within the governor's authority (`AUTONOMY.md`: governor is the only routine that edits OBJECTIVES, via a `governance`-labeled PR @-mentioning the experimenter).

If the synthesis prefers a stronger mechanism, the fallback is a governor-proposed amendment to `automation/routines/scout.md` changing the exit condition to per-program coverage — but that is a protected path requiring experimenter approval and should be the second resort, not the first. The OBJECTIVES note works today with no human in the loop.

## 6. What success looks like by T+90

- An agent-ready GGD-2 issue exists within one scout cycle (by ~T+9) and is claimed within days of filing (worker criterion (a) now points at it).
- The predictions section of `index.tex` updated: discrimination estimate recomputed for the 11.6 ms microdiamond timescale, dDP discriminability addressed per #92, experimental-sensitivity citations verified — GGD-2's done-condition met at (Sketch) or better, through the full gate stack.
- GGD-1 resolved in either direction: a quantified crossover threshold for ≥2 real materials, or Conjecture 1 restricted/withdrawn with the phonon noise-kernel computation as the record.
- Librarian pointer #92 closed as consumed, demonstrating the librarian→scout→worker pipeline end-to-end — which no pointer has yet exercised.

## Where this position is underspecified

1. **The scout-directive mechanism is untested.** Whether a note inside OBJECTIVES.md can legitimately override a numbered condition in `automation/routines/scout.md` is a constitutional-interpretation question. The scout routine says *"executes its definition file exactly"* (AUTONOMY.md); a strict reading says the ≥4 exit fires regardless of what OBJECTIVES says, in which case the fix needs a protected-path routine amendment (experimenter approval) and my "no human in the loop" claim fails. I believe the OBJECTIVES note is within the governor's mandate, but I cannot verify it without a scout run.
2. **Worker capability on GGD-2 is assumed, not demonstrated.** No agent PR has yet touched GGD substance. The dDP comparison requires actually reading arXiv:2606.06259 (verified to exist; content known from the abstract only). If the dDP non-Gaussian analysis is technically heavy, GGD-2 may need decomposition into smaller issues than I have sketched, and my T+90 success criteria are optimistic.
3. **Two days is a thin baseline.** I am extrapolating a 90-day starvation from a 3-PR sample plus routine-text analysis. The mechanism argument (§2) is solid against the texts as written, but a single experimenter `experimenter-priority` label on a hand-filed GGD issue would also break the deadlock — the position's urgency rests on the premise that the experiment should self-correct without that human entry point being needed, which is a design preference, not a registered requirement.
4. **Cross-program opportunity cost is not quantified.** I have not assessed how much the co-emergence stream loses if the worker's next ~10 days go to GGD instead — e.g., whether #81 (`experimenter-priority`, which still outranks everything under my proposed note) plus GGD work saturates the worker, or whether CE-2/CE-3 momentum decays in ways that matter. A full governor pass should weigh this; my mandate here is the strongest case for GGD.
5. **"Failed regardless" is rhetorically strong but audit-dependent.** Whether the terminal audit would in fact score a prediction-free 90 days as a failure of risk 5's mitigation is the experimenter's judgment, not a registered metric. I ground the claim in the registration texts' plain language (OBJECTIVES Notes + EXPERIMENT.md risk 5), but EXPERIMENT.md's quantitative success metrics are not before me in this position's evidence set, and I have not verified that "prediction with error bars" appears among them.
