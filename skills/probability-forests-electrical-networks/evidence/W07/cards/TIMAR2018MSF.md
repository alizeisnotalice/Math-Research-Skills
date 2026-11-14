# TIMAR2018MSF — indistinguishability of random spanning-forest components

**Source:** Ádám Timár, “Indistinguishability of the Components of Random Spanning Forests,” *Annals of Probability* 46(4) (2018), 2221–2242, DOI 10.1214/17-AOP1225. Complete 18-page PDF read (SHA-256 `0ed888682bede1efddbcb1da2c27e0eefb75b4b121381ee491c8dcc811dd7a1a`). Physical PDF pages are cited below; Definition 1 was visually checked on rendered PDF pp. 3–4.

## Main conclusions and hypotheses

Theorems 1.1 and 1.2 (PDF pp. 2–3) are stated for unimodular quasi-transitive graphs, and the proofs extend to unimodular random graphs. If FUSF differs from WUSF, Theorem 1.1 says FUSF has either one or infinitely many components, each component has infinitely many ends, and invariantly defined component properties are indistinguishable. If FMSF differs from WMSF, Theorem 1.2 gives the corresponding conclusions for FMSF. The paper identifies the latter inequality with (p_c<p_u). These are theorem-level inequality hypotheses; do not silently replace them by the separate θ((p_c),G)=0 assumption used for Lemma 1.4 below.

## Weak insertion tolerance: exact modification and proof inputs

For an edge (e=\{x,y\}), the paper defines
\[
\pi_e^f\omega := (\omega\cup\{e\})\setminus\{f\},\qquad
f\in E(G)\cup\{\varnothing\}.
\]
Definition 1 (physical PDF p. 4) says WIT holds if, for every (e,r,\omega) with (x,y) in different components, there is a measurable choice (f=f(\omega,e,x,r)) such that for every positive-probability event (A) on which (C_x\ne C_y) almost surely, \(\mathbb P(\pi_e^f A)>0\). If (f\ne\varnothing), then it lies in (C_x\cap B(x,r)^c) almost surely. Thus the edge is inserted while a possibly **far-away** edge in the (x)-component is removed: WIT is not a local modification that keeps the forest unchanged outside (B(x,r)).

Lemma 1.3 (PDF pp. 4–5) proves WIT for FUSF/WUSF by finite wired approximations and the UST edge exchange; it gives a bound \(\mathbb P(\pi_e^f A)>\delta(r)\mathbb P(A)\). Lemma 1.4 (PDF p. 5) proves WIT for FMSF/WMSF under the separate assumption \(\theta(p_c,G)=0\). Corollary 1.5 states that FMSF\(\ne\)WMSF also implies WIT for both minimal forests, without making \(\theta(p_c,G)=0\) the corollary's hypothesis. In its proof route, the lemma's \(\theta=0\) criterion and the corollary's FMSF/WMSF inequality criterion must remain distinct.

## Consequences and proof route

Theorem 3.1 (PDF p. 9) combines WIT with ergodicity to show that if a component with infinitely many ends occurs, then all components have infinitely many ends. Theorem 3.3 (PDF p. 10) uses the mass-transport principle and WIT to rule out a finite nonzero number of components. Theorem 4.3 (PDF pp. 14–17) proves indistinguishability by a pivotal modification and a Radon–Nikodym comparison of the modified law. These conclusions require the stated invariance/unimodularity and ergodicity inputs; WIT alone does not imply indistinguishability (Example 4.1, PDF p. 14).

## Reading coverage

Complete PDF read: introduction and main theorem statements, §1 (PDF pp. 1–3); WIT definitions and proofs, §2 (pp. 3–7); mass transport and component-count/end consequences, §3 (pp. 8–12); pivotal modification and indistinguishability proof, §4 (pp. 13–17); acknowledgements/references (p. 18). The exact WIT map and the location of the deleted edge were checked in rendered PDF pp. 3–5.

## Scope boundary

Do not use WIT as synonymous with local insertion tolerance. For a minimal forest, verify whether the application uses FMSF\(\ne\)WMSF (equivalently (p_c<p_u), as stated here) or the separate \(\theta(p_c,G)=0\) condition of Lemma 1.4. Verify unimodularity, quasi-transitivity/random-rooted-graph scope, and ergodicity before invoking the component conclusions.
