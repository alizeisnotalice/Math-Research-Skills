<!-- Card revision: W15; theorem numbers, assumptions, and PDF locations checked. -->
# K. Sigman (2018), “Introduction to Renewal Theory”

- Source: Columbia University lecture notes (2018), 15 PDF pages. Local PDF: `evidence/fulltexts/R03.pdf` (SHA-256 `5552b1ef843fb5be6be76c969124dec6d8c81ed8c9bb7f1da4787794c68708eb`).
- Reading: full text, all 15 PDF pages; the existing card author attribution is retained.
- Relevance: renewal reward, age, and residual-life calculations for A007.

## Results and conditions

Theorem 1.1 (PDF p. 1) gives the elementary renewal theorem for an ordinary renewal process with i.i.d. positive interarrival times and finite mean. Theorem 2.1 (PDF p. 11) assumes a positive recurrent renewal process and i.i.d. cycle pairs `(X_j,R_j)` with `E|R_j|<∞`; it yields the almost-sure long-run reward rate `E[R]/E[X]` and an expected-rate limit. The proof uses cycle-count sandwiching for nonnegative rewards, decomposes signed rewards into positive and negative parts, and invokes uniform integrability for the expectation statement (PDF pp. 11–12).

The equilibrium excess/forward-recurrence distribution has cdf `F_e(x)=λ∫₀ˣ P(X>u)du` (PDF p. 3, equation (4)); this is distinct from the renewal-epoch interarrival law and captures length bias at a generic observation time.

## Migration gap

An arbitrary polling epoch is not a renewal epoch. A nonexponential interarrival law has a nonmemoryless residual time, so the residual-life distribution must be tracked at server visits. The renewal theorem alone does not provide the simultaneous stationary and large-switch-over limit asked in A007.
