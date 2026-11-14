<!-- Card revision: W15; exact theorem labels and proof locations checked against the full PDF. -->

# Y. Kanoria and A. Montanari (2013), “Optimal Coding for the Binary Deletion Channel With Small Deletion Probability”

- Source: IEEE Transactions on Information Theory 59(10), 6192–6219 (2013), DOI https://doi.org/10.1109/TIT.2013.2262020; arXiv:1104.5546. Local PDF: `evidence/fulltexts/I03.pdf` (45 pages; SHA-256 `e2b588df01e0a8c01b3cbad33a4fe4c87a2c40c247ac8b26ecb93e4e7b6ec462`).
- Reading status: full text, all 45 PDF pages including appendices.
- Direct relevance: B051, the binary i.i.d. deletion channel and small-deletion asymptotics.

## Exact theorem

Theorem 1.1 states that for every ε>0 there is a sufficiently small deletion-rate range in which

`C(d) = 1 + d log₂(d) − A₁ d + A₂ d² + O(d^(3−ε))`.

The constants are defined by the series in Theorem 1.1; the paper reports A₁≈1.15416377 and A₂≈1.67814594. The `O(d^(3−ε))` term is asserted for every fixed ε>0, with constants/range allowed to depend on ε. The theorem does not state an exact `d³` coefficient, a full asymptotic expansion to every order, or convergence of an infinite series.

The paper proves capacity through matching upper and lower estimates at the displayed order. The stationary-ergodic variational characterization is Lemma 2.2 (PDF p. 5), not Theorem 2.1 or Theorem 2.2. Achievability is Lemma 4.1 (PDF p. 8): an i.i.d.-run input with the stated deletion-rate-dependent perturbation of the geometric run law achieves the displayed rate up to `O(d^(3−ε))`. Theorem 1.1 proof begins on PDF p. 9; the proof of Lemma 4.1 is on p. 22 and that of Lemma 2.2 on p. 27. The upper-bound argument modifies the deletion channel to manage runs with many deletions, partitions ambiguous run alignments, controls long-run tails/super-runs, and uses entropy deficits to constrain near-capacity inputs (Sections 4–5 and appendices).

## Explicit open question

Section 6 (PDF pp. 26–27) asks whether the capacity has a higher-order expansion `C(d)=1+d log₂(d)−A₁d+A₂d²+A₃d³+A₄d⁴+…`, and whether this series converges for small positive d. The preceding estimates only establish the second-order truncation and the stated fractional-power remainder. The discussion’s exponentially decaying-correlation / nearby-deletion-cluster picture is heuristic, explicitly not a proof of convergence. The conjectured next-order input correction can involve inter-run dependence; the paper does not provide a closed all-orders recursion.

## Numerical cross-check

`evidence/W16/validate_constants.py` recomputes the displayed coefficient series using 50-digit Decimal arithmetic, with finite cutoffs N=30, 50, 80, 120. The output stabilizes to the printed values by N=80. This checks the arithmetic and the displayed finite sums; it is not a rigorous tail bound for the constants and gives no evidence that the channel-capacity expansion converges.

## Migration gap

An all-orders proof needs uniform control of the optimizing input law and of the error after arbitrary truncation order. It must also bound high-order interactions/tails with constants that permit the desired limiting operation. Neither coefficient evaluation at finitely many orders nor finite-blocklength numerics supplies these controls.
