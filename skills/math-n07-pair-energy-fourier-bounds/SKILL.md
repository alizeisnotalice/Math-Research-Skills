---
name: math-n07-pair-energy-fourier-bounds
description: Derive lower bounds for planar pair energies from Fourier-positive Schwartz minorants and transfer all Gaussian bounds to nonnegative completely monotone potentials. Use for locally finite configurations with centered disk density, including singular potentials and extended energies.
---

# N07 · Fourier pair-energy lower bounds

Use this skill when a planar locally finite configuration has centered disk density one and the task is to turn a Fourier-positive minorant into an ordered-pair energy lower bound. It also transfers a family of Gaussian bounds to every nonnegative completely monotone potential of squared distance.

1. Fix the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R^2}f(x)e^{-2\pi i x\cdot\xi}\,dx\). Let \(C_R=C\cap B_R\), \(N_R=\#C_R\), and verify \(N_R/(\pi R^2)\to1\).
2. For the Fourier step, require a real even Schwartz function \(f\) with \(\widehat f\ge0\). Read [the density-only Fourier bound](references/density-and-mixtures.md#density-only-fourier-bound) before applying it. The result is an off-diagonal lower bound \(\widehat f(0)-f(0)\).
3. To compare with an interaction \(\Phi\), establish \(\Phi(x)\ge f(x)\) for every \(x\ne0\). A pointwise minorant is needed. Fourier nonnegativity alone supplies no pair-energy comparison.
4. To pass from Gaussian bounds to a smooth nonnegative completely monotone \(g\), read [the shifted mixture transfer](references/density-and-mixtures.md#shifted-positive-mixtures). Keep every finite-radius energy sum nonnegative, shift first by \(\varepsilon>0\), and only then use Fatou and Tonelli.

The density hypothesis concerns the centered disks used in the energy definition. It gives no estimate in translated disks or in smaller disks. This skill proves an inequality for the lower energy per particle and does not characterize equality cases, construct the Fourier minorant, or establish a Coulomb, Riesz, or jellium theorem.

The lattice-specific constructions in the cited OpenAI preprints are evidence for particular Gaussian minorants. Their interval certificates, atomic columns, and full interpolation systems require their own source data and are outside this generic entry.
