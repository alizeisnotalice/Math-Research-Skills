# Accepted source register — G03

This register contains all rows accepted by R01 for this specific skill. It is generated from the exact accepted aggregate snapshot below; claims stay within each row’s theorem and hypotheses. All file references in this portable register resolve within this package. Original project paths and SHA-256 values are preserved in the local evidence map for provenance. The whole-entry review, root work-family deduplication/registration, and publication remain open. For provenance, original project paths are retained as `origin_path` in the local evidence map.

- Accepted rows: **32**; distinct work families: **32**; target range: **30–100**.
- Aggregate accepted snapshot: `../evidence/reviewer_records/aggregate_source_uses.json` (SHA-256 `bd02011dbfc2a1d3013fc4bb2baca2d9b317dae7cf207b4d232d0ba0f1c381d9`). The exact bytes are copied in `evidence/accepted_source_uses.json`.
- A source appearing under multiple method IDs remains one work in the total. Source-use row acceptance does not approve method completeness or release.
- Evidence artifact byte copies for the portable package are indexed by `evidence/source_evidence_manifest.json`; older source-card `pending` text is historical and does not override the explicit R01 admission row/review decision captured in the accepted snapshot.


## Portable evidence lookup

Every canonical source/evidence path below is preserved for provenance. In this package, resolve each exact artifact through `evidence/source_evidence_manifest.json`（本机附件：`evidence/source_evidence_manifest.json`）: the matching `origin_path` gives its byte-verified relative `portable_path` under `evidence/artifacts/`. The complete R01 decision chronology and exact supplemental review files are indexed in `evidence/reviewer_records_manifest.json`（本机附件：`evidence/reviewer_records_manifest.json`）.

## EXSRC-06692acb1e45b351 — The a priori Tan Theta Theorem for Spectral Subspaces

**Bibliography:** Sergio Albeverio, Alexander K. Motovilov (2010). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/06692acb1e45b3518a9cc21a6714dda6cfb3d1c229482f62f5af4f606f2d5fea/albeverio_motovilov_apriori_tan_theta_spectral_subspaces_arxiv1012.1569v3.pdf`; SHA-256 `06692acb1e45b3518a9cc21a6714dda6cfb3d1c229482f62f5af4f606f2d5fea`; version: Exact assigned arXiv:1012.1569v3, revised5July2012,18 physical/printed pages. Related IEOT73(2012)413–430 metadata independently verified from official records, not attributed to PDFp1; no VOR substitution/page mapping..

**Accepted interface:** Theorem 1 gives an a priori norm bound for the difference of the unperturbed spectral projection E_A(sigma0) and the actual perturbed in-gap projection E_(A+V)(omega0): ||P−Q||≤sin(arctan(||V||/d))<sqrt(2/3). In the selected finite-dimensional common-inner-product use, this is a projector-stability prerequisite for a separate Kato cluster argument; it does not give branch derivatives or splitting.

**Conditions:** Finite-dimensional Hermitian A,V in one fixed inner product. Exact spectral split sigma0/sigma1 with sigma0 inside finite open gap Delta of sigma1, both endpoints in sigma1; positive d=dist(sigma0,sigma1), D>=2d. V exactly off-diagonal relative to P=E_A(sigma0). L=A+V; Q=E_L(spec(L)∩Delta). Strict ||V||<sqrt2 d; for certified bounds use d_L<=d,v_U>=||V||,v_U<sqrt2 d_L and actual/validated projectors. Keep named external graph/Riccati and low-norm results explicit.

**Transfer limits:** No eigenvalue derivative, branch splitting, eigenvector regularity, root count, target index, gap-size estimate, non-self-adjoint transfer or application when the perturbation is not off-diagonal. Markov use additionally requires a fixed common Hilbert inner product and a separate proof of self-adjoint conjugation, off-diagonal structure and the norm bound.

**Usage card:** `../evidence/artifacts/38d9e3a80e3a1ebecfd592f2aca8afff793a5a83e621e26d44c5cce40e507522/EXSRC-06692acb1e45b351.md` (SHA-256 `38d9e3a80e3a1ebecfd592f2aca8afff793a5a83e621e26d44c5cce40e507522`).
**Reader freeze:** `../evidence/artifacts/821444c8e18880b537ef15465bd401093c1c0a9b712779dee3b89ccbb16ea2bd/freeze_round39_Albeverio_metadata_locator_delta.json` (SHA-256 `821444c8e18880b537ef15465bd401093c1c0a9b712779dee3b89ccbb16ea2bd`).
**Independent review:** `../evidence/artifacts/ba4ba8f616e03c535c5874edc7f0bf0120d3d50674fb9acf88f20e56cff3a9c4/review.json` (SHA-256 `ba4ba8f616e03c535c5874edc7f0bf0120d3d50674fb9acf88f20e56cff3a9c4`).
**Source card:** `../evidence/artifacts/e4b92cd89f65d69164ba7e4cc6e5273ed7fae6e90376f094a4b7c51f10b8d48a/EXSRC-06692acb1e45b351.md` (SHA-256 `e4b92cd89f65d69164ba7e4cc6e5273ed7fae6e90376f094a4b7c51f10b8d48a`).
**Accepted reading evidence:**
- `../evidence/artifacts/7302f3298a59ae55332c419ce4301beb696e5ef90a61c2f9afe8bc8ebb3f7da1/EXSRC-06692acb1e45b351.json` (SHA-256 `7302f3298a59ae55332c419ce4301beb696e5ef90a61c2f9afe8bc8ebb3f7da1`).
- `../evidence/artifacts/e4b92cd89f65d69164ba7e4cc6e5273ed7fae6e90376f094a4b7c51f10b8d48a/EXSRC-06692acb1e45b351.md` (SHA-256 `e4b92cd89f65d69164ba7e4cc6e5273ed7fae6e90376f094a4b7c51f10b8d48a`).
- `../evidence/artifacts/efc016f85bc4e861e8571d07d2430bd8a6f552f293b1eaaa9e674e2e23b8616c/albeverio_motovilov_exact.py` (SHA-256 `efc016f85bc4e861e8571d07d2430bd8a6f552f293b1eaaa9e674e2e23b8616c`).
- `../evidence/artifacts/258e159277ce5ffc3d62b3c9a33f0f89db77b35836a45a90c42d3f5dc5753267/albeverio_motovilov_exact.out.json` (SHA-256 `258e159277ce5ffc3d62b3c9a33f0f89db77b35836a45a90c42d3f5dc5753267`).
- `../evidence/artifacts/d5205698ce8ad52808144c17e0e269f0ca19c6d90856b1dd9a5ee929135c8893/albeverio_motovilov_proof_check.md` (SHA-256 `d5205698ce8ad52808144c17e0e269f0ca19c6d90856b1dd9a5ee929135c8893`).
- `../evidence/artifacts/0cf83e59045901338f9a1870cb34951c387047ee5ce1a7689ecebc4968db786c/render_manifest.json` (SHA-256 `0cf83e59045901338f9a1870cb34951c387047ee5ce1a7689ecebc4968db786c`).
**Additional review context:**
- `../evidence/artifacts/e5e43522e37fb17bc2ba0472782eb18ccc3b8c8178bb3871aec0a24022b7d2df/proof_check.md` (SHA-256 `e5e43522e37fb17bc2ba0472782eb18ccc3b8c8178bb3871aec0a24022b7d2df`).
- `../evidence/artifacts/a9117eb42d49486eeb4bbe6da20f50d6d6b237fc9145fc0f215d71eb8538369f/binding_check.json` (SHA-256 `a9117eb42d49486eeb4bbe6da20f50d6d6b237fc9145fc0f215d71eb8538369f`).
- `../evidence/artifacts/653643745e48dde7074b94dea22f121308d671a49d10238c573d6c12830e8646/preimage_verification.json` (SHA-256 `653643745e48dde7074b94dea22f121308d671a49d10238c573d6c12830e8646`).
- `../evidence/artifacts/da4858d4c12fe264f63e6ef9a7c43573d9d28e62584aad9a0d29dc2c6b8b0c7d/independent_checks.out.json` (SHA-256 `da4858d4c12fe264f63e6ef9a7c43573d9d28e62584aad9a0d29dc2c6b8b0c7d`).
- `../evidence/artifacts/5938a6a6e54c05b8acf572366140940f997684920ca7a55f15603771451e34de/reader_rerun_evidence.json` (SHA-256 `5938a6a6e54c05b8acf572366140940f997684920ca7a55f15603771451e34de`).
- `../evidence/artifacts/bddf222949f789b2d98d43783d0c10d01fa21d562e3dc5ae43b09c1e67a9d485/review.json` (SHA-256 `bddf222949f789b2d98d43783d0c10d01fa21d562e3dc5ae43b09c1e67a9d485`).
- `../evidence/artifacts/cc4b036b38ff8610cacd4b4021739b59db3ee3ad2f13f3a7befd42af246f610d/L01_AlbeverioMotovilov_round38.json` (SHA-256 `cc4b036b38ff8610cacd4b4021739b59db3ee3ad2f13f3a7befd42af246f610d`).
- `../evidence/artifacts/b5b25434ec44b305358e7f7143f02c0ce10e0425bce8757714b06147643d45a3/delta_verification.json` (SHA-256 `b5b25434ec44b305358e7f7143f02c0ce10e0425bce8757714b06147643d45a3`).

## EXSRC-08911b9c86681d44 — On the convergence of the quadratic method

**Bibliography:** Lyonell Boulton, Aatef Hobiny (2016). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/08911b9c86681d442f153bfe031944ddb5e436b297679fbe7f313def7fe91009/boulton_hobiny_quadratic_method_2016_preprint.pdf`; SHA-256 `08911b9c86681d442f153bfe031944ddb5e436b297679fbe7f313def7fe91009`; version: Exact assigned Heriot-Watt early-version PDF; arXiv:1307.0313v2, 29 physical pages (one cover + 28 printed article pages)..

**Accepted interface:** Theorem 2.3 (physical p.8 / printed p.7) gives a closed interval containing at least one spectral point whenever A is self-adjoint, finite-dimensional L⊂D(A), and µ∈Spec₂(A,L). This is the interval-inclusion component only; pair it with an independent one-point count/bracket to claim an isolated named eigenvalue. The unshifted source coordinate is z; any separately introduced shift ζ=z−t must be returned to µ=t+ζ and its final interval translated by t.

**Conditions:** A self-adjoint on its actual operator domain; nonzero finite-dimensional L subset D(A), independent basis with positive Gram A0. In original coordinates A1=<Abj,bk>, A2=<Abj,Abk>, not A1 squared. Certify a true root of Q=A2−2mu A1+mu²A0. Use the closed interval Re(mu)±|Im(mu)|; return mu=t+zeta if deliberately shifted. Separate rigorous bracket/count for a target index, uniqueness, multiplicity or gap.

**Transfer limits:** No count, index, uniqueness, multiplicity, gap, Sturm/inertia procedure, non-self-adjoint transfer, form-domain-only inputs, or floating-root certification.

**Usage card:** `../evidence/artifacts/2d65e80e42cc08bdd673216eb2e4516fde882a732a40064d6f90b99b3fb15eaa/EXSRC-08911b9c86681d44.md` (SHA-256 `2d65e80e42cc08bdd673216eb2e4516fde882a732a40064d6f90b99b3fb15eaa`).
**Reader freeze:** `../evidence/artifacts/553c033a0a8a115f848ac4c8970f71c0ecd551e4757e471acdfce427800f544e/freeze_round34_Boulton_shift_coordinate_microdelta.json` (SHA-256 `553c033a0a8a115f848ac4c8970f71c0ecd551e4757e471acdfce427800f544e`).
**Independent review:** `../evidence/artifacts/7ac3b60d00e1330ea785709416455b2449ee06a1ec98d75dccc0f082fbd92623/review.json` (SHA-256 `7ac3b60d00e1330ea785709416455b2449ee06a1ec98d75dccc0f082fbd92623`).
**Source card:** `../evidence/artifacts/9ae15d5508611c55039ac41df7ceda7c21aab8565b399cba4558c5262bdb54ea/EXSRC-08911b9c86681d44.md` (SHA-256 `9ae15d5508611c55039ac41df7ceda7c21aab8565b399cba4558c5262bdb54ea`).
**Accepted reading evidence:**
- `../evidence/artifacts/666c4002bc6d0129d1538c85067d6f39355c99e60e47550ceb07ccb217aa0fa9/EXSRC-08911b9c86681d44.json` (SHA-256 `666c4002bc6d0129d1538c85067d6f39355c99e60e47550ceb07ccb217aa0fa9`).
- `../evidence/artifacts/9ae15d5508611c55039ac41df7ceda7c21aab8565b399cba4558c5262bdb54ea/EXSRC-08911b9c86681d44.md` (SHA-256 `9ae15d5508611c55039ac41df7ceda7c21aab8565b399cba4558c5262bdb54ea`).
- `../evidence/artifacts/b48ddd921685446be0feace65ad367f2c3a74a4db96d97e653072cab702cca26/boulton_quadratic_enclosure_exact.py` (SHA-256 `b48ddd921685446be0feace65ad367f2c3a74a4db96d97e653072cab702cca26`).
- `../evidence/artifacts/cb14f3e77a09a2f3a76c9500b5c66916e1708a6112b663eea9353dbebb49b036/boulton_quadratic_enclosure_exact.out.json` (SHA-256 `cb14f3e77a09a2f3a76c9500b5c66916e1708a6112b663eea9353dbebb49b036`).
- `../evidence/artifacts/7354a8fc880096dd4c45020bfa5e563c21c33167d95b2adc0bef0c3d8353d997/boulton_quadratic_enclosure_proof_check.md` (SHA-256 `7354a8fc880096dd4c45020bfa5e563c21c33167d95b2adc0bef0c3d8353d997`).
- `../evidence/artifacts/47e77da8c7b9cef4818d898538ceb55454fd63c9430669bfbdccb8512039bd98/render_manifest.json` (SHA-256 `47e77da8c7b9cef4818d898538ceb55454fd63c9430669bfbdccb8512039bd98`).
**Additional review context:**
- `../evidence/artifacts/811c75ef3e6d2f955e2308fd0dca01876601fd30b574ef7cafa0c2523e02c8d8/proof_check.md` (SHA-256 `811c75ef3e6d2f955e2308fd0dca01876601fd30b574ef7cafa0c2523e02c8d8`).
- `../evidence/artifacts/5bf1815575fa8f9455560e37c23f02fd6d0ed8a02e2d8a49ab480ec5f6f28f34/binding_check.json` (SHA-256 `5bf1815575fa8f9455560e37c23f02fd6d0ed8a02e2d8a49ab480ec5f6f28f34`).
- `../evidence/artifacts/01a7e63f0f825f8dbd91c553d800cf6a42e2278e9292482df5a8dca0b801f38d/preimage_verification.json` (SHA-256 `01a7e63f0f825f8dbd91c553d800cf6a42e2278e9292482df5a8dca0b801f38d`).
- `../evidence/artifacts/1703d4ac7d7ed5e965ca1c0be4c64bdb5db61ecae768f73362abe4d9d105f8b0/independent_checks.out.json` (SHA-256 `1703d4ac7d7ed5e965ca1c0be4c64bdb5db61ecae768f73362abe4d9d105f8b0`).
- `../evidence/artifacts/f56a736da8a8c72c4328885feab82d7e589e35f26e89b8c8a1e2b81d70421b81/reader_rerun_evidence.json` (SHA-256 `f56a736da8a8c72c4328885feab82d7e589e35f26e89b8c8a1e2b81d70421b81`).
- `../evidence/artifacts/6249266af2e80ef695efebaf9c431277b8a91436fc5329e6228106ac93253856/freeze_round33_BoultonHobiny_Theorem2_3.json` (SHA-256 `6249266af2e80ef695efebaf9c431277b8a91436fc5329e6228106ac93253856`).

## EXSRC-11d2f38c7084d7d1 — On the Perturbation Series for Eigenvalues and Eigenprojections

**Bibliography:** Martin Wahl (2019). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/11d2f38c7084d7d143d7b73de081263bdb30ab45ea18b7f97d9f7dfa78e550be/wahl_perturbation_series_eigenvalues_eigenprojections_arxiv1910.08460v1.pdf`; SHA-256 `11d2f38c7084d7d143d7b73de081263bdb30ab45ea18b7f97d9f7dfa78e550be`; version: Exact assigned arXiv:1910.08460v1, submitted 18 October 2019; 40-page preprint without journal-reference field..

**Accepted interface:** Finite Hermitian interior SIMPLE projector expansion, source physical4 and PROJECTOR portion of Cor2 physical7: P^(n)=(-1)^(n+1) sum_(k1+...+k(n+1)=n) R^(k1)E...ER^(k(n+1)), where R^(0)=−P and R^(k)=R^k for k>0. For c=||PE|R|^(1/2)||HS and delta_prime<1/4, every integer p>=1 has HS remainder<=4g^−1/2 c(4delta_prime)^(p−1)/(1−4delta_prime)<=(4delta_prime)^p/(1−4delta_prime). Independent finite rank-one counting and Riesz proof close this interface without the excluded original general HS clause or Eq3.20.

**Conditions:** Finite-dimensional Hermitian baseline Sigma and perturbation E in one fixed inner product; interior1<j<d simple ordered target with g=min adjacent gaps>0. P=P_j and R=sum_(k!=j)(lambda_k−lambda_j)^−1 P_k from true full baseline spectral data or independently controlled errors. Delta_prime=max{|||R|^(1/2)E|R|^(1/2)||op, g^−1/2|||R|^(1/2)EP||HS, g^−1||PEP||HS}<1/4. A certified outward upper u<1/4 permits tail(4u)^p/(1−4u). Actual ordered perturbed rank-one projector required; no floating-only gap/projector/resolvent certificate.

**Transfer limits:** No multiple-eigenvalue Theorem 3 use (source omits its proof), no eigenvector regularity, branch splitting, multiplicity/root count, gap-size bound, nonnormal theorem, or automatic Markov transfer. Theorem 1 sharp finite-order bound is outside this scope. Exact SymPy checks validate only the displayed finite example; the selected general proof route awaits R01 formal record.

**Usage card:** `../evidence/artifacts/53f50f1ab539ef5c76c43537f8940109bf0e65c451895b659b7289977be45666/EXSRC-11d2f38c7084d7d1.md` (SHA-256 `53f50f1ab539ef5c76c43537f8940109bf0e65c451895b659b7289977be45666`).
**Reader freeze:** `../evidence/artifacts/848ef3ce28df55bac8b7439f3678035bac466e9fd6f1d3d141128425d9a56a5e/freeze_round40_Wahl_Corollary2_weighted_projector_tail.json` (SHA-256 `848ef3ce28df55bac8b7439f3678035bac466e9fd6f1d3d141128425d9a56a5e`).
**Independent review:** `../evidence/artifacts/b53ff01e7eb459d1c9be8f754b580b9de69103e6e55ab30526a2c85d70d95915/review.json` (SHA-256 `b53ff01e7eb459d1c9be8f754b580b9de69103e6e55ab30526a2c85d70d95915`).
**Source card:** `../evidence/artifacts/4271b74dcb7a45c175d17b60d5e727cd63847b735ae3f036c91d7b847da8d286/EXSRC-11d2f38c7084d7d1.md` (SHA-256 `4271b74dcb7a45c175d17b60d5e727cd63847b735ae3f036c91d7b847da8d286`).
**Accepted reading evidence:**
- `../evidence/artifacts/bb535463dbf147b51541d7af5ffc9aff48860d16051519ea1712c4aec3b66e6a/EXSRC-11d2f38c7084d7d1.json` (SHA-256 `bb535463dbf147b51541d7af5ffc9aff48860d16051519ea1712c4aec3b66e6a`).
- `../evidence/artifacts/4271b74dcb7a45c175d17b60d5e727cd63847b735ae3f036c91d7b847da8d286/EXSRC-11d2f38c7084d7d1.md` (SHA-256 `4271b74dcb7a45c175d17b60d5e727cd63847b735ae3f036c91d7b847da8d286`).
- `../evidence/artifacts/5abf59d0cefb0a4c1e042ac5788236ccbd28abb4589ae8afe5331ebbb512d3c7/wahl_simple_weighted_exact.py` (SHA-256 `5abf59d0cefb0a4c1e042ac5788236ccbd28abb4589ae8afe5331ebbb512d3c7`).
- `../evidence/artifacts/6dc03fbe1eade39e8d3f6f4c0de2eed81bffd013dca3f467685cbe96a53bd157/wahl_simple_weighted_exact.out.json` (SHA-256 `6dc03fbe1eade39e8d3f6f4c0de2eed81bffd013dca3f467685cbe96a53bd157`).
- `../evidence/artifacts/e4d3663237247a9f36c8422d837336c999a82e1430cd32a84d8089e25bad9747/wahl_proof_check.md` (SHA-256 `e4d3663237247a9f36c8422d837336c999a82e1430cd32a84d8089e25bad9747`).
- `../evidence/artifacts/63351a16abca54f5017899fd5853424350f66376827f22577f5286675f4f6932/render_manifest.json` (SHA-256 `63351a16abca54f5017899fd5853424350f66376827f22577f5286675f4f6932`).
**Additional review context:**
- `../evidence/artifacts/d015834827402537f62ff38ae0a53c4a6d879f083876cdf85054be12fadf9c4b/proof_check.md` (SHA-256 `d015834827402537f62ff38ae0a53c4a6d879f083876cdf85054be12fadf9c4b`).
- `../evidence/artifacts/62ea984050c7fa79bed5ed1a0fa2e65fef52ad8183803377163b9d1035c9e28c/binding_check.json` (SHA-256 `62ea984050c7fa79bed5ed1a0fa2e65fef52ad8183803377163b9d1035c9e28c`).
- `../evidence/artifacts/eee86071f51218fbbf349e39469ac5d01efa58b6eee541dda0b3986672d04f58/preimage_verification.json` (SHA-256 `eee86071f51218fbbf349e39469ac5d01efa58b6eee541dda0b3986672d04f58`).
- `../evidence/artifacts/d7e421357fcce1c62e4f69e39c8f9ba586af8e9e563856faecdcf951d4b8c5b8/replay_evidence.json` (SHA-256 `d7e421357fcce1c62e4f69e39c8f9ba586af8e9e563856faecdcf951d4b8c5b8`).
- `../evidence/artifacts/277c6cb6bd744ed15c6a4eb66affb013e1cc3a94be4b3ee03233da3623eea3cd/independent_checks.out.json` (SHA-256 `277c6cb6bd744ed15c6a4eb66affb013e1cc3a94be4b3ee03233da3623eea3cd`).

## EXSRC-216c2d777a98991f — Persistence of Spectral Projections for Stochastic Operators on Large Tensor Products

**Bibliography:** Robert S. MacKay (2025). **Method IDs:** G03.02, G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/216c2d777a98991f23e3ff0e11141a3bf77a05b3deedbf4dfea2b34d8bf29aad/mackay_persistence_spectral_projections_2025.pdf`; SHA-256 `216c2d777a98991f23e3ff0e11141a3bf77a05b3deedbf4dfea2b34d8bf29aad`; version: Journal of Applied Probability 62(1) (2025), 1–14.

**Accepted interface:** Qualitative C^r persistence of a separated invariant spectral projection on a verified fixed Banach space; P-prime is obtained from the invertible Sylvester commutator on the off-diagonal tangent space.

**Conditions:** C^r norm-smooth bounded family; bounded commuting idempotent; disjoint spectra on its invariant image/complement; a genuine complete chosen function space. Unqualified sep-only uniformity is not accepted.

**Transfer limits:** No unqualified countable-product setup, separation-only uniform-in-size ambient bound, individual eigenvalue label, ordered-gap sign, continuous-time theorem or automatic Ising/Glauber transfer. R16 neutral and R01 addendum retained.

**Usage card:** `../evidence/artifacts/4c634bc7836a049f3ae67d2091f88f737a85ae886b7d2ed6d6b139bf460feb26/EXSRC-216c2d777a98991f.md` (SHA-256 `4c634bc7836a049f3ae67d2091f88f737a85ae886b7d2ed6d6b139bf460feb26`).
**Reader freeze:** `../evidence/artifacts/a5d5d7d7876968843c8f80030a0e9d3e3268c74a32bf2e0272705bc7e3c54c88/freeze_round16_round15_microdelta.json` (SHA-256 `a5d5d7d7876968843c8f80030a0e9d3e3268c74a32bf2e0272705bc7e3c54c88`).
**Independent review:** `../evidence/artifacts/278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475/review.json` (SHA-256 `278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475`).
**Accepted reading evidence:**
- `../evidence/artifacts/b331bfcf085f7533cd5966d3a18ac07b5d2187201eee2b2ccda4f364d95ad9d5/EXSRC-216c2d777a98991f.json` (SHA-256 `b331bfcf085f7533cd5966d3a18ac07b5d2187201eee2b2ccda4f364d95ad9d5`).
- `../evidence/artifacts/a7825850b38306bd50a133bac4c941d7f04129f5d64d640cfd9e11589a8b95ae/EXSRC-216c2d777a98991f.md` (SHA-256 `a7825850b38306bd50a133bac4c941d7f04129f5d64d640cfd9e11589a8b95ae`).
**Additional review context:**
- `../evidence/artifacts/461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11/review.json` (SHA-256 `461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11`).

## EXSRC-2aa898e771f4a6e2 — Guaranteed Lower Eigenvalue Bounds for Spectral Galerkin Methods with Application to Schrödinger Operators

**Bibliography:** Xuefeng Liu (2026). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/2aa898e771f4a6e233414320ba74800d36ac0b7bc844adcec79fa00688a0b503/liu_spectral_galerkin_eigenvalue_bounds_2026v1.pdf`; SHA-256 `2aa898e771f4a6e233414320ba74800d36ac0b7bc844adcec79fa00688a0b503`; version: Assigned arXiv:2607.04247v1, submitted 5 July 2026; exact 28-page PDF..

**Accepted interface:** Theorem4.9 Eqs4.16–4.17, physical=printed12, supplies ordered CONTINUOUS bounded-box Schrodinger eigenvalue lower endpoint lambda_kN/(1+c lambda_kN), c=(1+min(X²,X))/nu_star, X=Vmax/lambda1N, from the standard conforming Laplacian-Galerkin matrix. Conforming Rayleigh–Ritz supplies mu_k<=lambda_kN. This is G03.06 interval isolation only: strict adjacent ordered enclosure separation certifies a gap, without Sturm/inertia/root-count claims.

**Conditions:** Bounded rectangular box with homogeneous Dirichlet H1_0 or Neumann H1 form domain; bounded real V>=0 a.e., positive on a nonempty open subset; finite conforming exact Laplacian spectral space. nu_star is the actual smallest omitted Laplace eigenvalue and must be positive; lambda1N>0 is the smallest FULL standard matrix K+P eigenvalue. Full potential-form Ritz P differs from modal P0. Bounds apply1<=k<=M, and gap comparison1<=k<M. Certified upper Vmax, positive lower lambda1N/nu_star, nonnegative finite eigenvalue lower endpoints and finite upper endpoints with correct ordering/multiplicity required; use lower/(1+c_upper*lower) and finite upper for continuous endpoints.

**Transfer limits:** No general domain, negative/unbounded/singular potential or whole-space truncation theorem, composite4.12, tail-refined constant, benchmark table certification, Sturm/inertia/root count, Markov/moving-metric transfer. Exact examples do not prove the general theorem, which is separately reclosed in the report.

**Usage card:** `../evidence/artifacts/c16b35389501757e7b70e45fe067646b91ce99d88df342b9324cbdb6f57f242c/EXSRC-2aa898e771f4a6e2.md` (SHA-256 `c16b35389501757e7b70e45fe067646b91ce99d88df342b9324cbdb6f57f242c`).
**Reader freeze:** `../evidence/artifacts/a9de6d478d1030df94f9e5cf729f333586cf37b67ae872ecbc185db108e95fdf/freeze_round44_Liu2026_Theorem4_9_standard_matrix_lower_enclosure.json` (SHA-256 `a9de6d478d1030df94f9e5cf729f333586cf37b67ae872ecbc185db108e95fdf`).
**Independent review:** `../evidence/artifacts/419205ac9e1621a4a8360dce9db28045d0b7048bd28ad4609b9466b91e113802/review.json` (SHA-256 `419205ac9e1621a4a8360dce9db28045d0b7048bd28ad4609b9466b91e113802`).
**Source card:** `../evidence/artifacts/ff2c9f9903048289744e410c1d0abaa08d2fd0f6193ab80af83bdce0b861af19/EXSRC-2aa898e771f4a6e2.md` (SHA-256 `ff2c9f9903048289744e410c1d0abaa08d2fd0f6193ab80af83bdce0b861af19`).
**Accepted reading evidence:**
- `../evidence/artifacts/a7cbdc28f17393b31d19d5735a27bca4a3e0e46ed3f502f82962ad755b71aade/EXSRC-2aa898e771f4a6e2.json` (SHA-256 `a7cbdc28f17393b31d19d5735a27bca4a3e0e46ed3f502f82962ad755b71aade`).
- `../evidence/artifacts/ff2c9f9903048289744e410c1d0abaa08d2fd0f6193ab80af83bdce0b861af19/EXSRC-2aa898e771f4a6e2.md` (SHA-256 `ff2c9f9903048289744e410c1d0abaa08d2fd0f6193ab80af83bdce0b861af19`).
- `../evidence/artifacts/082b85304fe45d3eeebe043db1d5329f7405ebe450be738ef0ba1d5d41e8403e/liu_2026_thm49_exact_example.py` (SHA-256 `082b85304fe45d3eeebe043db1d5329f7405ebe450be738ef0ba1d5d41e8403e`).
- `../evidence/artifacts/21ce7726e5a135015d4419afd66d943554b977076ccf65e335621b129851d063/liu_2026_thm49_exact_example.out.json` (SHA-256 `21ce7726e5a135015d4419afd66d943554b977076ccf65e335621b129851d063`).
- `../evidence/artifacts/d17002a42ff9cf30ee5bae7280eccc0bea78e7d3f7c3062b816f2e373513c9e1/liu_2026_thm49_proof_check.md` (SHA-256 `d17002a42ff9cf30ee5bae7280eccc0bea78e7d3f7c3062b816f2e373513c9e1`).
**Additional review context:**
- `../evidence/artifacts/56c487d5e8ed262f7dfe4de78698b2f3f0dd7e7cea28d3e2bb2b5b5e74d26697/proof_check.md` (SHA-256 `56c487d5e8ed262f7dfe4de78698b2f3f0dd7e7cea28d3e2bb2b5b5e74d26697`).
- `../evidence/artifacts/21fdfb67f64558293933fc1b634f0b726b244e64475b8f91888ddb5eff08366c/final_scope.md` (SHA-256 `21fdfb67f64558293933fc1b634f0b726b244e64475b8f91888ddb5eff08366c`).
- `../evidence/artifacts/23ae40e994222bae764bf5ddcfb489140925b5b00bb43753c502b2e8e8d6332b/binding_check.json` (SHA-256 `23ae40e994222bae764bf5ddcfb489140925b5b00bb43753c502b2e8e8d6332b`).
- `../evidence/artifacts/dd18622756914e80a64c9c301170e3899e43d8ab1a3e584e5cdcd23c758b9818/preimage_verification.json` (SHA-256 `dd18622756914e80a64c9c301170e3899e43d8ab1a3e584e5cdcd23c758b9818`).
- `../evidence/artifacts/9748da8ae789d099cde70feca546787dc5a31353ba87b2fcb03402ebcc88f94b/render_text_verification.json` (SHA-256 `9748da8ae789d099cde70feca546787dc5a31353ba87b2fcb03402ebcc88f94b`).
- `../evidence/artifacts/8eab12ae43263089f1fc858b8eb7b1efb99d155bd51f51e7b057f432cc2a007b/replay_evidence.json` (SHA-256 `8eab12ae43263089f1fc858b8eb7b1efb99d155bd51f51e7b057f432cc2a007b`).
- `../evidence/artifacts/9e4cd3ea4397cb315b2807430de6bdd0fc1fe55198ef81f923ab8d610e136411/independent_checks.out.json` (SHA-256 `9e4cd3ea4397cb315b2807430de6bdd0fc1fe55198ef81f923ab8d610e136411`).

## EXSRC-2b06c4f0c00ebed2 — A useful variant of the Davis–Kahan theorem for statisticians

**Bibliography:** Yi Yu, Tengyao Wang, Richard J. Samworth (2015). **Method IDs:** G03.02, G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/2b06c4f0c00ebed2c87c28e93fefefbe0e2fb684c1b7709d120b17df412e84dd/yu_wang_samworth_davis_kahan_2015.pdf`; SHA-256 `2b06c4f0c00ebed2c87c28e93fefefbe0e2fb684c1b7709d120b17df412e84dd`; version: Biometrika 102(2) (2015), 315–323, author-hosted 9-page full-text.

**Accepted interface:** Population-external-gap real-symmetric consecutive-block subspace stability and block Procrustes bound, without internal branch selection.

**Conditions:** Real symmetric p by p Sigma and Sigmahat; eigenvalues nonincreasing;1<=r<=s<=p,d=s-r+1; gamma=min(lambda_(r-1)-lambda_r,lambda_s-lambda_(s+1))>0 with lambda0=+infinity,lambda_(p+1)=-infinity. Orthonormal eigenvector matrices for corresponding indexed blocks. Bounds are Frobenius sinTheta<=2 min(sqrt(d)||E||op,||E||F)/gamma and Procrustes<=2^(3/2) times that numerator/gamma.

**Transfer limits:** Apply after symmetric conjugation and a separately bounded conjugated perturbation. This is a subspace-angle bound, not interval isolation or an eigenvalue derivative, ordered cluster-member selection, monotonicity or a Markov conjugation theorem. May be vacuous for large perturbations.

**Usage card:** `../evidence/artifacts/4a4e5080773cf61e19b317270b5c7ae7f9beaa3930fdd749dd8d0597bd63508f/EXSRC-2b06c4f0c00ebed2.md` (SHA-256 `4a4e5080773cf61e19b317270b5c7ae7f9beaa3930fdd749dd8d0597bd63508f`).
**Reader freeze:** `../evidence/artifacts/e40a3737b206cbb6438661ec3591d32e5015cf9f8525bdd466ea1b291a703dc7/freeze_round12_round9_use_corrections.json` (SHA-256 `e40a3737b206cbb6438661ec3591d32e5015cf9f8525bdd466ea1b291a703dc7`).
**Independent review:** `../evidence/artifacts/ef5419f726320194b696611600b55202cad47e00c2d63898e89e6a1e95edec11/review.json` (SHA-256 `ef5419f726320194b696611600b55202cad47e00c2d63898e89e6a1e95edec11`).
**Accepted reading evidence:**
- `../evidence/artifacts/626daf863b67f827b0a6f4047765ea1e6264b46e6d9676d16ae5d3a073827e43/EXSRC-2b06c4f0c00ebed2.json` (SHA-256 `626daf863b67f827b0a6f4047765ea1e6264b46e6d9676d16ae5d3a073827e43`).
- `../evidence/artifacts/78c357a0e7f296aca1da23e5787fbbeba4d41db81c6b460215a339419e2d9778/EXSRC-2b06c4f0c00ebed2.md` (SHA-256 `78c357a0e7f296aca1da23e5787fbbeba4d41db81c6b460215a339419e2d9778`).

## EXSRC-301ec07214974142 — First-order Perturbation Theory for Eigenvalues and Eigenvectors

**Bibliography:** Anne Greenbaum, Ren-Cang Li, Michael L. Overton (2019). **Method IDs:** G03.03, G03.04, G03.05. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/301ec0721497414252f2360a2468e4aa2514b9d4bed34eee4a805a2729596b3f/greenbaum_li_overton_first_order_2019v2.pdf`; SHA-256 `301ec0721497414252f2360a2468e4aa2514b9d4bed34eee4a805a2729596b3f`; version: arXiv:1903.00785v2 (3 June 2019); published SIAM Review 62(2) (2020), 463–482.

**Accepted interface:** Analytic algebraically simple eigenvalue/eigenvector/projector perturbation, separately derived centered Markov inverse -S, and accurate semisimple nonanalyticity boundary.

**Conditions:** Finite complex-analytic matrix family near tau0; algebraically simple lambda0; y_star x=1; left row y_star analytic; appropriate derivative normalization for vector formulas. Hermitian real-family specialization only after symmetric conjugation and branch conditions.

**Transfer limits:** No arbitrary-graph Ising sign, unresolved ordered-branch derivative, strict numerical certificate or unproved high-order remainder. The current wider source/use cards require the listed corrections; exact first-order interfaces were independently supported.

**Usage card:** `../evidence/artifacts/5b5b7ad675d41bc10694a41d819b43043eea0f6e69a5b8f5d3fcbc9f96e86d71/EXSRC-301ec07214974142.md` (SHA-256 `5b5b7ad675d41bc10694a41d819b43043eea0f6e69a5b8f5d3fcbc9f96e86d71`).
**Reader freeze:** `../evidence/artifacts/b3f95b0d3bb4ee256bbb37e54a800bc3087a0ea7650a180973259491889c67e2/freeze_round10.json` (SHA-256 `b3f95b0d3bb4ee256bbb37e54a800bc3087a0ea7650a180973259491889c67e2`).
**Independent review:** `../evidence/artifacts/66b99deb125376891d89cafd37879dc4990029fec502313ed02e7d6e9805d1c6/review.json` (SHA-256 `66b99deb125376891d89cafd37879dc4990029fec502313ed02e7d6e9805d1c6`).
**Accepted reading evidence:**
- `../evidence/artifacts/e4cbfb879701ab837f999210ebb9210990a079416d4f09fec79e36dfcb80f8d0/EXSRC-301ec07214974142.json` (SHA-256 `e4cbfb879701ab837f999210ebb9210990a079416d4f09fec79e36dfcb80f8d0`).
- `../evidence/artifacts/3a1a5153778d6637840b8c7994067163f8a4e518d9d552e4519b22b27e8cada2/auth-3a1a5153778d6637840b8c7994067163f8a4e518d9d552e4519b22b27e8cada2.json` (SHA-256 `3a1a5153778d6637840b8c7994067163f8a4e518d9d552e4519b22b27e8cada2`).
- `../evidence/artifacts/96f5ef84e350ccf3cd26f83f0aed4fbbaf0cc0e2904a276131e3ee9a93769bcb/EXSRC-301ec07214974142.md` (SHA-256 `96f5ef84e350ccf3cd26f83f0aed4fbbaf0cc0e2904a276131e3ee9a93769bcb`).

## EXSRC-340856dc37e67363 — Basic Matrix Perturbation Theory

**Bibliography:** Benjamin Texier (2018). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/340856dc37e673637d2f62ae45cdf5a21a3517cb8e04629a1b05083b30c289d8/texier_basic_matrix_perturbation_2018.pdf`; SHA-256 `340856dc37e673637d2f62ae45cdf5a21a3517cb8e04629a1b05083b30c289d8`; version: L’Enseignement Mathématique (2) 64 (2018), 249–263.

**Accepted interface:** Total projection and first one-sided semisimple derivative, compression on RanP0, with only base-centered Lipschitz estimate under pointwise differentiability.

**Conditions:** Continuous finite-matrix family on open real parameter domain, differentiable at x0; isolated base eigenvalue semisimple. Proposition3.3 has isolated coalescence; Corollary3.6 drops that auxiliary isolation. Use full spectral projection; compress to RanP0, excluding complement zeros. Base-centered Lipschitz estimate is not a two-point neighborhood estimate under pointwise differentiability alone.

**Transfer limits:** Total projection and semisimple first-order derivative only; source Lemma3.5/Prop4.2 higher-order index-based remainder excluded. Pointwise differentiability gives a base-centered estimate, not a two-point neighborhood Lipschitz constant. No ordered branch selection or strict numerical certificate.

**Usage card:** `../evidence/artifacts/5de0b33c6fec892d72214e20e48d12bc76d7a3fdf21e68b39fe5f58ec5ce035a/EXSRC-340856dc37e67363.md` (SHA-256 `5de0b33c6fec892d72214e20e48d12bc76d7a3fdf21e68b39fe5f58ec5ce035a`).
**Reader freeze:** `../evidence/artifacts/b3f95b0d3bb4ee256bbb37e54a800bc3087a0ea7650a180973259491889c67e2/freeze_round10.json` (SHA-256 `b3f95b0d3bb4ee256bbb37e54a800bc3087a0ea7650a180973259491889c67e2`).
**Independent review:** `../evidence/artifacts/66b99deb125376891d89cafd37879dc4990029fec502313ed02e7d6e9805d1c6/review.json` (SHA-256 `66b99deb125376891d89cafd37879dc4990029fec502313ed02e7d6e9805d1c6`).
**Accepted reading evidence:**
- `../evidence/artifacts/1f7bfd28c4dc50f6cb2434689be9ea8fcca46d75a660ff5d7a3b8276a72339ba/EXSRC-340856dc37e67363.json` (SHA-256 `1f7bfd28c4dc50f6cb2434689be9ea8fcca46d75a660ff5d7a3b8276a72339ba`).
- `../evidence/artifacts/550b78274dfe7749e9c800fc0c40d5f2364e49086cba16193767bf2432c9a9a7/auth-550b78274dfe7749e9c800fc0c40d5f2364e49086cba16193767bf2432c9a9a7.json` (SHA-256 `550b78274dfe7749e9c800fc0c40d5f2364e49086cba16193767bf2432c9a9a7`).
- `../evidence/artifacts/62e70cb9957ce358b8f8372626d7948efc597180afe63a19d3b8ab48a688ad87/EXSRC-340856dc37e67363.md` (SHA-256 `62e70cb9957ce358b8f8372626d7948efc597180afe63a19d3b8ab48a688ad87`).

## EXSRC-344d4d2458b42fa2 — Perturbed Markov Chains with Damping Component

**Bibliography:** Dmitrii Silvestrov, Sergei Silvestrov, Benard Abola, Pitos Seleka Biganda, Christopher Engström, John Magero Mango, Godwin Kakuba (2021). **Method IDs:** G03.05. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/344d4d2458b42fa2afccb8085bdddb85cd26d321f04917363327b60579a6fcff/silvestrov_perturbed_markov_damping_2021.pdf`; SHA-256 `344d4d2458b42fa2afccb8085bdddb85cd26d321f04917363327b60579a6fcff`; version: Methodology and Computing in Applied Probability 23 (2021), 369–397.

**Accepted interface:** Theorem 1 discounted-resolvent stationary formula plus the reader-derived single-class Poisson response r=(d−π0)[(I−P0+Π)^−1−Π]. Differentiability is proved using the finite complementary inverse; derivative normalization and uniqueness are proved in the independent report.

**Conditions:** Single finite irreducible aperiodic class; unique stationary π0; strictly positive d; D=1d; h=1.

**Transfer limits:** Stationary-law response only; no nontrivial eigenvalue/gap derivative, no reversible L2 bound, no multi-class derivative. New tool reuse adds zero further full-text reads.

**Usage card:** `../evidence/artifacts/3886bd7475417182dcc9caad05b226030108fc92fb792d120bcc8877d4158ada/EXSRC-344d4d2458b42fa2-G03.05.md` (SHA-256 `3886bd7475417182dcc9caad05b226030108fc92fb792d120bcc8877d4158ada`).
**Reader freeze:** `../evidence/artifacts/b5364ca2ee71662c4c40ae86987e96c3e66a93cb48e7c786da1991f9e399cd53/freeze_round27_Silvestrov_locator_correction.json` (SHA-256 `b5364ca2ee71662c4c40ae86987e96c3e66a93cb48e7c786da1991f9e399cd53`).
**Independent review:** `../evidence/artifacts/25d4581d0432ca8025d834dc67f2bb69f4a25fca2b8622dab64fbd7b7448997c/review.json` (SHA-256 `25d4581d0432ca8025d834dc67f2bb69f4a25fca2b8622dab64fbd7b7448997c`).
**Accepted reading evidence:**
- `../evidence/artifacts/6f3dc3d238c7d3ba25b241d8b0edd2667c8c7833af4309a7993ee6faf133f707/EXSRC-344d4d2458b42fa2.json` (SHA-256 `6f3dc3d238c7d3ba25b241d8b0edd2667c8c7833af4309a7993ee6faf133f707`).
- `../evidence/artifacts/77ca579f0db8f2f493910281768df6a49f77116bf1217e9eaf3faac62848fcdb/EXSRC-344d4d2458b42fa2.md` (SHA-256 `77ca579f0db8f2f493910281768df6a49f77116bf1217e9eaf3faac62848fcdb`).
**Additional review context:**
- `../evidence/artifacts/85d17382fb53fc945b82a9cdb43a77a22227ff4d4b4c931ec7c23335443d7d73/proof_check.md` (SHA-256 `85d17382fb53fc945b82a9cdb43a77a22227ff4d4b4c931ec7c23335443d7d73`).
- `../evidence/artifacts/acaa13f84b0cae3179f90d3adb0f34438bdc60d552310962cc8e1f5f9f799d74/binding_check.json` (SHA-256 `acaa13f84b0cae3179f90d3adb0f34438bdc60d552310962cc8e1f5f9f799d74`).
- `../evidence/artifacts/c20f50e043d8eafdf326b06a0b9ec0a089a42d38f4606a8c80a2fd6bc1ce90de/reader_rerun_evidence.json` (SHA-256 `c20f50e043d8eafdf326b06a0b9ec0a089a42d38f4606a8c80a2fd6bc1ce90de`).
- `../evidence/artifacts/b7637771a93886cc5f084b7d68d9d80b36ec3f538c580dc3c27beb9bc135a20d/independent_checks.out.json` (SHA-256 `b7637771a93886cc5f084b7d68d9d80b36ec3f538c580dc3c27beb9bc135a20d`).

## EXSRC-350fec75694d14a8 — On the Hellmann-Feynman theorem for degenerate states

**Bibliography:** Francisco M. Fernández (2019). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/350fec75694d14a86f5122a2da884b20a7eb0970a2f9c53bba97eef7e331d360/fernandez_hellmann_feynman_degenerate_states_2019v1.pdf`; SHA-256 `350fec75694d14a86f5122a2da884b20a7eb0970a2f9c53bba97eef7e331d360`; version: Exact assigned first-posted arXiv:1912.04876v1 PDF; 13 physical pages..

**Accepted interface:** §2 Eq. (8), physical pp.3–4, selects degenerate first-order directions by diagonalizing the derivative compressed to the eigenspace. Independently derived finite-dimensional block reduction gives, for H(t)=H0+tK+o(t), an isolated finite-multiplicity eigenvalue E, and t↓0, the unordered cluster expansion E+t·spec(PKP|Pℋ)+o(t). Exact source example checks the compressed slopes and distinguishes them from 45° averages.

**Conditions:** Finite-dimensional Hermitian family in a fixed inner product; one real parameter; operator-norm first-order expansion.; An isolated eigenvalue of finite multiplicity and its orthogonal projection P.; Use an orthonormal eigenspace basis; branchwise HFT additionally requires a differentiable normalized eigenpair branch.; the norm expansion is at the base point; conditional branchwise HFT applies only where both operator and normalized eigenpair derivatives exist. Use exact or independently error-controlled projections and matrix data.

**Transfer limits:** No continuous or C1 eigenvector/label theorem, multi-parameter global labeling, unbounded operator, moving domain, varying Gibbs inner product, or Markov transfer. The two-fermion cusp has distinct one-sided slopes, not a two-sided derivative.

**Usage card:** `../evidence/artifacts/cb605828f7fef51f8b6fad526a24ec4be0e337c2571fdbd948652135413f32cf/EXSRC-350fec75694d14a8.md` (SHA-256 `cb605828f7fef51f8b6fad526a24ec4be0e337c2571fdbd948652135413f32cf`).
**Reader freeze:** `../evidence/artifacts/95955e87e2d489f728ead3af2e2333be4cddba2ae1b8fe7660304039713c3122/freeze_round32b_Fernandez_runtime_metadata_correction.json` (SHA-256 `95955e87e2d489f728ead3af2e2333be4cddba2ae1b8fe7660304039713c3122`).
**Independent review:** `../evidence/artifacts/c81b9d35e7f8a5ae1a861d64ac737b272d1f132a9baa0a2653d232c289259416/review.json` (SHA-256 `c81b9d35e7f8a5ae1a861d64ac737b272d1f132a9baa0a2653d232c289259416`).
**Accepted reading evidence:**
- `../evidence/artifacts/d545841e5d510095335bbdc2146dd4beed7254e5e7a83ee2a1a9965bfdda19b8/EXSRC-350fec75694d14a8.json` (SHA-256 `d545841e5d510095335bbdc2146dd4beed7254e5e7a83ee2a1a9965bfdda19b8`).
- `../evidence/artifacts/cee13ad2e91142f60663d383521038095d0fc302fe33cb3894227181f3fc55e7/EXSRC-350fec75694d14a8.md` (SHA-256 `cee13ad2e91142f60663d383521038095d0fc302fe33cb3894227181f3fc55e7`).
- `../evidence/artifacts/098d145def2122f44f5d4e57e700b970a37b465d15cf618482434825ed0bd8d2/fernandez_degenerate_hft_exact_check.py` (SHA-256 `098d145def2122f44f5d4e57e700b970a37b465d15cf618482434825ed0bd8d2`).
- `../evidence/artifacts/a13410d763e2c0cf3e720ea69dca74c07a52fd678f1f9753bb6f2b4e7696011b/fernandez_degenerate_hft_exact_check.out.json` (SHA-256 `a13410d763e2c0cf3e720ea69dca74c07a52fd678f1f9753bb6f2b4e7696011b`).
- `../evidence/artifacts/c57800b4c4f56c6d56d9302b9935113746aa3de8cd47032bbea274881abb25e7/finite_cluster_slope_proof.md` (SHA-256 `c57800b4c4f56c6d56d9302b9935113746aa3de8cd47032bbea274881abb25e7`).
- `../evidence/artifacts/b40987f602acb217c8e0af426aa630a39466a30a88fb3327fd11c30951253728/render_manifest.json` (SHA-256 `b40987f602acb217c8e0af426aa630a39466a30a88fb3327fd11c30951253728`).
**Additional review context:**
- `../evidence/artifacts/b556a88a00d87f80917de08b1523e5fe63e0d43f0700f95e48a6a65b25f69f71/proof_check.md` (SHA-256 `b556a88a00d87f80917de08b1523e5fe63e0d43f0700f95e48a6a65b25f69f71`).
- `../evidence/artifacts/e6037c83b553ed974106dcf63ced73d5689278c22696a9aee8c7b621a9229d07/binding_check.json` (SHA-256 `e6037c83b553ed974106dcf63ced73d5689278c22696a9aee8c7b621a9229d07`).
- `../evidence/artifacts/8247f61913552a501d609bbf785b2031d7c7561d5772a69121878689e2ac0a53/preimage_verification.json` (SHA-256 `8247f61913552a501d609bbf785b2031d7c7561d5772a69121878689e2ac0a53`).
- `../evidence/artifacts/8ae52e79d24a24a7ddf54e14e3184cadc31b94c88143ff77fa8a242f43afa577/independent_checks.out.json` (SHA-256 `8ae52e79d24a24a7ddf54e14e3184cadc31b94c88143ff77fa8a242f43afa577`).
- `../evidence/artifacts/b4e3ee3627cfe72c055e81604cc1fac7570dcb37a59be23f4ab47e91b8a0630c/reader_rerun_evidence.json` (SHA-256 `b4e3ee3627cfe72c055e81604cc1fac7570dcb37a59be23f4ab47e91b8a0630c`).

## EXSRC-36ecf2ea6618ba20 — Eigenvalue enclosures and exclosures for non-self-adjoint problems in hydrodynamics

**Bibliography:** B. Malcolm Brown, Matthias Langer, Marco Marletta, Christiane Tretter, Markus Wagenhofer (2010). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/36ecf2ea6618ba20405d45704128dc1b891b20207c27d5e75e302354f58c2db1/brown_langer_marletta_tretter_wagenhofer_exclosures_2010.pdf`; SHA-256 `36ecf2ea6618ba20405d45704128dc1b891b20207c27d5e75e302354f58c2db1`; version: Complete institutional-repository article copy; LMS Journal of Computation and Mathematics 13 (2010), printed pp.65–81.

**Accepted interface:** Validated analytic characteristic-function zero count/enclosure/exclosure on one rectangle with strict entire-edge right-half-plane bounds.

**Conditions:** g analytic on neighborhood of closed rectangle; nonzero boundary vertices including corners, CCW traversal; validated Re(g(entire edge segment)/g(vertex))>0 on every segment; validated winding interval contains exactly one integer. Zeros counted with multiplicity.

**Transfer limits:** Only the analytic boundary-ODE rectangle method with validated enclosures; global claim needs independent localization of the relevant target region. No bounded-whole-spectrum conclusion, distinct-root count from multiplicity, VNODE table rerun, half-line Levinson proof acceptance or arbitrary Markov transfer.

**Usage card:** `../evidence/artifacts/b0a025f4cdb84a856b567e1f27b04ef37bc812390976c588b40cc6004e542dfe/EXSRC-36ecf2ea6618ba20.md` (SHA-256 `b0a025f4cdb84a856b567e1f27b04ef37bc812390976c588b40cc6004e542dfe`).
**Reader freeze:** `../evidence/artifacts/a5d5d7d7876968843c8f80030a0e9d3e3268c74a32bf2e0272705bc7e3c54c88/freeze_round16_round15_microdelta.json` (SHA-256 `a5d5d7d7876968843c8f80030a0e9d3e3268c74a32bf2e0272705bc7e3c54c88`).
**Independent review:** `../evidence/artifacts/278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475/review.json` (SHA-256 `278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475`).
**Accepted reading evidence:**
- `../evidence/artifacts/6f11ee47c6a2d496276a4ae3ac47f031579d37bba5a33886b58af92f240fff83/EXSRC-36ecf2ea6618ba20.json` (SHA-256 `6f11ee47c6a2d496276a4ae3ac47f031579d37bba5a33886b58af92f240fff83`).
- `../evidence/artifacts/5d5849739c3e52272ca13fd507170de9e60d8b7f3eb0a56fc8bdce55ceadbeef/EXSRC-36ecf2ea6618ba20.md` (SHA-256 `5d5849739c3e52272ca13fd507170de9e60d8b7f3eb0a56fc8bdce55ceadbeef`).
**Additional review context:**
- `../evidence/artifacts/f4267a503da7eab20a256c1433a608ef580c3d85da839b4ea84a62ba28f02959/review.json` (SHA-256 `f4267a503da7eab20a256c1433a608ef580c3d85da839b4ea84a62ba28f02959`).

## EXSRC-444d583231bf5f30 — Verified Error Bounds for All Eigenvalues and Eigenvectors of a Matrix

**Bibliography:** Siegfried M. Rump (2022). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/444d583231bf5f30f67bcd6d23d3013728a8818d5770758fff57e118da439720/rump_verified_error_bounds_all_eigenvalues_eigenvectors_2022_author_ms.pdf`; SHA-256 `444d583231bf5f30f67bcd6d23d3013728a8818d5770758fff57e118da439720`; version: Complete 19-page public author manuscript associated with SIAM J. Matrix Anal. Appl. 43(4) (2022), 1736–1754, DOI 10.1137/21M1451440; assigned copy is marked for review purposes only, publisher-layout equivalence not asserted..

**Accepted interface:** Theorem2.2 specific-map finite invariant restriction/wholecluster inclusion, manuscript5–6, with Brouwer+specific invertible Ri independently reclosed. Strict interval self-inclusions enclose Mi in lambda_i I+Vi^T Zi and normalized Yi in Vi+QiZi. Non-singleton Mi is an interval MATRIX enclosure, whose entries are not individual eigenvalue intervals; scalar spectral regions need a separate valid spectral enclosure step. For successful selected J, use the frozen STRONGER Remark2.4 induced magnitude norm1<1 OR norminfinity<1 to obtain independent restriction blocks; alln successful coordinates imply full algebraic spectrum representation.

**Conditions:** Finite real/complex exact A or containing interval input; nominal coordinate blocks partition ALL[n] with pairwise distinct centers; D and exact/rigorously enclosed specific reciprocal-gap Ri satisfy source identities. Bounded compact convex interval box, all relevant operations outward-enclosed, source block extraction and strict Zi subset interior(XVi). For global conclusion use successful principal submatrix Z_J and certified ||mag Z_J||1<1 OR ||mag Z_J||infinity<1; actual selected-row basis error has zero own block diagonal and is magnitude-dominated by Z_J. Full spectrum requires successful sizes sum n; scalar output regions also need a separately valid spectral outer enclosure for every nonsingleton Mi. Practical similarity input needs certified nonsingular W and enclosure of exact W^−1BW; transform bases back by W. Uniform interval tests are pointwise ∀A∃Mi(A),Yi(A).

**Transfer limits:** Only finite real/complex G03.06 conditional invariant-block and eigenvalue-inclusion component. No weaker raw-radius global proof, Jordan indecomposability, smooth eigenvectors, stochastic/mixing/gap theorem, Sturm/inertia/root-isolation implementation, infinite/generalized eigenproblem or empirical performance guarantee.

**Usage card:** `../evidence/artifacts/0c177eca8e56700c5afe240f733a5d2b221ffc7417a6936db29ea09c7256dc69/EXSRC-444d583231bf5f30.md` (SHA-256 `0c177eca8e56700c5afe240f733a5d2b221ffc7417a6936db29ea09c7256dc69`).
**Reader freeze:** `../evidence/artifacts/ed49a68ab5ede73758f99173e8fbb0315622788a9ba04c93b89b854b73e92767/freeze_round49_Rump2022_coverage_proof_binding.json` (SHA-256 `ed49a68ab5ede73758f99173e8fbb0315622788a9ba04c93b89b854b73e92767`).
**Independent review:** `../evidence/artifacts/50b70cf30799b7475c949e7cda9156718ded3b300372724fdb222344b1e38d58/review.json` (SHA-256 `50b70cf30799b7475c949e7cda9156718ded3b300372724fdb222344b1e38d58`).
**Source card:** `../evidence/artifacts/36c05bc9172708a66457079c9f7da2e60ec8cefb23160622d96321fb471f5a7f/EXSRC-444d583231bf5f30.md` (SHA-256 `36c05bc9172708a66457079c9f7da2e60ec8cefb23160622d96321fb471f5a7f`).
**Accepted reading evidence:**
- `../evidence/artifacts/721788728638a7a28c4f2c872b412cb67c61a8b523229e2aafd19e8c14c2d196/EXSRC-444d583231bf5f30_round49_proof_binding.json` (SHA-256 `721788728638a7a28c4f2c872b412cb67c61a8b523229e2aafd19e8c14c2d196`).
- `../evidence/artifacts/36c05bc9172708a66457079c9f7da2e60ec8cefb23160622d96321fb471f5a7f/EXSRC-444d583231bf5f30.md` (SHA-256 `36c05bc9172708a66457079c9f7da2e60ec8cefb23160622d96321fb471f5a7f`).
- `../evidence/artifacts/0c177eca8e56700c5afe240f733a5d2b221ffc7417a6936db29ea09c7256dc69/EXSRC-444d583231bf5f30.md` (SHA-256 `0c177eca8e56700c5afe240f733a5d2b221ffc7417a6936db29ea09c7256dc69`).
- `../evidence/artifacts/61c1142739c95a0e9e2003eb41773e78cfaba0e0406546aed9f19d601a7f94a3/rump_theorem22_interval_example.py` (SHA-256 `61c1142739c95a0e9e2003eb41773e78cfaba0e0406546aed9f19d601a7f94a3`).
- `../evidence/artifacts/fdce2a17db94b432294e24dae5701cf2ca5257ca4d7453e6e5294d5926e7021f/rump_theorem22_interval_example.out.json` (SHA-256 `fdce2a17db94b432294e24dae5701cf2ca5257ca4d7453e6e5294d5926e7021f`).
- `../evidence/artifacts/4630ec1ca8b7c971a16a776e1e25f92c081663ee5a023a2479a6f0c8b6ade37e/rump_theorem22_proof_check.md` (SHA-256 `4630ec1ca8b7c971a16a776e1e25f92c081663ee5a023a2479a6f0c8b6ade37e`).
**Additional review context:**
- `../evidence/artifacts/e7f992678052a75f5fc8de8a635ba8d2ea7b0db8839360a27f3ec20663797773/proof_check.md` (SHA-256 `e7f992678052a75f5fc8de8a635ba8d2ea7b0db8839360a27f3ec20663797773`).
- `../evidence/artifacts/7e6011b0136dd62c6e768f8eb27558e1a8215315e76ce9bb6f779443df717f7c/identity_check.json` (SHA-256 `7e6011b0136dd62c6e768f8eb27558e1a8215315e76ce9bb6f779443df717f7c`).
- `../evidence/artifacts/0a55d7e1c4d9af903e77c4598791f494cc0b9a4be0421bac7582a0e84dd90856/binding_check.json` (SHA-256 `0a55d7e1c4d9af903e77c4598791f494cc0b9a4be0421bac7582a0e84dd90856`).
- `../evidence/artifacts/c4520bce238035eaaff70cf481354740ea41daf8861cd9af9963f9dbe17f7976/delta_binding_check.json` (SHA-256 `c4520bce238035eaaff70cf481354740ea41daf8861cd9af9963f9dbe17f7976`).
- `../evidence/artifacts/8609de94c67d5823943139ba669379558e5b2c633f7a1a4340edaaf3f662302d/preimage_verification.json` (SHA-256 `8609de94c67d5823943139ba669379558e5b2c633f7a1a4340edaaf3f662302d`).
- `../evidence/artifacts/8cd3f281a0e8bb5524836213b4513d7452689dedf469ce037476b4c7d83fa0df/reading_assets_verification.json` (SHA-256 `8cd3f281a0e8bb5524836213b4513d7452689dedf469ce037476b4c7d83fa0df`).
- `../evidence/artifacts/73980e25d27e3a97a35f00f37e9a0c9878f9fe83f0eec1c6252cca858310d59f/replay_evidence.json` (SHA-256 `73980e25d27e3a97a35f00f37e9a0c9878f9fe83f0eec1c6252cca858310d59f`).
- `../evidence/artifacts/30e58b0757ab6773afde4a3b2f3907f01c20cfd89725a5ccadf9f1c6abb3049c/independent_checks.out.json` (SHA-256 `30e58b0757ab6773afde4a3b2f3907f01c20cfd89725a5ccadf9f1c6abb3049c`).

## EXSRC-4673193ed5c8aeac — Shape Derivatives of the Eigenvalues of the de Rham Complex for Lipschitz Deformations and Variable Coefficients: Part I

**Bibliography:** Pier Domenico Lamberti, Dirk Pauly, Michele Zaccaron (2026). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/4673193ed5c8aeacd1c0d365201d7b4d1ae3753b76d3dd6f0010b12745e2d58e/lamberti_pauly_zaccaron_hellmann_feynman_part1_2024v3.pdf`; SHA-256 `4673193ed5c8aeacd1c0d365201d7b4d1ae3753b76d3dd6f0010b12745e2d58e`; version: Local PDF is arXiv:2410.19960v3, stamped 17 Feb 2025; manuscript date 18 Feb 2025. Later journal manifestation: Mathematical Methods in the Applied Sciences 49(8) (2026), 7975–8005; local PDF is not the publisher version..

**Accepted interface:** Domain transplantation and unitary equivalence of deRham/Maxwell operator families in moving weighted Hilbert products; conditional normalized eigenfield derivative formula.

**Conditions:** Bounded weak-Lipschitz pairOmega,Gamma_t; admissible biLipschitzPhi with positive essinfJacobian; positive bounded admissible coefficients and source boundary spaces. C1coefficient/form dependence and normalized pulled-back eigenfield differentiability in relevant graph/form norms for derivative formula. Retain full weighted products and transformed domains.

**Transfer limits:** No general multiple/multiparameter eigenfield differentiability; source external mixed-boundary/compactness dependencies retained; no arbitrary Markov or gap monotonicity transfer. PartI/II distinct uses, root final dedup.

**Usage card:** `../evidence/artifacts/b52f62f57826265592206002539105f04bb8495039f730e49918e81901631fb2/EXSRC-4673193ed5c8aeac.md` (SHA-256 `b52f62f57826265592206002539105f04bb8495039f730e49918e81901631fb2`).
**Reader freeze:** `../evidence/artifacts/3cef515cf88dcfe6dd6b7bc6dc0182127d237c9200059a334db2d615c0e03932/freeze_round15_round13_14_source_corrections.json` (SHA-256 `3cef515cf88dcfe6dd6b7bc6dc0182127d237c9200059a334db2d615c0e03932`).
**Independent review:** `../evidence/artifacts/278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475/review.json` (SHA-256 `278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475`).
**Accepted reading evidence:**
- `../evidence/artifacts/84a8cdc82c0726e6a1954da37a4b7a982214e56fdd71f66bed38f1f38f46c0ce/EXSRC-4673193ed5c8aeac.json` (SHA-256 `84a8cdc82c0726e6a1954da37a4b7a982214e56fdd71f66bed38f1f38f46c0ce`).
- `../evidence/artifacts/2856c8849c98087cb86c3b753a625187c370c2e8f8efb70a059522c425c6528c/EXSRC-4673193ed5c8aeac.md` (SHA-256 `2856c8849c98087cb86c3b753a625187c370c2e8f8efb70a059522c425c6528c`).
**Additional review context:**
- `../evidence/artifacts/f4267a503da7eab20a256c1433a608ef580c3d85da839b4ea84a62ba28f02959/review.json` (SHA-256 `f4267a503da7eab20a256c1433a608ef580c3d85da839b4ea84a62ba28f02959`).

## EXSRC-4ffcf4d9f2ef240c — On a Subspace Perturbation Problem

**Bibliography:** Vadim Kostrykin, Konstantin A. Makarov, Alexander K. Motovilov (2002). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/4ffcf4d9f2ef240cc2e22c10598aebe1ff767acd1a83a00582586ce9785d657e/kostrykin_makarov_motovilov_subspace_perturbation_arxiv_math0203240v3.pdf`; SHA-256 `4ffcf4d9f2ef240cc2e22c10598aebe1ff767acd1a83a00582586ce9785d657e`; version: Exact assigned arXiv:math/0203240v3, last revised 27 June 2002; 8 physical/printed pages; no VOR page mapping claimed..

**Accepted interface:** Theorem1, physical2, with Hypothesis1 physical1: bounded self-adjoint A,V, spec(A)=sigma union Sigma with d>0, P=E_A(sigma), Q=E_(A+V)(open U_(d/2)(sigma)); ||P−Q||<1 if ||V||<2d/(2+pi), OR if ||V||<d/2 AND [conv(sigma)∩Sigma=∅ OR conv(Sigma)∩sigma=∅], with INCLUSIVE OR. This is a projection-persistence prerequisite for G03.04 only, with quoted Prop2.1 as explicit external analytic dependency.

**Conditions:** Bounded self-adjoint A,V in a single fixed separable Hilbert space; nonempty closed spectral partition separated by true d>0; exact/validated baseline and perturbed spectral projections. For certification use 0<d_L<=d, v_U>=||V|| and v_U<2d_L/(2+pi), OR exact inclusive one-sided convex separation with v_U<d_L/2. Use open d/2 neighborhood; narrower d_L/2 gives same cluster because spectral distance<=v_U<d_L/2. Retain external Prop2.1 hypothesis and constants; sufficient thresholds only.

**Transfer limits:** No derivative, repeated-root splitting, target index/count, gap-size estimate, validated numerical root certificate, non-self-adjoint transfer, or moving-inner-product extension without a separate norm-correct conjugation. Stronger sqrt(2)/2 bound requires mutual convex-hull separation. The 2002 paper calls an intermediate range open only in its own historical text; this card makes no current-status claim. Theorem 1 thresholds are sufficient only, not asserted optimal.

**Usage card:** `../evidence/artifacts/9c741d8eab1a935ab10bc04eafd580e18edc2165e90d494ab623d81bfd0dc000/EXSRC-4ffcf4d9f2ef240c.md` (SHA-256 `9c741d8eab1a935ab10bc04eafd580e18edc2165e90d494ab623d81bfd0dc000`).
**Reader freeze:** `../evidence/artifacts/012d184986c394223b6c2827d47331b16fc0c4763842d892d604f7f8693525c6/freeze_round37_KMM_closed_neighborhood_microdelta.json` (SHA-256 `012d184986c394223b6c2827d47331b16fc0c4763842d892d604f7f8693525c6`).
**Independent review:** `../evidence/artifacts/5f370a022aba611fb9a86b3409077ea9764e555bd4b8b70d64acf03ed22e1bd6/review.json` (SHA-256 `5f370a022aba611fb9a86b3409077ea9764e555bd4b8b70d64acf03ed22e1bd6`).
**Accepted reading evidence:**
- `../evidence/artifacts/83ebb714cef46c939c85add38c020a05b27c6eee3b79830e372987b0c132438c/EXSRC-4ffcf4d9f2ef240c.json` (SHA-256 `83ebb714cef46c939c85add38c020a05b27c6eee3b79830e372987b0c132438c`).
- `../evidence/artifacts/789168da9434cfac96ae65d41a82a40c683de651393144df05357e25c9047335/EXSRC-4ffcf4d9f2ef240c.md` (SHA-256 `789168da9434cfac96ae65d41a82a40c683de651393144df05357e25c9047335`).
- `../evidence/artifacts/cced5f9174d79f151e550b9aced5069cbde88296c3f255a0a5ec01e615c29d6b/subspace_projection_persistence_exact.py` (SHA-256 `cced5f9174d79f151e550b9aced5069cbde88296c3f255a0a5ec01e615c29d6b`).
- `../evidence/artifacts/3eb66ef8601a4f8c4d091d6f6ce7c30248dc19afa2fbac92de7f3fa1c37ab0db/subspace_projection_persistence_exact.out.json` (SHA-256 `3eb66ef8601a4f8c4d091d6f6ce7c30248dc19afa2fbac92de7f3fa1c37ab0db`).
- `../evidence/artifacts/c9aeb06ddbe20cc24d34d3a97445eec255fa1085a5e2c03e234d0ade6ad85e93/subspace_projection_persistence_proof_check.md` (SHA-256 `c9aeb06ddbe20cc24d34d3a97445eec255fa1085a5e2c03e234d0ade6ad85e93`).
- `../evidence/artifacts/f35d682f9352af36409221e7a45d6dae815d7e1e389ce368d38bdd39916c55c0/render_manifest.json` (SHA-256 `f35d682f9352af36409221e7a45d6dae815d7e1e389ce368d38bdd39916c55c0`).
**Additional review context:**
- `../evidence/artifacts/da4aac9e3f8594bdc92791af60c34b9f8e8c5f7fe3ca7e49b43f5607d9304aee/proof_check.md` (SHA-256 `da4aac9e3f8594bdc92791af60c34b9f8e8c5f7fe3ca7e49b43f5607d9304aee`).
- `../evidence/artifacts/dbb75304296521d6e587820a81f984c3eae36ce6c621e89b4c9004afb5d15887/binding_check.json` (SHA-256 `dbb75304296521d6e587820a81f984c3eae36ce6c621e89b4c9004afb5d15887`).
- `../evidence/artifacts/582c65ef3a7e9a9fb360f7b137036f47869a860e7980a2a10298e6545c87884b/preimage_verification.json` (SHA-256 `582c65ef3a7e9a9fb360f7b137036f47869a860e7980a2a10298e6545c87884b`).
- `../evidence/artifacts/9a6729a2a63288210af4883d4f4cf1d91aa661cba73e4f0a266ec8a44820d3d9/independent_checks.out.json` (SHA-256 `9a6729a2a63288210af4883d4f4cf1d91aa661cba73e4f0a266ec8a44820d3d9`).
- `../evidence/artifacts/80578494ff2ca32f08abaf88eb2f2e0c1285d7ec9c793e5bf52946e5260e4f17/reader_rerun_evidence.json` (SHA-256 `80578494ff2ca32f08abaf88eb2f2e0c1285d7ec9c793e5bf52946e5260e4f17`).
- `../evidence/artifacts/8a30c71d497c10c92e922e11a032be60637da33ec13792d504faa19e0dfa659d/freeze_round35_KMM_spectral_projection_persistence.json` (SHA-256 `8a30c71d497c10c92e922e11a032be60637da33ec13792d504faa19e0dfa659d`).
- `../evidence/artifacts/51ab5064c5ecb7073f1aa02323fb3377419dfd6c15a31c9a0efeb9a5d5c05b8f/freeze_round36_KMM_certificate_scope_microdelta.json` (SHA-256 `51ab5064c5ecb7073f1aa02323fb3377419dfd6c15a31c9a0efeb9a5d5c05b8f`).

## EXSRC-5a24037450459fdd — Shape Derivatives of the Eigenvalues of the de Rham Complex for Lipschitz Deformations and Variable Coefficients: Part II

**Bibliography:** Pier Domenico Lamberti, Dirk Pauly, Michele Zaccaron (2025). **Method IDs:** G03.03, G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/5a24037450459fdd0d39f62f791b8d2d8e318deb3fbfdf6d5f6f8b6ec40727ea/henrot_part2_feynman_hellmann_2025.pdf`; SHA-256 `5a24037450459fdd0d39f62f791b8d2d8e318deb3fbfdf6d5f6f8b6ec40727ea`; version: arXiv:2502.12670v1 (18 February 2025).

**Accepted interface:** Moving-energy minus lambda-times-moving-mass derivative compression for a positive isolated finite-multiplicity self-adjoint operator cluster.

**Conditions:** Common full closed-operator domain V/equivalent graph norms, equivalent moving Hilbert products; source reduced-domain compact embedding (or explicit stronger full-V compact subcase); C^r form maps and isolated positive finite cluster; one real parameter for C1/analytic labels.

**Transfer limits:** Only positive isolated finite cluster in the stated common-domain/reduced-compactness framework. Keep all moving-mass terms and elementary-symmetric prefactor. No zero-cluster extension or complete all-PDE/surface-formula proof; no arbitrary Markov transfer. Part I and II distinct uses; root final deduplication.

**Usage card:** `../evidence/artifacts/3118213e426cf879464d5f9f60ed9352496801b81d47df881f7c4260e9b6a88c/EXSRC-5a24037450459fdd.md` (SHA-256 `3118213e426cf879464d5f9f60ed9352496801b81d47df881f7c4260e9b6a88c`).
**Reader freeze:** `../evidence/artifacts/a5d5d7d7876968843c8f80030a0e9d3e3268c74a32bf2e0272705bc7e3c54c88/freeze_round16_round15_microdelta.json` (SHA-256 `a5d5d7d7876968843c8f80030a0e9d3e3268c74a32bf2e0272705bc7e3c54c88`).
**Independent review:** `../evidence/artifacts/278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475/review.json` (SHA-256 `278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475`).
**Accepted reading evidence:**
- `../evidence/artifacts/bac001186cdb3d8bffc55c9c196ccf93089e37d79122dd086f52ffb99f607441/EXSRC-5a24037450459fdd.json` (SHA-256 `bac001186cdb3d8bffc55c9c196ccf93089e37d79122dd086f52ffb99f607441`).
- `../evidence/artifacts/f522b6787fc85c30a53c473927c2706a7e12d25944d88a61bd758b7b86f7b8e8/EXSRC-5a24037450459fdd.md` (SHA-256 `f522b6787fc85c30a53c473927c2706a7e12d25944d88a61bd758b7b86f7b8e8`).
**Additional review context:**
- `../evidence/artifacts/461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11/review.json` (SHA-256 `461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11`).

## EXSRC-8591580ae82070e1 — Perturbation Theory of Polynomials and Linear Operators

**Bibliography:** Adam Parusiński, Armin Rainer (2023). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/8591580ae82070e18e1542e27999175c2e5eccfc043a7c8d3209b6acb8122661/parusinski_rainer_perturbation_2023v3.pdf`; SHA-256 `8591580ae82070e18e1542e27999175c2e5eccfc043a7c8d3209b6acb8122661`; version: arXiv:2308.01299v3 (22 October 2024).

**Accepted interface:** G03.04 critical condition boundary: analytic relabeling can coexist with a corner in sorted eigenvalues; a Lipschitz normal two-parameter family can have monodromy obstructing continuous eigenvalue selection. Survey statement/condition selection is checked with primary proof dependencies explicit.

**Conditions:** Crossing witness diag(t,-t) is analytic Hermitian, with largest sorted eigenvalue |t| and one-sided slopes -1,+1. Independent normal Lipschitz witness A(z)=[[0,z],[|z|,0]] has no continuous eigenvalue selection on any full neighborhood of0. Invoking survey Cor3.45 requires a continuous selection on open V subset U and its stated family hypotheses; invoking the labeling theorems retains the named primary proof dependencies.

**Transfer limits:** No claim to close the primary Rellich/Rainer C1/C2 global labeling proofs. No differentiable eigenvectors, sorted branch derivative or gap sign, automatic Markov transfer, or validation certificate. Accepted key proof is the direct boundary example, not those external positive theorems.

**Usage card:** `../evidence/artifacts/0d5a9f7259d91ccf869426bfc96896cf0f826eba5af811199f983e5a2c87a2fb/EXSRC-8591580ae82070e1.md` (SHA-256 `0d5a9f7259d91ccf869426bfc96896cf0f826eba5af811199f983e5a2c87a2fb`).
**Reader freeze:** `../evidence/artifacts/a5d5d7d7876968843c8f80030a0e9d3e3268c74a32bf2e0272705bc7e3c54c88/freeze_round16_round15_microdelta.json` (SHA-256 `a5d5d7d7876968843c8f80030a0e9d3e3268c74a32bf2e0272705bc7e3c54c88`).
**Independent review:** `../evidence/artifacts/278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475/review.json` (SHA-256 `278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475`).
**Accepted reading evidence:**
- `../evidence/artifacts/0ac3f31e28298a15635c5b84baf0492e4fc98f8b549af8c0fba31ab423751a40/EXSRC-8591580ae82070e1.json` (SHA-256 `0ac3f31e28298a15635c5b84baf0492e4fc98f8b549af8c0fba31ab423751a40`).
- `../evidence/artifacts/aca376932dbe52207c5c2819ddf5f086a3f158045313297895d497ccc0b73d6c/EXSRC-8591580ae82070e1.md` (SHA-256 `aca376932dbe52207c5c2819ddf5f086a3f158045313297895d497ccc0b73d6c`).
**Additional review context:**
- `../evidence/artifacts/461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11/review.json` (SHA-256 `461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11`).

## EXSRC-8ae92494bfc03225 — Eigenvalues and Eigenvectors of a Matrix Dependent on Several Parameters

**Bibliography:** Ji-Guang Sun (1985). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/8ae92494bfc03225842d9602bc5c674d3412c3da9e8daa0c8f15d8e3a01129fd/sun_eigenvalues_eigenvectors_multivariate_parameters_1985.pdf`; SHA-256 `8ae92494bfc03225842d9602bc5c674d3412c3da9e8daa0c8f15d8e3a01129fd`; version: Exact 14-page publisher scan, Journal of Computational Mathematics 3(4) (1985), printed pp. 351–364..

**Accepted interface:** G03.04 first-order compression of an isolated multiple real-symmetric eigenvalue. Source Theorem4.1 Eq4.6 physical12/printed362 gives the coordinate one-sided slope-set union sigma(X1^T ∂_i A X1). After restoring O(t²) in printed364, Weyl closes its first-order conclusion. Separately derived and independently reclosed: for a C1 real-symmetric path A(t)=A0+tH+o(|t|), the signed r-cluster-shift multiset tends from either side to sigma_mult(X1^T H X1); negative t reverses ordered index matching.

**Conditions:** One fixed finite-dimensional real Euclidean inner product; source A(p) real analytic and symmetric near0; full isolated multiplicity-r eigenspace at lambda, orthonormal X1 and separated complement lambda outside sigma(A2). For the derived path version differentiability at0 in operator norm suffices. Full compressed derivative, not arbitrary diagonal Rayleigh entries or partial eigenspace; nonorthonormal coordinates require their Gram metric. Exact/validated eigenspace, derivative and separation needed for any numerical certificate. Set statement versus derived multiplicity-resolved multiset explicitly separated.

**Transfer limits:** Finite real symmetric/fixed inner product, first-order one-coordinate or fixed-direction path only. No global analytic labeling, continuous/differentiable eigenbasis, higher-order degenerate splitting, moving Gibbs metric transfer, gap derivative, counting, Sturm/inertia, or Markov conclusion.

**Usage card:** `../evidence/artifacts/8ba2106e8ae6ab1341260b2d95539ce4cc78f0928d3a49264184b8f6ac16edba/EXSRC-8ae92494bfc03225.md` (SHA-256 `8ba2106e8ae6ab1341260b2d95539ce4cc78f0928d3a49264184b8f6ac16edba`).
**Reader freeze:** `../evidence/artifacts/9d7abe4dfa85d0bfa7756cb927b34bd6ad5b3fe5dd5cf4f206381d35ec0a0ab4/freeze_round45_Sun_first_order_remainder_Weyl_delta.json` (SHA-256 `9d7abe4dfa85d0bfa7756cb927b34bd6ad5b3fe5dd5cf4f206381d35ec0a0ab4`).
**Independent review:** `../evidence/artifacts/54cda65e448a3ecec5149e0654a8747b873f5477515d62255b164d271689a3ae/review.json` (SHA-256 `54cda65e448a3ecec5149e0654a8747b873f5477515d62255b164d271689a3ae`).
**Source card:** `../evidence/artifacts/02cef4db0c395b76095aed79b6c892219ff35c3d12d04b2785102fae5dce7fe1/EXSRC-8ae92494bfc03225.md` (SHA-256 `02cef4db0c395b76095aed79b6c892219ff35c3d12d04b2785102fae5dce7fe1`).
**Accepted reading evidence:**
- `../evidence/artifacts/35a65bea767554795698ea21b5432cc238f97da380fb17fcacede94147f50eaa/EXSRC-8ae92494bfc03225.json` (SHA-256 `35a65bea767554795698ea21b5432cc238f97da380fb17fcacede94147f50eaa`).
- `../evidence/artifacts/02cef4db0c395b76095aed79b6c892219ff35c3d12d04b2785102fae5dce7fe1/EXSRC-8ae92494bfc03225.md` (SHA-256 `02cef4db0c395b76095aed79b6c892219ff35c3d12d04b2785102fae5dce7fe1`).
- `../evidence/artifacts/32aa7147701d9879e71ecb9ca53ba11b1d26432bddb441f7c5472c04fe0137d6/sun_multiple_eigenvalue_slopes_exact.py` (SHA-256 `32aa7147701d9879e71ecb9ca53ba11b1d26432bddb441f7c5472c04fe0137d6`).
- `../evidence/artifacts/e2c1a2a07376394bcc58b59c06b3c165a5d90ddb1ff34bf9aafe60272de502bb/sun_multiple_eigenvalue_slopes_exact.out.json` (SHA-256 `e2c1a2a07376394bcc58b59c06b3c165a5d90ddb1ff34bf9aafe60272de502bb`).
- `../evidence/artifacts/0cbe4d1a524a873f41f3343e74efa08fc037de5775850ef4c2349e584d45ee17/sun_first_order_remainder_exact.py` (SHA-256 `0cbe4d1a524a873f41f3343e74efa08fc037de5775850ef4c2349e584d45ee17`).
- `../evidence/artifacts/83764f8c32c3a42c1c8d10c17194a93dc376577bfbaa4bba838c7c666837f4b4/sun_first_order_remainder_exact.out.json` (SHA-256 `83764f8c32c3a42c1c8d10c17194a93dc376577bfbaa4bba838c7c666837f4b4`).
- `../evidence/artifacts/6635690bb7409e8a7ff61e1d86e5f15369217bf811cc264f2299d33a6a80d5fa/sun_multiple_eigenvalue_slopes_proof_check.md` (SHA-256 `6635690bb7409e8a7ff61e1d86e5f15369217bf811cc264f2299d33a6a80d5fa`).
**Additional review context:**
- `../evidence/artifacts/7086cd31a1b0dfaa66e0ba6b03002d4f5139d2f6c3bdeefce787df117b03d69c/proof_check.md` (SHA-256 `7086cd31a1b0dfaa66e0ba6b03002d4f5139d2f6c3bdeefce787df117b03d69c`).
- `../evidence/artifacts/53135e06cf2e57bf264311d0c75c09cf134f8ee1c3e4eec50178ee99e33beecd/identity_check.json` (SHA-256 `53135e06cf2e57bf264311d0c75c09cf134f8ee1c3e4eec50178ee99e33beecd`).
- `../evidence/artifacts/fdb7b9d00491b498dfb84ef3bcf562cad35dd0364a19b635fd4a41374cb86cfa/binding_check.json` (SHA-256 `fdb7b9d00491b498dfb84ef3bcf562cad35dd0364a19b635fd4a41374cb86cfa`).
- `../evidence/artifacts/44338dd6d671a57741c335d485130d08a5a596cf44c7bd3c6c0fb68b55d4e3cb/delta_binding_check.json` (SHA-256 `44338dd6d671a57741c335d485130d08a5a596cf44c7bd3c6c0fb68b55d4e3cb`).
- `../evidence/artifacts/99f52a84ca81766e4758b6b44b446a8dea5be056cee5bbc283c87c19628e9946/preimage_verification.json` (SHA-256 `99f52a84ca81766e4758b6b44b446a8dea5be056cee5bbc283c87c19628e9946`).
- `../evidence/artifacts/988c26195e001d39d2fb7fe7ae468a49e859983b9502d7ac5a808b72d44a3eff/replay_evidence.json` (SHA-256 `988c26195e001d39d2fb7fe7ae468a49e859983b9502d7ac5a808b72d44a3eff`).
- `../evidence/artifacts/5e5938b9af3291138ce47efae7d4abcf12de651234342bd9ade651fc7fd11164/delta_replay_evidence.json` (SHA-256 `5e5938b9af3291138ce47efae7d4abcf12de651234342bd9ade651fc7fd11164`).
- `../evidence/artifacts/0bda4e57a5d238e5b411190182070d977e3666c3cae812a45b96dd4d1d26f779/independent_checks.out.json` (SHA-256 `0bda4e57a5d238e5b411190182070d977e3666c3cae812a45b96dd4d1d26f779`).

## EXSRC-9526ff2748a7a983 — Verified numerical computations for multiple and nearly multiple eigenvalues of elliptic operators

**Bibliography:** Kazuaki Toyonaga, Mitsuhiro T. Nakao, Yoshitaka Watanabe (2002). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/9526ff2748a7a983d216c7dd30e8d5cfca1ebbe14ad0ad74c3178f6c0f41145b/toyonaga_nakao_watanabe_multiple_eigenvalues_2002.pdf`; SHA-256 `9526ff2748a7a983d216c7dd30e8d5cfca1ebbe14ad0ad74c3178f6c0f41145b`; version: Author-hosted complete article copy; Journal of Computational and Applied Mathematics 147 (2002), 175–190.

**Accepted interface:** Two-basis invariant-subspace elliptic eigenvalue enclosure by verified finite/infinite-dimensional fixed-point inclusion and tail bounds.

**Conditions:** Bounded convexOmega subsetR2, realLinfq, DirichletH01; Sh subsetH01 intersectH2; n2 computable certificate, validated finite inverse, positiveX and X+Z<=W, all residual/tail bounds, certified independent basis. Fourier constant only(pi-square,N=min cutoffs).

**Transfer limits:** Computed certificate only the displayed n=2 scope, with the stated square/cutoff Fourier bound. Overlapping intervals do not certify equality. No whole-spectrum count, arbitrary operator transfer or rerun of INTLAB tables.

**Usage card:** `../evidence/artifacts/e84a4300b94661131066ebed36cadd0a22d13b9a96b7bebaada3d452767e180f/EXSRC-9526ff2748a7a983.md` (SHA-256 `e84a4300b94661131066ebed36cadd0a22d13b9a96b7bebaada3d452767e180f`).
**Reader freeze:** `../evidence/artifacts/3cef515cf88dcfe6dd6b7bc6dc0182127d237c9200059a334db2d615c0e03932/freeze_round15_round13_14_source_corrections.json` (SHA-256 `3cef515cf88dcfe6dd6b7bc6dc0182127d237c9200059a334db2d615c0e03932`).
**Independent review:** `../evidence/artifacts/278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475/review.json` (SHA-256 `278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475`).
**Accepted reading evidence:**
- `../evidence/artifacts/cfd96caf103ef27c36d91532a6f33611dc42cfb4770ee8df61ec204d8a2cbcc0/EXSRC-9526ff2748a7a983.json` (SHA-256 `cfd96caf103ef27c36d91532a6f33611dc42cfb4770ee8df61ec204d8a2cbcc0`).
- `../evidence/artifacts/3c2de2dec80463699d39194697230d6994e1b23e2b5a0e864a79b13523a145c5/EXSRC-9526ff2748a7a983.md` (SHA-256 `3c2de2dec80463699d39194697230d6994e1b23e2b5a0e864a79b13523a145c5`).
**Additional review context:**
- `../evidence/artifacts/f4267a503da7eab20a256c1433a608ef580c3d85da839b4ea84a62ba28f02959/review.json` (SHA-256 `f4267a503da7eab20a256c1433a608ef580c3d85da839b4ea84a62ba28f02959`).

## EXSRC-b69b39b5ee6c4569 — Spectral Enclosures and Complex Resonances for General Self-Adjoint Operators

**Bibliography:** E. Brian Davies (1998). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/b69b39b5ee6c4569f3feb2ce48ae891cc3ff56a53462d3714d156c9099b4bf1b/davies_spectral_enclosures_complex_resonances_1998.pdf`; SHA-256 `b69b39b5ee6c4569f3feb2ce48ae891cc3ff56a53462d3714d156c9099b4bf1b`; version: Publisher article PDF; LMS Journal of Computation and Mathematics 1 (1998), printed pp.42–74.

**Accepted interface:** Validated residual enclosure of one isolated self-adjoint spectral point using a separately certified uniqueness bracket.

**Conditions:** H self-adjoint; finite nonzero L subsetDomH; rho-<sigma-<sigma+<rho+; unique spectral point in bracket; validated upper residual bounds obey both strict margins.

**Transfer limits:** Small residual localizes spectrum; Theorem3 still requires the externally verified unique-point bracket. No bracket discovery, derivative, monotonicity or unvalidated Ritz certificate.

**Usage card:** `../evidence/artifacts/2917c0ba724a3500c209eed8cfcca40857c236759938d8b40928f641bc4b942e/EXSRC-b69b39b5ee6c4569.md` (SHA-256 `2917c0ba724a3500c209eed8cfcca40857c236759938d8b40928f641bc4b942e`).
**Reader freeze:** `../evidence/artifacts/3cef515cf88dcfe6dd6b7bc6dc0182127d237c9200059a334db2d615c0e03932/freeze_round15_round13_14_source_corrections.json` (SHA-256 `3cef515cf88dcfe6dd6b7bc6dc0182127d237c9200059a334db2d615c0e03932`).
**Independent review:** `../evidence/artifacts/278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475/review.json` (SHA-256 `278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475`).
**Accepted reading evidence:**
- `../evidence/artifacts/595a37a92ff05648ff0df0428f06dc8ed2e75c80c25021fcd200fcdf60a1af0c/EXSRC-b69b39b5ee6c4569.json` (SHA-256 `595a37a92ff05648ff0df0428f06dc8ed2e75c80c25021fcd200fcdf60a1af0c`).
- `../evidence/artifacts/76239699bf6e44ac355eeeda9725b46e0c77de0870f096f85f6def524de54786/EXSRC-b69b39b5ee6c4569.md` (SHA-256 `76239699bf6e44ac355eeeda9725b46e0c77de0870f096f85f6def524de54786`).
**Additional review context:**
- `../evidence/artifacts/461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11/review.json` (SHA-256 `461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11`).

## EXSRC-c6dace1707facd75 — Effective Perturbation Theory for Simple Isolated Eigenvalues of Linear Operators

**Bibliography:** Benoît R. Kloeckner (2019). **Method IDs:** G03.03. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/c6dace1707facd7560c748825b4e9b2fad298ecd7b2c4628f6d859119fe1b392/kloeckner_effective_simple_isolated_2019.pdf`; SHA-256 `c6dace1707facd7560c748825b4e9b2fad298ecd7b2c4628f6d859119fe1b392`; version: Complete local author manuscript dated 20 December 2018, physical pp.1–21; later JOT 81(1) (2019), pp.175–194, DOI 10.7900/jot.2017dec22.2179; local PDF is not journal layout.

**Accepted interface:** Explicit local simple-isolated eigenvalue radius and derivative/Taylor bounds in a fixed Banach operator norm.

**Conditions:** L0 bounded on fixed real/complex Banach X; simple isolated lambda0; phi0(u0)=1; tau0=||P0||,gamma0=||S0||; ||M||<1/(6tau0gamma0); K>1 smaller ball for stated remainder.

**Transfer limits:** Exact 21-page author manuscript version; no multiple branch or untreated changing metric. Separate leading-gap contraction assumption.

**Usage card:** `../evidence/artifacts/da10f897625e25a9deb76364a4cdc7051e1046a22904920cad041414fbf89807/EXSRC-c6dace1707facd75.md` (SHA-256 `da10f897625e25a9deb76364a4cdc7051e1046a22904920cad041414fbf89807`).
**Reader freeze:** `../evidence/artifacts/3cef515cf88dcfe6dd6b7bc6dc0182127d237c9200059a334db2d615c0e03932/freeze_round15_round13_14_source_corrections.json` (SHA-256 `3cef515cf88dcfe6dd6b7bc6dc0182127d237c9200059a334db2d615c0e03932`).
**Independent review:** `../evidence/artifacts/278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475/review.json` (SHA-256 `278bbf81591ec0ab143068d7f7accbeb677505df46d0c73504680d1f86796475`).
**Accepted reading evidence:**
- `../evidence/artifacts/78a6977af188c95b80a12575f169ade3d13ac58e90d2ce117a9df4c002ab9ff6/EXSRC-c6dace1707facd75.json` (SHA-256 `78a6977af188c95b80a12575f169ade3d13ac58e90d2ce117a9df4c002ab9ff6`).
- `../evidence/artifacts/2cd6570f535147e34998340c5c410d9b119c7803a3a05c302d2d269b2114b85f/EXSRC-c6dace1707facd75.md` (SHA-256 `2cd6570f535147e34998340c5c410d9b119c7803a3a05c302d2d269b2114b85f`).
**Additional review context:**
- `../evidence/artifacts/461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11/review.json` (SHA-256 `461e4e3c3af8f165170ab75c2b12d81d34f3b6445ed742b8a470f32f19df2d11`).

## EXSRC-d0a801e6072f50c3 — Certified Spectral Approximation of Transfer Operators and the Gauss Map

**Bibliography:** Isaia Nisoli (2026). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/d0a801e6072f50c3c90973492e4916d26ef993ce76b1a0086929745bf24350fb/nisoli_certified_spectral_approximation_transfer_operators_gauss_map_arxiv2602.19435v2.pdf`; SHA-256 `d0a801e6072f50c3c90973492e4916d26ef993ce76b1a0086929745bf24350fb`; version: Exact assigned arXiv:2602.19435v2, revised 1 March 2026; 36-page main paper; supplement excluded..

**Accepted interface:** Assumption2.8/Lemma2.9 physical=printed9: in one fixed complex Banach norm, certified error epsilon and full-contour resolvent bound M with q=epsilon M<1 certify contour exclusion and ||P_L−P_N||<=length(Gamma)epsilon M²/[2pi(1−q)]. If this displayed bound<1, Remark2.10 gives isomorphic Riesz ranges and equal finite algebraic rank.

**Conditions:** Bounded operators on the same complex Banach space; positively oriented bounded-domain piecewise C1 Jordan boundary contained in model resolvent set; certified same B→B approximation error; certified full operator resolvent bound over the entire contour, including complement action/basis norms; strict q<1. For the admitted close-projection isomorphism route additionally check displayed bound<1. This is sufficient, not necessary rank control. Finite rank/generalized spectral subspace is distinct from geometric eigenspace dimension.

**Transfer limits:** No DFLY weak-error lifting, implementation/SVD certification, Gauss benchmark digits or unread supplement, eigenvector regularity, parameter derivative, individual eigenvalue enclosure, or automatic probability/mixing result. No automatic strict contour condition from a closed pseudospectral-component boundary. The elementary selected Banach argument and exact finite examples are independently verified in the formal R01 report.

**Usage card:** `../evidence/artifacts/00763405a87c8ebd4220e66510f1ecf790a7f27959c64bd3a0e67a1ab045e7e4/EXSRC-d0a801e6072f50c3.md` (SHA-256 `00763405a87c8ebd4220e66510f1ecf790a7f27959c64bd3a0e67a1ab045e7e4`).
**Reader freeze:** `../evidence/artifacts/3707000b5a8b53ff8724e7f7cbdcfa74e786c8dc85b74d208181f660a98714ee/freeze_round42_Nisoli_rank_homotopy_and_binding_delta.json` (SHA-256 `3707000b5a8b53ff8724e7f7cbdcfa74e786c8dc85b74d208181f660a98714ee`).
**Independent review:** `../evidence/artifacts/5ba42f5669e5200bd103c085f728e27e79986d751b67da29517e36839c9485cb/review.json` (SHA-256 `5ba42f5669e5200bd103c085f728e27e79986d751b67da29517e36839c9485cb`).
**Source card:** `../evidence/artifacts/faebb280c9b812d7017bdfc01c40a53c1032c136d4d2849023fe1eed69f8360e/EXSRC-d0a801e6072f50c3.md` (SHA-256 `faebb280c9b812d7017bdfc01c40a53c1032c136d4d2849023fe1eed69f8360e`).
**Accepted reading evidence:**
- `../evidence/artifacts/175bb195791a2c5a932ebb295b2a6fb113ae7d78aaaf9b878bd100dfed7eb1fd/EXSRC-d0a801e6072f50c3.json` (SHA-256 `175bb195791a2c5a932ebb295b2a6fb113ae7d78aaaf9b878bd100dfed7eb1fd`).
- `../evidence/artifacts/faebb280c9b812d7017bdfc01c40a53c1032c136d4d2849023fe1eed69f8360e/EXSRC-d0a801e6072f50c3.md` (SHA-256 `faebb280c9b812d7017bdfc01c40a53c1032c136d4d2849023fe1eed69f8360e`).
- `../evidence/artifacts/083b94a23789d18bc8119a386af816759e50f3671bdbe78ccb3745db5d9afe94/nisoli_riesz_projection_exact.py` (SHA-256 `083b94a23789d18bc8119a386af816759e50f3671bdbe78ccb3745db5d9afe94`).
- `../evidence/artifacts/f4d5432a32a8f7e4e6587d0fbd01e556eb84131bd4d80a6b538082915f53f301/nisoli_riesz_projection_exact.out.json` (SHA-256 `f4d5432a32a8f7e4e6587d0fbd01e556eb84131bd4d80a6b538082915f53f301`).
- `../evidence/artifacts/efb04de7876c7f7b00b68fbfbfb051824974bc9c77a347b02b42e69705eb96db/nisoli_riesz_projection_proof_check.md` (SHA-256 `efb04de7876c7f7b00b68fbfbfb051824974bc9c77a347b02b42e69705eb96db`).
**Additional review context:**
- `../evidence/artifacts/696d345e60780f7825977db953d260da8f2c6bb8345f8837402d3118c259cbaa/proof_check.md` (SHA-256 `696d345e60780f7825977db953d260da8f2c6bb8345f8837402d3118c259cbaa`).
- `../evidence/artifacts/791473f055bc6201d4e5f8666ca47666fb6a98b006a50743489db15ed1735b76/binding_check.json` (SHA-256 `791473f055bc6201d4e5f8666ca47666fb6a98b006a50743489db15ed1735b76`).
- `../evidence/artifacts/6712870a35d87b8dc89a4b384ccb627002b4a7397866550816ffd3f9e4ae2b10/delta_binding_check.json` (SHA-256 `6712870a35d87b8dc89a4b384ccb627002b4a7397866550816ffd3f9e4ae2b10`).
- `../evidence/artifacts/d92be12bf8ed56daaec5470c79371a49991aaec7276a7587b740b324012edd0d/preimage_verification.json` (SHA-256 `d92be12bf8ed56daaec5470c79371a49991aaec7276a7587b740b324012edd0d`).
- `../evidence/artifacts/5ab0105cd8e092096d72c93cc39671e3d14bd97de02863d2dd6a05a45b15fc53/replay_evidence.json` (SHA-256 `5ab0105cd8e092096d72c93cc39671e3d14bd97de02863d2dd6a05a45b15fc53`).
- `../evidence/artifacts/3bcc4f9801e6baad643faf72b16ba61df21788ea798b48919ef6765ec62579a2/independent_checks.out.json` (SHA-256 `3bcc4f9801e6baad643faf72b16ba61df21788ea798b48919ef6765ec62579a2`).

## EXSRC-d6ada59b1c42f828 — A framework of verified eigenvalue bounds for self-adjoint differential operators

**Bibliography:** Xuefeng Liu (2015). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/d6ada59b1c42f82831e5a98a8537a58ef541406d4248fcae7908642b4d680912/liuxuefeng_verified_eigenvalue_bounds_2015.pdf`; SHA-256 `d6ada59b1c42f82831e5a98a8537a58ef541406d4248fcae7908642b4d680912`; version: Exact local 15-physical-page in-press/corrected-proof copy; publisher record metadata is Applied Mathematics and Computation 267 (2015), 341–355; no physical-page map asserted..

**Accepted interface:** Fixed one-dimensional Dirichlet Laplacian on (0,1), V=H0^1, conforming continuous P1 subspace Vh⊂V. For k≤dim(Vh), Theorem 2.1 gives λh,k/(1+Ch^2 λh,k)≤λk and conforming min–max gives λk≤λh,k, with Ch=h/π.

**Conditions:** Real self-adjoint Dirichlet Laplacian on (0,1), energy form M=∫u'v' and mass form N=∫uv.; Compact embedding H0^1(0,1)↪L2(0,1) and ordered exact eigenvalues.; Conforming continuous piecewise-linear trial space Vh⊂H0^1; therefore V(h)=V and the abstract error assumption is applied on its stated domain.; Mesh parameter h is the maximum subinterval length; projection is the nodal/energy projection and interval Poincaré inequality gives Ch=h/π.; Finite generalized eigenvalues are exact or independently one-sided interval-certified; rounded point approximations alone are not certificates.; global all-u projection residual estimate, verified Ch upper input, and correctly indexed positive generalized eigenvalue enclosures required.

**Transfer limits:** Only the conforming 1D fixed-operator variational enclosure and strict adjacent-eigenvalue isolation interface; no Sturm/inertia, nonconforming upper bound, 2D/3D constants, parameter derivative, Markov/Gibbs transfer.

**Usage card:** `../evidence/artifacts/62e6aef182964663da1e68a45ebab2937e001d9d2f310a737c2e569b5ab18e76/EXSRC-d6ada59b1c42f828.md` (SHA-256 `62e6aef182964663da1e68a45ebab2937e001d9d2f310a737c2e569b5ab18e76`).
**Reader freeze:** `../evidence/artifacts/a52e42fca67801a0dddf12768dbf7efb6bcb93238c0bd0dd57e0de0ec67ade4a/round31_Liu2015_domain_extension_binding_addendum.json` (SHA-256 `a52e42fca67801a0dddf12768dbf7efb6bcb93238c0bd0dd57e0de0ec67ade4a`).
**Independent review:** `../evidence/artifacts/be49d8e303182e8ccaf3b64648c774ec44c4196a319cb19d034bc137b176c0e0/review.json` (SHA-256 `be49d8e303182e8ccaf3b64648c774ec44c4196a319cb19d034bc137b176c0e0`).
**Accepted reading evidence:**
- `../evidence/artifacts/356784d8e133359c53db95442f728f7d46cdb99c341ffa4ad2b66438aeb8aa03/EXSRC-d6ada59b1c42f828.json` (SHA-256 `356784d8e133359c53db95442f728f7d46cdb99c341ffa4ad2b66438aeb8aa03`).
- `../evidence/artifacts/a4717eb2005b0f8eda53711e12694cca2d09731b1dccb426cf7dad6aa63f5b52/EXSRC-d6ada59b1c42f828.md` (SHA-256 `a4717eb2005b0f8eda53711e12694cca2d09731b1dccb426cf7dad6aa63f5b52`).
- `../evidence/artifacts/5a4e36adc9d0b43f1169153fcd573ad2d2b122c941eedae3245041df2e2c0b61/liu_1d_exact_gap_check.py` (SHA-256 `5a4e36adc9d0b43f1169153fcd573ad2d2b122c941eedae3245041df2e2c0b61`).
- `../evidence/artifacts/6fb40c2fa8c344fca30b7d94fee0919436eeb01a7892ebb137a8b9d7e8f797b0/liu_1d_exact_gap_check.out.json` (SHA-256 `6fb40c2fa8c344fca30b7d94fee0919436eeb01a7892ebb137a8b9d7e8f797b0`).
**Additional review context:**
- `../evidence/artifacts/c672fcca578c75ea6876907b7b33aa6049e305e5707dc58cda0a8c40afbd9564/proof_check.md` (SHA-256 `c672fcca578c75ea6876907b7b33aa6049e305e5707dc58cda0a8c40afbd9564`).
- `../evidence/artifacts/083e15928e62248a93286bb02c1f43209b603355cea11c56ed0ba7234e0fa26f/round31_binding_check.json` (SHA-256 `083e15928e62248a93286bb02c1f43209b603355cea11c56ed0ba7234e0fa26f`).
- `../evidence/artifacts/c1af893263f8cfe1c8196eaba5367edb43a14fdf2f3b6bc2d3cf35ec29959c38/addendum_binding_check.json` (SHA-256 `c1af893263f8cfe1c8196eaba5367edb43a14fdf2f3b6bc2d3cf35ec29959c38`).
- `../evidence/artifacts/4278c6e0ea1f5c353b6808f512206cbf2966268acd23c14ca77a66cbab7ae36f/independent_checks.out.json` (SHA-256 `4278c6e0ea1f5c353b6808f512206cbf2966268acd23c14ca77a66cbab7ae36f`).
- `../evidence/artifacts/f3e5738db1a4da50851e82b5c687438cd33553fbe2b593333458bb58b70cac13/freeze_round31_Liu2015_conforming_1D_enclosure.json` (SHA-256 `f3e5738db1a4da50851e82b5c687438cd33553fbe2b593333458bb58b70cac13`).

## EXSRC-ec4eb0aeceb6a01e — Perturbation Theory of Eigenvalue Problems

**Bibliography:** Franz Rellich (1954). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/ec4eb0aeceb6a01e99911f25191cdd664e4cee614d206de66b8e7a53ee9eb4ea/rellich_perturbation_theory_eigenvalue_problems_1954_IA.pdf`; SHA-256 `ec4eb0aeceb6a01e99911f25191cdd664e4cee614d206de66b8e7a53ee9eb4ea`; version: NYU IMM-NYU212 August1954 report/book scan; acquired complete PDF, not fully read.

**Accepted interface:** A continuously differentiable finite-dimensional Hermitian family on one open real interval has a C1 relabeling of scalar eigenvalues. At a repeated eigenvalue, the one-sided slope multisets are the spectrum of P A-prime P restricted to the eigenspace.

**Conditions:** One real parameter; fixed finite-dimensional Hilbert space and norm; Hermitian at each parameter; A-prime exists and is continuous. No constant multiplicity needed. Locally bounded compressed slopes follow from ||A-prime||.

**Transfer limits:** No sorted C1 claim or eigenvector continuity, general normal/non-Hermitian, multiparameter or infinite-dimensional theorem, Markov transfer, ordered-gap sign or certificate. Analytic/Puiseux option not part of this accepted proof interface. Named Puiseux, unread appendix and ChapterII dependencies and isolated source discrepancies are retained.

**Usage card:** `../evidence/artifacts/98f6953f12116dac75602004c5485e3f1a202407bd950ce6da68b9393f483b42/EXSRC-ec4eb0aeceb6a01e.md` (SHA-256 `98f6953f12116dac75602004c5485e3f1a202407bd950ce6da68b9393f483b42`).
**Reader freeze:** `../evidence/artifacts/e3e007120c8406f79affebf00c4d9d9f52f1f27e298893698add0d29b753af12/freeze_round19_Rellich_C1_eigenvalue_only_delta.json` (SHA-256 `e3e007120c8406f79affebf00c4d9d9f52f1f27e298893698add0d29b753af12`).
**Independent review:** `../evidence/artifacts/c2dd91faf054b137053e401306725f25157249e0ad269d3183423bdb7d49bf02/review.json` (SHA-256 `c2dd91faf054b137053e401306725f25157249e0ad269d3183423bdb7d49bf02`).
**Accepted reading evidence:**
- `../evidence/artifacts/46290fde9ca3bf8c839e8a3b6582d4ec3b957fa3ef915c5e1ddbba544e11335c/EXSRC-ec4eb0aeceb6a01e.md` (SHA-256 `46290fde9ca3bf8c839e8a3b6582d4ec3b957fa3ef915c5e1ddbba544e11335c`).
- `../evidence/artifacts/ff4a2f9e447db518cdbd7c2d798da14db21011a3893b474bda3d9e5ae7d40f67/EXSRC-ec4eb0aeceb6a01e.json` (SHA-256 `ff4a2f9e447db518cdbd7c2d798da14db21011a3893b474bda3d9e5ae7d40f67`).
- `../evidence/artifacts/504b775daf9c1563145613c215f617b30d77165757516a9d44aed2e72bba975b/binding_check_round18.json` (SHA-256 `504b775daf9c1563145613c215f617b30d77165757516a9d44aed2e72bba975b`).
**Additional review context:**
- `../evidence/artifacts/3b592688f753da3d4cc980704144d42634226f5bf77078365d7fb13e081b5da7/review.json` (SHA-256 `3b592688f753da3d4cc980704144d42634226f5bf77078365d7fb13e081b5da7`).

## EXSRC-ee9ae08fab8fd140 — First-order asymptotic perturbation theory for extensions of symmetric operators

**Bibliography:** Yuri Latushkin, Selim Sukhtaiev (2024). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/ee9ae08fab8fd1400aaf74355433b841fd5acb7e3a0869a26cd771b37046aac7/latushkin_sukhtaiev_first_order_perturbation_2024v3.pdf`; SHA-256 `ee9ae08fab8fd1400aaf74355433b841fd5acb7e3a0869a26cd771b37046aac7`; version: arXiv2012.00247v3;7July2024 margin and9July2024 physical1 body date;74-page author manuscript, not publisher layout.

**Accepted interface:** With a fixed finite metric graph, fixed endpoint boundary triplet and fixed real bounded potential, a one-real-parameter differentiable boundary path satisfying XY*=YX* and full row rank has operator-norm differentiable resolvent locally at a base resolvent point. At an isolated finite-multiplicity eigenvalue, the branch slope multiset is the spectrum of the induced finite boundary Hermitian compression. In the fixed-star delta subcase, a suitable compression eigenbasis gives lambda-prime_j=|u_j(center)|^2.

**Conditions:** Finite positive edge lengths and finitely many edges/vertices; fixed trace and fixed Hilbert space; real parameter, norm-differentiable finite boundary matrices; XY*=YX* and XX*+YY* invertible; fixed real bounded V; isolated finite-multiplicity base cluster and separating contour; common resolvent point for any two-parameter identity. Choose a basis diagonalizing the compressed derivative, not an arbitrary basis. Local or one-sided endpoint derivatives only.

**Transfer limits:** Fixed finite graph-boundary and local first-order use only. No moving-trace or PDE4.22, literal4.14 clauses, Markov/Gibbs, multi-parameter, generic finite-matrix or global spectral-gap/eigenvector transfer. Source Kato1995 remains named and not newly read; the needed finite compression is independently verified. Unused R01-origin source concerns are isolated pending another Sol, and do not support this accepted interface.

**Usage card:** `../evidence/artifacts/d80c41a5dd603b535b1d3964a300350b0c6b6440ea3d24efdab66357dd48100c/EXSRC-ee9ae08fab8fd140.md` (SHA-256 `d80c41a5dd603b535b1d3964a300350b0c6b6440ea3d24efdab66357dd48100c`).
**Reader freeze:** `../evidence/artifacts/6f35d628e02b073d0ffcf3d30c2409e7c67be649a2cedf86c16b6027702fc2c2/freeze_round21_Latushkin_fixed_trace_graph_slopes.json` (SHA-256 `6f35d628e02b073d0ffcf3d30c2409e7c67be649a2cedf86c16b6027702fc2c2`).
**Independent review:** `../evidence/artifacts/4b9ee39bd90c92a30640ad96e229e9f7f4f3daca4772fa865a58c5f9ffaca960/review.json` (SHA-256 `4b9ee39bd90c92a30640ad96e229e9f7f4f3daca4772fa865a58c5f9ffaca960`).
**Accepted reading evidence:**
- `../evidence/artifacts/c9512154a87c21d9555c4f2d8feba4733e9b1aeb244b2a5ed139038742181ef8/EXSRC-ee9ae08fab8fd140.md` (SHA-256 `c9512154a87c21d9555c4f2d8feba4733e9b1aeb244b2a5ed139038742181ef8`).
- `../evidence/artifacts/32ae03c826fe8612c7aeffc999818aa1fec4401d6b06a29cba0f4c6e10da6396/EXSRC-ee9ae08fab8fd140.json` (SHA-256 `32ae03c826fe8612c7aeffc999818aa1fec4401d6b06a29cba0f4c6e10da6396`).
- `../evidence/artifacts/5749477d992394f66d30f7440076fabf09dc1173b3f41ed2670c9cfab1e6dca6/coverage_and_grant_check.json` (SHA-256 `5749477d992394f66d30f7440076fabf09dc1173b3f41ed2670c9cfab1e6dca6`).

## EXSRC-ee9f5379e998e083 — On the Eigenvalue-Separation Properties of Real Tridiagonal Matrices

**Bibliography:** Yan Wu, Ludwig Kohaupt (2023). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/ee9f5379e998e083e32cf87acd3e2aead01fecb3dc0827feba794d2627fb3569/wu_kohaupt_tridiagonal_sturm_2023.pdf`; SHA-256 `ee9f5379e998e083e32cf87acd3e2aead01fecb3dc0827feba794d2627fb3569`; version: Publisher PDF, Constructive Mathematical Analysis 6(4) (2023), pp.210–221..

**Accepted interface:** For every finite real tridiagonal matrix with a_j*d_j>0 for each adjacent pair, its leading-principal characteristic polynomials obey the continuant recurrence, have real simple roots, and consecutive leading blocks strictly interlace. Symmetric matrices require all adjacent offdiagonals nonzero.

**Conditions:** Finite n; real diagonal and offdiagonal entries; strict positivity for every j1..n-1. Only leading-principal consecutive blocks are asserted to interlace strictly. Exact reduction and sign verification are required before a matrix outside this representation can use the certificate.

**Transfer limits:** Static leading-principal real-tridiagonal certificate only; exact positivity/reduction required. No arbitrary principal block or general reversible matrix, derivative, crossing, gap monotonicity, unvalidated floating strict-gap or coefficient-independent separation claim. Stummel–Hainer is named, not newly read; independent induction closes this interface.

**Usage card:** `../evidence/artifacts/d41e1bb9a6e450cfafa938e0cac9f167b7cf03a551c871a0f4de34786f03c3d8/EXSRC-ee9f5379e998e083.md` (SHA-256 `d41e1bb9a6e450cfafa938e0cac9f167b7cf03a551c871a0f4de34786f03c3d8`).
**Reader freeze:** `../evidence/artifacts/ef2a6db9d34f9a3210c89404d02c4eb419d2f19fd203c846242a1d6d4dae9c6c/freeze_round23_WuKohaupt_G03_06.json` (SHA-256 `ef2a6db9d34f9a3210c89404d02c4eb419d2f19fd203c846242a1d6d4dae9c6c`).
**Independent review:** `../evidence/artifacts/2f180c97a1da58fbf76ff3fd85e2080908a7c89a33df14417483de8aa11377b0/review.json` (SHA-256 `2f180c97a1da58fbf76ff3fd85e2080908a7c89a33df14417483de8aa11377b0`).
**Accepted reading evidence:**
- `../evidence/artifacts/48faae33db4e4c38fa67e891b544822abec8530489baac76e0e908bfd83a6dd9/EXSRC-ee9f5379e998e083.md` (SHA-256 `48faae33db4e4c38fa67e891b544822abec8530489baac76e0e908bfd83a6dd9`).
- `../evidence/artifacts/6dab285ff4ac87d504c883e6a96eac7d325219f1ecb06d6adfbe0fc6cfd7a6f0/EXSRC-ee9f5379e998e083.json` (SHA-256 `6dab285ff4ac87d504c883e6a96eac7d325219f1ecb06d6adfbe0fc6cfd7a6f0`).
- `../evidence/artifacts/2a8428673259b29c358e9a76ccc2bcda5432bf5a176894da64cb6648e32eaae2/coverage_and_grant_check.json` (SHA-256 `2a8428673259b29c358e9a76ccc2bcda5432bf5a176894da64cb6648e32eaae2`).

## EXSRC-f7488ea07a85fb95 — On Perturbation of Operators and Rayleigh-Schrödinger Coefficients

**Bibliography:** Marcus Carlsson, Olof Rubin (2024). **Method IDs:** G03.03, G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/f7488ea07a85fb95d13b643d766587edf6eb2caa21d2bb5d1401a339a677f6c5/carlsson_rubin_operator_perturbation_2024.pdf`; SHA-256 `f7488ea07a85fb95d13b643d766587edf6eb2caa21d2bb5d1401a339a677f6c5`; version: Complex Analysis and Operator Theory 18 (2024), article 47, 15-page publisher PDF.

**Accepted interface:** Small self-adjoint effective matrix B=E11-E12(A22-lambda I)^(-1)E21 approximates the isolated finite cluster by lambda+eig(B)+O(||E||^3). For affine simple branch, separate linear and quadratic coefficients. Correct affine expansion separates t V11 from the t^2 coefficient -V12(A22-lambda I)^(-1)V21; the derivative itself at second order is twice that coefficient.

**Conditions:** Fixed finite self-adjoint A, isolated eigenvalue lambda multiplicitym, orthogonal decomposition RanP plus complement and delta=dist(lambda,spectrum(A22))>0; small self-adjoint E. B is self-adjoint; sorted corresponding cluster/multiset, constants local in A/delta/m. For the scalar expansion require m1 and E=tV with fixed self-adjoint V. Bounded-operator extension additionally requires an isolated discrete finite-multiplicity eigenvalue on a separable Hilbert space.

**Transfer limits:** No arbitrary graph gap sign, no smooth label through internal crossings, no norm-independent strict interval certificate. For a nonlinear parameter path include its actual higher derivatives separately; this card admits only affine scalar coefficient extraction.

**Usage card:** `../evidence/artifacts/3ac4903dbed203db7b38eb878a5c51bd745f4447369880b3e057eb172cb318dd/EXSRC-f7488ea07a85fb95.md` (SHA-256 `3ac4903dbed203db7b38eb878a5c51bd745f4447369880b3e057eb172cb318dd`).
**Reader freeze:** `../evidence/artifacts/e40a3737b206cbb6438661ec3591d32e5015cf9f8525bdd466ea1b291a703dc7/freeze_round12_round9_use_corrections.json` (SHA-256 `e40a3737b206cbb6438661ec3591d32e5015cf9f8525bdd466ea1b291a703dc7`).
**Independent review:** `../evidence/artifacts/ef5419f726320194b696611600b55202cad47e00c2d63898e89e6a1e95edec11/review.json` (SHA-256 `ef5419f726320194b696611600b55202cad47e00c2d63898e89e6a1e95edec11`).
**Accepted reading evidence:**
- `../evidence/artifacts/9f9d1dd075525cbedcdbe57cc3a969f33c9663eb6168098c04ed689c3394feeb/EXSRC-f7488ea07a85fb95.json` (SHA-256 `9f9d1dd075525cbedcdbe57cc3a969f33c9663eb6168098c04ed689c3394feeb`).
- `../evidence/artifacts/117a7fde4e317ff68edcdc9a5ae22f1bb7262aa6cd58a129044a85854dc75fa6/EXSRC-f7488ea07a85fb95.md` (SHA-256 `117a7fde4e317ff68edcdc9a5ae22f1bb7262aa6cd58a129044a85854dc75fa6`).

## EXSRC-f86cfaf2be2ba326 — On the Perturbation Theory of Closed Linear Operators

**Bibliography:** Tosio Kato (1952). **Method IDs:** G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/f86cfaf2be2ba3262e454a80bd4373ff682c86c8157e03f1e3cc89c2dcfde8a7/kato_closed_linear_operators_1952.pdf`; SHA-256 `f86cfaf2be2ba3262e454a80bd4373ff682c86c8157e03f1e3cc89c2dcfde8a7`; version: Journal of the Mathematical Society of Japan 4(3–4) (1952), 323–337.

**Accepted interface:** Analytic isolated finite cluster projection and analytic intertwiner; finite-matrix reduction and distinction between cluster projection and individual branch projections at exceptional collisions.

**Conditions:** Closed dense-domain operator with common-domain analytic power-series perturbation and Eq1.2 graph bounds, contour in resolvent and fundamental disk |epsilon|<(p+alpha)^-1; for the admitted downstream finite-matrix use verify analyticity and contour separation directly. Finite-rank subspace for Section3 secular matrix; unitary transport only for real parameter normal/self-adjoint Hilbert-space families.

**Transfer limits:** No arbitrary-graph Ising sign, unresolved ordered-branch derivative, strict numerical certificate or unproved high-order remainder. No scalar/compressed derivative theorem is attributed to Kato1952.

**Usage card:** `../evidence/artifacts/48e889599ee10df39bac384f2563aa7ce1835e6ca289ca40a403487be0c2a645/EXSRC-f86cfaf2be2ba326.md` (SHA-256 `48e889599ee10df39bac384f2563aa7ce1835e6ca289ca40a403487be0c2a645`).
**Reader freeze:** `../evidence/artifacts/2d4b8b9b45441779b984799fe4ece572c54393beb93ab163fd68ddba22954c9b/freeze_round6.json` (SHA-256 `2d4b8b9b45441779b984799fe4ece572c54393beb93ab163fd68ddba22954c9b`).
**Independent review:** `../evidence/artifacts/253130d07966bc98d2e4a38569b2f1d2970ec12cad2259464c5d909c6d298ef0/review.json` (SHA-256 `253130d07966bc98d2e4a38569b2f1d2970ec12cad2259464c5d909c6d298ef0`).
**Accepted reading evidence:**
- `../evidence/artifacts/b127d3a4e7cda008981453023929c789d59c523bb245bacc9d23e5dd73040b7d/EXSRC-f86cfaf2be2ba326.json` (SHA-256 `b127d3a4e7cda008981453023929c789d59c523bb245bacc9d23e5dd73040b7d`).
- `../evidence/artifacts/5a4bd15aa3e80993f046a53514522a29ca3ba32665776a235d4d57723b39531b/EXSRC-f86cfaf2be2ba326.md` (SHA-256 `5a4bd15aa3e80993f046a53514522a29ca3ba32665776a235d4d57723b39531b`).
- `../evidence/artifacts/e04ee67971bbf27dd0ce0d4516166279a6a9f1482f3e13a1a95edc3a2d5c6596/auth-e04ee67971bbf27dd0ce0d4516166279a6a9f1482f3e13a1a95edc3a2d5c6596.json` (SHA-256 `e04ee67971bbf27dd0ce0d4516166279a6a9f1482f3e13a1a95edc3a2d5c6596`).

## PR-035bbf5b7ba1 — Perturbation of the Stationary Distribution Measured by Ergodicity Coefficients

**Bibliography:** Eugene Seneta (1988). **Method IDs:** G03.05. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/02ea5da334d253223b9bc1ec059f98faf8c2250012e7f0d551c79047d0778674/C036.pdf`; SHA-256 `02ea5da334d253223b9bc1ec059f98faf8c2250012e7f0d551c79047d0778674`; version: Cambridge publisher PDF, 3 pages.

**Accepted interface:** Finite stationary-law perturbation under a scrambling margin, using the fundamental-matrix identity and zero-sum Neumann contraction; a concrete moving-law interface for G03.05.

**Conditions:** Two finite row-stochastic matrices with unique stationary laws; tau1(P)<1 at the base; row action induced norm max_i sum_j |E_ij|; probability normalization. Uniform family use requires uniform margin.

**Transfer limits:** Controls the invariant law only; no nontrivial spectral-gap ordering, eigenbranch derivative or arbitrary-graph Ising sign.

**Usage card:** `../evidence/artifacts/151b1c307971e6c13ab0e1c83abf2856412868436ecab5e8e4aa6da36a729ca1/usage_cards.md` (SHA-256 `151b1c307971e6c13ab0e1c83abf2856412868436ecab5e8e4aa6da36a729ca1`).
**Reader freeze:** `../evidence/artifacts/53eed943b0aeb8f76b967fe6e1ce24bff4ee3b0b9ef57117524e16fdef488a33/freeze_round5.json` (SHA-256 `53eed943b0aeb8f76b967fe6e1ce24bff4ee3b0b9ef57117524e16fdef488a33`).
**Independent review:** `../evidence/artifacts/696f3b4ecfb1df1c6d4ff5f350be0144ff53bfd6b903fd07a1b7cf87a7cc4bd2/review.json` (SHA-256 `696f3b4ecfb1df1c6d4ff5f350be0144ff53bfd6b903fd07a1b7cf87a7cc4bd2`).
**Accepted reading evidence:**
- `../evidence/artifacts/29599654d3860933ee47fb91de293a709138aa8c5840d416211fd1e975441aa2/canonical_complete_read_record.json` (SHA-256 `29599654d3860933ee47fb91de293a709138aa8c5840d416211fd1e975441aa2`).
- `../evidence/artifacts/c73e5afb49d53c5f576392f3ac43fde980c4ee6d6fb06d61e52f78c85cf4ca8b/reading_coverage.json` (SHA-256 `c73e5afb49d53c5f576392f3ac43fde980c4ee6d6fb06d61e52f78c85cf4ca8b`).
- `../evidence/artifacts/8f5f78c260448f3d4dde391b025dab1eeb8f527c65647b0c3daf807ff35f811e/cards.md` (SHA-256 `8f5f78c260448f3d4dde391b025dab1eeb8f527c65647b0c3daf807ff35f811e`).

## PR-ade6cc42ac8b — Relaxation Time Is Monotone in Temperature in the Mean-Field Ising Model

**Bibliography:** Vladislav Kargin (2011). **Method IDs:** G03.03, G03.04. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/c04a56cbde84fa812351728e6a12ddec964df9cd9668477d660551a92e715760/Kargin2011.pdf`; SHA-256 `c04a56cbde84fa812351728e6a12ddec964df9cd9668477d660551a92e715760`; version: arXiv:1103.0327v1, 6 pages.

**Accepted interface:** Normalized reversible simple-branch derivative with moving-pi cancellation; homogeneous complete-graph zero-field common-J calibration.

**Conditions:** Fixed finite C1 reversible P_theta and positive pi_theta; differentiable simple eigenpair normalized in L2(pi_theta). Certified model use: K_n, common positive J, zero field, random-site discrete heat-bath; per-site clock Q=n(P-I).

**Transfer limits:** Printed uniform-field theorem not fully proof-certified here; reflection proof only H0. Lemma5 imports Ding-Lubetzky-Peres2009 Prop3.9. No one-edge arbitrary-graph sign or repeated ordered scalar derivative.

**Usage card:** `../evidence/artifacts/335e4c14471e361b94186c74bd825cec99d7324ed13f23e3ac97e51f2f5077b0/usage_cards.md` (SHA-256 `335e4c14471e361b94186c74bd825cec99d7324ed13f23e3ac97e51f2f5077b0`).
**Reader freeze:** `../evidence/artifacts/53eed943b0aeb8f76b967fe6e1ce24bff4ee3b0b9ef57117524e16fdef488a33/freeze_round5.json` (SHA-256 `53eed943b0aeb8f76b967fe6e1ce24bff4ee3b0b9ef57117524e16fdef488a33`).
**Independent review:** `../evidence/artifacts/696f3b4ecfb1df1c6d4ff5f350be0144ff53bfd6b903fd07a1b7cf87a7cc4bd2/review.json` (SHA-256 `696f3b4ecfb1df1c6d4ff5f350be0144ff53bfd6b903fd07a1b7cf87a7cc4bd2`).
**Accepted reading evidence:**
- `../evidence/artifacts/27b66df3b81f090409b4191ffffdd102aeb8703cb11e6c6be2f741f9fb90b08f/canonical_complete_read_record.json` (SHA-256 `27b66df3b81f090409b4191ffffdd102aeb8703cb11e6c6be2f741f9fb90b08f`).
- `../evidence/artifacts/cfa7cdfbc5df494bf2ba50257aa6084997e931072faa38538f8fb743fefbb1c2/reading_coverage.json` (SHA-256 `cfa7cdfbc5df494bf2ba50257aa6084997e931072faa38538f8fb743fefbb1c2`).
- `../evidence/artifacts/67d96384412fdaa147b06e1ec6643098ee539c8a0a7bcd7af95854c64ce7c0ab/cards.md` (SHA-256 `67d96384412fdaa147b06e1ec6643098ee539c8a0a7bcd7af95854c64ce7c0ab`).

## EXSRC-646e7cd383d64482 — Fast Computation of Error Bounds for All Eigenpairs of a Hermitian and All Singular Pairs of a Rectangular Matrix with Emphasis on Eigen- and Singular Value Clusters

**Bibliography:** Siegfried M. Rump, Marko Lange (2023). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/646e7cd383d6448222b143a01bbf56fa35c0f219abc4f0e0e14df513cd7a4c46/rump_lange_fast_verified_cluster_bounds_hermitian_2023.pdf`; SHA-256 `646e7cd383d6448222b143a01bbf56fa35c0f219abc4f0e0e14df513cd7a4c46`; version: Complete 30-physical-page public author manuscript; first and last pages mark it for review purposes only; no publisher-layout equivalence asserted. Associated journal metadata: JCAM 434 (2023), article 115332, DOI 10.1016/j.cam.2023.115332..

**Accepted interface:** Theorem 4.2 / verifyeigall (physical pp.8–10): finite real-symmetric/complex-Hermitian eigenvalue cluster enclosures with exact cluster multiplicities after interval residual and positive basis lower bounds pass and final cluster unions are pairwise disjoint.

**Conditions:** Finite real symmetric or complex Hermitian target. For interval input, the matrices to which the guarantee is applied must be Hermitian/symmetric and belong to the validated interval family. The interval residual must outward-enclose E=A Xtilde−Xtilde Lambdatilde; all residual upper bounds and basis-column or cluster sigma_min lower bounds must be valid. Every required lower bound for a column norm and for sigma_min(Xtilde(:,mu)) must be positive; otherwise the algorithm may return infinite radii and no finite inclusion. Use the source’s overlap graph and recomputed block residual bounds until final cluster unions are pairwise disjoint. Theorem 4.1 is a named source-stated input. Full coverage and exact cluster multiplicities are claimed only after Theorem 4.2’s final disjoint-cluster conditions hold. A gap conclusion needs a separately justified eigenvalue ordering and strict separation of scalar enclosures.

**Transfer limits:** No inertia/Sturm method or automatic gap; no Markov/stationary/mixing/reversibility claim; no eigenvector/subspace or singular-value/vector scope in this candidate. A gap needs separate ordering and strict interval separation.

**Usage card:** `../evidence/artifacts/06666500dfd90af826c1c4c40edf5aa302a0be8da8c8689155e887d3fb182608/EXSRC-646e7cd383d64482.md` (SHA-256 `06666500dfd90af826c1c4c40edf5aa302a0be8da8c8689155e887d3fb182608`).
**Reader freeze:** `../evidence/artifacts/c8cad2e652a91aeb59f116ef089370ee86943d32d8cfd87e1fbf3acf3033a23f/freeze_round47_RumpLange_Theorem4_2_Hermitian_clusters.json` (SHA-256 `c8cad2e652a91aeb59f116ef089370ee86943d32d8cfd87e1fbf3acf3033a23f`).
**Independent review:** `../evidence/artifacts/9b08a57d96e2b1c25e46e5d75392ff975d78001e7989e2a73ce9869f91ec9d18/review.json` (SHA-256 `9b08a57d96e2b1c25e46e5d75392ff975d78001e7989e2a73ce9869f91ec9d18`).
**Source card:** `../evidence/artifacts/842b763c72e8cc6e46470ad03697a0cc01d33e8d5b2e7ae99980f9df8c1901ad/EXSRC-646e7cd383d64482.md` (SHA-256 `842b763c72e8cc6e46470ad03697a0cc01d33e8d5b2e7ae99980f9df8c1901ad`).
**Accepted reading evidence:**
- `../evidence/artifacts/875ceb2ab64421fc7236c4ec4125efd256a11a850397f9aa1584526bfb452abb/EXSRC-646e7cd383d64482.json` (SHA-256 `875ceb2ab64421fc7236c4ec4125efd256a11a850397f9aa1584526bfb452abb`).
- `../evidence/artifacts/842b763c72e8cc6e46470ad03697a0cc01d33e8d5b2e7ae99980f9df8c1901ad/EXSRC-646e7cd383d64482.md` (SHA-256 `842b763c72e8cc6e46470ad03697a0cc01d33e8d5b2e7ae99980f9df8c1901ad`).
- `../evidence/artifacts/06666500dfd90af826c1c4c40edf5aa302a0be8da8c8689155e887d3fb182608/EXSRC-646e7cd383d64482.md` (SHA-256 `06666500dfd90af826c1c4c40edf5aa302a0be8da8c8689155e887d3fb182608`).
- `../evidence/artifacts/d4b6d64383e3bcb7553edbbbcb9d98f9a6829e71c3cdca4a4f307367381ef755/rump_lange_theorem42_exact_examples.py` (SHA-256 `d4b6d64383e3bcb7553edbbbcb9d98f9a6829e71c3cdca4a4f307367381ef755`).
- `../evidence/artifacts/3a9c81a1436adaef7443774048e7a1860895991e585944c5fff7d97ec97c68fa/rump_lange_theorem42_exact_examples.out.json` (SHA-256 `3a9c81a1436adaef7443774048e7a1860895991e585944c5fff7d97ec97c68fa`).
- `../evidence/artifacts/e1b8713d920bdb1a5487fa053b4d08b70f1ccb4677749516a38f5e7314707979/rump_lange_theorem42_proof_check.md` (SHA-256 `e1b8713d920bdb1a5487fa053b4d08b70f1ccb4677749516a38f5e7314707979`).
**Additional review context:**
- `../evidence/artifacts/d42589946f063b834e13dc4deecbd6ea08c640c4e24ef8e5b53104859f9bac42/proof_and_entry_review.md` (SHA-256 `d42589946f063b834e13dc4deecbd6ea08c640c4e24ef8e5b53104859f9bac42`).
- `../evidence/artifacts/c56c148c36ea2785e0084a9faeab6f8e15de2562b8980afe4426ac3e8856d5dc/independent_math.py` (SHA-256 `c56c148c36ea2785e0084a9faeab6f8e15de2562b8980afe4426ac3e8856d5dc`).
- `../evidence/artifacts/f500f58a34c2efedc7b1a7359389eebd2ccdb433092824f32ac0e50a83e552d2/independent_math.out.json` (SHA-256 `f500f58a34c2efedc7b1a7359389eebd2ccdb433092824f32ac0e50a83e552d2`).
- `../evidence/artifacts/6035271ff79eda52078ed21f80e677dafdea2280377da67fc4b58f14dd95aba8/reading_assets_and_bindings.json` (SHA-256 `6035271ff79eda52078ed21f80e677dafdea2280377da67fc4b58f14dd95aba8`).

## PR-70ce6c24e1e6 — Comparison Theorems for Reversible Markov Chains

**Bibliography:** Persi Diaconis, Laurent Saloff-Coste (1993). **Method IDs:** G03.01. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/2b52c200e491c37c7350254e626d2ae40e6d713328a23dbf4dc25292206118bb/DiaconisSaloffCoste1993.pdf`; SHA-256 `2b52c200e491c37c7350254e626d2ae40e6d713328a23dbf4dc25292206118bb`; version: Ann. Appl. Probab. 3(3) (1993), 36 physical pages including cover.

**Accepted interface:** Theorem2.1/Eq2.4 and the Rayleigh/minimax Eq2.3, physical4–5/printed698–699: finite reversible fixed-kernel Dirichlet comparison with path load A and pointwise stationary-measure factor a gives gap(P)>=a/A*gap(P_tilde). Direct G03.01 gap/Rayleigh ingredient.

**Conditions:** Finite irreducible reversible kernels P,P_tilde on the same state space; full-support normalized stationary laws pi,pi_tilde; each positive offdiagonal P_tilde transition has a simple directed path of positive P edges; source directed edge-flow congestion A>0 finite; rigorous pi_tilde(x)>=a*pi(x) for every state with a>0. Exact or outward-certified inequalities required for a strict quantitative result.

**Transfer limits:** Fixed-kernel Poincare gap only. No derivative, parameter monotonicity, absolute gap, TV estimate, automatic comparison across different state spaces, or automatic interval certificate. Bottom endpoint needs the separate plus-form/odd-path route, not this admitted Dirichlet-only row.

**Usage card:** `../evidence/artifacts/c543cc7f674d607576712bf729cd24950d5e81ee36e8f2d5ff42b7c629628676/usage_cards.md` (SHA-256 `c543cc7f674d607576712bf729cd24950d5e81ee36e8f2d5ff42b7c629628676`).
**Reader freeze:** `../evidence/artifacts/53eed943b0aeb8f76b967fe6e1ce24bff4ee3b0b9ef57117524e16fdef488a33/freeze_round5.json` (SHA-256 `53eed943b0aeb8f76b967fe6e1ce24bff4ee3b0b9ef57117524e16fdef488a33`).
**Independent review:** `../evidence/artifacts/5277a678bbc6f8a35c068526a744324b50478839f9cf431406cefbe5a6eab8d0/review.json` (SHA-256 `5277a678bbc6f8a35c068526a744324b50478839f9cf431406cefbe5a6eab8d0`).
**Accepted reading evidence:**
- `../evidence/artifacts/16dd4fd534f190334b82048401a5d830b504cc3ceb089f8754725fef87d9566a/canonical_complete_read_record.json` (SHA-256 `16dd4fd534f190334b82048401a5d830b504cc3ceb089f8754725fef87d9566a`).
- `../evidence/artifacts/8fad597d09e6096e8d466d48ec7da6fb28619ede461f2815a15b6d6b8908e4cd/reading_coverage.json` (SHA-256 `8fad597d09e6096e8d466d48ec7da6fb28619ede461f2815a15b6d6b8908e4cd`).
- `../evidence/artifacts/9827d5e52798c0cfcba15c911370d6467234398703705b77e9006a5cd9b0dd60/cards.md` (SHA-256 `9827d5e52798c0cfcba15c911370d6467234398703705b77e9006a5cd9b0dd60`).
**Additional review context:**
- `../evidence/artifacts/48c3abeeb880c2fc3ccd97bdf0c4c30a81135fae765f9ecaada4f3c4c6542e48/proof_check.md` (SHA-256 `48c3abeeb880c2fc3ccd97bdf0c4c30a81135fae765f9ecaada4f3c4c6542e48`).
- `../evidence/artifacts/034c5684657409ef77d06b7f601e208fb9f02b33f6c73481119b584a97c17496/exact_measure_factor.py` (SHA-256 `034c5684657409ef77d06b7f601e208fb9f02b33f6c73481119b584a97c17496`).
- `../evidence/artifacts/69dcea306580825d206b7d27df4c6df84338b7970207b3eb665bac67a34c67c7/exact_measure_factor.out.json` (SHA-256 `69dcea306580825d206b7d27df4c6df84338b7970207b3eb665bac67a34c67c7`).

## EXSRC-8f1143c5c5b2f63f — Fast Verification for All Eigenpairs in Symmetric Positive Definite Generalized Eigenvalue Problems

**Bibliography:** Shinya Miyajima, Takeshi Ogita, Siegfried M. Rump, Shin'ichi Oishi (2010). **Method IDs:** G03.06. **Decision:** `accepted_for_scoped_use`.

**Source file:** `../evidence/artifacts/8f1143c5c5b2f63f97f5b57514c3e31f3d5309e694036d693bfe9c3609bfa365/miyajima_ogita_rump_oishi_spd_generalized_eigenpairs_2010.pdf`; SHA-256 `8f1143c5c5b2f63f97f5b57514c3e31f3d5309e694036d693bfe9c3609bfa365`; version: Complete Reliable Computing 14 (2010), pp.24–45 journal PDF, 22 physical pages..

**Accepted interface:** Theorem 4, §3.1, physical p.6/printed29, proof p.7/printed30: with Gg=XᵀBX, F=I−Gg and Rg=AX−BXD, the source gives all-index ordered inclusion at radius β||Rg||₂/(1−||F||₂), with no square root. Strict disjointness of outward-certified intervals yields indexed isolation. Finite G03.06 use only.

**Conditions:** A and B real symmetric; X is the full square approximate eigenvector matrix, D diagonal, and exact/approximate eigenvalues are ordered nondecreasingly. Set Gg=XᵀBX, F=I−Gg and Rg=AX−BXD. Require ||F||₂<1; the source first proves Gg≻0 and then B≻0 by congruence/inertia equality. Require rigorous β≥sqrt(||B⁻¹||₂); the source radius is δ̂=β||Rg||₂/(1−||F||₂), with no square root on this denominator. Outward-certify residual and inverse-norm bounds. Strictly disjoint certified ordered intervals are needed for an individual isolation conclusion.

**Transfer limits:** No Sturm sequence, inertia algorithm, standalone root-count procedure, eigenvector bound, eigenvector regularity, derivative/perturbation-branch theorem, non-self-adjoint or infinite-dimensional extension, Theorem 7/10 implementation, benchmark certification, or quadratic-pencil claim.

**Usage card:** `../evidence/artifacts/6ec885722d562238386e7c6323ef505b6788ee339e87343f6fe1d9268b351b61/usage_card.md` (SHA-256 `6ec885722d562238386e7c6323ef505b6788ee339e87343f6fe1d9268b351b61`).
**Reader freeze:** `../evidence/artifacts/18b0f736efe630b0ea5c31722d7d2067b5894022459695320b0f3df6f2265902/freeze_round52_Miyajima_Theorem4_gram_defect_consistency.json` (SHA-256 `18b0f736efe630b0ea5c31722d7d2067b5894022459695320b0f3df6f2265902`).
**Independent review:** `../evidence/artifacts/8034034054e7f90fde5ec5c82f0022c3861da6508d2b7980255f000acc267fa5/review.json` (SHA-256 `8034034054e7f90fde5ec5c82f0022c3861da6508d2b7980255f000acc267fa5`).
**Source card:** `../evidence/artifacts/d878631e74c0b9f52b3b0fb8abf8529f342670b66b753198e5042d580057b5f8/EXSRC-8f1143c5c5b2f63f.md` (SHA-256 `d878631e74c0b9f52b3b0fb8abf8529f342670b66b753198e5042d580057b5f8`).
**Accepted reading evidence:**
- `../evidence/artifacts/cd7dd88603b57542c3c83e550ff95d1576e0914ae849e37339ebae9760f749f4/EXSRC-8f1143c5c5b2f63f.json` (SHA-256 `cd7dd88603b57542c3c83e550ff95d1576e0914ae849e37339ebae9760f749f4`).
- `../evidence/artifacts/d878631e74c0b9f52b3b0fb8abf8529f342670b66b753198e5042d580057b5f8/EXSRC-8f1143c5c5b2f63f.md` (SHA-256 `d878631e74c0b9f52b3b0fb8abf8529f342670b66b753198e5042d580057b5f8`).
- `../evidence/artifacts/312297f8c14fc288aa86be0d50d81fbe7adc92468c05d8ea99645aba558deece/miyajima_theorem4_exact_example.py` (SHA-256 `312297f8c14fc288aa86be0d50d81fbe7adc92468c05d8ea99645aba558deece`).
- `../evidence/artifacts/8962d64f7d039dcaef4084983415dc0da2ab1dcffbd48081b0802382b6742fce/miyajima_theorem4_exact_example.out.json` (SHA-256 `8962d64f7d039dcaef4084983415dc0da2ab1dcffbd48081b0802382b6742fce`).
- `../evidence/artifacts/cc66ed18af5de82e0769aa639dd439667fa73e106ce8aa1ae8d1fd000fab240a/proof_check.md` (SHA-256 `cc66ed18af5de82e0769aa639dd439667fa73e106ce8aa1ae8d1fd000fab240a`).
- `../evidence/artifacts/b2f29ab35d4a979bcf7a11d460d9f65b626ddbc38c38f9131d3653b5aaa326cf/miyajima_formula_discrimination_exact.py` (SHA-256 `b2f29ab35d4a979bcf7a11d460d9f65b626ddbc38c38f9131d3653b5aaa326cf`).
- `../evidence/artifacts/ce7506aa50381192c3660b3f6ef89ea35128266e6d866881b6a66e1b80b62a0d/miyajima_formula_discrimination_exact.out.json` (SHA-256 `ce7506aa50381192c3660b3f6ef89ea35128266e6d866881b6a66e1b80b62a0d`).
**Additional review context:**
- `../evidence/artifacts/662fd6e944ef337836cd2d20e37286906cb2fe3d59fe65d713e34350255f4957/proof_check.md` (SHA-256 `662fd6e944ef337836cd2d20e37286906cb2fe3d59fe65d713e34350255f4957`).
- `../evidence/artifacts/30a7b8bc7b523d0c4b5920d5e7565b470befecc160f697fa9b77ee57710a5b3b/binding_and_preimage_verification.json` (SHA-256 `30a7b8bc7b523d0c4b5920d5e7565b470befecc160f697fa9b77ee57710a5b3b`).
- `../evidence/artifacts/f500f58a34c2efedc7b1a7359389eebd2ccdb433092824f32ac0e50a83e552d2/independent_math.out.json` (SHA-256 `f500f58a34c2efedc7b1a7359389eebd2ccdb433092824f32ac0e50a83e552d2`).
