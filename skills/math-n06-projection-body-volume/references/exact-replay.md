# 单纯形比较的精确复现

令 \(T_d=\operatorname{conv}(0,e_1,\ldots,e_d)\)。原文计算
\[
|T_d|=\frac1{d!},\qquad
|\Pi T_d|=\frac{d+1}{((d-1)!)^d}.
\]
所以分母确实取 \(|T_d|^{d-1}\) 时
\[
R_d(T_d)=\frac{(d+1)/((d-1)!)^d}{(1/d!)^{d-1}}
=\frac{(d+1)d^d}{d!}=:c_d.
\]

对 \(T_{10}\times T_{10}\)，多面体直积公式给出
\[
\frac{R_{20}(T_{10}\times T_{10})}{c_{20}}
=\frac{c_{10}^2}{c_{20}}
=\frac{121\binom{20}{10}}{21\,2^{20}}
=\frac{5\,588\,869}{5\,505\,024}>1.
\]
本机 Python 的实际有理数复现为

```python
from fractions import Fraction
from math import factorial

def simplex_ratio(d):
    return Fraction((d + 1) * d**d, factorial(d))

ratio = simplex_ratio(10) ** 2 / simplex_ratio(20)
assert ratio == Fraction(5_588_869, 5_505_024)
assert ratio.numerator > ratio.denominator
```

输出比例约为 `1.0152306329636347`，而严格性由分子减分母 `83845` 承担。浮点输出不是严格不等式的证书。

该计算与单纯形投影体的几何推导见同一固定版本 PDF 第 4--6 页 Proposition 5 与 Theorem 1。源文件 SHA-256 为 `1d2211bb8d175f40fb55554586f02538fc9f4c04ecdc9793999a6f7ec514720a`。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/paper.pdf)
