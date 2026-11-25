# 来源核验与范围

本技能只采用下面四份本机 OpenAI 预印本共同给出的有限图对偶构件。它们均使用固定提交 `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6` 的版本，未按正式发表结果处理。

- *Critical Center Magnetization in the Planar XY Model*，PDF p. 4，Lemma 2.1。固定边界图中，中心到边界的电流去除后旋转为高度梯度。SHA-256 `8347485745eaf5838417cebd36128198c7520b4e651091cb0f0ad8944ab87d1f`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Critical-Center-Magnetization-in-the-Planar-XY-Model-October-5-2026/paper.pdf)
- *The Critical Spin Field of the Planar XY Model*，PDF p. 7，Lemma 2.1。任意整数源可分别接到边界，孔洞周期由所包电荷指定。SHA-256 `486481fbcc54fe62c8d14e4f4a65869facc2a7f8a4c32647649468f91825ac47`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Critical-Spin-Field-of-the-Planar-XY-Model-October-5-2026/paper.pdf)
- *The critical correlation exponent of the planar XY model*，PDF p. 4，Lemma 2.1。自由边界盒的双源扭曲、切开图的单值分支及外部高度约定。SHA-256 `e58587be77cd0256a9c426942dbc656bf3ae679cc4681a5e196bb333825eba17`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-critical-correlation-exponent-of-the-planar-XY-model-September-24-2026/paper.pdf)
- *The critical logarithmic correction for the planar XY model*，PDF pp. 5–6，Lemma 2.1 和规范变换说明。固定边界与自由盒的常数模式、积分规范和观测变换。SHA-256 `5c357d1c416119fa157cddaa3e06854fd47bc1020cb7a797949ee42544272a8a`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-critical-logarithmic-correction-for-the-planar-XY-model-October-5-2026/paper.pdf)

PDF p. 5 的有限比较规则及其后的连续标度陈述没有进入本技能。它们实际使用了 Regev–Stephens-Davidowitz 格点不等式、链式 Bessel 逼近或同族论文的临界高度输入，需单独核验。
