---
name: math-m04-measurable-supremum-selection
description: 处理可测上确界、解析投影和可测选择，核对参数空间、可测性及选择器范围。
---

# M04 · 可测上确界、解析投影与合法选择器

> **当前核验范围（2026-10-07）：** 本 Skill 仍属于 L–N 组进行中的审核；逐条数学与能力状态记录在完整交付包的 `audit_current/ln/claims.json`，案例定义记录在 `audit_current/ln/cases.json`；单独安装目录不包含这两份包级账本。请按 [`references/portable-audit-access.md`](references/portable-audit-access.md) 通过 bundle-root resolver 访问。以下限定只陈述已绑定账本的证据边界，不代表整项验收完成。

> 便携文献定位见 [本 Skill 证据索引](references/handoff-evidence-index.csv)。若需读取包外 PDF，以数据包根目录为 `EVIDENCE_ROOT`，按索引中的相对路径定位。

> **本项边界：** 账本 M04-SEL-01 只核验五个参数点上的有限选择器；M04-BOUNDARY-01 是删除可测性假设后唯一选择器不可测的解析边界论证。一般可测最大值/选择定理、解析投影及 API 仍未完成证明或运行核验。

## 输入与产出

可测参数空间、可行多值映射、图像/逆像可测性、目标函数可测或 Carathéodory 条件、紧性与可积性。

产出应包含适用性判断、使用的假设、数学步骤、证书或界的方向、常数依赖，以及尚未解决的缺口。

## 执行步骤

1. 写清各个 sigma-代数，并按所用定理的精确图像或逆像条件核验多值映射可测。
2. 在调用可测最大值定理前，检查值集非空紧，以及目标函数的可测性或 Carathéodory 正则性。
3. 在对应投影/选择定理的假设下，证明上确界或值函数可测。
4. 只有 argmax 多值映射满足定理假设时才构造可测最大化选择器，并逐点验证可行。
5. 需要 Borel 仿射主控时，使用 Clerico 的限域结果。核对标准 Borel 参数空间、有限维 Borel 值域、上半解析目标以及逐点存在的有限仿射主控。一般 argmax 仍须按步骤 1–4 核对。
6. 对条件上确界，区分最小可测上包络与由某个索引达到的最大值；增序列可交换的结论不得推广为降序列或任意极限。
7. 引用积分兼容选择定理时逐项区分标量HK、HKP和Banach范数Henstock可积；P-a594 Theorem4.3的HK statement/HKP proof差异与积分选择集合闭包必须显式保留，不认证strongHK。

## 证据与失败处理

逐点存在、光滑有限维选择定理或值集紧本身，不足以在缺少图像可测性等条件时得到可测选择器。 条件本质上确界不保证索引达到；HKP不等于强HK，积分选择集合闭包不可在OCR中丢失。

引用定理前按 [来源与阅读状态](references/provenance.md) 定位版本和证据。只有预印本支持的陈述须核对实际依赖的结论、证明步骤和假设。来源或适用范围未核实时，保留已独立推导的部分，并将相应陈述留作研究线索。
需要完整步骤时读 [方法说明](references/method.md)。只有当前请求明确涉及对应的中心立方体研究任务时，才使用 [历史课题接口](references/cube-interface.md)，并先复核当前问题与该接口的假设。
遇到定义缺失、条件不满足或来源未核验，指出具体缺项，保留可证明的弱结论。不得将迁移推断写成原文定理。
依赖表提供方法路线，不表示所有工具之间存在无条件定理蕴含。

用 [适用案例](examples/positive.md) 与 [条件缺失案例](examples/negative.md) 检查适用边界。

## 有理单纯形上的局部仿射选择

给定顶点、对应值和严格内部点时，用[仿射选择证书](references/local-affine-simplex-selector.md)认证重心坐标及选值。提供凸图的有理半空间表可核验图成员关系；仅声明凸图时输出为条件式。

## OpenAI 原稿中的方法

- [Borel relation compression interface](references/openai-borel-cost-compression-wave4-spectral2.md)
