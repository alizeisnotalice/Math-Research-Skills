# Conditional finite selection for sums and products

Source: OpenAI, *Monochromatic finite sums and products in the positive integers*, SHA-256 \`ab835f6a98c10d6d4498b19e7446facd7b481fef85fee54232c76b45bc9e0888\`, physical pp. 1, 5, 7-10, 38, 51, 64 and 66, Principles 2.3-2.4, Lemma 2.5 and Section 2.5. Pinned snapshot: https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6

The finite deduction fixes a target chain length \(m\), then the Prediction step bound \(s(m)\), then lists \(B,A\) and a positive Alignment mass \(\delta\).  Only afterwards it selects \(0<\tau<1/4\) and \(\eta>0\) so the finite calibration/counting errors satisfy the displayed budget (2.14).  Prediction supplies step-at-most-\(s\) models; Alignment supplies an event of lower probability at least \(\delta\), uniformly in \(\tau\) and model complexity.

On their intersection Lemma 2.5 selects a chain and a color; singleton product masks and weighted sum conditions yield an actual monochromatic finite configuration.  The later model, cube-law, diagonal, and palette/alignment stages establish the two principles.  Do not use the finite deduction without those stated principles and their parameter order.

## 固定来源

- 物理页 1, 5, 7, 8, 9, 10, 38, 51, 64, 66。Principles 2.3-2.4, Lemma 2.5, deduction in Section 2.5, later cube/alignment stages SHA-256 `ab835f6a98c10d6d4498b19e7446facd7b481fef85fee54232c76b45bc9e0888`。[Monochromatic finite sums and products in the positive integers](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Monochromatic-finite-sums-and-products-in-the-positive-integers-September-23-2026/paper.pdf)
