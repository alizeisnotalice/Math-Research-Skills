# 直接来源与核验边界

本技能只从以下两个本地 OpenAI 预印本抽取两个窄接口。两者在本地 inventory 中都是当前 GitHub 原始 PDF，而非已核对的正式发表版本；读取日期为 2026-11-25。

## 分支稳定子度数

- **来源：** OpenAI, *Étale covers with a prescribed exterior sheet*, September 24, 2026，PDF p. 3，Lemma 2.1；其商覆盖度数用法见 p. 6。
- **本地文件：** `current/Etale-covers-with-a-prescribed-exterior-sheet-September-24-2026/main.pdf`。
- **SHA-256：** `713430a73f1530f5d89cd38050c45a6bc2ccc458878a191917bb37b451b2f26a`。
- **固定原始版本：** [OpenAI math commit 3344da5](https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6)，[PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Etale-covers-with-a-prescribed-exterior-sheet-September-24-2026/main.pdf)。

Lemma 2.1 的原始范围是：\(f:C\to X\) 为连通有限 étale Galois 覆盖；\(D\) 为文中紧外域 \(U\) 或指定开盘 \(V_i\)。它证明分支满射、群在分支上传递、分支度数为稳定子阶。技能中的商公式只记录本文 p. 6 已执行的同一分支计算，额外要求使用者核对商和分支像的解析条件。

该文的覆盖**存在**部分不是本技能的结论：p. 2–6 还使用了非奇异性消解、稳定骨架、图覆盖到解析/代数覆盖的实现和 proper GAGA。特别是 p. 2 以 Mochizuki--Tsujimura 的 \(\Sigma\)-RNS 为几何输入；p. 5 使用 de Jong 的局部平凡化，p. 5–6 使用 Poineau 的 proper GAGA、SGA 1 的不变性。它们应逐项另行核验。

## 环域单位根

- **来源：** OpenAI, *The p-adic section conjecture*, October 6, 2026，PDF pp. 8–9，Lemma 4.1。
- **本地文件：** `current/The-p-adic-section-conjecture-October-6-2026/main.pdf`。
- **SHA-256：** `f3c8d6f784d6bae48305f6959c44c7cc337f9c2b6078d93a5595d317b3a82f40`。
- **固定原始版本：** [OpenAI math commit 3344da5](https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6)，[PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-p-adic-section-conjecture-October-6-2026/main.pdf)。

直接检查的前提在 p. 8：\(p\) 为素数、\(k/\mathbb Q_p\) 有限、\(\Omega=\widehat{\bar k}\)，并固定 \(\ell\ne p\)。Lemma 4.1 本身给出 disk/annulus 的单位分解及根传递。它引用 annular factorization 作比较，但在 pp. 8–9 给出了所需论证。

不要把这个局部引理升级为其后的 Lemma 4.2（稳定节点环域上构造全局有限 étale 覆盖）。后者在 pp. 9–10 实际依赖 metrized-complex tame-cover lifting、\(\operatorname{Pic}^0\) 可除性和稳定性论证，均不在本技能中承担。
