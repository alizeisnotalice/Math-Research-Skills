---
name: math-l03-rational-and-interval-certificates
description: 构造或核验区间算术、有理对偶与证明型数值证书，检查舍入和全域覆盖。
---

# L03 · 区间算术、有理对偶与证明型数值

> **当前核验范围（2026-10-07）：** 本 Skill 仍属于 L–N 组进行中的审核；逐条数学与能力状态记录在完整交付包的 `audit_current/ln/claims.json`，案例定义记录在 `audit_current/ln/cases.json`；单独安装目录不包含这两份包级账本。请按 [`references/portable-audit-access.md`](references/portable-audit-access.md) 通过 bundle-root resolver 访问。以下限定只陈述已绑定账本的证据边界，不代表整项验收完成。

> 便携文献定位见 [本 Skill 证据索引](references/handoff-evidence-index.csv)。若需读取包外 PDF，以数据包根目录为 `EVIDENCE_ROOT`，按索引中的相对路径定位。

> **本项边界：** 账本 L03-RAT-01、L03-LP-WD-01、L03-CONE-WD-01 分别覆盖有理端点平方比较、有限维 LP 弱对偶、锥对偶弱对偶。L03-API-01 仍未验证任何带向外舍入保证的浮点区间库；不能声称通用区间 API 已测试。

## 输入与产出

精确数学主张、可用的有理输入、浮点候选、区间/对偶证书格式及舍入约定。

产出应包含适用性判断、使用的假设、数学步骤、证书或界的方向、常数依赖，以及尚未解决的缺口。

## 执行步骤

1. 写明需要认证的符号或不等式，并将其改写成方向明确的残差。
2. 有理输入优先用精确算术。若用区间，先依据 [数学工具引导](../math-tool-router/SKILL.md) 确认本轮实现对每种所需操作都保证向外舍入，并包住输入误差。核对最终区间在所需方向上不含零。
3. 对 LP 或锥规划，同时给出原问题可行见证与对偶可行见证，并精确核对目标间隙。
4. 把启发式搜索和证书核验分开，保存足以复现的位数或有理数据。
5. 若区间跨过零，或求解器状态没有可行见证，就报告尚不能判断，而不是证明成立。

核对已给出的幂等式与有限群的子群成员证书时，读[有限群见证](references/finite-subgroup-witness.md)。

## 无限系数表的存在性与误差

用有限表近似无限插值方程时，读[有限块与无限尾部逆证书](references/finite-tail-inverse.md)。分别认证有限逆、尾部算子范数和残差包围。

## 分段一维 ODE 残差证书

若未知函数 `u` 满足 `u''+b u'-c u=0`，且有逐段有理多项式近似 `v`，可用[分段 ODE 残差证书](references/piecewise-ode-residual.md)认证 **函数值** 误差。逐段精确检查残差、`c>=mu>0`、`C1` 拼接和外部给出的两端误差界 `B` 后，最大值原理只给出 `||u-v||_infinity <= max(B,rho/mu)`。

使用[精确 Bernstein 检查器](scripts/check_piecewise_ode_residual.py)时，输入多项式以局部单项式有理系数给出；它将其精确转换到 Bernstein 系数以包围每段的 `c` 和残差。该程序不验证未知解的端点误差，也不输出导数误差。

导数界必须另给一阶误差方程、一个锚点（或边界）界及实际积分因子界；正零阶系数和函数值最大值原理本身不能推出 `||u'-v'||`。不要把本节用于非线性方程、弱解、非 `C1` 拼接或未认证端点数据。

## 取整时的二进制 Newton 证书

用定向二进制舍入算倒数或平方根，并恢复精确商或整数平方根时，按[变精度 Newton 与最终整数检查](references/dyadic-newton.md)核对归一化、保护位与最后一步的精确检验。

## 证据与失败处理

小数区间很窄并不等于经过认证；必须保证向外舍入并包住输入误差。原/对偶界的方向还取决于优化方向。

引用定理前按 [来源与阅读状态](references/provenance.md) 定位版本和证据。只有预印本支持的陈述须核对实际依赖的结论、证明步骤和假设。来源或适用范围未核实时，保留已独立推导的部分，并将相应陈述留作研究线索。
需要完整步骤时读 [方法说明](references/method.md)。只有当前请求明确涉及对应的中心立方体研究任务时，才使用 [历史课题接口](references/cube-interface.md)，并先复核当前问题与该接口的假设。
遇到定义缺失、条件不满足或来源未核验，指出具体缺项，保留可证明的弱结论。不得将迁移推断写成原文定理。
依赖表提供方法路线，不表示所有工具之间存在无条件定理蕴含。

用 [适用案例](examples/positive.md) 与 [条件缺失案例](examples/negative.md) 检查适用边界。

将已核验的周期积分不等式转到有限均匀网格时，按[周期网格与分母误差](references/periodic-grid-transfer.md)保留导数界及正分母下界。

## 模整数的线性关系

给定完整的有限矩阵关系时，调用[模整数线性消元](references/modular-unimodular-relations.md)，用 Bézout 行操作寻找可逆主元，并检查消元后的多余行及原始方程残差。

若关系来自一个已经给定的有限循环单位群，且需要同时核对群等式与由满张成关系推出的指数，读[有限循环关系证书](references/cogentic-cyclic-relation-certificates.md)。检查器要求每个群元素的指数模数幂为一，逐条复算关系，再执行模线性消元并复算结论幂等式。

## 散度型方程的精确残差修复

给定一维有理多项式与非零 jet 时，用[修复证书](references/divergence-residual-repair.md)核验散度残差抵消与修正系数的 Bernstein 正性。
