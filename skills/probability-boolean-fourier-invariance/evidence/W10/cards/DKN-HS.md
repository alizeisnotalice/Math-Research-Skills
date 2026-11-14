# DKN-HS — Bounded Independence Fools Halfspaces

- Reading provenance: prepared by helper L08 in `evidence/W10/reader_batches/L08_batch2`; integrated here without a second full-text read.


## Identity and reading evidence

- Ilias Diakonikolas, Parikshit Gopalan, Ragesh Jaiswal, Rocco A. Servedio, Emanuele Viola. Complete author manuscript dated 27 May 2010; SIAM Journal on Computing 39(8) (2010), 3441–3462; preliminary FOCS 2009 extended abstract noted by the manuscript. DOI: https://doi.org/10.1137/100783030. 27 physical PDF pages; journal/article pagination ends at 26.
- Local PDF: `evidence/fulltexts/DKN-HS.pdf`; SHA-256 `46a01e50a63e5693e46c79ce11007cfcc8ba6ed93712c07e0887763e9c6cb6ba`.
- Physical p.1 identity and page count checked visually. Full text pp.1–27 read, including references. The main statement and technical polynomial/critical-index proof pages were rendered and checked (pp.2, 9, 13, 20, 22). Full coverage: `../reader_batches/L08_batch2/reading_coverage.json#sources.DKN-HS`; review pending.

## Model and main theorem

Let $h(x)=\operatorname{sign}(w\cdot x-\theta)$ on $\{-1,+1\}^n$ with arbitrary real weights and threshold. Let $U$ be uniform. A distribution D is k-wise independent if every projection to k coordinates is uniform.

**Theorem 1.2 (Main; physical p.2).** There is an absolute constant C such that any k-wise independent D satisfies
$$
|\mathbb E_D h-\mathbb E_U h|\le\epsilon
\quad\text{whenever}\quad k\ge C\epsilon^{-2}\log^2(1/\epsilon).
$$
The claim is for halfspaces over the uniform Boolean cube; the threshold and weights are unrestricted. The paper gives a matching lower-bound example up to a logarithmic factor. Via standard explicit k-wise independent spaces, the resulting generator has seed length $O(\log n\,\epsilon^{-2}\log^2(1/\epsilon))$.

## Proof architecture

### Regular halfspaces

After normalizing $\|w\|_2=1$, the paper calls $h(x)=\operatorname{sign}(w\cdot x-\theta)$ $\epsilon$-regular exactly when $|w_i|\le\epsilon$ for every i (Definition 3.1, physical p.8). **Theorem 3.2 (p.8)** says a $K(\epsilon)$-wise independent distribution fools such an $\epsilon$-regular halfspace with error at most $12\epsilon$, where $K(\epsilon)=O(\log^2(1/\epsilon)/\epsilon^2)$.

The technical polynomial is **Theorem 3.5 (p.9)**: for $0<\epsilon<0.1$ and the paper's stated a,K, a univariate P of degree at most K satisfies (i) $P(t)\ge\operatorname{sign}(t)\ge-P(-t)$ for every real t; (ii) $P(t)\in[\operatorname{sign}(t),\operatorname{sign}(t)+\epsilon]$ on $[-1/2,-2a]\cup[0,1/2]$; (iii) $P(t)\in[-1,1+\epsilon]$ on $(-2a,0)$; and (iv) $|P(t)|\le2(4|t|)^K$ for $|t|\ge1/2$. The source defines $a=\epsilon^2/(C\log(1/\epsilon))$ and $K=4c\log(1/\epsilon)/a+2=O(\log^2(1/\epsilon)/\epsilon^2)$, with positive constants chosen later and C much larger than c. It builds P from **Theorem 3.10 (p.13)**: degree at most $2m+1$, error at most $\epsilon^2$ on $a\le|t|\le1$, values in $[-(1+\epsilon^2),1+\epsilon^2]$ on $[-a,a]$, and monotone increase on $(-\infty,-1]$ and $[1,\infty)$. Section 4 (pp.15–17) applies the sandwich to $w\cdot x-\theta$, splitting into threshold/variance cases; Berry–Esseen anti-concentration and Hoeffding tails control the exceptional central and large-deviation events. Do not assume stronger approximation properties than these intervals state.

### Arbitrary weights: critical-index dichotomy

Sort $|w_1|\ge\cdots\ge|w_n|$. The $\tau$-critical index $\ell(\tau)$ (Definition 5.1, physical p.18) is the first i at which the remaining vector is $\tau$-regular, i.e. the largest remaining weight is at most $\tau$ times the remaining $\ell_2$ norm. With $L(\epsilon)=8\log^2(10/\epsilon)/\epsilon^2$ and K as in the regular theorem:

- **Theorem 5.3 (physical p.19):** if $\ell(\epsilon)\le L(\epsilon)$, then $(K(\epsilon)+L(\epsilon))$-wise independence O($\epsilon$)-fools h. Condition on the first $\ell(\epsilon)-1$ coordinates; the remaining halfspace is $\epsilon$-regular by the critical-index definition, and the conditional tail remains K-wise independent, so Theorem 3.2 applies. The extra L-wise budget supplies the head marginal.
- **Theorem 5.4 (physical pp.19–22):** if $\ell(\epsilon)>L(\epsilon)$, then $(L(\epsilon)+2)$-wise independence fools h with error at most $9\epsilon$.

For the second case, split coordinates into a separated set G and its complement around the critical head/tail. **Lemma 5.5 (p.20)** gives geometric decay up to the critical index; Claim 5.6 bounds the tail norm and Claim 5.7 provides separation of signed head sums. Lemma 5.8 (p.22) gives a margin except with probability O($\epsilon$). The tail’s 2-wise independence yields a Chebyshev error $O(\epsilon^2)$, and the uniform tail uses Hoeffding. Adding the margin and tail errors produces the stated $9\epsilon$ bound. The constants and independence orders belong to this partition argument; replacing either theorem by a generic “critical-index method” loses its guarantee.

Finally §5.1 (physical p.23) combines the two regimes and compares K and L, both $O(\epsilon^{-2}\log^2(1/\epsilon))$, proving Theorem 1.2.

## Limits and transfer cautions

- The theorem compares D to uniform cube measure. It does not automatically fool a biased product law or a correlated/non-product reference distribution.
- It concerns linear threshold functions, not arbitrary degree-d polynomial threshold functions; those require separate invariance/regularity results.
- Preserve the exact $k$-wise independence requirement, error norm (expectation difference), and real threshold/weight setup.
- Berry–Esseen and Hoeffding inequalities are invoked as standard results; the paper’s proof does not establish those inequalities from first principles.

## Full section coverage

See `../reader_batches/L08_batch2/reading_coverage.json#sources.DKN-HS`; physical pp.1–27, including acknowledgments and all references, were read.
