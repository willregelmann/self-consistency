# AGENTS.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Project

A research program developing a geometric block universe framework for quantum gravity. Papers are exploratory and at varying stages of completion. New papers are added as the program develops — do not assume the list below is exhaustive; check `src/` for the current set.

## Current papers

**`src/gaussian-gravitational-decoherence.tex`** — *Gaussian temporal profile of gravitational decoherence from the Einstein-Langevin equation.* Derives that the Einstein-Langevin equation predicts Gaussian (not exponential) decoherence at the Diosi-Penrose timescale, identifies the material-dependent profile transition, and gives experimental predictions for BMV and decoherence experiments.

**`src/fixed-point-existence.tex`** (DRAFT) — *Fixed-point existence of self-consistent semiclassical gravity.* Establishes that the semiclassical Einstein equation has self-consistent solutions at three levels: exact (Starobinsky), perturbative (Banach contraction estimate), and conditional non-perturbative (Schauder theorem).

**`src/wheeler-dewitt-block.tex`** (DRAFT) — *The Wheeler-DeWitt equation and the block universe: a diagnostic of hidden temporal structure.* Audits every known formulation of the WdW equation against Axiom 2 (no evolution parameter), identifies where each formulation reintroduces foliation or temporal structure, and states necessary conditions for a genuinely timeless formulation of quantum gravity.

**`src/self-consistency-hierarchy.tex`** (DRAFT) — *A self-consistency hierarchy for timeless quantum gravity.* Proposes a novel four-level formulation: topological (PL 4-manifolds, intersection form constraint), smooth (exotic smooth structures), metric (semiclassical Einstein fixed point), and effective QM (density matrices as marginals of the smooth-structure measure). Derives four-dimensionality from the unique richness of 4D smooth structures.

## Repository structure

```
src/            — LaTeX source for all papers
explorations/   — Structured research investigations that shaped the program's direction
METHODOLOGY.md  — Research-as-code workflow (read before contributing)
```

## Build

Each paper compiles independently:

```bash
pdflatex src/<paper-name>.tex
```

The bibliography uses `\begin{thebibliography}` (no separate .bib file), so no bibtex step is needed.

## Methodology

Read `METHODOLOGY.md` before contributing. It defines:

- The research-as-code workflow: contributions are PRs against issues, explorations are structured investigations committed directly to `explorations/`
- Rigor standards and lifecycle: Conjecture → Sketch → Rigorous, with explicit demotion paths
- Citation discipline: paper-grade citations must be verified via web search; exploratory references must be flagged as unverified
- Adversarial review modes: verification (check the math) and stress testing (actively try to break the result)
- Agent team patterns: when to use teams vs. subagents, standard roles, team size guidance

## Conventions

- LaTeX with `amsmath`, `amssymb`, `amsthm` for mathematics
- Custom theorem environments: `theorem`, `axiom`, `proposition`, `lemma`, `conjecture`, `definition`, `remark`
- All results labeled: **(Rigorous)**, **(Sketch)**, or **(Conjecture)**
- Equations labeled `\label{eq:...}`, sections `\label{sec:...}`
- References use `\cite{key}` with keys defined in `thebibliography`
- Accented names use LaTeX commands (e.g., `Di\'osi`, `M\o ller`)
- Date format: Month YYYY
- Authors: Will Regelmann, Claude (Anthropic)

## Before starting work

1. Read `METHODOLOGY.md` — understand the contribution workflow and rigor requirements.
2. Read relevant `explorations/` files if working on a topic that has been previously investigated.
3. Read the current state of the paper you are contributing to.
4. Check open GitHub issues for the relevant paper before opening a new one.
