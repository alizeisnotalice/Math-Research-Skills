# Finite-field separation by a Berlekamp algebra element

OpenAI, Family 142, *Deterministic Polynomial Factorization over Prime Fields*, PDF p. 38, Lemma 9.1. Local SHA-256 ed88aa5ba802311a21c4f265bcef43515a16019f4b5afdd7f52ecbd36ce0204d. [Pinned source](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/Deterministic-Polynomial-Factorization-over-Prime-Fields.pdf)

Input: a square-free h over a verified prime field F_p, and a candidate b in B_h = {a in F_p[X]/(h): a^p=a}. Compute the Frobenius-fixed space by linear algebra in the quotient. If h has r irreducible factors, the Chinese remainder theorem identifies B_h with F_p^r.

1. Compute multiplication by b on B_h and its characteristic polynomial C(T). If C is square-free, the values of b on the r factors are distinct.
2. For any nonconstant proper divisor S of C, reduce S(b) modulo h and take gcd(h,S(b)). CRT shows it is the product of the factors on which S vanishes. Verify a proper nontrivial gcd directly.
3. Search over b only when finding a separator is useful. Keep the cost of constructing a basis, finding b, and obtaining a divisor S separate. This component does not supply deterministic polynomial running time for the full factorization problem. It is a finite-field argument; real nonnegative factorization requires different hypotheses.

Local exact example over F_101: h=(X−1)(X−2)(X−3), b=1+X+X², component values 3, 7, 13; C has ascending coefficients [30,50,78,1]. Taking S=T−3 recovers X−1.
