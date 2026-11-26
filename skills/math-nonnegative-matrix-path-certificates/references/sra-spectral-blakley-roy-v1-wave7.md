# Sra, *A Spectral Blakley--Roy Inequality for Nonnegative Matrices* (v1)

- Source: [author preprint repository](https://github.com/suvrit/preprints/blob/main/preprints/pourya-rho/v1/pourya-rho-v1.pdf), local v1 PDF, 10 physical pages.
- Verified SHA-256: `2421188766a358079a059dc7aa1a57fe5b4e539a32c4d7f2d3e8d04451be823a`.
- Adopted locus: physical pp. 2--4, Theorem 1.2 and its proof; pp. 4--5 for the odd-product norm/spectral corollaries and the separate even-exponent boundary.

The adopted statement is the finite odd path inequality (1.3): for
entrywise-nonnegative symmetric same-order factors, nonnegative endpoints,
and \(k=2r+1\), it is exactly (P) in the skill.  This is a v1 preprint, so
the result is recorded with its source status rather than as an independently
published theorem.

## Checked proof dependency chain

1. On physical p. 2 the source writes both sides as short and long weighted
   path partition functions and invokes the finite Gibbs variational identity
   (Lemma 2.1) and finite Markov-chain entropy identity (Lemma 2.2).
2. On p. 3 it constructs the alternating forward/reverse Markov law.  Its
   energy identity uses symmetry; its entropy identity uses the odd number of
   traversals in each edge block.
3. On p. 4 equation (2.5) expresses the logarithmic gap as three relative
   entropies.  It then passes from strictly positive to nonnegative data by
   adding \(\varepsilon\) to every endpoint and matrix entry and taking a
   limit.
4. The spectral-radius consequence uses nonnegative maximizing singular
   vectors and Gelfand's formula (pp. 4--5); it is intentionally outside this
   finite exact replay.  The many-factor even-exponent analogue fails (p. 5,
   Remark 3.4).

The replay script checks only finite instances of (P) and the stated parity
boundary; it does not certify the paper's entropy proof or its asymptotic
spectral-radius passage.
