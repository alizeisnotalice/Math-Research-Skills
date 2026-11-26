---
name: math-modified-dirichlet-character-omega-bound
description: 对有限素数修改的原始 Dirichlet 特征，按解析、Baker 和差异度量门槛调用部分和的对数 Ω 下界。
---

# Modified-character partial-sum omega bound

Use only for a completely multiplicative `f` that agrees off a finite prime set `S` with
a **primitive** Dirichlet character `chi`, and satisfies `|f(p)|=1` for every `p in S`.
Under precisely these hypotheses the source theorem yields

```
sum_{n <= x} f(n) = Omega((log x)^((|S|-3)/2)).
```

Before invoking it, record the exact character modulus, values at every exceptional
prime, the finite set `S`, and the normalization of the partial sum. The proof route uses
the Euler factorization, a zero-free/functional-equation estimate for `L(s,chi)`,
Plancherel, a Baker lower bound for the prime logarithms, and an Erdős--Turán discrepancy
bound. None is replaced by finite samples of partial sums.

For a stronger exponent or for nonprimitive `chi`, nonunit exceptional values, or an
infinite modification set, stop. Read [the exact source contract](references/aymone-chaves-ramos-omega-bound.md).
