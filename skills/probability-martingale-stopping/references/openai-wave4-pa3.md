# Wave 4 PA3: massive-interface scalar and martingale interface

## Thermal FK--Ising interfaces and massive SLE

Source SHA-256 `c2a2a4a8b4213752e486fdc5efc675ddabfe6fd2360fd88fac0b91860619bd49`, physical pp. 5--6, 15--16, 30, and 39.  In a bounded marked simply connected domain, the positive-mass scalar observable is the unique bounded classical solution of
\[
\Delta h=-4m|\nabla h|,
\qquad h=1\ \text{on the primal bank},\quad h=0\ \text{on the dual bank}.
\]
For two solutions the difference solves `\Delta q+\beta\cdot\nabla q=0` with `|\beta|\le4m`; bounded-drift killed diffusion, stopped Itô, and prime-end exit control give uniqueness.  The limiting signed fermion satisfies
\[
M_t(w)^2=Dh_t(w),\qquad \bar\partial M_t+imM_t=0,
\]
and is a continuous local martingale at protected live points after the source's localization.  A common increasing clock dominates time, driver variation/bracket, and spatial brackets before stopped Girsanov identifies the driving law.

**Scope.** Scoped reference. It requires the marked-domain boundary conventions, the massive observable/regularity inputs, protected stopping and finite-energy localization.  It does not create a signed lift through swallowing, prove discrete tightness, or establish massive SLE for a different interface model.

## 固定来源

- 物理页 5, 6, 15, 16, 30, 39。Proposition 2.2; Proposition 3.10; Lemma 5.5; stopped Girsanov uniqueness SHA-256 `c2a2a4a8b4213752e486fdc5efc675ddabfe6fd2360fd88fac0b91860619bd49`。[Thermal FK–Ising interfaces and massive SLE](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Thermal-FK-Ising-interfaces-and-massive-SLE-October-5-2026/paper.pdf)
