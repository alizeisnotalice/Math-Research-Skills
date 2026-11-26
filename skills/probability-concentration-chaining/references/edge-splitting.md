# Edge-colouring cut-expansion certificate

## Contract

Let `P` be a finite simple graph on `r >= 2` vertices.  Suppose that for every nonempty proper `S`, writing `u = min(|S|, r-|S|)`,

\[
 e_P(S,V(P)\\setminus S)\ge h_0u. \tag{1}
\]

For a positive integer `l`, define

\[
 B(r,h_0,l)=2l\sum_{u=1}^{\lfloor r/2\rfloor}
 \left(r e^{-h_0/(8l)}\right)^u. \tag{2}
\]

If `B(r,h0,l) < 1`, then there is an edge partition `E(P)=E_1 disjoint-union ... disjoint-union E_l` such that every spanning graph `(V(P),E_j)` has cut expansion at least `h0/(2l)`.

This is the finite form of Lemma 4.1 on physical p.9 of *A linear cycle-and-edge decomposition of every graph*, OpenAI math preprint (pinned 2026-09-24 version, SHA-256 `4aa44187578ea59b64c78258eb8c5dd3601ee979a1a402ca9ed26696b30b515f`).  The paper uses it only after inserting an asymptotic scale regime; that regime is not part of this certificate.

## Proof and elementary lower-tail derivation

The binomial tail used below needs no external concentration theorem.  If \(X\) is binomial with mean \(\mu\), Markov's inequality at \(t=\log 2\) gives

\[
 \Pr[X\le \mu/2]\le e^{t\mu/2}\mathbb E e^{-tX}
 \le \exp\{\mu(t/2+e^{-t}-1)\}
 =\exp\{-\mu(1-\log2)/2\}\le e^{-\mu/8}.
\]

Assign each edge independently and uniformly a colour in `{1,...,l}`.  Fix a cut with smaller side size `u`, and write `e` for its original number of crossing edges.  For one colour its crossing-edge count is `X ~ Bin(e,1/l)` and (1) gives its mean `mu=e/l >= h0*u/l`.  The elementary multiplicative Chernoff lower-tail bound

\[
\Pr[X<\mu/2]\le e^{-\mu/8}
\]

therefore gives

\[
 \Pr[X<h_0u/(2l)]\le e^{-h_0u/(8l)}. \tag{3}
\]

For a fixed `u`, at most `2 binom(r,u) <= 2r^u` oriented choices of the smaller-side cut need be considered; this harmlessly double-counts balanced cuts.  Union-bound (3) over colours and over `1 <= u <= floor(r/2)`.  The probability that some colour fails on some cut is at most (2).  Strict inequality in (2) leaves a positive-probability colouring with no failed cut, proving the assertion.

The proof requires only finite independence of edge colours and the supplied all-cut hypothesis (1).  In particular it makes no claim about a random edge colouring chosen after conditioning, nor about nonuniform colours.

## Worked certificates and boundary

For `P=K_1024`, (1) holds with `h0=512`: if `u<=512`, a cut has `u(1024-u) >= 512u` edges.  With `l=2`, put `q=1024 e^{-32}`.  Since `e>2`, `q<2^{-22}`; hence

\[
 B(1024,512,2)<4\frac{2^{-22}}{1-2^{-22}}<1.
\]

The method therefore certifies an edge bipartition of `K_1024` whose two spanning classes each have cut expansion at least `128`.  This is an existence result, not the output of a colouring algorithm.

For `r=8`, `h0=4`, `l=2`, the base in (2) is `8e^{-1/4}>1` (because `e^{1/4}<2`), so this union-bound certificate is unavailable.  That failure does **not** say an appropriate partition does not exist; it only prevents this sufficient condition from being invoked.
