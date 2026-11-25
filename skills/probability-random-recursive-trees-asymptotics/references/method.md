# Method router and model gates

## Evidence and scope control

The source-bound matrix contains 30 R10 high-reviewed legacy scope overlays and 9 previously accepted R12 G23 scoped uses (39 use rows, 38 current distinct works after the RT004 duplicate). R10 checked 239 aggregate references with zero failures and added zero new read/source credit. Its decision is explicitly `PASS_30_exact_reader_scoped_bindings_not_whole_entry`. Use the exact row conditions and transfer limits in [the source ledger](sources.md); no broader theorem headline is admitted by a narrower row. The standalone portable build contains the same matrix and source evidence.

## 1. Normalize the model before choosing a method

Record the tree construction, split/offspring law, vertex or leaf labels and order, root convention, time versus edge metric, statistic/toll, sampling rule, conditioning sizes, and asymptotic regime. Write the finite-size recurrence including boundary terms before selecting a theorem. Distinguish CTCS continuous height `D_n`, DTCS hop height `L_n`, global maximum, fixed-gap pair, uniform random pair, and vertex-pair statistic.

## 2. Route to a source-matched interface

- For the critical Beta-splitting uniform-leaf CTCS recurrence, use RT002's admitted split/size-biased child law, holding rate, and mean/moment recurrence. RT002's p.24 bounded edge-variance remainder is held. Do not infer a CLT or pair theorem from the recurrence alone.
- For fixed-state harmonic-descent occupations, use RT005 with its exact transition law, fixed state and continuous-embedding rates. Do not infer a growing-state estimate or two-leaf law.
- For the reverse chain / sibling-tree interface, use RT003 only with the finite reverse flow, distinguished uniform leaf, fixed depth and terminal-state condition.
- For the finite harmonic-binomial mean identity, RT004 has an unconditional finite convolution proof. Its R12-approved Mellin route is a separate, single-uniform-CTCS-leaf interface requiring `Re(s)>1`, finite weighted measure, justified differentiation/residue subtraction, vertical integrability, and fixed-truncation remainder. It gives no pair-gap Tauberian result.
- For Markov-branching limits, RT009 requires the exact partition-law family and weighted rare-split condition; keep the leaf/vertex gate and the full stopped partition with multiplicities and unary delays. This overlay does not certify the full GHP route.
- For conditioned-GW pair sums/profiles, RT012/RT013 require critical finite-variance offspring, admissible sizes, the source contour representation, pair sample measure, and each separate moment/UI or profile-tightness hypothesis. These are global vertex-pair/empirical-profile methods, not cyclic leaf-gap methods.
- For each other legacy source use, consult the 30-row matrix. Examples of scope narrower than the source title: RT018 is accepted for its exact RRT fringe recurrence/moments only; RT028 for the finite-type activity/eigenvalue aggregation and explicit spectral gate; RT030 for first-moment Eq. 5.3 only; RT035 for the raw second-moment/martingale interface with A1–A6 and Jordan-L2 conditions; RT037 for a sampled-distance criterion with its log-depth/LCA bridge, not GHP convergence.

## 3. G23 atomic-method coverage: restricted interfaces only

Every entry in the method-condition matrix（本机附件：`references/method_coverage.json`） is an independently accepted source-specific interface. An accepted interface does not complete the general method or prove the target A127 limit.

| Method | Accepted scoped source interface | Required gate / remaining transfer gap |
|---|---|---|
| G23.01 double-marked spine/MRCA | Foutel-Rodier–Schertzer exact marked k-spine identity | Generation-indexed type-dependent branching process; conditional-iid child marks; positive finite h-transform, required factorial moments/normalizers, `ν_j>0`, integrable weighted test, exact `Δ_k` and `N−MRCA` metric. No verified CTCS representation or cyclic-gap transfer. |
| G23.02 many-to-two/joint moments | Foutel-Rodier–Schertzer many-to-few; Ma strict-prethreshold all-q-set PPP | Preserve each source's sampling, threshold and fragmentation hypotheses. Neither interface is a fixed cyclic-gap pair law. |
| G23.03 renewal/occupation/recursive comparison | Kolesnik Claim 3.5; Iksanov–Nikitin–Yakymiv Prop. 2.1; Ma DTCS maximum-height route; CMS tagged-potential route | Exact critical kernel, one-lineage or all-leaf statistic as selected, source's forcing/size and subordinator gates. No two-lineage fixed-gap inference. |
| G23.04 additive/martingale and maximum interfaces | Ma DTCS maximum height; CMS beta-fragmentation maximum | Exact zero-erosion binary fragmentation, independent labels/lifetimes, model and moment gates. Scalar maxima give no designated-pair limit. |
| G23.05 Mellin/singularity analysis | RT004 one-leaf mean-Mellin; CMS fixed-truncation mean expansion | Exact transform strip, integrable inversion or local-uniform positive-residue series, fixed truncation and remainder. No pair-gap uniformity. |
| G23.06 second-order UI | RT001 source-normalized marginal second moment and product-UI deduction | Critical Beta model and uniform marginals under the prescribed cyclic shift. Product UI follows from the source marginal bounds; it does not imply joint convergence or identify covariance. |
| G23.07 regular variation/tree scaling | HMPW conservative fragmentation scaling | Nontrivial conservative dislocation, zero erosion, regular variation with `γ∈(0,1)`, log-integrability and strong sampling consistency. Critical Beta `β=-1` is excluded; no CTCS fixed-gap law. |

The seven method IDs have scoped evidence rows, while the broad interfaces remain conditional on those gates. No `method_ids` were added by the 30 R10 legacy overlay rows. Historical RT018/RT028/RT030/RT035/RT037 headlines are not method credit beyond the current rows.

## 4. A127 gate: prescribed cyclic separation

A127 keeps CTCS, original interval/circular leaf order, a uniform random cyclic shift, and deterministic gap `r_n` with `log(r_n)/log(n)→α`. A uniformly chosen pair has a different sampling law. RT001 §3.9, equation (40), physical p. 22, calls the proposed `(1−α)` behavior Open Problem 1. The accepted RT001 contribution is the marginal-normalization/product-UI deduction only. A proof still needs a two-lineage law preserving the cyclic order and prescribed gap, plus uniform error control through the `r_n` regime. Neither the random-pair covariance in RT002, the tree-fragmentation q-set limit in Ma, nor the typed-spine formula in Foutel-Rodier–Schertzer supplies that target law.

## 5. Numerical checks

Use the saved exact calculation（本机附件：`evidence/calculations/recursive_cases.py`） and its output only as finite/symbolic checks: the CTCS kernel and mean identity are verified for `2≤n≤20`; one four-leaf comb separates cyclic gaps from the uniform-pair average; a Gaussian coupling shows UI does not force a covariance limit. None is a proof of an asymptotic theorem or a counterexample to A127's limit.
