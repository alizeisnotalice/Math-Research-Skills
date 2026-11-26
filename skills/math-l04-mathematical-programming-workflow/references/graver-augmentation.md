# 有限整数盒的 Graver 增广证书

用于已有可行整数点 \(x\) 的问题 \(\min\sum_i f_i(x_i)\)，约束为 \(Ax=b,\ \ell\le x\le u\)，向量界均为有限整数。输入给出候选的带符号整数核方向 \(g\)。核对 \(Ag=0\)，再逐坐标求可行整数步长上界。脚本接受可分离凸二次目标，或用离散二阶差分检查逐坐标整数值表。

## 整数线搜索与全局证书

- 记 \(\phi(t)=\sum_i f_i(x_i+t g_i)\)。凸情形的相邻差分 \(\phi(t+1)-\phi(t)\) 非降。查找第一个非负差分，得到盒内最优整数步长。输入值表未通过凸性检查时，程序改用有限线枚举。
- 若方向表包含 \(A\) 的完整 Graver 基，对每个符号兼容分解的方向段，都能从当前点在盒内走对应整数步长。可分离凸性的增广不等式确保有更优可行点时，至少一个方向段严格改进。因此凸目标且方向基完整时，停止可认证最优性。
- 运行结果报告本次提供的方向中有无改进。若完整性待核，小盒上可选择独立穷举，并对照确切最优值。达到迭代上限时需要检查剩余方向。

## 调用

~~~sh
python3 scripts/graver_augmentation_certificate.py --self-test
python3 scripts/graver_augmentation_certificate.py examples/graver-augmentation-positive.json --exhaustive
python3 scripts/graver_augmentation_certificate.py examples/graver-augmentation-incomplete-directions.json --exhaustive
~~~

JSON 字段为 `A`、`b`、`lower`、`upper`、`x`、`directions`、`objective`。二次型为 `type=separable_quadratic`、逐坐标 `quadratic` 和 `linear`。值表为 `type=separable_values` 及以各整数的十进制字符串为键的 `tables`。含符号方向逐条输入。完整方向例得到 \(x=(1,2,1)\)、目标值 \(-6\)。不完整方向例在 \(-4\) 停止，同一整数盒穷举仍为 \(-6\)。

## 原文

Shmuel Onn，*Theory and Applications of n-Fold Integer Programming*，*Mixed Integer Nonlinear Programming*，2012，pp. 559–593。本机 arXiv:0911.4191v2 原件 SHA-256 `ef567e72f815df404c1fea57e50c92b4fc4f8196634dd6cf86d19ee5f2cdec33`。物理页 16–23 为共形分解、Lemma 3.6 的二分、可分离增广与 Theorem 3.11。物理页 28–32 的多项式构造要求固定双矩阵的 n-fold 结构。此脚本的输入是方向表，完成有限增广和证书回放。 [原稿](https://arxiv.org/abs/0911.4191v2) · [正式章节](https://link.springer.com/chapter/10.1007/978-1-4614-1927-3_20)
