# 有限 Hofstadter 递推与比较

本入口采用的对象是 \(F_k(0)=0\) 与 \(F_k(n)=n-F_k^{\circ k}(n-1)\)。在有限前缀中，内层迭代的每个索引已经出现，因此整数递推无需浮点计算。

Pierre Letouzey，*Re-Ordering the Generalized Hofstadter Functions G, H, and Beyond*，本机 arXiv:2610.35994v1，SHA-256 `761786f28779fd36cc39acc25083d721b63b66d4af99c994c48872e4914529e4`。物理页 2 定义 \(F_k\)，陈述 \(F_k(n)\le F_{k+1}(n)\) 与 \(n>12(k+1)(k+6)\) 时的严格不等式。物理页 3--4 报告无公理 Rocq 验证及入口文件。有限脚本仅重放定义和给定范围的比较，未编译该形式化项目，也不以样本代替全称定理。
