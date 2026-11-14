---
name: probability-self-avoiding-walks-and-sle
description: Analyze rigorous self-avoiding-walk growth and graph methods, and audit proposed links from planar lattice walks to continuum SLE.
metadata:
  short-description: Audit SAW growth and SLE interfaces
---

# Evidence state

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

This independent W23 final-scope package contains 30 distinct works: 28 full-text reads and two accepted canonical SLE-use records. The latter reuse accepted W08 full reads and do not represent new readings. One full read is a complete 73-page proceedings-chapter/lecture-notes contribution, not a whole-book read. The final W23 scope passed R03 review with publication approval; this portable package is staged for independent runtime review, and nothing has been published or installed. See [stage status](evidence/W23/status.json), [runtime source ledger](evidence/W23/sources.json), [R03 final approval](evidence/review/review.json), [reading dossier index](review-index.json), and [source guide](source-guide.md).

# Choose the method by the path model

Before selecting a theorem, record: graph/lattice and dimension; rooted or unrooted counts; strict or weak self-avoidance; walk or trail; uniform or weighted law; finite or infinite graph; annealed or quenched environment; boundary/conditioning; observable; the exact limiting operation and quantifiers; and whether each bound is strict `<` or non-strict `≤`. Do not silently change the source inequality.

- **Scalar connective constants and graph SAW:** use the regular/transitive/height-function/bridge/weighted/extendability results only when the graph action, local finiteness, degree, unimodularity, orbit, weight, and bridge hypotheses match. Check whether the result is a supremal growth constant, a rooted liminf/limsup, or an actual limit.
- **Planar lattice counts:** use honeycomb parafermionic identities only for their stated lattice observable; use Hammersley–Welsh/bridge unfolding and polygon insertion only with the exact polygon abundance, joining cost, and length/density conclusion. Upper density one does not imply natural density one. Keep infinitely-many-length bounds, subsequence bounds, all-large-n bounds, and conditional theorems separate.
- **Bridge renewal and sub-ballisticity:** identify the bridge orientation, renewal points, stick-break/diamond assumptions, norm, threshold, and n or T range. Do not repair a source’s finite-size defect silently; record the source statement and separately state only a verified valid range or prefactor.
- **Quenched random environments:** distinguish environment law from path law and quenched from annealed counts. Preserve limsup versus limit, root dependence, p/dimension range, and any finite modification/coupling argument.
- **Continuum SLE:** SLE dimension/trace results apply after a separate discrete convergence and identification theorem. State curve topology and parametrization. Tightness, discrete domain-Markov/conditioning, convergence and identification are separate obligations; a scalar connective constant or discrete-holomorphic identity does not provide them.
- **Specialized auxiliary methods:** random quadrangulations/LQG, hyperbolic graphs, finite hypercubes, spread-out lace expansion, and continuous-time weak SAW are valid only in their own stated models. Do not transfer their limits to fixed honeycomb lattice or the planar quenched-percolation problem without a proved interface.

# Required analysis and output

For each proposed claim, give (1) exact model and law; (2) theorem/source and physical PDF page; (3) all hypotheses and quantifiers; (4) proof chain and constants; (5) proof inputs cited but not read, omitted/sketched steps, or source anomalies; (6) conclusion type (limit, limsup, liminf, upper-density-one, subsequence, finite-range estimate); (7) the precise transfer interface still needed. Keep a source theorem distinct from any derivation or conditional template.

Use [mapping.json](mapping.json) to route C107/C108 and [reading_coverage.json](reading_coverage.json) for complete read coverage. The cards under [evidence/root/workers/W23/cards](evidence/root/workers/W23/cards) are the exact R03-bound card bytes. Local evidence uses paths inside `evidence/root/`; [portable_path_bindings.json](portable_path_bindings.json) maps original repository-relative paths to the packaged copies.

# Non-transfer rules

- **C107 remains unproved here:** no lattice SAW curve tightness, discrete DMP, curve-topology weak convergence, or SLE(8/3) identification is established by these 30 sources. The two canonical SLE cards are continuum-only.
- **C108 remains unproved here:** S003 gives a root-independent limsup rate and strict planar quenched/annealed gap; it does not establish the full nth-root limit or root independence of that limit.
- Preserve P50’s unresolved boundary-to-radius/pattern proof inputs, P51’s literal all-Ω counterexample and conditional kite/lift assumptions, P54’s exact official-v1/date caveat and spread-out hypotheses, P56’s weak-SAW Z^4 model and imported RG proofs, P29’s random-map metric model and GM16 dependency, and P43’s finite-hypercube range/denominator boundary.
- Numerical MATLAB/Python artifacts are finite algebra/count consistency evidence only. They do not prove asymptotics, strict gaps, tightness, or convergence.

For concrete positive, conditional, and missing-interface patterns, see [examples/positive.md](examples/positive.md), [examples/conditional.md](examples/conditional.md), and [examples/missing-interface.md](examples/missing-interface.md).
