# G26 method interfaces

The main probability interface is A175: independent, finitely supported integer-valued `X,Y`, with arbitrary finite supports that may have gaps; `X+Y` is uniform on its support. The factor coefficients are nonnegative reals. A rationality or integrality premise on the factors is not part of the problem.

## PGF normalization and converse

Translate the supports so their minima are zero. Write

`P_X(z)=Σ_x P(X=x)z^x`, `P_Y(z)=Σ_y P(Y=y)z^y`.

Uniformity of `X+Y` on `S` means

`P_X P_Y = F/|S|`, `F(z)=Σ_{s∈S} z^s`.

The leading coefficient of the product comes from the unique pair of maximal support points; hence `F` is monic. Multiplying one probability factor by `|S|` gives a factorization of `F` into nonnegative real polynomials. Reciprocal rescaling makes each factor monic: if `F=G H` with positive leading coefficients, take `A=G/lc(G)`, `B=lc(G)H`. Conversely, if `F=A B` is a monic factorization with nonnegative coefficients, normalize each factor at 1; since `A(1)B(1)=F(1)=|S|`, their PGFs multiply to `F/|S|`.

The original summands are uniform on their supports iff the corresponding monic factors have 0–1 coefficients. The implication “monic nonnegative factors have coefficients at most 1” follows when `F(0)=1`: endpoint coefficient comparisons give `A(0),B(0)≤1`, their product is 1, hence both are 1; then `F_i≥A_i B_0=A_i` and `F_i≥A_0 B_i=B_i`. The conclusion is only `0≤A_i,B_i≤1`, not integrality and not fairness. If an unshifted target has `F(0)=0`, first write `F=z^r F_0`, strip the factors' monomial valuations, and apply the constant-term argument to `F_0(0)=1`.

## G26.01 — PGFs and nonnegative polynomial semigroups

Use the exact product identity above for arbitrary finite supports, including gaps. Record the support Minkowski sum and the number of representations of each sum. Uniform output requires every coefficient of `F` to be 0 or 1 after the common normalization; it does not require the factor supports to be intervals.

## G26.02–.03 — exact elimination and semialgebraic feasibility

For fixed factor degrees `r,s`, set `A=Σ_{i=0}^r a_i z^i`, `B=Σ_{j=0}^s b_j z^j`, impose `a_r=b_s=1`, `a_i,b_j≥0`, and the exact diagonal constraints `Σ_{i+j=t}a_i b_j=F_t`. Branch explicitly on zero coefficients when support shape changes. Gröbner reduction certifies polynomial equalities/ideal consequences; real closed field quantifier elimination can decide a fully encoded finite system of equations and inequalities. A numerical optimizer, a finite degree cap, or an excluded branch cannot prove the unrestricted conjecture.

For a fixed ordered degree profile with all factor coefficients strictly positive and each PGF normalized at 1, a pairwise-coprime factor tuple is also a regular point of the multiplication map: the source differential determinant is nonzero, and for two factors this is equivalent to `Res(A,B)≠0`. The inverse function theorem gives local uniqueness of the same degree profile. This does not decide global feasibility and does not apply at support-gapped/zero-coefficient boundary points.

## G26.04, .07 — root geometry and algebraic-height tools

Root-location, cyclotomic, Mahler-measure, and separation theorems apply only after their exact integer/monic/height/irreducibility/root hypotheses are established for the polynomial in question. If `F∈Z[z]` is monic and `F=A B` with monic real polynomial factors, each root of `A` or `B` is a root of `F`, hence an algebraic integer; their coefficients, as elementary symmetric polynomials in those roots, are real algebraic integers. This derived fact does not make them rational or integers. For a monic 0–1 target of degree d, the Cauchy bound gives root moduli at most 2; Vieta then gives factor-coefficient conjugate bounds \(\binom{d}{j}2^j\le3^d\). Thus degree- and target-height-dependent coefficient bounds are derivable. The cited factorization arguments here do not supply a degree-independent bound or the particular root-separation estimate a later theorem may require. For arbitrary unnormalized PGF factors, first establish the positive reciprocal monic normalization. Do not infer cyclotomic roots from the 0–1 target alone.

## G26.05 — coefficient recurrences

Convolution gives `F_t=Σ_{i+j=t}a_i b_j`. If investigating a first coefficient outside `{0,1}`, state which prior coefficients are known and derive each forcing equation from this diagonal sum. Results for a specified factor shape, first nonbinary location, or degree cap remain conditional on those assumptions. A coefficient bound `[0,1]` does not make a coefficient binary.

## G26.06 — additive uniqueness and tiling

For 0–1 support masks, a proved unique-sum representation gives an additive set factorization and can connect to integer tilings. Check whether the operation is ordinary addition on `Z`, cyclic addition modulo `N`, or a finite-group law. A cyclic identity may wrap high-degree terms and cannot be substituted for ordinary PGF multiplication without a proved no-wrap lift.

## Conditional separated-block result

Hasanbegović, Theorem 4 (physical p. 5), has the form

`f(z)=z^(n-deg w)w(z)+v(z)` is fair when `v,w` are nonzero 0–1 polynomials, `v` is fair, and `n≥max{deg(w)+2deg(v),2deg(w)}`.

The proof uses the high-block separation and a low-block recurrence (Lemma 5, physical pp. 6–8) to rule out a positive-index double-pair, then invokes Theorem 1. Transfer to A175 only under the monic nonnegative-factor normalization. Also exclude `v=w=1,n=0`, which yields `f=2`; for a proposed application verify the shifted supports are disjoint and `f` is itself 0–1. This is one conditional family theorem, not the general conjecture.

## Model boundaries

- A signed-factor epsilon relaxation is not a nonnegative PGF factorization.
- A polynomial identity in a quotient ring modulo `z^N−1` is not an ordinary polynomial identity.
- A theorem for integer-coefficient factors does not apply to arbitrary real factors unless integrality is derived.
- A source about nonnegative values on the positive half-line does not automatically give global nonnegativity, a sum-of-squares certificate, or a factor classification.
