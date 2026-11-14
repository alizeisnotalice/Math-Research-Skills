# MZ-PTF — Pseudorandom Generators for Polynomial Threshold Functions

- Reading provenance: prepared by helper L08 in `evidence/W10/reader_batches/L08_batch2`; integrated here without a second full-text read.


## Identity and reading evidence

- Raghu Meka and David Zuckerman, arXiv:0910.4122v5, dated 15 November 2011; complete 28-physical-page arXiv article. Published in SIAM Journal on Computing (2013); preliminary STOC 2010 version noted by the paper. https://arxiv.org/abs/0910.4122.
- Local PDF: `evidence/fulltexts/MZ-PTF.pdf`; SHA-256 `2546fc2c3c232371b31438c8c04cb2db96dd8821cb6f3403edaeb59c0c6bdf45`.
- Physical p.1 identity and page count checked visually. Full text pp.1–28 read, including Appendix A and references. Rendered theorem/proof pages include pp.2, 15, 22–24 (physical page numbers); these were visually checked to resolve the regularity exponent and cap argument. See `../reader_batches/L08_batch2/reading_coverage.json#sources.MZ-PTF`; review pending.

## Setting and principal guarantees

A degree-d polynomial threshold function (PTF) is $f(x)=\operatorname{sign}(P(x)-\theta)$ on the Boolean cube, with P multilinear of degree at most d. A generator $\epsilon$-fools a class when the output expectation differs from uniform by at most $\epsilon$ for every test in the class.

- **Theorem 1.2 (physical p.2):** for $0<\epsilon<1$, there is an explicit PRG fooling degree-d PTFs with error at most $\epsilon$ and seed length $2^{O(d)}\log n/\epsilon^{8d+3}$.
- **Theorem 1.3 (p.2):** for every fixed c and $\epsilon\ge n^{-c}$, an explicit PRG fools halfspaces with error $\epsilon$ and seed length $O(\log n+\log^2(1/\epsilon))$.
- **Theorem 1.4 (p.3):** for a universal c>0 and $\epsilon>c\log n/n^{1/4}$, spherical caps have an explicit PRG with error $\epsilon$ and seed length $O(\log n+\log^2(1/\epsilon))$.

Do not omit the degree-dependent $2^{O(d)}$ and $\epsilon^{-(8d+3)}$ in the general theorem, the fixed-c/polynomially-small error regime in the halfspace result, or the lower error threshold in the cap result.

## Generator and proof dependencies

Section 2 (physical pp.5–8) recalls the INW generator for read-once branching programs and proves the “monotone ROBP” reduction: partition acceptance probabilities into intervals to reduce width to $O(\log(2T/\epsilon))$. Section 3 (pp.8–9) builds the generator by hashing variables into buckets and applying a small-space PRG together with a limited-independence generator inside buckets. The table on p.9 lists different independence and balance parameters for each test class; they are not interchangeable.

### Halfspaces

Regularity for halfspaces in §4.1 is the coordinate condition $|w_i|\le\epsilon\|w\|_2$ for all i. It implies the useful fourth-moment estimate $\sum_i w_i^4\le\epsilon^2\|w\|_2^4$, but the paper's definition is the coordinate condition. **Theorem 4.3 (physical p.10)** assumes H is $\alpha$-almost pairwise independent for $\alpha=O(1)$ and $G_0$ generates a $\delta$-almost 4-wise independent distribution with $\delta=\epsilon^2/(4n^5)$. The resulting construction fools regular halfspaces with error $O(\epsilon)$ and seed $O(\log n/\epsilon^2)$. The proof uses hybrid replacement, invariance/normal approximation and Berry–Esseen, controlling fourth moments of the bucket sums. “Almost 4-wise” is part of the stated hypothesis.

For arbitrary halfspaces, **Theorem 4.8 (physical pp.11–12)** assumes sorted weights $w_1\ge\cdots\ge w_n$ and $\sum_iw_i^2=1$. It gives $K=O(\log^2(1/\epsilon)/\epsilon^2)$ and either (1) the tail vector $(w_{K+1},\ldots,w_n)$ is $\epsilon$-regular, or (2) for every D whose first K coordinates are $\epsilon$-close to uniform and whose conditioned tail is $(1/n^2)$-almost pairwise independent with probability at least $1-\epsilon$, the head truncation $h'(x)=\operatorname{sign}(\sum_{i\le K}w_ix_i-\theta)$ disagrees with h with probability at most $2\epsilon$. A balanced-hash construction (**Theorems 4.10–4.11, pp.12–13**) then gives O($\epsilon$)-fooling. Section 4.3 (pp.13–14) derandomizes using the INW small-space generator and the monotone-ROBP trick, proving Theorem 1.3. The structural alternative’s distributional side conditions must travel with any use.

### Polynomial threshold functions

Definition 5.1 (physical p.15) calls a normalized degree-d multilinear polynomial $\epsilon$-regular when the sum of squared coordinate influences/derivatives $\sum_i\tau_i(P)^2$ is at most $\epsilon^2\|P\|_2^2$. **Theorem 5.2 (p.15)**: if H is $\alpha$-almost pairwise independent for $\alpha=O(1)$ and $G_0$ is 4d-wise independent, then the construction fools an $\epsilon$-regular degree-at-most-d PTF with error
$$
O\!\left(d\,\epsilon^{2/(4d+1)}\right).
$$
The exponent is the fraction $2/(4d+1)$ (rendered source p.15); it is not $2/(4d+1)$ multiplying epsilon or a linear-$\epsilon$ error. The proof in §5.1 (pp.15–19) compares the polynomial under the generator to a Gaussian via an invariance lemma, then uses anti-concentration around the threshold.

Sections 5.2–5.3 (physical pp.19–23) handle arbitrary PTFs. Random restrictions (Lemma 5.13) yield a regular residual PTF with constant probability; high-bias cases are controlled separately (Lemma 5.14). A block decision tree of block size $L=\Theta_d(\log(1/\epsilon)/\epsilon^2)$ and depth $O_d(\log(1/\epsilon))$ has all but O($\epsilon$) path mass on leaves that are either high-bias under the allowed limited-independence distributions or regular. **Theorem 5.18 (p.21–22)** combines $(t+4d)$-wise inner independence, with $t=\Theta_d(\log^2(1/\epsilon)/\epsilon^2)$, and the regular theorem to obtain error $O(\epsilon^{2/(4d+1)})$ and seed length $O_d(\log n\log^4(1/\epsilon)/\epsilon^4)$. Its proof conditions on each restriction leaf; preservation of the generator hypotheses under this conditioning is a required step, not automatic for arbitrary pseudorandom sources.

### Spherical caps

Section 6 (physical pp.23–25) first compares Gaussian and spherical halfspace probabilities (Lemma 6.2, error $O(\log n/n^{1/4})$). Lemma 6.3 shows that for 8-wise independent cube input and the paper’s random-sign/orthogonal transform, the transformed vector has fourth moment $\sum_i v_i^4$ at most $\gamma/n$ except with probability $O(\gamma^{-2})$. **Theorem 6.4 (p.24–25)** combines this with Theorem 4.3 for unit-norm cap normal and $\epsilon>C\log n/n^{1/4}$. This is a specific spherical-cap transfer, not a general invariance theorem for arbitrary product measures.

## External dependencies and limits

- The regular PTF argument imports an invariance principle and polynomial anti-concentration results; cite these as dependencies rather than as newly proved here.
- The random-restriction decomposition is a PTF-specific structural lemma, not a conclusion for arbitrary Boolean functions.
- Section 6’s cap result needs its explicit unit norm and error lower bound.
- Appendix A (physical p.28) records non-explicit existence bounds; it is not part of the explicit PRG constructions in Theorems 1.2–1.4.

## Full section coverage

See `../reader_batches/L08_batch2/reading_coverage.json#sources.MZ-PTF`; all physical pp.1–28, including Appendix A and references, were read.
