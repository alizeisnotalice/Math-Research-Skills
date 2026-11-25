# 类型配置与实物配置

给定物品尺寸 \(a_i\in(0,1]\)、容量 1，把每个尺寸及其输入份数 \(b_a\) 保留下来。

- 数值类型配置为整数向量 \(c\ge0\)，满足 \(\sum_a a c_a\le1\)。每一列可有 \(c_a>b_a\)。要求加权列在类型 \(a\) 的覆盖质量至少 \(b_a\)。
- 实物配置是物品索引集合，索引不可重复，每列总尺寸至多 1。每个索引的分数覆盖至少 1。

逐类型汇总每个实物列，得到可行的类型解，故两值满足 \(\mathrm{OPT}_{\rm type}\le\mathrm{OPT}_{\rm ind}\le\mathrm{OPT}_{\rm integer}\)。若附加限制 \(c_a\le b_a\)，则有界类型配置 LP 与实物 LP 等价。反向从每个类型列独立均匀选该类型的 \(c_a\) 个实际副本，把列权按各选法分摊。每个类型为 \(a\) 的实际副本得到该列权的 \(c_a/b_a\) 倍覆盖，所以所有物品约束成立，目标权重总和保持。

精确例子是输入只有一件大小 \(1/3\) 的物品。无份数限制的类型 LP 给三份同型物品的列权 \(1/3\) 即可。其目标不能更低，因每列最多含三份。实物 LP 中含该件物品的唯一非空列权至少 1。若所有尺寸严格大于 \(1/6\)，每个有效实物列最多五件。改变严格性时重查此枚举范围。用已选配置约定生成及验收证书，避免混用两个不同的下界。

来源为 OpenAI 预印本，PDF 1–2 页，式 (1.1)–(1.2) 的两种模型；这里只使用配置定义。SHA-256 cf1e9b383ad38a1c6b8d0117e1e6f485a482480d05471d11de02c81020cbb9e6。[Additive hardness and unbounded configuration gaps in bin packing](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf)
