# 匹配奇偶路径与见证恢复

输入是有限无自环无向图，边有独立身份，允许平行边。若有孤立顶点且要求覆盖所有顶点，它直接给出失败证书。

对度数 r≥1 的顶点，用含 2r−1 个点的路径替换，依次把 r 条外部关联边接到从 1 起算的奇编号。新图最大度三。任何新图的完美匹配都需让每个偶编号点与某个奇编号点内部配对。共有 r−1 个偶编号点，因此恰一个奇位置使用外接边。这让保留的原边组成原图完美匹配。反向给定原图完美匹配，其对应奇编号点用于外接边，两边剩下的路径长度为偶数个顶点，各自内部配对即可。度数 1 的替换体只有一个点。

对所有原顶点保存关联边 ID。若原图有 v 个顶点和 e 条边，替换顶点共 4e−v 个，线性总规模。本机穷举四个标号顶点的 64 个简单图，逐一核对完美匹配的存在性及替换前后的等价。此构造是见证保持的预处理，运行时间不利用原文的匹配主算法。

OpenAI 预印本 PDF 77 页，Lemma 9.3。SHA-256 3cce6ec72ecade6973049c2b7bfd6bbac378f10e0dfdc303af666271bbb60959。[Almost-Linear-Time Maximum-Cardinality Matching in General Graphs](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/main.pdf)
