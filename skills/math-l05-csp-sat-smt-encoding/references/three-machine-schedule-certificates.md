# 三元槽位的路径式排程见证

给定有限作业偏序和子集 \(W\)，每个作业单位时长，槽内恰放三个作业。状态 \((L,Z,R)\) 分割 \(W\)，要求 \(Z\) 是三元反链，并且任何后一组的作业均不先于前一组的作业。兼容性按传递偏序核查。

若一列状态满足 \(L_i\cup Z_i\subseteq L_{i+1}\)，且已经找到 \(L_1\)、每个 \(L_{i+1}\setminus(L_i\cup Z_i)\) 和末尾 \(R_k\) 的满槽排程，则把这些间隙与各 \(Z_i\) 依次拼接。包含关系给互不相交的全覆盖，跨分块的反向前置由一个分隔相应两块的状态排除。单状态路径合法，空间隙不需要槽。每步左部增加至少三件作业，可以保存前驱路径和已有子日程。

这个构造可以作为有限动态规划的可靠接收证书。要据此判定不可排程，仍须证明任何可排实例都有允许的描述族中的此类层级。三个机器、单位作业、原始偏序及同步槽容量都应保留。

- OpenAI 预印本 PDF 5–6 页，式 (3.1)–(3.2)、Proposition 3.1 的可靠性与 Lemma 3.3 的条件完备性。SHA-256 2080c4ad5953f225c1db7fe803c6d8602ae499510719cfe0cb4f22f99bccff1e。[A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf)
