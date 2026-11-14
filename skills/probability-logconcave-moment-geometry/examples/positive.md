# Positive transfer patterns

## CI to norm deviations (conditional on the actual premise)

Let $\mu$ be a symmetric log-concave law whose $Z_p$ expansion is known with constant $\beta$, and let $||\cdot||$ be any norm. Symmetric log-concave moments are $1$-regular. Therefore Proposition 3.15 of Latała–Wojtaszczyk, under its stated CI premise, gives for every $p\ge2$:
$$
\big(E|\,||X||-\operatorname{Med}||X||\,|^p\big)^{1/p}
\le2\beta\,\sup_{||v||_*\le1}\|\langle v,X\rangle\|_p.
$$
This is a valid conditional consequence. It does not establish C154; the missing step is proving CI($\beta$) uniformly for all symmetric log-concave $\mu$.

## Product coordinates to convex IC and moments

If $X$ has independent symmetric coordinates with log-concave tails, the one-dimensional convex IC theorem tensorizes. The source then obtains, for every norm and $p\ge2$,
$$
(E||X||^p)^{1/p}\le E||X||+D\,\sigma_{||\cdot||,X}(p),
$$
with an absolute $D<70223$. The first-moment coefficient is $1$. The coordinate independence and log-concave-tail hypotheses are essential to this cited result; this does not resolve C153 for a general dependent vector.
