---
name: math-lattice-heat-asymptotics
description: Prove and safely use the first large-time correction for the continuous-time nearest-neighbor lattice heat kernel. Use for the exact dispersion 2(1-cos k), tensor-product dimensions, and clearly separated physical scaling.
---

# Nearest-neighbor lattice heat asymptotics

Use this reference method when the kernel is exactly
\[
 I(t)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{-2t(1-\cos k)}\,dk,\qquad t\ge1,
\]
or when a d-dimensional independent-coordinate kernel is its d-th power.  It proves
\[
 I(t)=(4\pi t)^{-1/2}\left(1+\frac1{16t}+O(t^{-2})\right),\qquad
 I(t)^d=(4\pi t)^{-d/2}\left(1+\frac d{16t}+O_d(t^{-2})\right).
\]

Read [the proof and boundaries](references/nearest-neighbor-heat-kernel.md) before transferring this calculation to a physical observable.  State the dispersion, kernel normalization, dimension, and any external time scaling (for example t=beta S).  The calculation proves only the ideal lattice heat-kernel expansion; it does not prove an interaction correction or identify a model-dependent remainder.

For a different finite-range dispersion, do not reuse the coefficient 1/16.  First derive the Taylor jet at its non-degenerate minima and separately control all other frequencies.
