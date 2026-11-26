# Integer-linear-form proof gates

Use this procedure before turning an approximation, recurrence, Padé construction, or numerical pattern into an irrationality or irrationality-exponent claim. It is independent of the source that produced the candidate.

## 1. Normalize one target

Fix the constant \(\xi\), index set, and actual remainder
\[
R_n=q_n\xi-p_n.
\]
Expose every other logarithm, zeta value, period, or auxiliary constant. A form in several constants is not a proof about \(\xi\) alone unless a separately proved elimination or linear-independence statement supplies that reduction.

## 2. Prove integrality on the same indices

Choose a positive denominator multiplier \(D_n\) and prove
\[
D_np_n,\ D_nq_n\in\mathbb Z.
\]
State prime ranges, multiplicities, exceptional indices, and any common gcd before reduction. Define the actual integer form \(L_n=D_nR_n\); do not combine an integrality statement for one coefficient with a different denominator bound for the other.

## 3. Prove nonzero and smallness for that same form

On an infinite specified index set, establish both \(L_n\ne0\) and \(|L_n|\to0\). A sign certificate, strict remainder bound, determinant separation, or a source theorem may establish nonvanishing, but state its index range. Convergence \(p_n/q_n\to\xi\) by itself is insufficient: it must survive multiplication by \(D_nq_n\).

If \(\xi=a/b\in\mathbb Q\), then \(bL_n\) is integral. A nonzero integral subsequence cannot tend to zero, giving the contradiction.

## 4. Upgrade only with uniform rate data

For a denominator-wise lower bound or irrationality exponent, retain matching-index, all-large-\(n\) bounds for coefficient height and both upper and lower remainder scales. If there are several forms sharing coefficients, prove every required integer combination is eventually nonzero; separate nonzero remainders may cancel.

## 5. Classify computational output correctly

Exact recurrence checks, rational intervals, finite p-adic valuations, and numerical slope fits can certify only their explicitly checked finite range. Save inputs, exact output/interval direction, software version, and index range. They do not establish the infinite integrality, nonzero, or decay quantifiers above.
