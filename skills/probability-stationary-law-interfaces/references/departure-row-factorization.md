# Departure-row factorization and record regeneration

This reference isolates a finite-prefix calculation from three OpenAI preprints in Family 220. The sources are preprints. The statements below are limited to their locally checked finite-word and record arguments.

## Input contract

Fix a deterministic finite nearest-neighbour word
\[
  \gamma=(x_0,x_1,\ldots,x_m),\qquad x_{j+1}-x_j\in U.
\]
Its departure set is
\[
  \operatorname{Dep}(\gamma)=\{x_0,\ldots,x_{m-1}\}.
\]
The terminal arrival uses no transition row unless the word left that vertex earlier. Repeated visits to one departure vertex use repeated factors from the same row.

For an iid environment of transition rows, put
\[
 p_\omega(\gamma)=\prod_{j=0}^{m-1}\omega(x_j,x_{j+1}-x_j),
 \qquad W(\gamma)=\mathbb E[p_\omega(\gamma)].
\]
If \(f\geq0\) is measurable with respect to all rows outside \(\operatorname{Dep}(\gamma)\), then
\[
 \mathbb E[p_\omega(\gamma)f]=W(\gamma)\,\mathbb E[f]. \tag{1}
\]
The equality is only a product-measure factorization. It does not require independence among the different directions inside one row.

For an \(R\)-dependent row field, replace \(\operatorname{Dep}(\gamma)\) by the active departure set \(\operatorname{Act}(\gamma)\), namely the departures at which the transition factor genuinely uses the environment. If a splitting/mark construction makes the remaining steps deterministic, and
\[
 \operatorname{dist}_\infty(\operatorname{Act}(\gamma),B)>R,
\]
then (1) holds for every nonnegative \(f\) measurable with respect to the rows in a deterministic set \(B\). This requires the specified finite-range independence of the row field. It does not turn an arbitrary unmarked prefix into an independent object.

If a second path is stopped on its first arrival in the forbidden departure set, its finite stopped prefixes use only rows outside that set. Cylinder generation then gives the same measurability for every event of the stopped path, including an infinite event which implies that it never arrives. This is the safe way to put a continuation or avoidance probability into \(f\).

## Regeneration use

Let \(h(x)=v\cdot x\), and write
\[
 D_v=\{h(X_n)\geq0\ \text{for every }n\geq0\},\qquad p_v=P_0(D_v).
\]
Use this part only after separately proving \(p_v>0\), defining a finite word whose preterminal departure heights lie below its terminal strict record, and proving that every earlier candidate record is invalidated within that word.

For such a word \(\gamma\) ending at \(z\), factor its finite prefix against a translated suffix constrained to stay above \(h(z)\). The departure-row separation gives
\[
 P_0\{\text{first word}=\gamma,\ \text{translated suffix}\in B\}
   =W(\gamma)P_0(B\cap D_v). \tag{2}
\]
After division by \(p_v\), successive relative words are iid with mass \(W(\gamma)\). Equation (2) is an enumeration of finite prefixes. A true cut is selected using the future, so an annealed Markov property at that cut is unavailable and must not replace this calculation.

For real directions, count ordinary strict-record indices rather than height values. If every height gain per record is at most one and a regeneration word has gain \(L\) and \(S\) ordinary records, then \(L\leq S\). When the factorization also proves that every record index has conditional probability at least \(p_v\) of being a true boundary, the renewal argument gives
\[
 0<\mathbb E L\leq\mathbb E S\leq p_v^{-1}.
\]
This controls projected spatial width. It supplies no moment for word duration, and it supplies no speed or ballisticity conclusion.

## Exact finite check

Consider independent rows on \(\mathbb Z\), each uniformly chosen from two types with right-step probabilities \(2/3\) and \(1/3\). For the word \(0,1,0,1\),
\[
 W(\gamma)=\mathbb E[p_0^2(1-p_1)]=\frac5{36}.
\]
With \(f=p_3\), the row at \(3\) is disjoint from the departure rows \(0,1\), and exact enumeration of the eight row-type triples gives
\[
 \mathbb E[p_0^2(1-p_1)p_3]=\frac5{72}
 =\frac5{36}\cdot\frac12.
\]
This checks the row convention and (1) on a finite model. It is not a random-environment regeneration theorem.

## Source pins and exclusions

- *A directional zero–one law under strict ellipticity*, OpenAI fixed source, SHA-256 `245e917113b3545b311c4c9eab739227d530f527081c1b0be4a92ea904559683`, PDF p. 5, Lemma 2.1, and pp. 8–9, Lemmas 2.4–2.5. [Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf)
- *A directional zero–one law for finite-range-dependent random environments*, SHA-256 `010edc479fd820382bf7dd600793ff5ab361216ce1ac06bb007f5505787cf958`, PDF p. 5, Lemma 2.1, and pp. 7–9, Propositions 2.2–2.4. Its marked active-row construction is required for the finite-range version. [Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/directional-zero-one-finite-range.pdf)
- *Directional transience implies ballisticity*, SHA-256 `8b305d1fbb11b2a62d76f7decbc45accf5d1c02362937d0af5c4108dd0cc1411`, PDF pp. 5–7, Lemma 2.1. The source's speed conclusion depends on its later quenched crossing and entropy argument and is not included here. [Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf)

Do not infer a directional zero–one law, a finite radius moment, a duration moment, a law of large numbers, or ballisticity from this reference. Each requires the separate hypotheses and later arguments of its source.
