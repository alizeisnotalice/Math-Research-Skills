# 全二叉协议树的叶数平衡证书

## 来源与版本

构件来自 Google Cogentic 的 *Breaking the Square-Root Barrier for the Log-Rank Conjecture*，本机原件
`05_logrank_conjecture.pdf`（SHA-256
`9c941a918c5e5cea1624adee676c010efb85b60b3cd77455640cd578f54f6bc9`），物理 PDF p. 35，
Appendix Proposition A.3 的首段。对应 Google Research 固定提交为
`4a7bc8ab0bc7`。这是在该命题的“每个有限 Boolean 矩阵都有统一密度的单色矩形”条件之后使用的
有限协议树转换步骤，不是该条件的证明。

## 精确有限命题

设 \(T_0\) 是有 \(L\ge2\) 个叶的根全二叉树。沿着叶数严格大于 \(2L/3\)
的子节点向下走。抵达内部节点 \(u\) 时，其较大子节点 \(v\) 满足
\[
L/3<L_v\le2L/3,\qquad 1\le L-L_v<2L/3.
\]
沿途叶数严格递减。停止时 \(u\) 的叶数仍大于 \(2L/3\)，其较大子节点至少含其中一半的叶。
脚本以 \(3L_v>L\) 和 \(3L_v\le2L\) 检查这一步。

若原树是有效的一比特 Alice/Bob 协议树，节点 \(v\) 对应矩形 \(A_v\times B_v\)。
双方各发送一个成员比特。在该矩形运行 \(v\) 的子树。对其余三个矩形，保留原树在 \(u\)
之外的节点，并以 \(v\) 的兄弟子树替换 \(u\) 处的子树。两类分支至多有 \(2L/3\) 个叶，
强归纳给出 \(D_{\mathrm{cc}}(M)\le2\lceil\log_{3/2}L\rceil\)。
脚本用 \(3^d\ge L2^d\) 求最小整数 \(d\)，调用者负责核对协议和矩形语义。

## 可执行核验

输入是仅含 `tree` 的 JSON 对象。叶为 `null`；内部节点必须恰有 `left`、`right` 两个字段。这个刻意
狭窄的格式只表达树形状，避免误把未给出的协议语义当作已核验。

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_protocol_tree_balancing.py examples/seven-leaf-skew.json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_protocol_tree_balancing.py examples/not-full-binary.json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_protocol_tree_balancing.py --self-test
```

第一个示例有 7 个叶，输出的选择子树有 4 个叶，属于 \((7/3,14/3]\)；第二个输入应以退出码 2
拒绝非全二叉树；自检穷举 2--10 个叶的全部 6,917 个有序全二叉树形状。

## 与现有技能的路由和边界

用 `check_rank_halving_tree.py` 核对给定树的矩形分割及叶单色性，再调用本脚本计算叶数划分和整数深度界。
需要由调用者保留所选 `parent_path` 到实际协议节点／矩形的映射；本脚本不检查该映射。

它不验证该树是 Alice/Bob 1-bit 查询协议，不验证叶矩形单色，不搜索单色矩形，也不证明对所有
秩 (\le k) 的矩阵都存在密度下界。因此不能单独推出 Proposition A.3 的通信复杂度结论，更不能
独立认证该稿 Theorem 1.1、其高秩结构定理或尚未交付的 Lean 形式化。
