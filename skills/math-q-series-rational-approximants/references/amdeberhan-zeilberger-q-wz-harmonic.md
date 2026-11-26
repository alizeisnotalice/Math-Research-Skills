# Exact q-WZ check for the q-harmonic construction

Source: G. Amdeberhan and D. Zeilberger, *q-Apery Irrationality Proofs by q-WZ Pairs*, arXiv:math/9804122v1, physical pp. 1--4. The paper was subsequently published in *Advances in Applied Mathematics* 20 (1998), 275--283.

For an integer \(q\) with \(|q|>1\), write
\[
 (q)_n=\prod_{j=1}^{n}(1-q^j),\qquad
 \binom nk_q=\frac{(q)_n}{(q)_k(q)_{n-k}}.
\]
The q-harmonic example on physical p. 2 gives
\[
 F(n,k)=-\frac{1}{\binom{n+k+1}{k}_q(q)_{n+1}},\qquad
 G(n,k)=F(n,k)\frac{q^{n+1}}{q^{n+1}-1},
\]
and the finite identity
\[
 F(n+1,k)-F(n,k)=G(n,k+1)-G(n,k).
\]

Use `scripts/check_q_wz_harmonic.py` when an exact finite check of this pair is useful:

```bash
python3 scripts/check_q_wz_harmonic.py 2 --max-n 4 --max-k 4
```

The script uses rational arithmetic and verifies only the displayed identity on the requested finite grid. It does not prove the infinite telescoping limit, its boundary terms, denominator control, asymptotic estimates, or any irrationality statement. Supply those target-specific arguments separately before routing a resulting linear form to an irrationality workflow.
