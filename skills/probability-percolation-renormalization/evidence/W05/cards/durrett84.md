# durrett84 — Oriented percolation in two dimensions

**Reading status:** `fulltext_read`; complete 43-page local scan read (PDF pp. 1–43; article text pp. 2–43, printed pp. 999–1040). Boundary-speed, block-renormalization, contour, and tail formulas were checked on rendered pages. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Richard Durrett, “Oriented Percolation in Two Dimensions,” *The Annals of Probability* 12(4) (1984), 999–1040, DOI [10.1214/aop/1176993140](https://doi.org/10.1214/aop/1176993140). Local PDF SHA-256: `d04e2889157dd82d92d7d668445c8ad580558e340fc5f66457d6b90c535b5c31`.

## Model and edge-speed criterion

The paper studies iid oriented **bond** percolation on the two-dimensional north-east lattice (equivalently, after rotation, a one-dimensional space-time process with edges to the two neighbouring sites in the next time layer). Each directed bond is independently open with probability \(p\). From the singleton origin, write \(\xi_n^0\) for the reachable sites at layer \(n\), \(r_n=\sup\xi_n^0\), and \(\ell_n=\inf\xi_n^0\), with \(\sup\varnothing=-\infty\) and \(\inf\varnothing=+\infty\). Define the enlarged half-line process \(\bar\xi_n=\{x:\text{some }y\le0\text{ has an open path from }(y,0)\text{ to }(x,n)\}\) and \(\bar r_n=\sup\bar\xi_n\). It is this enlarged edge—not the singleton edge—that has an unconditional Kingman-type speed in §3: \(\bar r_{0,n}/n\to a(p)\) a.s., with \(a(p)=\inf_{n\ge1}\mathbb E[\bar r_n/n]\). Equation (7) (PDF p. 8) gives \(r_n/n\to a(p)\) and \(\ell_n/n\to-a(p)\) **on** \(\Omega_\infty\); after extinction the singleton edges are infinite-valued by convention, so those limits are not unconditional.

Theorem/criterion in §3 (PDF pp. 5–10; printed pp. 1002–1007) shows \(a(p)<0\Rightarrow\mathbb P_p(\Omega_\infty)=0\), while \(a(p)>0\Rightarrow\mathbb P_p(\Omega_\infty)>0\), and identifies \(p_c=\inf\{p:a(p)>0\}\). A common-uniform coupling and a first-discrepancy argument give \(a(p)-a(p')\ge2(p-p')\) when \(p>p'\) and \(a(p')> -\infty\); hence the speed leaves zero immediately to the right of \(p_c\). The paper later proves \(a(p_c)=0\) by coarse-graining a positive-speed process into a high-density 1-dependent oriented site process, contradicting criticality if the critical speed were positive (§9, PDF pp. 26–29).

For \(p>p_c\), the stationary-increments edge process and Harris/FKG give \(\mathbb P_p(\Omega_\infty)\ge a(p)^2\), and the speed increment inequality supplies the explicit quadratic lower bound \(4(p-p_c)^2\) recorded in §5 (PDF pp. 13–16). This is not an exact critical exponent.

## Tail and block mechanisms

Below criticality, §7 (PDF pp. 19–24) proves exponential decay of survival to layer \(n\), exponential tails for the right edge, and an exponential tail for total cluster size \(|C_0|\). The cluster-size proof first chooses a finite block whose expected offspring is subcritical, dominates later growth by a bounded-offspring branching process, and uses a random-walk total-progeny estimate. In the supercritical phase, §9 constructs a finite-range-dependent coarse site process from long crossing events. A Peierls contour bound for that high-density process is then pulled back to the original oriented model in §10, yielding \(\mathbb P_p(\tau^A<\infty)\le C e^{-\gamma|A|}\) for a finite initial set \(A\), with \(p>p_c\) (PDF pp. 29–33). A restart argument in §12 gives \(\mathbb P_p(n<\tau^A<\infty)\le C e^{-\gamma n}\), with constants independent of \(A\); it also gives the supercritical finite-cluster tail of order \(e^{-c\sqrt n}\) (PDF pp. 34–36).

Sections 4–6 build the stationary edge law, recurrence results, and branching-process lower bounds on \(p_c\). Section 8 develops time-reversal duality. Section 11 (PDF pp. 33–34) proves its large-deviation bound for the **half-line** edge \(\bar r_n\), not the singleton edge that can equal \(-\infty\) after extinction, and proves continuity of \(a(p)\) for \(p>p_c\). Section 13 uses finite-range dependence, correlation estimates, and Newman–Wright methods for a law of large numbers and partial CLT for the occupied interval. Section 14 proves infinite differentiability of \(\mathbb P_p(\Omega_\infty)\) for \(p>p_c\).

**Visual checks:** rendered PDF pp. 5, 7–8 for the separate singleton/half-line definitions and conditional/unconditional speed statements, p. 33 for the large-deviation theorem’s \(\bar r_n\) notation, pp. 29–30 for the contour estimate, p. 34 for the restart tail, and p. 40 for the differentiability argument.

## Transfer limits

The paper concerns independent oriented bonds in a fixed 2D space-time lattice. Exponential extinction tails and positive survival do not by themselves decide a two-player game, prove a draw, or transfer to dependent random directions. They also do not establish bootstrap infection-time tails: there the state-dependent local rule and source of randomness differ. For B177/B178, this source is an oriented-path comparison tool only; optimal play remains an unproved interface.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/durrett84`).
