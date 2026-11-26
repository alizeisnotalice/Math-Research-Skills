# 有理双矩阵博弈的零和安全值证书

对 \(R,C\in[0,1]^{m\times n}\cap\mathbb Q^{m\times n}\)，给出六个有理对象

\[
(x_{\mathrm{row}},y_{\mathrm{min}},v_R),\qquad
(y_{\mathrm{col}},x_{\mathrm{min}},v_C).
\]

脚本逐条验证

\[
x_{\mathrm{row}}^TRe_j\ge v_R\quad(\forall j),\qquad
e_i^TRy_{\mathrm{min}}\le v_R\quad(\forall i),
\]

和

\[
e_i^TCy_{\mathrm{col}}\ge v_C\quad(\forall i),\qquad
x_{\mathrm{min}}^TCe_j\le v_C\quad(\forall j).
\]

给定同一个值的可行上下界时，弱对偶强迫每对界相等。由收益非负，策略对
\((x_{\mathrm{min}},y_{\mathrm{min}})\) 的两侧后悔分别至多为 \(v_R,v_C\)。这是一个验算器，输入需要已经求得的有理可行解。

Google Cogentic 论文 *An Exact Polynomial-Time Algorithm for 1/5-Approximate Nash Equilibria in Bimatrix Games* 的 Lemma 2.2 在物理页 6--7 给出相同的零和 LP 结构与这个后悔界。固定下载件 SHA-256 为 `ed65664e8817e323a1613f95f4fc98689719c86fb2708974bb69cc1edc139485`，新版 SHA-256 为 `32196e6a64d13fbd216c7e7353a3b44a46e8389eb3d15bad48ffb3dd926cc337`。本构件不运行或认证该论文的 Step 3、Volterra 系统或全局 \(1/5\) 近似 Nash 结论。[Google Research 修订版](https://github.com/google-research/google-research/blob/3f540f420bfae7e6ce48365a68d0ae003feb2f87/cogentic_research_papers/bimatrix_nash_equilibrium/paper.pdf)

运行 `scripts/security_screen_certificate.py INPUT.json`。`--self-test` 穷举 256 对二元 \(2\times2\) 零一收益矩阵，使用分母二策略格点构造并验证两个零和证书，并检查无效 minimax 见证遭拒绝。
