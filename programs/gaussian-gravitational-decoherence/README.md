# Gaussian Gravitational Decoherence

**Status:** Pre-submission draft

Derives that the Einstein-Langevin equation predicts Gaussian (not exponential) decoherence at the Diosi-Penrose timescale for massive bodies in spatial superposition.

## Results

1. The decoherence timescale is tau_coh = (4sqrt(2)/5) hbar/E_Delta ~ 1.13 tau_DP, determined by the same gravitational self-energy as the Diosi-Penrose prediction.
2. The temporal profile is Gaussian, not exponential -- a consequence of the noise kernel for stationary matter being time-independent in the Newtonian limit.
3. The profile is material-dependent: rigid crystalline bodies give Gaussian decoherence, while soft or amorphous bodies whose acoustic modes approach the gravitational coherence frequency transition toward exponential.

## Relationship to other programs

This paper's predictions are understood within the self-consistency hierarchy as Level 2 (metric) phenomena: the Einstein-Langevin equation is the stochastic extension of the semiclassical Einstein equation whose fixed-point structure is established in `fixed-point-existence`.

## Build

```bash
pdflatex index.tex
```
