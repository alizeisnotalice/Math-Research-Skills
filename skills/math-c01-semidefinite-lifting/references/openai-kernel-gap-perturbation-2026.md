# Kernel-gap second-order energy contract

Source: *Continuum Coulomb hardness with binary nuclear charges* (OpenAI,
24 Sep 2026), SHA-256 `290f40f845dc3e0d56dfab4572a4f260c089df2f31e2677e23faa5e464d57190`,
physical pp. 5–7, Lemma 2.2. Pinned source:
<https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026/Continuum-Coulomb-hardness-with-binary-nuclear-charges-September-24-2026.pdf>.

For finite-dimensional self-adjoint `A>=gQ`, `P=ker(A) != 0`, `Q=I-P`,
`PBP=0`, and `||B||<=epsilon*g` with `0<=epsilon<1/2`, the source states

`|E(A+B)-E(-P B A^{-1} B P|P)| <= 2 g epsilon^3`.

Use it only for a certified kernel projection and gap; it controls the bottom
energy, not a spectral reduction, a Coulomb realization, or QMA-hardness.
The companion checker accepts a rational diagonal certificate and a sufficient
row-sum norm bound; it does not estimate eigenvalues numerically.

Run the exact diagonal example from the skill directory.

```sh
python3 -B scripts/kernel_gap_perturbation.py examples/kernel-gap-diagonal.json
```

It returns the compressed matrix `[["-11/576"]]` on the kernel and energy
error bound `1/16`. Supply integers or rational strings.
