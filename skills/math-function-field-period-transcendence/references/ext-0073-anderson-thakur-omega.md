# Anderson--Thakur omega interface

Source reviewed: local arXiv:1610.04048v2, *On a variant of Schanuel
conjecture for the Carlitz exponential*; physical p.10 of the reviewed
29-page PDF.

For the source-normalized Anderson--Thakur function in the Tate algebra,
Proposition 9 states

\[
\tau(\omega)=(t-\theta)\omega,
\qquad
\omega=(-\theta)^{1/(q-1)}\prod_{i\ge0}(1-t/\theta^{q^i})^{-1}.
\]

It also states meromorphic continuation with simple poles at
\(t=\theta,\theta^q,\ldots\), and
\(\operatorname{Res}_{t=\theta}\omega=-\widetilde\pi\). The paper derives
the proposition from its Anderson--Thakur/Carlitz construction and refers to
its cited source for details; consequently the caller must separately supply
that normalized construction and Frobenius relation. This is not an adoption
of the paper's later conjectural Carlitz-Schanuel statements.
