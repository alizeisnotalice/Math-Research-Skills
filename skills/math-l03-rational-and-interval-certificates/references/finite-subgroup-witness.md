# 有限群的成员与非成员见证

给定群元素 \(g,h\)，成员证书是一个明确的 \(x\) 及恒等式 \(g^x=h\)。非成员证书是正整数 \(E\)，满足 \(g^E=1\) 且 \(h^E\ne1\)。若 \(h=g^x\)，则 \(h^E=(g^E)^x=1\)，因此第二种证书严格排除成员关系。证书条件失败时，仅说明所给指数未认证该结论。在非循环环境中还可能不存在这种单指数证书。

[有限模群脚本](../scripts/check_cyclic_group_certificates.py) 接受整数模数 \(M\ge2\)；先核对 \(g,h\) 均为模 \(M\) 的单位，再做精确幂模运算。

```sh
python3 scripts/check_cyclic_group_certificates.py member 17 4 16 2
python3 scripts/check_cyclic_group_certificates.py nonmember 17 4 3 4
python3 scripts/check_cyclic_group_certificates.py nonmember 17 4 3 2
```

前两次分别认证成员与非成员，第三次因 \(4^2\not\equiv1\pmod{17}\) 而未认证。以上检查要求给出指数。来自 Cogentic 固定版本的离散对数稿，物理页 1–3 的任务与输出约定。有限域扩张需另供应正确的域运算，论文的搜索及复杂度假设在[论文索引](../../math-research/references/google-cogentic-2026-11-25.md)单独登记。
