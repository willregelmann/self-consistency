# Objectives — gaussian-gravitational-decoherence

Governor-maintained objective function for this program (see `AUTONOMY.md`).
Edits only via `governance`-labeled PRs.

| ID | Milestone | Done = | Status | Issues |
|----|-----------|--------|--------|--------|
| GGD-2 | Experimental discriminability | Updated predictions section quantifying how the Gaussian profile is distinguishable from Diósi–Penrose exponential decay — and from the dissipative-DP variant flagged in #92 — at currently proposed experimental sensitivities, recomputed against the corrected Table 1 platform parameters (errata PR #73), with verified citations to the experimental literature | **Done** (PR #105, merged 2026-06-15; issue #102 closed) — §5 gives the discriminant: max fractional-coherence difference 0.22 (BMV) / ≈0.18 (MAQRO), 3σ-resolvable with ~8000 shots, dDP subsection added, three verified experimental citations. (Row corrected from a stale "Open" in the 2026-07-05 monthly pass — a bookkeeping desync.) | #102 (closed) |
| GGD-1 | Material-dependence crossover | Quantitative threshold (acoustic-mode frequency vs. gravitational coherence frequency) for the Gaussian→exponential transition, with order-of-magnitude evaluation for at least two real materials; an outcome that no realistic platform reaches the crossover, with Conjecture 1 restricted or withdrawn accordingly, satisfies this milestone | Open — PR **#141** open (Conjecture 1 restricted: no accessible platform reaches the crossover; head-SHA carries a `quorum:accept` verdict) but **halted under `needs-human`**, awaiting the experimenter's citation-allowlist unblock (co-emergence entries landed via PR #142, merged 2026-07-12; `verify` needs a fresh CI run). Not marked Done until #141 merges. | #92 (informs), #136, #141 (PR) |
| GGD-3 | Independent noise-kernel cross-check | An independent linearized-gravity noise kernel (arXiv:2606.04099, `informs-issue` #107) is first shown *comparable in setup* to `eq:N0000_static`, then either reproduces the time-independent static kernel that yields the Gaussian t² exponent — hardening Result 2 (the Gaussian profile) beyond the framework's built-in Gaussian-noise Assumption 1 — or is shown to disagree under matched assumptions, a demotion signal for Result 2. **Precondition:** establishing kernel comparability is part of the done-condition; agreement/disagreement is signal only under a matched Newtonian/stationary setup. Sketch level acceptable | Open — added 2026-07-05 monthly pass (Position D; consumes librarian pointer #107) | #107 (informs) |
| GGD-4 | Ensemble-averaging and the predicted observable (Result 2 integrity) | Decide, with a concrete argument in the Einstein–Langevin/Gaussian-noise model already in the paper (Result 2, Remark 2), whether the ensemble-averaged coherence suppression coincides with single-system decoherence for the bimodal superposed-rigid-body state: compute the reduced-system coherence for a *single* noise realization vs. the ensemble average, and check whether the Gaussian $t^2$ suppression survives per-realization or only after averaging. Done = one of — (i) per-realization survival (or provable in-regime irreversibility of the averaging) shown, and Remark 2 restated as **resolved** with the §5 visibility discriminant (0.22 fractional-coherence difference, PR #105) confirmed as the single-run observable; (ii) the suppression shown to be an in-principle-reversible averaging artifact, and the §5 discriminant re-scoped to the observable it actually predicts, or Result 2 demoted — an honest negative result either way; or (iii) the resolution shown to **require a postulate beyond the framework's axioms** about operational decoherence in the ensemble, in which case escalate `needs-human` naming the specific postulate (per AUTONOMY — the *work* is a postulate-free calculation; only one outcome branch escalates). | Open — promoted from thread-proposal #149 (governor weekly pass 2026-07-12); `agent-ready` | #149 |

## Notes

This is the program with the most direct falsifiable-prediction content; GGD-2
is the experiment's primary "prediction with error bars" deliverable.

**Cross-program priority (governor, 2026-07-05 monthly pass; GGD-4 inserted
governor weekly pass 2026-07-12; supersedes the 2026-06-11 ordering, of which
5 of its top 9 slots — GGD-2, FPE-4, SCB-2/3, SCB-6, FPE-1 — are now
Done/void):** open milestones in priority order —
GGD-1 (PR #141, halted on `needs-human`) > CE-13 (co-emergence anchor-language
audit; contains the confirmed L980 demotion) > GGD-4 (Result 2 observable
integrity, #149 — merged-headline integrity on the frontier program; the
2026-07-05 debate rated it sharper than more discriminability arithmetic, so it
outranks GGD-3, which only hardens the shape) > FPE-5 (Schauder M6/M7) > FPE-7
(well-definedness M8/M9) > GGD-3 (noise-kernel cross-check, needs #107) >
CE-10 follow-ons > CE-11, CE-12 (promoted 2026-06-21; scout to spec) > FPE-6
(Planck-boundary retirement) > FPE-2 (assumption A3) > CE-5 (#45, in-flight) >
CE-6..CE-9.
Halted/blocked, unranked: the signature-change-boundary thread (`needs-human`
#75 — only correction PR #147 proceeds); FPE-3 (blocked by FPE-4); SCB-5
(experimenter-gated `.github/` edit); SCB-4 (certification void, T2).
`experimenter-priority` issues outrank all of it, per the worker routine.
Rationale: `explorations/governance/2026-07-05-monthly-record-integrity.md`.
