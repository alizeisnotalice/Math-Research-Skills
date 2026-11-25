# 两条精确对照递推

使用 [comparison_pairs.py](../scripts/comparison_pairs.py) 的 aptekarev 或 rivoal 分支。比较同一 n 下的逼近误差、清分母代价和约分后余项。这里的 p、q 保留原论文标度。

- Aptekarev 等，本机 EXT-0513，对应 [arXiv:0902.1768v2](https://arxiv.org/abs/0902.1768v2)，物理页 3 式 (8)–(9)。输入初值 (0,2,31)、(1,3,50)，从 n=2 开始求第 n+1 项。n=3 的对照整数是 (1209,2022)。误差可衰减而整系数余项的主阶仍带 (2n)!，用于检查将逼近误差与线性形式等同的错误。
- Rivoal，本机 G03，*Rational approximations for values of derivatives of the Gamma function*，物理页 4 Corollary 1(i)。初值 (−1,4,77/4)、(1,7,65/2)，从 n=0 开始求第 n+3 项。页 3–4 Theorem 1 给出 n!² 的整数化系数。针对原作者稿的更强整性猜想，若需要使用后续结果，单独匹配定理与归一化。相关论文中出现的 log x 只在 x=1 消失。
