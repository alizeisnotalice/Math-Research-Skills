# 次模秩约束的精确分离

给定有限地面集 \(E\)、整数次模秩 \(r\) 的精确值 oracle，和有理向量 \(x\)。对基多面体的总质量约束先检查 \(x(E)=r(E)\)。若定义中另规定 \(x\ge0\)，也直接检查。剩余约束为 \(x(A)\le r(A)\) 对所有 \(A\subseteq E\)。

函数 \(f_x(A)=r(A)-\sum_{i\in A}x_i\) 仍为次模，因为第二项为模函数。令 \(D>0\) 为所有坐标既约分母之积。调用精确整数次模最小化 oracle，对 \(D f_x\) 返回最小值及集合。如果最小值为负，则相应集合给出原坐标的分离超平面，否则所有集合约束成立。\(D\) 的二进制位长至多分母位长求和。已知包含集 \(F\) 和排除集 \(G\) 时，二者应不交。把变量限制在 \(E\setminus(F\cup G)\)，令函数为 \(A\mapsto D f_x(A\cup F)\)，保留次模性。

本机对 \(r(A)=\min(2,|A|)\)、\(x=(1/4,3/2,1/4)\) 的 8 个集合精确枚举。\(D=32\)、最小值 \(-16\) 在第二个元素的单点取得，分离式为 \(x_2\le1\)。

此接口调用次模最小化器。只有另核对已知多面体坐标界、单条不等式编码界和强分离等价的输入条件，才可加上精确多面体优化。公共基计数及对大容量的复杂度分析需要进一步证明。

来源为 OpenAI 预印本，PDF 4–5 页，Proposition 2.1 后的分离构造。SHA-256 c14d087890444879a1ff0d492e8cfc3fdb976af562c966ee5c5bd3c3e2ade2e8。[An FPRAS for Common Integer Polymatroid Bases with Binary Capacities](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-FPRAS-for-Common-Integer-Polymatroid-Bases-with-Binary-Capacities-October-5-2026/polymatroid-fpras.pdf)
