# 工作流衔接

按用户本次目标取所需步骤，短任务不强制走完整链。

- **证明与计算**：固定数学对象 → 选方法技能 → 核对定理假设 → 用合适本机工具检查有决策价值的实例/边界/残差 → 完成数学论证并标明检查范围。
- **数值探路与认证**：保留精确模型 → 实际运行搜索 → 独立核对候选可行性 → 需要严格结论时转精确/区间证书及全域覆盖论证。阴性搜索不能证明不存在。
- **文献到论文**：`academic-literature-search` 或 `literature-search-download` 获取核验题录 → 需要翻译时用 `academic-paper-translator` → 用对应方法/专题检查适用范围 → `math-paper-writing` 写作，再按需用 `anti-defensive-writing` 精简表达；不把下载成功当作读完或证明完毕。
- **建模交付**：`math-modeling-audit` 核对真实模型与账本 → 只在请求范围内补做计算 → `matlab-plotting` 绘图 → `math-modeling-paper` 编排 → `math-modeling-delivery` 核对支撑包。

重复入口保留调用兼容：`mathematica-research` → `mathematica-math`，`literature-download` → `literature-search-download` 的按清单下载流程，`pdf-paper-translate` → `academic-paper-translator` 的 PDF 输入流程。旧流程中仍有用的专项说明留在各入口的参考资料中，不能覆盖用户当次选择。
