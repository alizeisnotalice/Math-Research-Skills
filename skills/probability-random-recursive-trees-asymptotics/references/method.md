# Method router and model gates

**Immutable evidence state: 30 distinct complete source works independently accepted. Exact source versions, theorem/proof boundaries and source-local defects are retained in cards and local source decisions. A127 remains unproved.**

## 1. Normalize the model before choosing a theorem

Record:

- the split/growth kernel (q(m,i)), or the offspring law / insertion rule;
- whether edge lengths are unit, exponential, or another distribution;
- CTCS continuous time versus DTCS split-count time;
- ordered interval leaves versus an unordered topology, and whether leaf labels are exchangeable;
- whether a vertex, a leaf, an unordered pair, or a prescribed geometric pair is sampled;
- the statistic/toll and its boundary values;
- the target scale, centering, variance and mode of convergence.

For the critical Beta-splitting sources read in this batch,
\[
q(m,i)=\frac{m}{2h_{m-1}i(m-i)},\quad 1\le i<m,
\]
with CTCS hold rate $h_{m-1}$. For a uniform random leaf, the next clade size $k<m$ has law $1/[h_{m-1}(m-k)]$. Consequently the source-level recurrences are
\[
\mathbb ED_m=\frac1{h_{m-1}}\left(1+\sum_{k<m}\frac{\mathbb ED_k}{m-k}\right),\qquad
\operatorname{Var}D_m=\frac1{h_{m-1}}\sum_{k<m}\frac{\operatorname{Var}D_k+(\mathbb ED_m-\mathbb ED_k)^2}{m-k},
\]
and
\[
\mathbb EL_m=1+\frac1{h_{m-1}}\sum_{k<m}\frac{\mathbb EL_k}{m-k},\qquad
\operatorname{Var}L_m=-1+\frac1{h_{m-1}}\sum_{k<m}\frac{\operatorname{Var}L_k+(\mathbb EL_m-\mathbb EL_k)^2}{m-k}.
\]
These equations are for the source's uniform-leaf quantities. Do not transfer them to a maximum, another leaf-pair rule or another edge-time convention without deriving the change.

For the harmonic-descent transforms in RT002, \(\phi_n(u)=\mathbb E e^{uD_n}\), so this is a positive-mgf convention even though the paper calls it a Laplace transform. Use the common real domain \(u<1\) for all \(n\ge2\); \(D_2\sim\mathrm{Exp}(1)\) makes the moment infinite at \(u\ge1\). Verify transform domains before differentiating or iterating the recurrence.

## 2. Choose the proof route by the actual recurrence/interface

### Exact moments and recursive height limits

Use the recurrence itself when it is available. Differentiate a generating/Laplace recurrence only after checking the transform convention and boundary terms. A variance equation may contain a non-obvious additive term (the source's edge-height variance recurrence has (-1)); do not infer it from the time-height one. For asymptotic CLTs proved through recursive envelopes, record the envelope inequality, uniform range, transform convergence theorem, and whether the proof establishes all moments.

- RT002 uses a direct sum recurrence, harmonic-sum/Euler–Maclaurin estimates, comparison sequences, and Laplace-transform upper/lower envelopes. Its leading (D_n) variance equivalent and CLT do not require the h-ansatz; its sharper (O(1)) variance remainder and random-pair decorrelation do. For Proposition 2.8's \(\operatorname{Var}L_n=c\log^3 n+O(1)\), retain the theorem statement but isolate the final p. 24 bounded-residual argument as unverified: a unit-row-sum recurrence with bounded forcing alone does not establish a uniform bound. The same harmonic weights with forcing 1 give the mean recurrence for \(L_n\), whose source asymptotic grows like \(\log^2 n\); this is a counterexample to that inference rule, not to Proposition 2.8's variance result. Do not use finite-n recurrences to certify the remainder or infer that the theorem is false.
- For a maximum over leaves, first obtain a uniform-leaf tail/mgf estimate, then apply the explicit union bound used by the source. Do not confuse its scale with the uniform leaf's mean.

### Harmonic descent and Mellin inversion

Use this route if the target is representable as absorption/occupation along the harmonic-descent chain and the source's limiting partition process applies. For critical Beta splitting, RT005 gives the transition $p(j,i)=1/[(j-i)h_{j-1}]$ and fixed-state occupation limit $a(n,i)\to 6h_{i-1}/[\pi^2(i-1)]$. Its proof first identifies the stationary-flow solution, then establishes existence by continuous-time shift coupling and a logarithmic overshoot bound. The separately cited absorption-time estimate is an input, not proved in RT005. This is a one-uniform-leaf fringe input, not a prescribed pair-separation result. Preserve the real parameter range and root choice in the digamma equation. A Mellin argument needs the source's transform identity, convergence strip, inversion/integrability justification, contour displacement, residues, and remainder bounds. A list of poles or formal residue sum alone is insufficient.

- RT004 provides very sharp one-leaf $D_n$ expansions, variance, mgf, CLT and large deviations. Its p. 3 prose swaps D/L labels immediately after (1.3), while (1.4)–(1.5) and the theorem scales use \(D_n=\) CTCS continuous time-height and \(L_n=\) DTCS hop-height; preserve this discrepancy and keep the equation-consistent convention explicit. The source's \(\sim\) expansions mean that each finite truncation has an error of the largest omitted order (§3.1), and the formal infinite sum need not converge. At \(z=0\), interpret the gamma-prefactor by its removable limit 1 (§12.1, equation (12.10)). RT004 explicitly says its Mellin methods give only the mean for $L_n$, not an $L_n$ variance/CLT.
- RT003 gives exchangeable-partition construction, an exact typical-leaf fringe chain, and independent side subtrees conditional on reverse-chain transitions. Its growth construction starts at the root and traverses toward a uniformly chosen target bud, with source CTCS rate per edge/time length. It does not provide the A127 fixed-separation covariance limit.

### Markov-branching scaling limits

Use RT009 only after expressing the finite trees through the paper's partition-law Markov-branching family. Check the weighted rare-macroscopic-split condition
\[
n^\gamma\ell(n)(1-s_1)q_n(ds)\xrightarrow{w}(1-s_1)\nu(ds)
\]
as finite measures, with $\gamma>0$ and $\ell$ slowly varying. Theorem 5 concerns a prescribed number of leaves with uniform leaf measure; Theorem 6 concerns a prescribed number of vertices and additionally requires $q_1((1))=1$ and either $0<\gamma<1$, or $\gamma=1$ with $\ell(n)\to0$. Both use rooted GHP convergence at scale $n^\gamma\ell(n)$. Verify the measured space, branching convention and edge metric separately: a global metric-measure limit does not by itself yield a pair law conditioned on a deterministic circular gap. The conditioned-GW and unordered-tree applications in §§5–6 need their own offspring/split-law and approximation checks.

### Fringe/additive functionals in BST and recursive trees

For (F(T)=\sum_{v\in T} f(T(v))), check the actual tree family, size profile, moments of (f(T_k)), and variance kernel. In Holmgren–Janson Theorem 1.20, the BST conditions are
\[
\sum_k\frac{\sqrt{\operatorname{Var}f(\mathcal T_k)}}{k^{3/2}}<\infty,\quad
\operatorname{Var}f(\mathcal T_k)/k\to0,\quad
\sum_k(\mathbb Ef(\mathcal T_k))^2/k^2<\infty;
\]
the random-recursive-tree theorem uses its own Λ-law and covariance kernel. The paper's cyclic representation and Stein couplings are model-specific. The sufficient growth corollary (|f(T)|=O(|T|^\alpha)), α<1/2, only applies within the stated BST/RRT settings.

### Additive tolls on conditioned critical Galton–Watson trees

For the read conditioned-GW theorem, take \(n\to\infty\) only along admissible sizes with \(\mathbb P(|\mathcal T|=n)>0\); periodic offspring laws can restrict the support. Require (E\xi=1), (0<\operatorname{Var}\xi=\sigma^2<\infty), an integrable toll, the stated conditional toll-mean limit, and (for its CLT) both (E f(\mathcal T_n)^2\to0) and \(\sum_n \sqrt{E f(\mathcal T_n)^2}/n<\infty\). Preserve
\[
\gamma^2=2E[f(\mathcal T)(F(\mathcal T)-|\mathcal T|\mu)]-\operatorname{Var}f(\mathcal T)-\mu^2/\sigma^2.
\]
The proof uses the conditioned i.i.d. degree sequence, an (m)-dependent CLT and projection correction for the conditioning variable, followed by truncation. At the finite-support projection step, source equations (7.8)–(7.10) give \(\operatorname{Cov}(Y,S_n)=-\mu\) and \(\widetilde Y_n=Y_n+(\mu/\sigma^2)(S_n-n)\); the plus sign yields residual variance \(\beta^2-\mu^2/\sigma^2\). Distinguish this root-local Kesten limit from the ordinary-GW limit for an annealed uniform fringe subtree in Theorem 1.3. Critical Beta-splitting is size-dependent and is not an ordinary iid-offspring conditioned-GW model by definition. Require a proved exact representation before transferring.

### Pair-distance sums and empirical profiles (auxiliary methods)

RT012 studies $W(T)=\tfrac12\sum_{v,w}d(v,w)$ for conditioned critical GW trees with mean-one offspring and $0<\sigma^2<\infty$, along admissible sizes. Its exact identity $W=nP-Q$ separates root path length $P$ and ordered common-ancestor sum $Q$; its contour proof gives an excursion functional, while the moment theorem additionally needs a uniform-integrability argument. RT013 treats the full ordered vertex-pair distance profile, including diagonal pairs and linear interpolation, with the same finite-variance conditioned-GW gates and $n^{1/2}$ graph-distance scale. For unrooted simply generated trees it additionally requires a positive radius of the weight EGF, an equivalent critical offspring law and finite variance. Its contour argument first identifies an empirical pair-distance measure; tightness is separately needed for convergence of profiles as functions.

These methods can analyze a globally averaged pair statistic or empirical profile after the tree model and sample measure match. They cannot replace a separation-conditioned two-leaf recursion. Uniform pairs, vertex pairs, leaf pairs, and a cyclically shifted pair at deterministic gap are distinct sampling laws even if their one-point marginals agree.

## 2A. Additional profile, fringe, urn, and split-vector routes (accepted in the current R02 30-source stage)

These methods are source-specific auxiliary routes. Their cards and page coverage are mirrored under `evidence/W22/`; all eight are included in the current central R02 accepted set of 30. Older per-batch pending labels are historical snapshots. None proves A127’s deterministic cyclic-separation covariance. RT007/RT037/RT042 passed the B7 helper stage and are now accepted in the R02 30-source binding; their source gates are recorded below and in `references/sources.md`.

- **Indexed level covariance/width (RT014):** use the RRT or BST bivariate profile generating function and the source’s uniform singularity/saddle-point estimates only for depth-level counts, with the stated `k,h≥1` and limiting depth ratios in `[0,2)`. Keep RRT and BST profile conventions separate. A level index is not circular leaf separation.
- **Function-valued search-tree profile (RT016):** first establish the exact `(m,t)` pivot recurrence, profile polynomial and dominant-root normalization. The contraction route requires the source Hilbert/analytic function-space, centering, moment, local `L^s` contraction and small-subtree hypotheses; coefficient extraction additionally uses its off-angle bounds and restricted `I′` range. Do not enlarge the source’s proved parameter interval or transfer to a Beta tree without an exact recursive distributional equation.
- **RRT profile via CMJ renewal (RT017):** the theorem uses `X_{floor(n^s)}` and the compact-uniform time change `tau_{floor(n^s)}/log n → s`, with product-`J1` convergence. Preserve its stated finite nonzero interarrival variance/moment conditions. It is a one-tree profile process, not a pair law.
- **Fixed-size fringe counts (RT018):** for RRT, the Berry–Esseen theorem assumes `k=o(sqrt(n))`; the Poisson approximation has its own growing-`k` range. The BST section states analogous results but omits proof details. Keep the vertex-fringe sampling and model-specific split recurrence; do not infer a leaf-pair theorem.
- **Stopped CMJ fringe embedding (RT022):** before using the survey’s fringe laws, verify A1–A5 (including nonlattice and Malthusian conditions), the selected characteristic’s A6 when required, and the exact stopping weight. For its size/time conclusions, verify the relevant weight condition and remember the lattice caveat. The survey does not supply an embedding of the target CTCS Beta clade law.
- **Finite-type urn CLT (RT028):** verify all of A1–A7, including the at-every-`n≥1` dominating-type condition, the replacement tenability convention, second moments, a simple positive dominant eigenvalue and strict non-dominant `Re(lambda)<lambda_1/2`. The source’s application bridge proves A7 for its particular positive-activity urns; positive activity alone is not a generic replacement for A7. Its m-ary-search-tree range is `2≤m≤26`.
- **Split-vector additive tolls (RT031):** match the full allocation rule and parameters `(s,s0,s1)`, fractional ball-loss condition, supercritical positive-mass requirement, toll-size/moment gates, and exact conclusion (first-moment asymptotics, weak law, or `L2` fixed point). The standing assumptions permit zero split coordinates, but the printed `log(V*)` lattice criterion does not define `log 0`; use the literal lattice dichotomy only under `P(V*>0)=1` or after a separate positive-support size-biased renewal argument.
- **RRT/PA split representation and pair decomposition (RT034):** use the GEM/PD split representation only for its linear PA/RRT parameter range and preserve the child relabeling/order-of-appearance caveat. The all-node-pairs common-ancestor statistic and its representation do not encode A127’s ordered leaves, cyclic shift, or deterministic gap.

## 2B. Beta-splitting definition, tree-limit topology, and finite-state GW recursion (B7 sources accepted; final closure pending)

These sources sharpen model and proof-interface checks but do not close the A127 gap. RT007 defines the finite-clade Markov-branching split kernel and beta family; match the target's exact finite-n split law, conditional uniform label-subset rule, edge-length convention, and leaf order before using its parameter-specific branch/depth results. Its 20-physical-page author manuscript is one chapter, not the edited book, and §5 gives proof outlines rather than full derivations of every asymptotic estimate.

RT037 distinguishes tree-limit notions through iid uniform-vertex distance matrices, long-dendron/metric-measure topology, and separate model-specific conditioned-GW, split-tree, and CMJ hypotheses. For logarithmic trees, Theorem 12.2 needs both a uniform-vertex depth limit and negligible LCA depth. Pair-distance tightness or a constant-twig limit does not establish an ordered leaf pair at deterministic circular separation. Keep topology and sample measure explicit.

RT042 applies to critical finite-variance conditioned GW trees, admissible conditioning sizes, a finite state space, iid node noise, and a recursive update whose common-noise spine chain is coalescent. Its conditioned-root proof uses local total-variation convergence to the Kesten tree, coupling of matching truncations, and the finite-variance off-spine height bound. Do not replace coalescence with a communicating-class condition. Theorem 2 is finite-state; unbounded path-length extensions require their own tightness and a valid target representation. The source's §7.3 edge/vertex convention discrepancy is recorded in its card.

None supplies an exact CTCS representation or fixed-gap ordered-leaf sampling interface for A127.

## 3. A127-specific gate: prescribed cyclic separation

For A127 retain all parts of the formal statement: CTCS$(n)$, interval/circular order, a uniform random cyclic shift, and a deterministic circular separation $r_n$ with $\log r_n/\log n\to\alpha$. Its two marginal heights are uniform-leaf $D_n$, but the joint law is not a uniformly chosen distinct pair. Accordingly:

- RT002's random-pair correlation (O(1/\log n)) (conditional on h-ansatz) is not the A127 result.
- RT003's exact \(\mathrm{Exp}(1)\) branchpoint for a random pair and its typical-leaf fringe chain do not encode deterministic circular distance.
- RT004's one-leaf CLT/mgf/large-deviation theorem has no pair process.
- RT019/RT020 local-fringe/additive CLTs do not transfer until the entire model, representation and toll hypotheses are shown.

A valid proof route needs a new separation-conditioned pair recursion or another representation preserving circular order, cyclic-shift sampling and (r_n); it also needs uniform error control over the regime that produces (1-\alpha\). An unverified heuristic or finite numerical fit is not a theorem.

## 4. Numerical and symbolic checks

Use local exact arithmetic for kernel normalization and rational transition sums, and a high-precision system for symbolic constants/finite recurrences where useful. Save code, runtime, output, and exact source equations. State explicitly what the calculation checks and does not check. First-batch calculations are in `../evidence/W22/checks/kernel_recurrence_check.py` and its `.txt` output; batch-2 occupation and Wiener-moment calculations are in `../evidence/W22/reading_batches/batch2/checks/RT005_RT012_checks.py` and its `.txt` output.
