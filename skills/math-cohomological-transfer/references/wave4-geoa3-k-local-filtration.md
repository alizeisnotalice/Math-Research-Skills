# Ordered K-local cofiber filtration

**Source.** OpenAI, *Filtered chromatic splitting at generic primes*, Proposition 2.1, PDF pp. 8--9; SHA-256 `f2aeefc98af1afcdab8b865cb76d08606e93b0439fb7fb578e367ef84ba53015`.

## Input contract

Fix odd `p`, `n>=1`, an `S`-module `D`, a specified `u:S -> D`, and maps `z_I: Sigma^(-d(I)) S -> D` for every `I subset {1,...,n-1}`, with `z_empty=u` and `d(I)=sum_(i in I)(2i-1)`.  Require both source hypotheses: (a) each stated wedge of components is a `K(t)`-equivalence for `1<=t<n`; (b) the specified rational graded dimensions of `L0 D`.  At `n=1`, also require nonzero `pi_0 L0 u`.

## Reuse

Set `X=L_(n-1)D`.  Attach the wedge blocks in increasing maximum index, using cofibers.  The proposition produces the ordered filtration whose successive height-local blocks are indexed by the relevant subsets `I`; after the final positive-height blocks, the rational dimension condition identifies the terminal rational block.  Preserve the given components and the unit compatibility: the procedure is not a claim of a canonical basis or filtration from dimensions alone.

The source uses the actual `K(t)` equivalences to remove exactly the earlier direct summands.  A dimension count without those equivalences, or a non-odd prime, is outside this interface.

## 固定来源

- 物理页 8, 9。Proposition 2.1 SHA-256 `f2aeefc98af1afcdab8b865cb76d08606e93b0439fb7fb578e367ef84ba53015`。[Filtered chromatic splitting at generic primes](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Filtered-chromatic-splitting-at-generic-primes-September-25-2026/paper.pdf)
