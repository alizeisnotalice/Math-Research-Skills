# OpenAI Wave 4 — adjoint and Iitaka source models

This is a source-locus index for the eleven pinned OpenAI drafts listed below.  The user has directed this wave to treat the originals as correct; consequently this record extracts their stated theorem models and reusable operations, but is **not** an independent proof audit.  These are conditional references: callers must separately supply every geometric, analytic, Hodge-theoretic, MMP, and characteristic assumption stated by the relevant source.  The finite ledger skill can only check any subsequently supplied divisor coefficients, section identities, indices, and intersection rows.

## 1. Logarithmic whole-fiber variation

*Logarithmic Kodaira dimension and whole-fiber variation*, SHA-256 `9b1b750b309e5c5a37fa1b472836f98c8eeffe69e4e7604452de18128a479e4a`, physical pp. 2, 6, 14--15, 52--53, 59; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/paper.pdf).

For a projective surjective connected-fibre map \(f:U\to V\) of smooth connected complex quasi-projective varieties, \(\bar\kappa(V)\ge0\), and geometric generic fibre \(F\), the stated model is
\[
 \bar\kappa(U)\ge\kappa(F)+\max\{\bar\kappa(V),\operatorname{Var}(f)\},
\quad
 \operatorname{Var}(f)=\min_L\operatorname{trdeg}_{\mathbb C}L,
\]
where \(L\) is an algebraically closed intermediate field over which the whole geometric generic fibre birationally descends.  Reusable operations are: retain a fixed log resolution and exceptional-section comparison, form the least-index cyclic root cover of a \(\kappa=0\) fibre, and record the finite splitting/constant-cocycle descent of the whole fibre.  Do not replace the logarithmic base hypothesis by ordinary Kodaira dimension or treat a field-of-definition computation as a finite divisor check.

## 2. Orbifold/logarithmic subadditivity

*Orbifold and logarithmic Iitaka subadditivity*, SHA-256 `b143366cc99615e19783fa075caafd8c9565e7bf5a554a612e086657c2aeeb79`, physical pp. 17, 20, 31, 39--40; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/paper.pdf).

The source records orbifold Iitaka subadditivity through the orbifold base \(B(f,\Delta)\): after its stated smooth/Fujiki-class-C resolution, flattening, coefficient-one and inf-multiplicity hypotheses, it uses
\[
 \kappa(X,K_X+\Delta)\ge
 \kappa(F,K_F+\Delta_F)+\kappa(Y,K_Y+B(f,\Delta)).
\]
The reusable bookkeeping operations are preserving inf-multiplicity inequalities under composition, retaining products/ratios in common divisible grading after section comparisons, and multiplying a verified relative section through a convex divisor decomposition.  This is not a routine computation of orbifold multiplicities, Hodge positivity, or log general-type addition.

## 3. Ordinary projective Iitaka subadditivity

*Projective Hodge lines and ordinary Iitaka subadditivity*, SHA-256 `564a98c625b94ef479a6690bed65451fee18c47c69c23e5d9e1f4fd181deca9a`, physical pp. 2, 25--28, 34, 39; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/paper.pdf).

For a connected-fibre surjective projective map of smooth connected projective varieties over an algebraically closed characteristic-zero field, the recorded theorem is
\[
 \kappa(X)\ge\kappa(F)+\kappa(Z).
\]
At the reusable source-interface level, generically generated reflexive symmetric powers are multiplied into a relative pluricanonical section; an effective multiple of a big divisor removes the twist; and flat proper base change preserves all pluricanonical section spaces and hence Kodaira dimension after a field extension.  The required Hodge-line, weak-positivity, rank, and canonical-bundle inputs remain external.

## 4. Reverse logarithmic inequality and additivity

*The reverse logarithmic Kodaira inequality and additivity*, SHA-256 `499df173e9f8ba2d88b644514c4ea3a797d5c00de4148bac246f7a4c857094f9`, physical pp. 5, 14, 20, 25, 37, 43, 46, 49--50; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf).

For the stated projective reduced-SNC pair fibration, with stratum-smoothness over the open base, this source supplies the complementary section construction: a nonzero total logarithmic pluricanonical section yields \(\kappa(Y,K_Y+D)\ge0\), with its prescribed-point vanishing refinement, and combines it with the cited logarithmic subadditivity theorem for additivity.  The reusable operations are to preserve the same resolved base and exact section lattice, carry a marked-period quotient, and state the orbifold cotangent determinant map only after the adapted-cover lattice is supplied.  It does not create a period quotient, verify pseudoeffectivity, or compute a Higgs map.

## 5. Kähler fourfold finite-null and conormal interfaces

*Abundance after nonvanishing for compact Kähler fourfolds*, SHA-256 `89b5dd1a939cd7a67bbc90c83fe34ac5398d08f9103aa1cf8351bb3825e09273`, physical pp. 10, 15--16; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Abundance-after-nonvanishing-for-compact-Kahler-fourfolds-September-27-2026/paper.pdf).

The usable source model is a normal connected ordinary \(\mathbb Q\)-factorial compact Kähler threefold with a nef-and-big class and finite null locus, followed by the stated contraction/conormal-layer interfaces.  The concrete operation is to record the full null locus
\[
 \operatorname{Null}(\alpha)=\bigcup_{\dim V>0,\ \alpha^{\dim V}\cdot V=0}V
\]
and distinguish its finite curve/surface components from a caller-supplied Grauert contraction and coherent conormal presentation.  It does not make the finite-null assertion a general semiampleness, fourfold-abundance, or analytic-contraction algorithm.

## 6. Conditional good Kähler models

*Conditional good minimal models for compact Kähler fourfolds*, SHA-256 `eebddaadef6935c3072a8c1eb556a002bbab27788c337bbba2f9e579bc81b6d3`, physical pp. 8--13; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Conditional-good-minimal-models-for-compact-Kahler-fourfolds-October-6-2026/paper.pdf).

This is a conditional model: globally strongly \(\mathbb Q\)-factorial compact Kähler klt fourfold pairs with effective rational boundary and analytically pseudo-effective actual adjoint, assuming the source's orbifold subadditivity, fourfold MMP, and abundance-after-nonvanishing inputs.  Reuse only the explicit dependency split: Assumption 2.2 supplies the logarithmic premise, Assumption 2.3 the pseudo-effective program, and Assumption 2.4 says an analytically nef actual \(\mathbb Q\)-Cartier adjoint with \(\kappa\ge0\) has a globally generated Cartier multiple.  No assumption is established by a finite record.

## 7. Moving-jet scalar-order interface

*Fourfold nonvanishing by minimal metrics and moving jets*, SHA-256 `1946d50201ab1ae0c02a6ba95143b55528b2525d45673a2985404aee4d8f2cb4`, physical pp. 8--10, 12; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Fourfold-nonvanishing-by-minimal-metrics-and-moving-jets-September-27-2026/paper.pdf).

The source's reusable model fixes an integral projective \(d\)-fold, an ample rational Cartier \(P\), a Cartier multiple \(kP\), and full kernels \(H_i(x)\) of order-\(\lceil k\tau_i\rceil\) jets at a moving smooth mark.  Under its very-general nonzero-kernel and positive-dimensional base-locus hypotheses, parameter differentiation gives ordinary ideal membership \(s\in\mathcal I_\Gamma^h\).  Its scalar-order consequence is
\[
 \operatorname{ord}_x(s)\le4k\rho t\le32k\varepsilon
\]
for the specified sufficiently small \(t\), very general \(x\), and source definitions of \(\rho,\varepsilon\).  The moving-centre, subadjunction, and incidence smoothness data are indispensable and are not checked here.

## 8. Reduced-support adjoint lifting

*Lifting sections from the reduced support of an adjoint*, SHA-256 `ecbc1b8c73fefb32ddbd51ef6fcc0cb2a91e935bea46075c557f07bcc86fb9ed`, physical pp. 9, 15--21; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Lifting-sections-from-the-reduced-support-of-an-adjoint-September-27-2026/paper.pdf).

The source theorem model starts with a projective \(\mathbb Q\)-factorial dlt pair \((V,C)\), \(A=K_V+C\), and \(0\ne G\ge0\), \(G\sim qA\), supported on \(\lfloor C\rfloor\), with \(\mathcal O_V(G)|_{G_{\rm red}}\) semiample; it concludes \(\kappa(V,A)>0\).  The operational record is: keep the residue injection on the reduced SNC support, use a transverse filtered-frame isomorphism only after its mixed-Hodge input, and use the source's affine-open surjectivity of truncation maps
\[
 g_*(\mathcal O_Z/\mathcal I^{k+1})\twoheadrightarrow g_*(\mathcal O_Z/\mathcal I^k).
\]
It does not test dlt, semiampleness on a nonreduced support, residues, or lifting obstructions.

## 9. Negative-part and fixed-section transport

*Log abundance for compact Kähler spaces under logarithmic Iitaka subadditivity*, SHA-256 `46adc5be1070213b3a553dbd691b61daffcb734e5616b627e26a573a39e44dd8`, physical pp. 7--10; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-6-2026/main.pdf).

For a supplied pseudo-effective class \(\alpha\), its source operations are divisorial negative-part bookkeeping: \(0\le F\le N(\alpha)\) gives \(N(\alpha-\{F\})=N(\alpha)-F\), nef \(\beta\) gives \(N(\alpha+\beta)\le N(\alpha)\), and a modification preserves prime minimal multiplicities on strict transforms.  For a rational line \(L\sim_{\mathbb Q}P+R\) with \(P\) semiample and \(R=N(L)\) rational, multiplication by the canonical section identifies the divisible spaces \(H^0(X,mP)\) and \(H^0(X,mL)\).  This does not compute currents, minimal multiplicities, or a Kähler MMP.

## 10. Relative denominators and rounded section spaces

*Relative denominators and effective systems for log Calabi--Yau fibrations*, SHA-256 `a539053eb28e6c4d8aa1724d461504b215ec29a55ca57dd45f24a4b998dce623`, physical pp. 10--11, 14--16; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Relative-denominators-and-effective-systems-for-log-Calabi-Yau-fibrations-September-27-2026/paper.pdf).

The recorded finite-denominator model is a projective contraction \(f:N\to C\) to a smooth curve, with \(F=f^*[c]\), \(T=F_{\rm red}\), \((N,T+H)\) dlt, coefficient set \(\Phi\), and an actual divisor identity
\[
 p_0(K_N+T+H)+\operatorname{Div}(\psi)=p_0\beta F.
\]
The source's uniform integer \(p=p(\Phi,p_0)\) yields \(p\beta\in\mathbb Z\).  Its section-space operation, under the exact pullback presentation, is
\[
 H^0(X,\mathcal O_X(\lfloor lL\rfloor))
 =\psi^{l/p_0}f^*H^0(Z,\mathcal O_Z(\lfloor lD_Z\rfloor))
\]
for the stated divisible \(l\); it retains ratio fields and effective rounded systems.  Supply the actual identity, dlt/residue data, and contraction separately; do not infer a denominator bound from coefficient arithmetic alone.

## 11. Frobenius connection and destabilization

*Abundance in numerical dimension one for terminal threefolds in positive characteristic*, SHA-256 `5e170f2c29b7026e53d167ee18a5fde3f6102de99b5e1484cd4633d03f73e26e`, physical p. 16; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Abundance-in-numerical-dimension-one-for-terminal-threefolds-in-positive-characteristic-September-24-2026/paper.pdf).

For a smooth variety \(V\) over a perfect field of characteristic \(p>3\), a semistable torsion-free \(E\), and an unstable Frobenius pullback with first Harder--Narasimhan term \(B\), the canonical connection gives the source-stated nonzero map
\[
 B\longrightarrow(F_V^*E/B)\otimes\Omega_V^1.
\]
The reusable operation is a Grassmannian-chart descent test: vanishing connection makes chart entries lie in \(K^p\), so their \(p\)-th roots define a pre-Frobenius generic subspace; saturation and Frobenius flatness then scale degree by \(p\), contradicting semistability.  This is not a finite-field/Frobenius calculator and requires the source's smoothness, perfectness, separable generation, torsion-free saturation, and slope hypotheses.
