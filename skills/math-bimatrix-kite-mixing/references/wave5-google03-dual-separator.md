# Exact dual separator for a fixed row anchor

## Source and revision check

This is the previously unused finite branch of Google Cogentic, *An Exact Polynomial-Time Algorithm for 1/5-Approximate Nash Equilibria in Bimatrix Games*, Lemma 2.3(b), physical pp. 8--10. The downloaded source is 41 pages, SHA-256
`ed65664e8817e323a1613f95f4fc98689719c86fb2708974bb69cc1edc139485`, from Google Research commit `4a7bc8ab0bc7`.

The located current Google revision is also 41 pages with SHA-256
`32196e6a64d13fbd216c7e7353a3b44a46e8389eb3d15bad48ffb3dd926cc337` (commit `3f540f420bfae7e6ce48365a68d0ae003feb2f87`). Its extracted physical pp. 8--10 retain the Lemma 2.3(b) primal LP marker, weak-duality identity, `Branch 2`, `lambda*`, and the welfare-cap expression. This finite tool is fixed to the downloaded source page numbering.

## Local theorem and audited proof dependency

Let `R,C` have rational entries in `[0,1]`, `0<r<1/2`, and `xbar` be a row strategy. Lemma 2.3(b) forms an exact rational primal-dual LP. If its common optimum is above `r`, its Branch 2 returns `lambda in [r,1-r]` and `u in Delta_m` such that for every column `j`, writing `M2(xbar)=max_l xbar^T C e_l`,

`(1-lambda)(u-xbar)^T R e_j + lambda(M2(xbar)-xbar^T C e_j) > r`,

`(f1(u,e_j),f2(u,e_j)) notin K_r`, and

`u^T R e_j + u^T C e_j < 2-r/(1-r)`.

The source proof read for this finite implication is pp. 9--10: it writes the primal and dual LPs, expands the exact weak-duality identity as a sum of nonnegative slacks, invokes rational LP strong duality, and derives the three displayed Branch-2 outputs from dual feasibility and the fact that each pure-column profile escapes `K_r`. This add-on independently checks the **output certificate** only. It neither solves the LP nor certifies the universal dichotomy, algorithmic encoding bounds, Volterra system, or the paper's global `1/5` theorem.

## Exact replay

Run:

```sh
python3 scripts/wave5_google03_dual_separator.py examples/wave5_google03_dual_separator_positive.json
python3 scripts/wave5_google03_dual_separator.py examples/wave5_google03_dual_separator_boundary.json
```

The first input supplies an exact Branch-2-style certificate. The boundary input violates strict separation and must exit with status 2. All arithmetic is `Fraction`; no floating comparison is used.

[固定版论文](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/bimatrix_nash_equilibrium/paper.pdf)。
所采用的 PDF 物理页 8–10 经两版逐词比对只有两处引文编号变动。[修订版论文](https://github.com/google-research/google-research/blob/3f540f420bfae7e6ce48365a68d0ae003feb2f87/cogentic_research_papers/bimatrix_nash_equilibrium/paper.pdf)。
