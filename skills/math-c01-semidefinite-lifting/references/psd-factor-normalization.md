# 最大行列式归一化

已知非零有限非负矩阵 \(S_{ij}=\operatorname{tr}(A_i B_j)\le B\)，因子为实对称 PSD。压缩到所有列因子像的张成空间，保持配对，设维数为 \(r\)。列因子的平均在该空间正定。取列因子凸包中的最大行列式点 \(J\)，它存在且正定。

沿 \(B_j-J\) 的单侧对数行列式导数不为正，故 \(\operatorname{tr}(J^{-1}B_j)\le r\)。将行因子改为 \(J^{1/2}A_iJ^{1/2}\)，列因子改为 \(J^{-1/2}B_jJ^{-1/2}\)。配对不变，列迹至多 \(r\)，行迹为 \(\operatorname{tr}(A_iJ)\)，作为该行条目的凸组合至多 \(B\)。若未压缩支撑，\(J\) 可能奇异，不能直接取逆。

本机 SymPy 检查列因子为 \(\operatorname{diag}(4,0),\operatorname{diag}(0,1),0\)、行因子为 \(I_2\) 的实例。\(J=\operatorname{diag}(2,1/2)\) 归一化后保持配对 \(4,1,0\)，行迹为 \(5/2\)，列迹为 \(2,2,0\)。本接口以既有因子为输入。

- OpenAI 预印本 PDF 16 页，Lemma 6.1 的归一化；指数 PSD 秩下界及 SDP 提升转换需另证。SHA-256 7e90c5f1e508114d849a1a299e889a520997f1a0b3eec4f09ee1da36a61e31d4。[Exponential PSD rank of positively shifted matching matrices](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Exponential-PSD-rank-of-positively-shifted-matching-matrices-October-5-2026/shifted-matching-psd.pdf)
