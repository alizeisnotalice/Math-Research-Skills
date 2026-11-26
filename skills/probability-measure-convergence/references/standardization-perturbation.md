# 标准化的有界二阶扰动

在同一概率空间上取中心化后的变量 \(X,Y\)，设 \(s=\|X\|_2>0\)、\(t=\|Y\|_2>0\)、\(r=\|Y-X\|_2\)。反三角不等式给出 \(|s-t|\le r\)。在同一个耦合下展开平方内积可得

\[
\left\|\frac Xs-\frac Yt\right\|_2^2=\frac{r^2-(s-t)^2}{st}.
\]

分别以 \(s\) 和 \(t\) 作分解，还有 \(\|X/s-Y/t\|_2\le 2r/\max(s,t)\)。因此当 \(r_n/s_n\to0\) 时，最终有 \(t_n>0\)、\(t_n/s_n\to1\)，两个标准化变量在给定耦合下的 \(L^2\) 距离趋于零。若原标准化变量的弱极限已独立成立，可用 Slutsky 转移到另一支。物理页 119 在 SK–Curie–Weiss 对比采用了反三角与 \(2r/t\) 的版本；该模型的涨落尺度和比较估计需要各自的证明。[固定原稿](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026/The-low-temperature-Sherrington-Kirkpatrick-free-energy-limiting-law-September-24-2026.pdf)

给出有限联合分布中的原子质量及两个实值。程序用有理数得到中心化均值、方差和协方差。对给定平方距离上界，按符号比较协方差与有理倍数的正平方根，避免浮点。输出为所给耦合的距离证书，也给出边缘分布间 Wasserstein 距离的上界。预期弱极限、实际输入耦合和渐近条件由调用者独立给出。

```sh
python3 scripts/check_standardization_perturbation.py examples/standardization-finite-joint-law.json
```

样例的平方距离为 \(2-\sqrt2\)。程序确认 \(3/5\) 是上界，并拒绝把同一输入的上界改为 \(1/2\)。严格正方差是标准化的条件。
