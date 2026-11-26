# 既有技能的来源复核

复核以共享盘上的原件及其 SHA-256 为准。下列改动只覆盖实际核对的定理和适用条件。旧附件统计用于定位历史来源。

## 可测选择

- Clerico，[arXiv:2603.19973v2](https://arxiv.org/abs/2603.19973v2)，SHA-256 `55ddb3291a49ef12137e7c9593f8b908e9e7afe198f16f4e99bb2830e7a2ddd2`。物理页 2，Theorem 1，要求标准 Borel 参数空间、有限维 Borel 值域、上半解析函数及逐点存在的有限仿射主控。Corollaries 2、4 另外保留各自的齐次或次梯度假设。
- Di Piazza–Sambucini，[arXiv:2507.19460v1](https://arxiv.org/abs/2507.19460v1)，SHA-256 `a594f1076246b51274f940f19c26438ad31c1633b2cc7ad90357dce75c78cda5`。物理页 8–9，Theorem 4.3 的文字与证明使用不同的可积性表述。保留标量可测、弱紧凸值集、选择积分集合闭包及外引假设。旧阅读卡的强 HK 与去闭包表述已收紧。
- Correa–Hantoute–López 的两篇上确界次微分论文只用于凸性、近活动集与闭包。Azouzi 等只用于有序条件上包络与单向极限。Messerschmidt 的连续选择仅是邻近方法。六个历史归属误配留作相关性复核记录。

## Cramér 型中偏差

| 来源 | 本轮采用的范围 |
| --- | --- |
| Fan–Grama–Liu，arXiv:1210.2198v3，SHA-256 53739dd293f0de1c466a278829271bd71c72b1e68af9504a9ae48a8cdab2dd83 | 核对原文 Theorems 2.1–2.2 与 Corollaries 2.1–2.4。所用鞅分支需要条件 Bernstein 与预测二次变差条件。较宽的 \(o(\sqrt n)\) 范围用于对数尾比，比例趋一须另外控制误差。 |
| Can–Pham，arXiv:1709.04267v2，SHA-256 650b110a482de2b217ed967a7cdcb0eed4c2ae7809a4d8ac6e49d3ed2ceae548 | 核对临界 Curie–Weiss Theorem 1.4。四次指数目标，\(n^{3/4}\) 标准化，定理闭区间与相对误差趋零开尺度分别记录。SymPy 精确验证 \(e^{t^4/12}p_2'(t)=t-11t^5/30+t^9/90\)，在 \(t=9\) 为 \(21415149/5>0\)。[期刊版](https://doi.org/10.1214/17-ECP96) |
| He，arXiv:2311.05409v1，SHA-256 318df19635ebf8e52c12d13ad29ed476599b17b9dffd9abe13932f1f452a1db6 | Theorem 1.4 是固定参数 iid 轨迹命中时间的对数 MDP。保留路径扩展、无命中约定及实际使用的外引条件。[预印本](https://arxiv.org/abs/2311.05409v1) |
| Fan–Hu–Liu，arXiv:2002.00310v1，SHA-256 90d38802ec47287e7d8eef5125d13c39bfb0b554b88230faed80ec3dfaf81026 | Theorem 2.1 和 Corollary 2.2 中 BPRE 的一致性变量是历史起点。用各自区间选择比例界或对数界。[期刊版](https://academic.hep.com.cn/fmc/EN/Y2020/V15/I5/891) |

统一的独立和或三角阵用法继续按所引用的定理核验。已复查的四个来源按独立和、鞅、临界相关模型或路径事件分别调用。

## 非局部 HJB 超解

Zhang–Zhang–Zhang，[arXiv:2410.22141v3](https://arxiv.org/abs/2410.22141v3)，SHA-256 `9873072d1f9301d32013e488954d90cbd9e4cc0885936f7101fde9bc7e5bf82f`。物理页 4–6 的结果限于带两类独立对称加性稳定噪声的有限时域快慢模型。原文区分先取控制上确界再积分与先平均再优化，后者需要另证。展示的 (4.49) 与 Theorem 2.2 的速率差异以及 (4.48) 的终端层迁移仍待检查。

技能已补充从 PDE 残差通往随机价值界的具体前提。使用受控过程时，分别核对可采纳控制、扩展生成元、跳跃 Itô 的局部化与取极限依据、终止收益的可积性及支配关系。五份邻近原件中，扩散的随机 Perron 方法提供比较参考，确定性、时滞、均值场及平稳模型分别保留其特定假设。

## 共正锥与非紧矩层级

本机 P-8656e750bc1e0cf5，arXiv:1012.2552v2，物理页 4 将所引结果印为 [12, Theorem 3.2]。已纠正技能中把印刷编号写作 3.3 的错误。对于非紧闭正交锥上的乘积指数测度，实际采用 Lasserre [arXiv:1009.0125v1](https://arxiv.org/abs/1009.0125v1) 物理页 6–7 的 Theorem 3.3。该用法依赖测度的乘积形式、支撑、全部多项式加权可积性及各固定移位的 Carleman 条件。无限交结论及有限维 CP/COP 对偶的原有边界保持有效。

## 滤过投影与补偿

查询五份实际依赖并核对滤过、过程类别与适用范围。Kiiski–Perkkiö 用于具备其条件的 integrand 投影。Kikuchi 的发表结果用于其离散条件期望投影。Janson–M'Baye–Protter 的补偿子迁移依赖滤过及绝对连续条件。Sarma–Selvamuthu 提供离散 Hawkes 算例，Zhunussova 的引用限定到其单跳模型。技能已按停时区分可选/可预测投影，并分别说明计数过程增补偿子与随机测度的补偿测度。[Kikuchi 期刊版](https://doi.org/10.5802/ambp.409)
