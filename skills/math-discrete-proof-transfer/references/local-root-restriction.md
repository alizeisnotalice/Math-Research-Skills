# Restricting a polynomial difference problem to a progression

OpenAI, *A Power Saving for Polynomial Differences at Prime Arguments*, Family 182, PDF pp. 3–4, §2.1 and Lemma 2.1. Archived SHA-256 b42ac864305ade86faecfe7a599249cf07a47681d7ce2008b51f6c8a3591f819. [Pinned manuscript](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/prime-argument-polynomial-differences.pdf)

Input a nonzero h in Z[x] and, for every prime p, a compatible p-adic unit root z_p with multiplicity m_p. The source assumes prime-intersectivity, meaning unit roots modulo every positive integer, and obtains compatible roots by a finitely branching tree. One modular root without a lifting argument does not suffice.

1. For l≥1 take λ(l)=∏ p^(m_p v_p(l)). Choose r_l in (−l,0] from the compatible roots modulo the prime powers dividing l. Define T_l(x)=r_l+l x and h_l(x)=h(T_l(x))/λ(l).
2. At p dividing l write T_l(x)=z_p+p^v Y with v=v_p(l) and Y in Z_p[x]. The Taylor expansion of h at z_p begins in degree m_p and has p-integral coefficients. Each coefficient after substitution is divisible by p^(v m_p), which proves h_l is integral. At other primes λ(l) is a unit.
3. For D≥1 write r_lD=r_l−i l with 0≤i<D. Then T_l(Dx−i)=T_lD(x) and h_l(Dx−i)=λ(D)h_lD(x). The source primes are therefore unchanged under this substitution and Dm−i≥1 for m≥1. Thus an avoiding set, restricted to a progression with step λ(D) and rescaled, remains avoiding with parameter lD. Track the progression step λ(D) separately from the argument scale D.

Exact control: h=(x−1)^2, z_p=1 and λ(l)=l². For l>1 the residue is 1−l, so h_l=(x−1)^2. For l=1, h_1=h by convention. The associated restriction identity can be checked by integer polynomial comparison. The manuscript's later prime distribution and density bound require additional arguments, including a companion zero-free statement. The local-root construction needs none of those later claims.
