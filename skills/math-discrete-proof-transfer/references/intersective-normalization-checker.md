# Finite checker for progression-compatible normalization

`scripts/check_intersective_normalization.py INPUT.json` checks the exact symbolic algebra in
`local-root-restriction.md` from finite data.  Its input has increasing-degree integer
`coefficients`, positive `l` and `D`, and, for each prime dividing `l*D`, a positive
`multiplicities[p]` and a `roots[p]` object containing an integer `residue` and a prime-power
`modulus` divisible by \(p^{v_p(lD)}\).  It rejects missing precision, a failed finite root
congruence, nonintegral normalized coefficients, or a failed progression identity.

On success it prints \(r_l,r_{lD},i,\lambda(l),\lambda(D)\), both normalized coefficient lists,
and the verified finite root congruences.  It checks
\[
h_l(Dx-i)=\lambda(D)h_{lD}(x),\quad D\mid\lambda(D),\quad
\lambda(D)\le D^{\deg h},\quad \operatorname{rad}\lambda(D)=\operatorname{rad}D.
\]

The checker only establishes those finite statements.  A residue modulo one p-power does not
certify a compatible \(\mathbb Z_p\) root, its multiplicity, intersectivity, or a density result;
record those as separate inputs.  The algebra is also independently derived in
`local-root-restriction.md`.

The broader (not necessarily unit-root) formulation used here is Lemma 2.2 and equation (2.2),
pp. 7--8, in OpenAI, *A power saving for intersective polynomial differences with an exponent
depending only on the degree* (5 October 2026), SHA-256
`d69e417ac953581d7f373c9457e809e47ad4b534c1f79407ff5c0e13f382b605`.
