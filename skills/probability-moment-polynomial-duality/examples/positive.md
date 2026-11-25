# Positive example: exact two-block moment LP

Let `X∈{0,1}^4` have two blocks of size two, reference law iid Bernoulli(1/2), and objective `f=1{S_1≥1 and S_2≥1}`. A valid k-wise LP for `k=2` must constrain:

- `E S_b=1` for each block;
- `E (S_b)_2=1/2` for each block;
- `E S_1 S_2=1`, the mixed cross-block pair constraint.

The last identity follows from the two coordinates per block and `p²=1/4`. It cannot be omitted merely because the reference total count `S_1+S_2` is known. The primal assigns mass to the nine `(S_1,S_2)` count pairs, with conditional uniformity within each block justified by block symmetrization. Its dual is a degree-≤2 polynomial majorant/minorant of `f` on the full four-bit cube, not just on an averaged count value unless the symmetry reduction is proved.

The L07 script also gives an exact alternative law that preserves the full distribution of `S_1+S_2` but has `E[S_1S_2]=3/4`, so a fixed pair across blocks has joint-one probability `3/16` instead of `1/4`. That law is a counterexample to the claim that matching total-count moments suffices for 2-wise independence; it is not a counterexample to the full mixed-moment characterization.


### Exact primal and dual certificate

A local exact-rational enumeration checked all 84 candidate bases of the six-constraint, nine-count-pair LP. Twenty bases give feasible vertices; the minimum is `1/2` and the maximum is `2/3`. One minimizing count law assigns mass `1/4` to each of `(S_1,S_2)=(0,1),(1,0),(1,2),(2,1)`. One maximizing law assigns masses `1/6` to `(0,0),(1,2),(2,1)`, `1/3` to `(1,1)`, and `1/12` to `(0,2),(2,0)`. Uniformly lifting either count law within blocks gives every bit mean `1/2` and every distinct pair joint-one probability `1/4`.

With basis `(1,S_1,S_2,(S_1)_2,(S_2)_2,S_1S_2)`, pointwise lower and upper polynomials are

`L = -1 + S_1 + S_2 - (S_1)_2/2 - (S_2)_2/2` and `U = S_1/3 + S_2/3 - (S_1)_2/3 - (S_2)_2/3 + S_1S_2/3`.

They satisfy `L≤f≤U` on all nine count pairs and have product-law expectations `1/2` and `2/3`. The exact basis enumeration, pointwise slacks, and lifted pairwise marginals are saved in the actual SymPy run（本机附件：`evidence/project/expansions/20261115/readers/L07/math/l07_initial_checks.py`） and run output（本机附件：`evidence/project/expansions/20261115/readers/L07/math/l07_initial_checks.run.txt`）. This finite certificate is an example, not a general theorem about arbitrary block trees.


## Revision9 accepted finite-event certificates

### Weighted partial-pair lower bound

Take two events with `P(A_1)=P(A_2)=1/2`, `P(A_1∩A_2)=1/4`, and `c=(1,1)`. Each Yang–Alajaji–Takahara local LP has `p_i+p_12=1/2` and `p_i+2p_12=3/4`, forcing both masses to `1/4`; each local contribution is `3/8`. The sum gives `P(A_1∪A_2)≥3/4`, attained by the stated joint law. This is a finite local-LP certificate.

### Mixed block moments

For two singleton blocks with `P(A_1)=P(A_2)=1/2`, keeping the mixed moment `S_(1,1)=P(A_1∩A_2)=1/4` fixes the union at `3/4`. In larger block-count problems, keep every mixed `S_alpha` supplied through total order `m`; a one-sided binomial-basis polynomial is checked at every point of the product count grid.

### Known-mode finite-support count bound

For `n=4`, fixed mode `k=2`, and moments `S_1=2`, `S_2=8/5`, the original-p shape-constrained LP gives the sharp range `P(xi≥3) in [6/25,19/50]`. The exact upper primal is `p=(7/50,7/50,17/50,17/50,1/25)`; a lower primal is `(3/25,3/25,13/25,3/25,3/25)`. The output and dual multipliers are in `l07_r9_exact_shape_lp.out.json`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision9_1/math/l07_r9_exact_shape_lp.out.json`）; this is an exact rational calculation checked against finite LP dual certificates.


## Revision11 exact finite checks (reader-computed; independently checked in scoped R07 review)

- Hoppe–Nediak count LP: n=5, E[N]=6/5, P(N≥3)≤1/10. Exact rational vertex enumeration returns the sharp lower union probability 9/20 at masses (11/20,0,7/20,0,0,1/10).
- Known-mode count LP: n=4, mode 2, S1=2, S2=8/5. Exact rational enumeration gives P(N≥3) from 6/25 to 19/50 with feasible endpoint masses saved in the script output.
- Finite moment hull: n=4, S1=2, S2=3/2 gives S3∈[1/3,2/3].
- Qiu–Ahmed–Dey Proposition 2 incidence rays were checked exactly for all n=2,…,7 and layer sizes; this is finite computational corroboration, not the general projection proof.
- Hermann reflection factors were checked exactly for two paired support nodes at n=11,k=4,p=1/3.

See `l07_rev11_exact_checks.py`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision11/math/l07_rev11_exact_checks.py`） and `l07_rev11_exact_checks.run.json`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision11/math/l07_rev11_exact_checks.run.json`）.


## Revision12 exact block-moment example (reader-computed; R07 accepted scoped use)

For two size-2 blocks, compare the `law_A` and iid count distributions in `l07_pvr_1998_exact_block_moments.py`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision14_1_metadata_binding_delta/math/l07_pvr_1998_exact_block_moments.py`）. Both have complete total-count law `(1/16,1/4,3/8,1/4,1/16)` and union probability `15/16`; `E[ξ₁ξ₂]` is `3/4` for `law_A` and `1` under iid fair bits. Exact enumeration verifies the mixed-binomial-moment identity for all five nonzero indices of total degree ≤2 on the four-bit cube.


## R07 exact checks for the revised source interfaces

- Adler–Karp–Ross physical-p.7 displayed input: exact Theorem-5 formula correction `129023/1250000`, resulting lower bound `437949/625000`; the exact product law gives union `1197392257/1562500000` and remainder `263798507/1562500000`. These exact values establish why the printed `0.1896/0.7871` table entries are isolated while the general formula remains accepted.
- Prékopa–Subasi–Subasi supplied-mode example: `n=4`, `M=2`, `S1=2`, `S2=8/5` gives union range `[43/50,24/25]` with exact primal/dual certificates. Its tail objective range `[6/25,19/50]` is a derived change of objective.
- Prékopa–Vizvári–Regős normalized full-grid LP/dual includes `α=0`, `S0=1`, constant `y0`, and the origin. R07 independently checked its exact primal/dual route; the displayed Eq. (29) is excluded.

The Adler and PSS values above are R07 reviewer calculations, not new L07 runs.


## Revision15 exact reader checks

- **Limited independence:** for three Bernoulli(1/100) indicators `B_i`, the law with `P(111)=0`, each exact two-one atom `1/10000`, each singleton atom `49/5000`, and `P(000)=9703/10000` has all one- and two-coordinate marginals equal to the product Bernoulli law. For `X_i=1−B_i`, exact SymPy arithmetic gives `E∏X_i=9703/10000`, independent product `(99/100)^3=970299/1000000`, gap `1/1000000`, and `Σ Var(X_i)=297/10000`. This demonstrates the small-variance approximate-product setting without purporting to verify universal theorem constants.
- **Finite marginal LP:** for three Bernoulli(1/2) coordinates and event `Σ_i c_i≥2`, the law assigning 1/4 each to `000,011,101,110` is feasible and has objective 3/4. The affine dual `(c_1+c_2+c_3)/2` dominates the event indicator at all eight cube points and has marginal expectation 3/4. The exact rational primal/dual check is saved in `exact_checks.py`（本机附件：`evidence/project/expansions/20261115/readers/L07/revision15/math/exact_checks.py`） and its output.

## Selecting an admitted model

- For labeled Boolean k-wise laws, use the cube LP with one row for every coordinate subset. The symmetric count LP above is exact only after the within-block averaging argument.
- For several block counts, keep every mixed factorial or binomial moment and check the dual on the full product grid. The two-block certificate above is an exact small example.
- For arbitrary dependence with fixed finite discrete marginals, use the full product-support atom LP. The three-bit example in the revision15 section has a matching primal law and full-domain marginal-indicator dual.
- For a bounded product under k-wise independence, use Gopalan–Yehudayoff only as the admitted approximate expectation or tail component under its variance and order conditions. It does not replace the LP and does not prove tree recursion.

The full source-to-method mapping is in the R07 scoped-use index（本机附件：`references/source_use_index.json`）.
