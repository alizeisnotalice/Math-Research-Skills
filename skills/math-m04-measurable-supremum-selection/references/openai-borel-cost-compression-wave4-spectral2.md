# Borel relation compression interface

Scoped reference. *A group without fixed price* (OpenAI, 5 Oct 2026),
SHA-256 `aa2ee4de0db26fc8aa62f95ec695e2ef11db6c9b326d2d354465aa50bee4c078`,
physical pp. 7--10, Lemmas 3.1--3.3 and Corollary 3.4.  On a finite-measure
standard Borel space with a countable measure-preserving Borel ambient
relation, use `kappa(U;W)=integral_W 1/|[z]_U| d lambda`.  First choose a
Borel `T`-complete set of measure at most `kappa(T)+epsilon` (one least
point per finite class; a finite separating partition and a marking for
infinite classes).  If `S subset T subset Q=S vee E`, delete one
shortest-distance edge from each finite `S`-class outside a complete set,
push surviving edges by a Borel map into that set, and split at both
endpoints.  The resulting partial-isomorphism family `F` obeys

`Q=T vee F`, `C(F) <= C(E)-kappa(S)+kappa(T)+epsilon`.

In particular a p.m.p. Borel relation with all classes infinite has cost at
least one. [Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-group-without-fixed-price-October-5-2026/unequal-costs-rank-100-amalgam.pdf).

The construction requires the displayed finite-measure, Borel enumeration,
measure-preservation, and finite-total-cost hypotheses.  It does not build
an orbit relation or establish a group cost statement without these inputs.
