# Principal spectral-phase trace

## Certified transfer

Let \((M,\tau)\) be a finite von Neumann algebra with a finite normal positive trace and
let \(U,V\in M\) be unitary.  With
\[
h(e^{2\pi i x})=x-\lfloor x\rfloor\in[0,1),\quad h(1)=0,
\qquad L(W)=\tau(h(W)),
\]
one has
\[
L(UV)\le L(U)+L(V). \tag{SP}
\]
If \(\tau\) is faithful, then \(L(W)=0\) iff \(W=1\).  No commutation between \(U\)
and \(V\) is assumed.  For matrices, either the ordinary trace or its normalized version
may be used consistently.

The direct source proves (SP) in a group right-translation commutant with its finite block
trace: OpenAI, *The Kervaire theorem for groups* (24 September 2026), Lemma 2.1,
physical pp. 3--5, pinned PDF SHA-256
`f43dad0504bcbe962f20a9e9a6f9eb016a21f5abff1e03cbc2c062ecd8f04449`.
The proof uses only the displayed tracial, normal functional-calculus properties, so the
finite tracial formulation above is the exact reusable operator statement.

## Proof

Put \(B=h(V)\), so \(B\ge0\) and \(e^{2\pi iB}=V\), and define
\(W_u=Ue^{2\pi i uB}\).  For a real smooth function \(f\) on the circle, Fourier
approximation and traciality give
\[
 {d\over du}\tau(f(W_u))=\tau(f'(W_u)B). \tag{1}
\]
Here derivative is in normalized angle.  If \(f'\le1\), positivity gives
\[
\tau(f'(W_u)B)=\tau(B^{1/2}f'(W_u)B^{1/2})\le\tau(B).
\]
Integrating (1) therefore gives
\[
\tau(f(UV))\le\tau(f(U))+\tau(h(V)). \tag{2}
\]

For \(0<\epsilon<1\), average the periodic fractional part forward against a smooth
nonnegative density supported in \((0,\epsilon)\).  The resulting smooth \(f_\epsilon\)
satisfies \(f'_\epsilon\le1\), is uniformly bounded, and converges pointwise to \(h\),
including at the cut because \(0\le f_\epsilon(1)\le\epsilon\).  Normality (or dominated
convergence for the scalar spectral measure) passes (2) to the limit and proves (SP).

## Boundary

This is not a statement about an arbitrarily selected matrix logarithm, a phase branch with
`h(1)=1`, nonunitary matrices, or a trace that is not positive and tracial.  It does not
give equality, a reverse inequality, continuity at the cut, a phase of a product computed
by addition, or the paper's subsequent degree/fixed-plane and group-theoretic conclusions.

The exact monomial script records a finite illustration.  It rejects a non-permutation
``perm`` field rather than treating it as a unitary.
