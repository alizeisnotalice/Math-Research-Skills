# equivalence from fully faithful cancellation

**Source.** *Global Quantum Geometric Langlands at Irrational Level*,
pp. 101, 111–112, 114, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/quantum-langlands.pdf).

**Input.** Provide categories \(A,B\), fully faithful comparison embeddings,
functors \(f:A\to B\), \(f'\), \(L,R,M,M',S,S'\), and pseudo-identities
\(e_A,e_B\), together with coherent natural isomorphisms sufficient to derive
the paper's identities
\[
(S')^\vee\simeq fL,\qquad R\simeq(M')^\vee e_B^{-1}\Phi,
\]
and Plancherel relations
\(e_A(R')^\vee R\simeq\mathrm{Id}_A\),
\(e_B(S')^\vee S\simeq\mathrm{Id}_B\).  If family compatibility is wanted,
also supply the comparison after localization and its collision/insertion
coherences.

**Procedure.** Define \(\Phi=e_Bf\). Form the left and right inverse
candidates from the displayed adjoints/duals. Use the identities and full
faithfulness to obtain \(\Psi_{left}\Phi\simeq\mathrm{Id}_A\) and
\(\Phi\Psi_{right}\simeq\mathrm{Id}_B\), then identify the two inverses by
composition. Lift localization compatibility through the fully faithful
embedding; uniqueness follows by precomposition with fully faithful
localization.

**Output.** A specified equivalence with specified inverse and, when supplied,
the inherited family/localization compatibility.

**Boundary.** This is diagram cancellation, not a constructor for Ran spaces,
torsors, Whittaker data, determinant twists, or the input period pairings.

## 固定来源

- 物理页 3, 101, 111, 112, 114。Lemma 12.2; equations (12.3), (13.3)–(13.5); Theorem 13.5 SHA-256 `8d9bc135865dbc97a76efbf10fd7b9631bbe1107bd87c467b64db60eb3f229f1`。[Global quantum geometric Langlands at irrational level](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Global-quantum-geometric-Langlands-at-irrational-level-October-4-2026/quantum-langlands.pdf)
