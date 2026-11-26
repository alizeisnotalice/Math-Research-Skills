# Proposed primitive: residue gluing for a cyclic Milnor-page lattice

**Source.** *Ambiently Homeomorphic Isolated Hypersurface Germs in C4 with
Multiplicities Four and Five*, p. 9, [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/paper.pdf).

## Input contract

Supply finite-rank integral lattices \(H,D,E\), a degree-\(k\) map with
projection \(\pi^*:D\to H\) and transfer \(\pi_!:H\to D\) satisfying
\(\pi^*\pi_!=k\), a residue map \(\tau:E\to\mathbb Z/k\), and integer
filling forms \(s_H,s_D,e\). Define \(K=\ker\pi^*\) and
\(\operatorname{pr}(l)=l-k^{-1}\pi_!\pi^*l\in K_{\mathbb Q}\).

## Construction and output

Form the exact fibre product
\[
\Lambda_\pi=\{(\operatorname{pr}(l),z)\in K_{\mathbb Q}\oplus(H\otimes E)_{\mathbb Q}:
\pi^*l\bmod kH=(1\otimes\tau)z\}.
\]
The source identifies the rational orthogonal filling form on it as
\(-s_D|_K\perp(s_H\otimes e)\). A finite matrix presentation and residue
congruence therefore assemble the candidate lattice/form.

## Boundary

Genuineness as a local Milnor lattice still requires the source's tube
regularity, isolation, Bockstein/transfer and page-comparison hypotheses. This
primitive does no singularity or ambient-homeomorphism classification.

## 固定来源

- 物理页 1, 3, 4, 5, 9, 10, 28。Theorem 4.1, equations (4.1)–(4.2), and character-sign construction SHA-256 `7b9c31dcfb1ba9b7c68b7ec31829963eebffcd6171a8139c26c20ee6c60e3b16`。[Ambiently homeomorphic isolated hypersurface germs in ℂ⁴ with multiplicities four and five](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Ambiently-homeomorphic-isolated-hypersurface-germs-in-C4-with-multiplicities-four-and-five-September-27-2026/paper.pdf)
