# Walsh-support product gate for conditional FEI

**Source status:** author-hosted preprint, not an independently replayed Lean certificate. **Source:** Horace Dong, *A product inequality for Walsh coefficients and two conditional Fourier entropy–influence bounds*, SHA-256 `101196d99d383432ef15512bca0854863fa17f05a725798f85666758741ee822`, physical pp. 1–4, [source PDF](https://github.com/Horace-Maxwell/ai4math-results/blob/main/papers/fei-nonflat-spectra/note.pdf).

This extends the current Boolean-Fourier skill: its existing method reference fixes the sign-cube Parseval and total-influence normalization, but does not supply this support-product/entropy gate.

For a sign-valued Boolean function, set `U={S: fhat(S)!=0}`, `K=|U|`, `t=|U\{empty}|`, `W=sum_{S in U}|S|`, `p(S)=fhat(S)^2`, `H=sum p(S)log2(1/p(S))`, and `I=sum |S|p(S)`. The source proves, by the integer determinant built from the inclusion matrix on an upward-closed support family,

`sum_{S in U} log2(1/p(S)) + 2t <= 4W`.

Its stated corollaries are conditional:

* if a supplied `delta>0` obeys `delta <= K p(S)` for every `S in U`, then `delta(H+2t/K)<=4I` and hence `H<=4I/delta`;
* if supplied `L>=1` obeys `p(S)<=L p(T)` for every nonempty comparable pair `S subseteq T` in `U`, then `H<=4LI`; the empty-frequency mass is unconstrained.

Use only after exact Fourier coefficients and each stated support/mass premise are checked. These gates do not prove the general FEI conjecture, construct a uniform `delta` or `L`, or validate the reported external Lean build.
