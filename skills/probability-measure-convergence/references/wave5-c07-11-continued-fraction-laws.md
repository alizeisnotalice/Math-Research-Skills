# Continued-fraction limit laws: two scoped references

## Rational points and weight-zero quantum modular forms

**Version and source statement.** Bettin--Drappeau, *Limit laws for rational continued fractions and value distribution of quantum modular forms*, local HAL `hal-02998562v2`, physical pp. 1, 3--6, with the local citation to *Proceedings of the London Mathematical Society* **125** (2022), 1377--1425, DOI `10.1112/plms.12485`. The publisher record identifies the same title, journal, volume, pages, and DOI.

For the uniform law on `Omega_Q={a/q:1<=a<=q<=Q,(a,q)=1}`, Theorem 1.1 concerns a weight-zero `SL(2,Z)` quantum modular form with `h_tau=0`, whose `h_sigma` has the stated Holder extension and endpoint growth. Under those conditions the suitably normalized rational values converge to the stable law selected by that endpoint growth. Theorem 2.1 specializes this to the Estermann function, with the displayed Gaussian normalization `sigma (log Q)^(1/2)(log log Q)^(3/2)` and `sigma=1/pi`; Theorem 2.3 gives the stated modular-symbol Gaussian law.

Use this only after specifying the rational-point sampling law, the actual QMF transformation identities, exact Holder/endpoint estimates, and normalization. It is not a statement about a prescribed irrational's continued-fraction convergents, and it supplies neither a way to verify QMF hypotheses nor a generic stable-limit theorem outside its Gauss-map setting.

## Trimmed Gauss-digit sums

**Version and source statement.** Bazarova--Berkes--Horvath, *On the Extremal Theory of Continued Fractions*, local physical pp. 1, 3, 11; published as *Journal of Theoretical Probability* **29** (2016), 248--266, DOI `10.1007/s10959-014-0577-5` (the DOI record corrects the older local index's journal/year description).

Let `a_j(x)` be the Gauss-map continued-fraction digits under Gauss measure and delete the `d_N` largest of the first `N` digits, where `d_N -> infinity` and `d_N/N -> 0`. With `eta_{d,N}` the `d`-th largest digit and
`m(t)=(log 2)^(-1) sum_{1<=k<=t} k log(1+1/(k(k+2)))`, Theorem 1.1 states

`(S_N^(d)-N m(eta_{d,N}))/(N/sqrt(d_N)) => Normal(0,(log 2)^(-1))`.

The stated consequence is `S_N^(d)/(N log(N/d_N)) -> 1/log 2` in probability. Apply only to Gauss-distributed inputs and the exact trimming regime; do not transfer it to deterministic digit sequences or turn it into an irrationality-measure estimate. The fourth-moment/mixing estimate on local p.11 is part of its probabilistic proof route, not a standalone bound for arbitrary continued-fraction data.
