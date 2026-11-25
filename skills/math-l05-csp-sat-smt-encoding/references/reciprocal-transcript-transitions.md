# 分阶段互反的局部证书

状态标记为公开阶段与已填位置和内容。每一步的读写地址由阶段和固定规格给定。前向写入的值由保留数据唯一决定。后继若有效，反向擦除应恢复唯一空符号及占用标志。若前向擦除的是计算前缀末端，后继要保留重算它的全部数据，反向补回同一值。对拷贝阶段，整份未动的带提供重算值。循环阶段还要逐个核对回绕边界。

将提案动作与有效性测试分开。在每个动作定义域的有效起点，只验那些可能因本次写入改变的条件，其余条件应由不变量维持。只有两个端点同时有效且正向提案得出该后继时才建边。若在这些有效端点上证明前后提案互逆，则图的出入度均至多一。公开阶段变更可以单独排除自边。端点性质、非孤立性和从手稿的其它归约得到复杂度的步骤需要另外证明。

- OpenAI 预印本 PDF 12 页，Lemma 2.4 的局部互反与有效性条件。SHA-256 a7ab4d86183890be9bfaa845f2c0eddf4ba89956911fc8318c47ac35f504e84b。[The PCP-for-PPAD conjecture: a quasilinear reduction](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-PCP-for-PPAD-conjecture-a-quasilinear-reduction-September-25-2026/paper.pdf)
