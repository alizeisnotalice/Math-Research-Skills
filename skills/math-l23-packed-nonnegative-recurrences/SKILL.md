---
name: math-l23-packed-nonnegative-recurrences
description: 核验用单个自然数的定宽数位计算非负整数递推。用于移位叠加、模截断、分拆表及逐字段进位检查。
---

# 非负整数递推的定宽打包

给定长度 \(n+1\) 的非负整数行 \((x_0,\ldots,x_n)\)。将行编码为
\[
 R=\sum_{i=0}^n x_i B^i,\qquad B=2^w.
\]
读取第 \(m\) 个字段时，右移 \(mw\) 位再取低 \(w\) 位。输入字段与每个保留的输出字段均须小于 \(B\)。

## 移位叠加

若第 \(k\) 行到第 \(k+1\) 行是已知非负整数核的截断卷积
\[
 y_m=\sum_{j=0}^m c_jx_{m-j},\qquad c_j\in\mathbb Z_{\ge0},
\]
可计算
\[
 R'=\left(\sum_{j=0}^n c_j B^j R\right)\bmod B^{n+1}.
\]
证明先把式中的整数当作以 \(B\) 为变量的多项式展开。余数丢掉所有次数大于 \(n\) 的项。只要保留的系数 \(y_0,\ldots,y_n\) 都小于 \(B\)，这部分已是规范数位，无进位传播。非负性保证每一部分和也受到同一字段界控制。

位宽必须对全部保留字段，在所需行范围统一成立。试算最大的已见字段不足以给更大输入的证明。若有负权、借位、额外压缩或非标准移位，先证明相应表示保持。复杂度要按所用整数长度和计算模型计费。

## 整数分拆实例

只允许不超过 \(k\) 的正部件，令 \(p_k(m)\) 是总和为 \(m\) 的分拆数。令 \(p_0(0)=1\)，其余 \(p_0(m)=0\)。第 \(k\) 行由上一行位移 \(0,k,2k,\dots\) 后叠加，恰按部件 \(k\) 的重数划分。论文用
\[
 p_k(m)=p_{k-1}(m)+p_k(m-k)\quad(m\ge k)
\]
通过双层归纳得 \(p_k(m)\le2^{m+k}\)。因此计算 \(0\le k,m\le n\) 时，可取 \(w=2n+1\)。

对这个实例，还有独立的计数界。对 \(m\ge1\)，先将各部件按大小排序，再作为一个有序组成。该映射为单射。用 \(m-1\) 个间隙是否断开编码所有组成，得到 \(p_k(m)\le 2^{m-1}\)。故可取 \(w=\max(1,n)\)。这里用到了分拆的组合意义，需要另证才可套到其他递推。

运行 [本机精确回放](scripts/check_packed_partitions.py)。它逐行比较普通整数表和打包表，并用不足位宽演示进位错误。来源只采用第 4–6 页的编码、式 (8)–(9)、Peeling Lemma 与位宽证明。Lean 内核计费与论文报告的性能仍由其原环境和验证命令决定。

Amey Thakur，*A Whole Table Row in One Natural Number: Kernel-Checked Dynamic Programming with a Proved Width Bound*，作者公开稿，2026-11-11。本机 SHA-256 为 4d6280e746446fdd750538dc4bb456c3aa7ebe16856669f1f48f55b124852f72。外部链接是作者仓库入口，本机版本用哈希和日期固定。[作者原文入口](https://github.com/Amey-Thakur/SAIR-FOUNDATION-FOR-SCIENCE-AND-AI-RESEARCH/blob/main/papers/V-lean-kernel.pdf)
