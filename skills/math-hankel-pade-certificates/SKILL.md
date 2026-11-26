---
name: math-hankel-pade-certificates
description: 对整数幂级数做精确 Hankel 行列式与 Padé 有限证书，核验正矩投影的有理下界，并审计 Mahler–Hankel 定理的独立准入门槛；不以有限计算断言超越性或无理度指数。
---

# Hankel–Padé 有限证书

用于研究整数系数幂级数 `f(z)=sum c_j z^j` 的 Hankel 行列式和 `[k-1/k]` Padé 逼近，尤其适合审计 Bugeaud–Han–Wen–Yao 的 Theorem 2.1 可否使用。先固定幂级数从 `c_0` 起的索引；不要把序列从 `c_1` 开始而未作平移。

运行 [scripts/hankel_pade_certificate.py](scripts/hankel_pade_certificate.py)，输入和输出均为 JSON；它只使用 Python 标准库的 `Fraction`，因此输出的行列式、分子、分母和余项首项均为精确有理数。

```sh
python3 scripts/hankel_pade_certificate.py examples/positive-catalan.json
python3 scripts/hankel_pade_certificate.py examples/ineligible-singular-hankel.json
```

`positive-catalan.json` 给出一个通过有限 Hankel–Padé 回放的正例；它**不是** Theorem 2.1 的结论实例。第二个例子精确显示一个二阶 Hankel 行列式为零，故不能作为该阶 Padé 证书的起点。

## 有限证书

输入 `order=k` 与 `later_order=ell`（`ell>k`）。程序会：

- 计算 `H_k`、`H_ell`，并从 `k` 到 `ell-1` 找最小的非零边界行列式 `H_{k,k_prime}`；
- 解归一化条件 `Q(0)=1`，构造 `deg P<=k-1`、`deg Q<=k` 的 `[k-1/k]` Padé 分式；
- 逐项复核 `Qf-P` 在 `z^(k+k_prime)` 前为零，并复核其首项是 `H_{k,k_prime}/H_k`。

这只是被给定的有限系数前缀蕴含的证书。`H_ell != 0` 和上面的边界行列式是 Theorem 3.1 的有限部分；它们不提供无限多个非零 Hankel 行列式。

## Theorem 2.1 的准入审计

原论文的 Theorem 2.1 有三个不能互相替代的全局前提。读 [references/source-and-scope.md](references/source-and-scope.md) 后分别记录证据：

1. `f=A/B+C f(z^d)` 是在形式幂级数（并且在单位圆内收敛）的已证明恒等式，系数为整数；
2. 有已证明的递增无限序列 `n_i` 使 `H_{n_i}!=0` 且 `n_(i+1)/n_i -> 1`；
3. 对所选整数 `b>=2`，`B(b^(-d^m)) C(b^(-d^m)) != 0` 对每个 `m>=0` 成立。

在 JSON 的可选 `theorem_2_1` 段填入 `B`、`C`、`d`、`b` 和 `nonvanishing_prefix`，脚本会精确审计有限个 `m`。无论前缀多长，输出都会标为 `finite_prefix_only`；函数方程和无限子序列必须由独立证明材料承担。不要从“没有发现零点”、浮点近似或有限 Hankel 表推出定理的结论。

输入格式及原文定位见 [references/source-and-scope.md](references/source-and-scope.md)。

## 正矩的行列式整化

若输入来自有限正测度的矩，另用 [Zudilin 正矩整化与容量检查](references/moment-hankel-irrationality-gates.md)。逐项核对无穷支撑、分母整除链、分母增长及容量衰减，再判断是否产生严格的无理性证书。

## 正矩投影下界

当目标值是未知的零阶矩、其余所需矩可精确计算时，用 [正矩投影的 Hankel 比值](references/hankel-projection-bounds.md) 求下界。对 γ、Euler–Gompertz 常数及 ζ(k) 可直接运行。报告有限的 Gram 子式检查和所用解析收敛条件。

## 齐次 Mahler 方程的单步间隙

若前置论证已认证 Laurent 连分式的相邻分母次数，用[Mahler 间隙转移](references/badziahin-mahler-gap-transfer.md)做有理多项式约分，核对新间隙的端点和严格增长条件。

## 补充来源的方法

- [Finite rationality test for a Mahler function](references/mahler-function-transcendence-admission.md)

## 补充来源中的方法

- [Hecke--Mahler sparse finite-difference audit](references/hecke-mahler-sparse-difference.md)
