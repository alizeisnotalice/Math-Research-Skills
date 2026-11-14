# Method: uniform convolution and 0–1 factorization

## Exact probability-generating-function reduction

Let $X,Y$ be independent, finitely supported integer-valued random variables. Translate each support by its minimum so both lie in $\mathbb Z_{\ge 0}$; translations preserve uniformity. Define

\[
P_X(z)=\sum_i\Pr(X=i)z^i,\qquad P_Y(z)=\sum_j\Pr(Y=j)z^j.
\]

If $X+Y$ is uniform on its support $S$, with $N=|S|$, then

\[
P_X(z)P_Y(z)=\frac1N\sum_{s\in S}z^s.
\]

Set $C(z)=\sum_{s\in S}z^s=N P_X(z)P_Y(z)$. The largest exponent in the product has a unique summand (the pair of maximum support points), so its coefficient in $P_XP_Y$ is $1/N$ and $C$ is monic with 0–1 coefficients. If $a_*=[z^{\deg P_X}]P_X>0$ and $b_*=[z^{\deg P_Y}]P_Y>0$, then $a_*b_*=1/N$. Thus $A=P_X/a_*$ and $B=P_Y/b_*$ are monic nonnegative real-coefficient polynomials and $AB=C$.

Conversely, suppose $C=AB$, where $C$ is monic 0–1 and $A,B$ are monic with nonnegative coefficients. Define probability-generating functions $P_X=A/A(1)$ and $P_Y=B/B(1)$. Since $A(1)B(1)=C(1)=|\operatorname{supp}C|$, the sum has PGF $C/C(1)$ and is uniform on the support of $C$. If $A,B$ themselves have only 0–1 coefficients, their normalized coefficient sequences are uniform on their respective supports. Therefore the probability question is exactly whether every such **monic-normalized** nonnegative factorization has 0–1 factors. No interval-support or rationality assumption is present. Do not test the raw coefficients of an arbitrary reciprocal rescaling: e.g. $1+z+z^2+z^3=(2+2z)(1/2+z^2/2)$ has nonbinary raw factors although reciprocal rescaling gives monic 0–1 factors. Hasanbegović (W18-X002) states nonnegative factors but does not explicitly give this normalization before claiming factor coefficients lie in $[0,1]$; use its coefficient lemmas only in the monic model. Its Theorem 4 also formally admits $v=w=1,n=0$, for which its display gives $f=2$; require $n\ge1$ or check that the blocks are disjoint and $f$ is 0–1 before transferring it.

## Finite coefficient search

For a proposed factor shape $A(z)=\sum_i a_i z^i$, write $B(z)=\sum_j b_jz^j$. Each product coefficient is a diagonal sum:

\[
\sum_{i+j=r} a_i b_j\in\{0,1\}.
\]

A bounded search may combine (i) $0/1/*$ propagation, (ii) branching on undecided coefficients, and (iii) exact polynomial equalities and strict inequalities decided by Gröbner-basis reduction and real quantifier elimination. Each certificate applies only to the candidate shape, cofactor-degree cap, and branch actually encoded. Numerical optimization alone is not a proof of infeasibility; use exact algebraic or interval certificates for any claimed exclusion.

Hare’s degree-15 experiment leaves 975 cases unresolved and imposes both a cofactor-degree cutoff and a per-instance time cap. The source’s reported category totals differ arithmetically from the reported total by one; retain the published values as reported and do not silently reconcile the discrepancy. This is finite evidence only.

## Cyclotomic mask and divisibility methods are conditional

For a finite set `A⊂Z` with mask polynomial `A(x)=Σ_{a∈A}x^a`, Coven–Meyerowitz (M0155) defines (T1) and (T2) through cyclotomic divisibility. Theorem A says (T1)+(T2) suffice for a translational tiling for every finite set; B1 gives general necessity of (T1), while B2 gives necessity of (T2) only under the article’s stated restriction that `|A|` has at most two prime factors. The source leaves general T2 necessity open. These statements concern unique additive tilings and 0–1 mask supports, not arbitrary nonnegative-real probability factors.

Billey–Swanson (W18-D04-EXT-001), Theorem/Definition 1, characterizes a nonnegative-integer polynomial whose roots are all zero or roots of unity by equivalent cyclotomic, q-integer, and independent-uniform-sum forms. Use that identity only after the cyclotomic-root premise is established for the polynomial at hand; the theorem does not establish that premise for an arbitrary A175 factor.

Steinberger (W18-D04-EXT-003), Theorem 1, proves the minimum-degree candidate for a nonnegative-coefficient multiple of `Φ_n` when `n` is even, a prime power, or satisfies the strict condition `2/p > Σ_i 1/q_i` (with `p` the smallest prime divisor and `q_i` the other distinct prime divisors). The general minimum-degree conjecture remains open in the read article. The result is a divisibility/positivity constraint, not a factorization classification.

## Conditional arithmetic constraints and non-transfer boundaries

Damianou (W18-D04-EXT-004) gives the Kronecker classification only for monic `Z[z]` polynomials with all roots in the closed unit disk. Ounaies–Rhin–Sac-Épée (EXT-006) gives Mahler/root constraints only with the theorem-specific hypotheses recorded in its card (including monicity, reciprocal structure, irreducibility or no-root-of-unity assumptions where stated). Lagarias–Wang (EXT-007) treats finite Abelian-group masks and periodic tilings; equality modulo `X^N−1` must not be replaced by equality of ordinary polynomials. These are conditional tools after the corresponding input structure is independently proved; none classifies arbitrary nonnegative-real factors. Pritsker (EXT-005) is asymptotic zero-distribution background only for the current mapping and is not quota-countable.

Blekherman (M0158) concerns global pointwise nonnegativity and sums of squares for homogeneous ternary sextics and quaternary quartics. Coefficientwise nonnegative PGFs need not be globally nonnegative, so the source supplies only a caution about positivity models, not an A175 method. Its original arXiv v2 card records a printed Theorem 7.1/proof discrepancy and keeps the proof-supported calculation separate.

## Finite-support PGF and conditional positivity tools

Klich (W18-D04-B10-001) directly identifies independent finite-support nonnegative-integer summands with products of normalized probability polynomials. Its support Minkowski, entropy, exact low-degree, and real-root/Hurwitz conclusions retain their individual hypotheses; it proves no Boolean closure of factors. Bausch–Cubitt (W18-D04-B10-002) distinguishes iid `n`-divisibility (`f=g^n`) from `n`-decomposability into possibly unequal factors and supplies complexity results for encoded decision problems. Preserve the card's source-page `S'`/scaling and coefficient-display discrepancies; do not cite the printed reduction as an uncorrected proof.

Reddy (W18-D04-B10-003) applies to a 0–1 mask already known to be divisible by `Φ_n` and to satisfy the minimal-vanishing-sum and arithmetic conditions. The `n=2pq` three-term minimum-degree formula is a conjecture in the source. Motzkin–Straus (W18-D04-B10-004) provides conditional positive-multiplier and root-angle statements. Separate coefficientwise positivity from copositivity; retain no-nonnegative-zero, sign, and leading/trailing homogeneous-part hypotheses. Its Theorem 2.1 missing-`r` display issue is isolated in the card. None of these results supplies the general real-to-Boolean factor bridge for A175.

## Translational-tiling references are auxiliary

M0157 studies periods of finite-set translational tilings, not probability-polynomial factors. In its physical pp. 7–8 proof of Theorem 3, isolate the reciprocal-coefficient error in the displayed sum from the preceding totient estimate; the generic-constant argument still supports the theorem’s stated exponent. Remark 4’s sharper estimate is cited from other work and is not proved in this article. Do not use the faulty line as evidence for the sharper estimate.

## Results for specific families

Dvorsky’s high-degree theorem rules out factors $1+a z^2+z^k$ for $k\ge341$, $0<a<1$; the complete theorem statement imports its bounded odd-degree cases from a companion preprint. It does not prove the general conjecture.

Hare’s $\epsilon$-unfair definition permits coefficients in $[-\epsilon,1+\epsilon]$. If a constructed factor has a negative coefficient, it lies outside the original nonnegative-factor hypothesis, however small the coefficient is.


## Further conditional Fourier and cyclic-mask methods (B11)

For a nonnegative-real polynomial already known to vanish at a specified set of roots of unity, Tan–Zhang (W18-D04-B11-001) proves an arc/support-diameter bound from vanishing Fourier moments; its rational-coefficient corollary uses Galois conjugacy, and its integer-tiling corollaries require both (T1) and (T2). De Carli–La Porta (B11-002) and Filaseta–Schinzel (B11-003) contribute exact cyclotomic/divisibility methods only under their coefficient and root hypotheses. Filaseta–Finch–Nicol (B11-004) has specialized 0–1 exponent and sparse-integer irreducibility results; retain the nested powers and corrected trace multiplier in its card.

Tan–Zhang (B11-005), Łaba–Londner (B11-006), and Lam–Leung (B11-007) concern finite cyclic or integer-group-ring tilings and root-of-unity relations. Their conclusions require the exact period, mask, divisibility, integer-coefficient, and signature assumptions listed in the cards. A transfer from A175 still needs a proof of integerization of arbitrary real PGF factors and a valid ordinary-to-cyclic/no-wrap representation. Modular identities must not be silently substituted for ordinary polynomial convolution. R06 accepted the B11 mother bindings and typed all seven as quota-eligible, bringing the A175 total to 33. This review confirms source-to-tool relevance under the listed hypotheses; it does not supply integerization of arbitrary real PGF factors or an ordinary-to-cyclic/no-wrap bridge, so the A175 mathematical status remains unresolved. Skill release awaits final hash binding.
