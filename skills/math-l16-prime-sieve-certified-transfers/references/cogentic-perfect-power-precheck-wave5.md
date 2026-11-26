# Bounded perfect-power divisor precheck

**Scope:** a small explicit integer precheck only. It is distinct from the existing supplied-exponent gcd splitter (which needs `a,E,q`), prime-sieve transfers, and subgroup-index exponent transfer (which needs a certified prime-factor exponent). It neither constructs a universal exponent nor factors a non-perfect-power composite.

## Pinned source and audited locus

Yang Cai et al., *Unconditional Deterministic Subexponential Integer Factoring and Quadratic Nonresidue Construction*, local PDF SHA-256 `0ccf115516dab3cbeee15167f2dea62fcb29d03a19224cb4a9ae69a5ce402993`, physical p. 57, proof of Theorem 1.1, steps 1–2. The locally downloaded original at `10_Google_Cogentic_2026-11-25/PDF/04_deterministic_factoring_l34.pdf` was rehashed against the cached Cogentic original: both equal that SHA. The source's pinned release is [Google Research commit 4a7bc8ab0bc7](https://github.com/google-research/google-research/blob/4a7bc8ab0bc7/cogentic_research_papers/deterministic_factoring_l34/paper.pdf).

## Finite interface

Input: an explicit integer `N >= 4`.

1. If `2 | N`, output `2`.
2. Put `b=floor(log2(N))+1`. For each `k=2,...,b`, use exact bounded integer powering/binary search to test whether `x^k=N` for some integer `x>=2`.
3. On the first equality, output `x`; otherwise return **inconclusive**.

The p. 57 proof checks the only adopted implication: if `x^k=N` with `k>=2`, then `1<x<=sqrt(N)<N`, so `x` is a proper divisor of `N`. The range through `b` is complete for an integer perfect-power representation because `2^k<=N<2^b`. The helper performs exactly this finite implication using integer arithmetic.

## Strict boundary

An inconclusive output does not imply primality, squarefreeness, absence of a factor, or a bound for a later splitter. The source's subsequent `Aexp`/`Asplit` steps and their subexponential complexity rest on further source results and are not adopted here.

Run:

```sh
python3 -B scripts/cogentic_perfect_power_precheck_wave5.py 27 91 64
```

[固定版论文](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf)。
