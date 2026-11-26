# Finite torus-packet source scope

OpenAI, *A smooth three-torus diffeomorphism with simple Lebesgue spectrum*, fixed `openai/math` commit `3344da59991ed94f9ba711217b29c1d760badfa6`, SHA-256 `0a6684b31440fc6b221df4abae9cf68ff989d6e4978cc53fa599fb4517b035c1`. Physical PDF pp. 3–4 define the twist, good arc, packet, disjoint list, color orthogonality, and equations (2.2)–(2.4). The source is a preprint. [Fixed primary PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/paper.pdf)

For a packet \(A(u,a)e(m\theta)\), equation (2.3) says that its spectral measure is
\[
(m\phi\mathbin{\bmod}1)_*(|A(u,a)|^2\,du\,da).
\]
When the integrated squared amplitude is constant \(q\) on one affine interval of slope \(s>0\), the change of variables has exact density \(q/|ms|\) on its modular image. The present checker is the finite rational specialization of this identity. Equal-frequency supports must be disjoint. Different frequencies are angularly orthogonal.

Equation (2.4) compares spectral densities of actual vectors for the same transformation. A finite density comparison does not determine \(\|F-G\|_2\) unless amplitudes and their relative phases are supplied, so the checker reports only its directly computed exact \(L^1\) density difference.

The source's later passage, stationary-phase, block, whitening, diagonal-limit, and simple-Lebesgue-spectrum claims require material beyond this interface. This skill does not use them.
