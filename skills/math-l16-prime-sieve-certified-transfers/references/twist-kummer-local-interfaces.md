# Twist and Kummer local interfaces

Sources: SHA `718fcfce4014a878685365edfb8a285a611512dea362dc5a9e1dc93d023cd7b1`
(p.6), `4d805627401fffef78e1f0d8e21a0585f6c733e8be90643d0065cd27ffaa24f2`
(pp.4--5), and `36a58d5f408acc3d5430e1da1397aaaa7900321c3322a2001dcf7e6fc4de7fc0`
(p.18). Scoped reference.

For a curve and finite bad-prime set `S`, split a signed squarefree twist `b=b_S b_0`;
choose the sign of `b_0` to obtain admissible `d==1 mod 4`, and retain the finite
`S`-twist `F'`. The source records `F(b)≅F'(d)` and `|d|<=|b|`; track the bounded
multiplicity rather than treating it as one-to-one.

For declared function fields, completion/norm bookkeeping gives a closed ell-saturated
subfield image and inclusion-then-norm equal to `[F:E]`. The exceptional-prime bound
uses a supplied cyclic character eigenspace of S-units; all ramification/active-prime
hypotheses must remain explicit.

## 固定来源

- 物理页 6。Lemma 2.1 reduces signed squarefree twists to a finite S-twist family and admissible d; Lemma 2.2 records the good-prime local twist rule. SHA-256 `718fcfce4014a878685365edfb8a285a611512dea362dc5a9e1dc93d023cd7b1`。[The mean analytic rank of quadratic twists of elliptic curves](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-October-6-2026/paper.pdf)
- 物理页 4, 5。Lemmas 2.1--2.4 give continuous Kummer evaluation, saturated subfield embeddings, finite-extension norm multiplication, and curve order kernels. SHA-256 `4d805627401fffef78e1f0d8e21a0585f6c733e8be90643d0065cd27ffaa24f2`。[The Bogomolov-Pop reconstruction theorem](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Bogomolov-Pop-reconstruction-theorem-September-23-2026/paper.pdf)
- 物理页 18。Proposition 5.3 bounds a specified set of missed primes using Kummer classes in one cyclic-character eigenspace and equivariant S-unit rank. SHA-256 `36a58d5f408acc3d5430e1da1397aaaa7900321c3322a2001dcf7e6fc4de7fc0`。[Open Homomorphisms of Global Solvably Closed Galois Groups](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/open-homomorphisms-solvably-closed-galois-groups.pdf)
