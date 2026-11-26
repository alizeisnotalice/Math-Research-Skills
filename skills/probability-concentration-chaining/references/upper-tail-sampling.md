# Fixed-coordinate upper-tail sampling

## Source and scope

OpenAI, *Threshold parallel repetition for finite-dimensional entangled games*, 25 September 2026, Lemma 2.2, PDF p. 6, pinned manuscript SHA-256 `ad2fcb38fca09ed70f48af4696d709617d424769ec1fe81a8e3313b2441b8234`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026/paper.pdf).

The component concerns arbitrary jointly distributed binary variables only.  Neither coordinate independence nor exchangeability is assumed.  The paper's subsequent threshold theorem additionally needs the separate conditional-mean hypothesis in Proposition 2.3; its entangled-game application uses Song's external conditioning estimate (Proposition 2.4).  Those are excluded here.

## Independent proof

Draw (J_1,\ldots,J_\ell) independently and uniformly from ([k]), independently of the binary vector, and let (C) be their distinct set.  Put

\[
a_C=\Pr(E_C),\quad b_C=\Pr(E_C, W<q_0k),\quad A=p_Hq^\ell.
\]

Conditioning on the binary vector gives

\[
\mathbb E_Ca_C=\mathbb E(W/k)^\ell\ge p_Hq^\ell=A,
\]

because (W/k\ge q) on (W\ge\lceil qk\rceil).  Similarly,

\[
\mathbb E_Cb_C
=\mathbb E[1_{\{W<q_0k\}}(W/k)^\ell]
\le q_0^\ell
\le \varepsilon A/4.
\]

The draws with (a_C<A/2) contribute at most (A/2) to (​\mathbb E_Ca_C).  The draws with (b_C>\varepsilon a_C) contribute at most (​\varepsilon^{-1}\mathbb E_Cb_C\le A/4).  Since the total (a_C)-weight is at least (A), some remaining draw has both (a_C\ge A/2) and (b_C\le\varepsilon a_C), proving the two conclusions.  Collapsing repeats only makes ​(|C|\leell).

The CLI does not attempt to sample the draw distribution; it exhaustively checks every subset of size at most ​(ell) for a supplied finite law.  This proves its returned certificate exactly, while the argument above proves general existence.

## Boundary

The threshold event must be nonempty and have positive probability, and the displayed ratio condition on ​(ell) is essential.  A conditional statement derived after testing (C) still needs its own model-specific inference.  In particular, this lemma alone does not bound ​(Pr(W\ge qk)), establish a repetition theorem, or certify an unenumerated empirical distribution.
