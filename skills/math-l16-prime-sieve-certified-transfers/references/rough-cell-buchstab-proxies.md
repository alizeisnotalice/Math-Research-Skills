# Rough-cell Buchstab proxies

Source: *Weighted dilation graphs, smooth shifted primes and totient fibers*,
SHA `351692885d112277e969901e75fe56eeee0d263d5d5847d0b980fe2c8c7744c0`,
physical pp. 57--60.

For a fixed `x`, roughness cutoff `W`, logarithmic cell `C_Y=(Y,e^Delta Y]`,
and a test `I`, use the exact full-cell proxy
`B_I(m)=c_I(C_Y) 1_{P^-(m)>W}` with
`c_I(C_Y)=sum_{m in C_Y} I(m) / #{m in C_Y:P^-(m)>W}`. The denominator must be
positive; the source's asymptotic lower bound is not a substitute for checking
it for a finite input. Full-cell sums of `I-B_I` vanish by construction;
partial cells must remain explicit error terms.

For fixed `w>gamma>0`, the finite Buchstab-coordinate sum is
`D_gamma(w)=1/w + sum_{l>=2} 1/l! integral_{t_i>=gamma, sum t_i<=w-gamma}
1/((w-sum t_i) product t_i) dt`.
Only finitely many terms survive. The source identifies the minimum-coordinate
decomposition
`integral_{b_1}^{1/2} D_alpha(1-alpha) d alpha/alpha = D_{b_1}(1)-1`.
Use it only with fixed positive cutoffs and declared external distribution
inputs; it neither creates Type I/II estimates nor proves a prime conclusion.

## 固定来源

- 物理页 57, 58, 59, 60。Equations (7.12)--(7.20) and Lemmas 7.3--7.4: rough-cell proxies, logarithmic Buchstab density, and the minimum-coordinate identity. SHA-256 `351692885d112277e969901e75fe56eeee0d263d5d5847d0b980fe2c8c7744c0`。[Weighted dilation graphs, smooth shifted primes and totient fibers](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf)
