# 精确分母单纯形舍入

## 可复用构件

给定有理概率向量 \(w\in\Delta_d\) 和正整数 \(D\)，令
\(q_i=\lfloor Dw_i\rfloor\)，按小数部分从大到小选出
\(r=D-\sum_iq_i\) 个坐标并各加一。小数部分相同时选较小的零起始索引。输出
\(x_i=\widehat q_i/D\)。

精确整数除法保证 \(0\le r<d\)、\(\sum_i\widehat q_i=D\)，所以
\(x\in\Delta_d\cap D^{-1}\mathbb Z_{≥0}^d\)。逐坐标误差不超过 \(1/D\)，故
\(\lVert x-w\rVert_1\le d/D\)。这是独立的有限算术论证。

## 来源与范围

Google Cogentic《An Exact Polynomial-Time Algorithm for 1/5-Approximate Nash
Equilibria in Bimatrix Games》，本机原件 SHA-256
`ed65664e8817e323a1613f95f4fc98689719c86fb2708974bb69cc1edc139485`，物理第 5--6 页
Lemma 2.1(b) 给出了同一构造。该原件的 Section 2.2 至 Section 5 进一步声称一个全局
\(1/5\)-近似 Nash 算法，本构件不依赖也不验证该主张。

## 可执行核验

运行 `scripts/simplex_denominator_rounding.py --self-test`。该自检穷举维数 1--5、源分母
1--7、目标分母 1--7 的有理单纯形格点，逐例核对单纯形条件和严格有理 \(\ell^1\) 界，另核对
等余数的索引决议。输入示例见 `examples/simplex-rounding-tie.json`。
