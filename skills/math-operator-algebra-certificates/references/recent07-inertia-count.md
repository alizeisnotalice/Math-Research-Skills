# Finite-rank inertia count by a Schur complement

Scoped reference. `linconj-v1.pdf`, SHA `4793f062c241e6e2d0125ef52607c744609e02d39203524f98707fd79b0e3c68`, author preprint v1, physical pp. 1--5.  This card adopts only the explicitly proved finite-dimensional inertia identity (Lemma 2.1), not the manuscript's claimed weighted singular-value theorem.

Let \(H=H^*\) be invertible on a finite-dimensional Hilbert space, let \(J:P\to\mathcal H\) be an isometric inclusion, and let \(W\succ0\) on \(P\).  Define
\[
 M=H+JWJ^*,\qquad G=W^{-1}+J^*H^{-1}J.
\]
Then
\[
 n_{\geq0}(M)=n_+(H)+n_{\leq0}(G),
\]
where every count includes algebraic multiplicity.  The proof is a two-Schur-complement calculation for
\[
 \begin{pmatrix}H&J\\J^*&-W^{-1}\end{pmatrix}:
\]
its complements are \(M\) and \(-G\), so inertia additivity yields the stated count.

Use it only when \(H\) is Hermitian and invertible, \(J^*J=I\), and \(W\) is strictly positive.  For a target assertion that \(M\) has at least \(r\) nonnegative eigenvalues, it is sufficient to retain a subspace of dimension \(r-n_+(H)\) on which the quadratic form of \(G\) is nonpositive.  A singular \(H\) needs a separately justified perturbation-and-limit argument; replacing inverse by a pseudoinverse is not licensed by this identity.

Use the [exact rational replay](../scripts/replay_inertia_count.py) with these fixtures:

```sh
python3 scripts/replay_inertia_count.py examples/inertia-valid-singular.json
python3 scripts/replay_inertia_count.py examples/inertia-valid-indefinite.json
python3 scripts/replay_inertia_count.py examples/inertia-valid-2x2-pivot.json
python3 scripts/replay_inertia_count.py --expect-invalid examples/inertia-invalid-nonisometric-j.json
```

The first fixture has singular \(M\), so the script explicitly checks that its zero eigenvalue is included in \(n_{\geq0}(M)\); the third forces an exact \(2\times2\) pivot.  The replay uses `fractions.Fraction`, not floating point: its symmetric congruence elimination records exact \(1\times1\) pivots and exact \(\begin{psmallmatrix}0&b\\b&0\end{psmallmatrix}\) pivots, then reports the positive/negative/zero counts.  It is a finite implementation check, not a proof of the general identity.
