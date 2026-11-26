# OpenAI tree-posterior components

These entries describe finite posterior interfaces only.  They do not prove a
reconstruction threshold, factor-of-IID construction, or global contraction
outside the supplied model class.

## Four-state capacity/flow interface

For the stated symmetric four-state posterior coordinates, conditionally
independent observations combine by the normalized product law.  The draft
then couples the reconstruction message to a bounded-degree flow/capacity
comparison, conditional on its posterior-product contraction.  A caller must
provide the four-state symmetry, channel parameter, offspring/degree data,
and the contraction premise; no general Potts-channel replacement is valid.

Source: *A Capacity Criterion for Four-State Potts Reconstruction on Trees*,
SHA-256 `6c725aee122ce7659ea4b30bbb9805e23b41666eb9922d6bc8778635f566de34`,
physical pp. 4--8, Theorem 1.1 and Proposition 2.1; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Capacity-Criterion-for-Four-State-Potts-Reconstruction-on-Trees-October-5-2026/four-state-capacity.pdf).

## Four-state polynomial potential cell

For posterior vectors in `Delta_4`, the stated source-specific potentials
`A,F,G,H` are used only with its exact polynomial-sign certificate.  Under a
symmetric posterior law satisfying `E[H]>=0`, its channel and independent
product closure give the displayed moment saving.  Retain the cubic remainder
and the ferromagnetic four-state parametrization; do not apply this entry to a
generic simplex recursion without a new exact sign certificate.

Source: *The Reconstruction Threshold for the Ferromagnetic Four-State Potts
Model*, SHA-256 `a8e3ff75c819ee3419e05b7eeca3ac5d69e46baa02fe77745f93e4c9a55adb01`,
physical pp. 6--8, Propositions 3.1--3.2; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Reconstruction-Threshold-for-the-Ferromagnetic-Four-State-Potts-Model-October-5-2026/four-state-potts.pdf).

## Removing sibling order from a finite tree observation

For an ordered Galton--Watson construction in which sibling descendant laws
are conditionally iid given the parent spin, forgetting sibling order leaves
the root posterior law unchanged.  The invocation must retain the uniform root
prior, the channel law, and all boundary decoration; it does not identify the
later threshold or special complex-coordinate interval certificate.

Source: *The exact reconstruction threshold for the three-state symmetric
channel*, SHA-256 `e87d0854f29320d5b8ddd3015f3f89964e32231eec54a609aa1a9567d582f71a`,
physical pp. 6--9, Lemma 2.1 and Proposition 2.4; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-exact-reconstruction-threshold-for-the-three-state-symmetric-channel-September-25-2026/paper.pdf).

## Exact binary posterior fusion

For a uniform binary latent sign and two signals conditionally independent
given that sign, posterior means `U,V` combine as `(U+V)/(1+UV)`.  The local
script in `../scripts/binary_posterior_fusion.py` checks this equality with
exact rational Bayes calculations for two binary symmetric channels.  It is a
finite demonstration of the conditional-independence contract, not a tree
reconstruction calculation.

Source: *The sharp factor-of-IID threshold for the free Ising model on regular
trees*, SHA-256 `aabb8cc15b9072c5d5f468d933ef929b19b654ea065b911445567d36570eabdd`,
physical pp. 8--10, Section 3.1/Lemma 3.1; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-sharp-factor-of-IID-threshold-for-the-free-Ising-model-on-regular-trees-September-26-2026/article.pdf).
