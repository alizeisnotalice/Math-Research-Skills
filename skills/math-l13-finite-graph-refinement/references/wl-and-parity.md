# 元组颜色和奇偶同态

## 共同颜色表

对两个显式有限简单图，在各自 \(k\)-元组上建立共同的颜色字典，\(k\ge2\)。初始签名保留所有坐标的相等及邻接关系。更新签名保留旧色，再计算所有替换：

- 联合约定中，同一个顶点 \(z\) 在每个坐标的 \(k\) 种替换产生一个颜色向量，然后对 \(z\) 取**向量多重集**。
- 分离约定中，每个坐标独立取替换颜色的多重集。侧重同一 \(z\) 的相关性时，两种约定可能把元组分得不同。

替换仅在元组所属图内进行。在两个表上共同编码完整签名，逐轮比对直方图。有旧色在，任何新分裂使共同类数增加。若某轮无分裂，只是对共有类作双射重命名，下一轮也无分裂。两图阶数同为 \(n\) 时，最多 \(2n^k\) 轮可确认稳定。若 \(k\ge n\ge2\)，初始颜色直方图相同已足以给同构：取含全部顶点的一个元组，匹配的颜色记录了对应顶点的完整相等与邻接。若图阶是 0 或 1，直接比对。经过联合更新稳定后，两个同色元组的向量多重集相同，可按向量分组构造**一个**共同的替换顶点双射。按每个坐标单独配对不能代替这个证书。

## 固定投影的奇偶提升计数

设每个目标基础顶点 \(u\) 有模板类型 \(a(u)\)，给每种邻接类型一个二元标签。固定一个源图到基础图的同态 \(\varphi\)，保留每个源顶点自己的标签变量。各顶点实施规定奇偶，各源边实施彼此对应坐标相同。这是 \(\mathbb F_2\) 上线性方程组 \(M z=b\)。对同一 \(\varphi\)，零右端提升数为 \(2^{d-\operatorname{rank} M}\)，有非零右端时为同样大小的仿射陪集或零。一个左零空间向量与 \(b\) 配对为 1 是不相容证书。不同源顶点即使投到同一 \(u\)，仍只按边和奇偶方程关联，不应强制它们共用变量。

有限复跑用六边形与不交的两个三角形。在 \(k=2\) 时，分离约定接受、联合约定区分。另对三角形的恒等投影，零奇偶有两个提升，只扭一个顶点的奇偶无提升。运行随附 Python 精确检查。已引用手稿的归约、复杂度与最小维数结论另有证明义务。

- OpenAI 预印本 PDF 8 页，Lemma 3.2 固定投影。SHA-256 742b4b63acfcfeec728427c388b0704c5e152f79cd9a8b5e9d16573fcb8177e7。[Parity lifts and bounded-treewidth witnesses for Weisfeiler–Leman equivalence](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Parity-lifts-and-bounded-treewidth-witnesses-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf)
- OpenAI 预印本 PDF 5 页，联合稳定类的顶点匹配。SHA-256 24d7566f85bda8e9102c44c82a29a47781c6204964ea8076aac0b109b450c3d5。[The complexity of identifying a graph by Weisfeiler–Leman refinement](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-complexity-of-identifying-a-graph-by-Weisfeiler-Leman-refinement-September-25-2026/paper.pdf)
- OpenAI 预印本 PDF 2–4 页，联合与分离约定及固定维数输入。SHA-256 5d58d0f7cee1b9ed468a083efaf94357885e251b203171139132d1643960c904。[Unconditional time lower bounds for Weisfeiler–Leman equivalence](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Unconditional-time-lower-bounds-for-Weisfeiler-Leman-equivalence-September-25-2026/paper.pdf)
- OpenAI 预印本 PDF 5–6 页，Lemma 2.2 与共同颜色表。SHA-256 5b3048ce062b1b8eb520ebf476284b7ebe1b2a65ffc3d7977e5f18cb62d82dc8。[Variable-dimension Weisfeiler–Leman equivalence on general and subcubic graphs](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Variable-dimension-Weisfeiler-Leman-equivalence-on-general-and-subcubic-graphs-September-25-2026/paper.pdf)
