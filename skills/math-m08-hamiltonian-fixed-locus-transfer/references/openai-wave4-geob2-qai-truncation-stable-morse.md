# Quadratic-at-infinity truncation before stable-Morse comparison

Source: *Hamiltonian Fixed Points Below the Stable Morse Number in Dimension
Twenty-Two*, OpenAI (5 October 2026), SHA-256
`12e5b850a57973914df99d6e8686b3b8c1bf77bd738605fffc1cd3cc26787058`,
[official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/hamiltonian-fixed-points-below-stable-morse-number.pdf).

## Scoped interface

This reference only gives the compact truncation bridge for a generating
function on `W x R^k` that equals a nondegenerate quadratic form outside a
compact set.  It belongs before any use of the fixed-locus transfer skill's
local fixed-point correspondence.  It is not a general fixed-point lower
bound and does not itself prove a stable-Morse comparison.

After a linear change of auxiliary coordinates, write

\[
 Q(u,v)=-|u|^2+|v|^2,\qquad (u,v)\in\mathbb R^d\times\mathbb R^{k-d}.
\]

Choose `R_0` so `F=Q` outside `W x B_{R_0}` and every critical point lies in
that core.  Choose `A,T` with

\[
 A>\max_{W\times B_{R_0}}\{|F|,|Q|\},\qquad T>R_0,\quad T^2>A,
\]

and set

\[
 K=W\times B_T,\qquad K^- =K\cap\{F\le-A\},\qquad
 K^+=K\cap\{F\le A\}.
\]

The endpoint sublevels agree with the quadratic ones,
`K^\pm=K cap {Q<=\pm A}` (source (2.2), physical p. 4).  Verify the source's
side-boundary condition before asserting that truncation adds no cells.

## Compactly supported replacement

For a cutoff `chi_R` equal to one on `|z|<=R`, zero on `|z|>=2R`, and
`||d chi_R||<=C/R`, replace the perturbation by `Q+chi_R h`.  On the
transition annulus the source bounds

\[
 \|d(\chi_Rh)\|\le L+C(K_0/R+2L),\qquad \|dQ\|\ge cR.
\]

For sufficiently large `R`, it has exactly the original critical points,
agrees with `F` near them, and equals `Q` outside a compact set (physical
p. 5).  Only after these checks may the cited torsion-inclusive Smale equality
be applied under its own assumptions (simply connected closed smooth `W`,
dimension `D>=9`).

Locators: physical pp. 4--5; (2.2) and Theorem 2.4.
