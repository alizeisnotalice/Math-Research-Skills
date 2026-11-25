# Missing-condition and invalid-transfer cases

## A corner theorem must match the reflection model

A proof writes inward normals at a triangle vertex and invokes a theorem for normal-cone reflection without checking the selected Skorokhod problem, its normal-set convention, or the theorem's geometric Conditions (A) and (B). This has not specified a well-posed marginal. A facewise SRBM theorem such as Dai–Williams or Kang–Williams also needs its own reflection matrix and active-face conditions; it is not interchangeable with every normal-reflection construction.

A normal-reflection theorem for a smooth boundary does not settle a polygon corner. For example, the accepted Bass–Burdzy uniqueness result assumes \(C^{1+\gamma}\), \(\gamma>1/2\), and \(d\ge3\); it is an individual-marginal theorem, not a corner coupling result (EXSRC-4fe672a8184ecea2).

## Do not impose co-adaptedness on every coupling

For a co-adapted mirror or common-noise construction, prove that each driver is Brownian in the joint filtration and verify both reflected marginals. An unrestricted coupling needs only the correct coordinate path laws; it need not provide a joint filtration with Brownian drivers. A theorem about one synchronous family does not restrict the target's unrestricted coupling class.

## Do not reverse the spectrum-to-coupling implication

A coalescing coupling with a tail upper bound yields a total-variation upper bound. A bounded Neumann eigenfunction instead forces a necessary lower bound on \(P(T>t)\) for any correct coupling that stays together after meeting. A numerical Neumann eigenvalue or a spectral lower bound does not construct a matching coupling-tail upper bound. For standard reflected Brownian motion, also distinguish \(\Delta\) from \(\tfrac12\Delta\). A killed-pair eigenvalue calculation has its own gate: first select a Markov joint process and verify its block covariance, actual product reflection/corner rules, killing set and boundary conditions. An unrestricted coupling need not be Markov. The symmetric-start interval calculation therefore does not automatically apply to other starts, triangles, or mirror couplings with a degenerate joint generator.

Laugesen–Siudeja's triangle inequality is for the first positive eigenvalue and is not the exact spectrum of a chosen triangle. Loper's diameter-based convex-domain coupling bound is not thereby sharp at that triangle's Neumann rate. The one-dimensional symmetric-interval killed-pair calculation requires \(x+y=L\); it does not extend to arbitrary starts or triangles.

## Preserve the exact scope of derivative and approximation results

- Lipshutz–Ramanan (2018) is admitted only for \(R=I,b=0,\sigma=I\) in the two-dimensional normal orthant with a pure feasible initial perturbation. The degenerate Appendix D.2 quotient is not an admitted non-differentiability counterexample. The 2019 paper is admitted only for the one-dimensional normal half-line with \(b=0,\sigma=1\) and constant data; at first contact, raw derivatives and the right-continuous derivative-process value can differ. Neither case is a general oblique-triangle derivative theorem (EXSRC-dbc465f6b783d606, EXSRC-6170b182ae853a60).
- Fradon's theorem uses one common positive-definite matrix \(\theta\theta^\top\) for all defining constraints. A family of arbitrary facewise oblique directions need not arise from one such matrix. The accepted triangle example takes \(\theta=I\), \(\sigma=I\), \(b=0\); it proves one individual marginal, not a pair coupling (EXSRC-630765515640def5).
- Esposito–Nitsch–Trombetti's reviewed use is the bounded-convex \(p=2\) specialization only. Do not treat the general \(p\ge2\) proof as independently certified or confuse this later theorem with Payne–Weinberger's unavailable 1960 text (EXSRC-61071ee2e4fdd736).
- Andres (2009) is admitted only for the additive-standard-noise, one-face half-space initial derivative, with \(b\in C^1\) globally Lipschitz and the oblique direction normalized as in the source. The raw derivative is stated on \([0,\tau)\setminus C\); its right-continuous extension is a separate process. No general diffusion coefficient or multi-face derivative transfer is admitted (EXSRC-8165568b79443bb0).
- Andres (2011) is admitted only for Proposition 3.2 same-noise stability in its bounded connected \(C^3\) domain, normal-reflection, additive-standard-noise setup with \(b\in C^1\). The general derivative-identification chain is not part of the admitted use (EXSRC-9cb049bfb70585af).
- Burdzy (2009) is admitted only for Lemma 3.3 uniform-over-starts local-time localization in its bounded smooth-domain normal-reflection setup. Its shape-operator derivative chain is not admitted (EXSRC-06c0e270c3e33ba2).
- Evans–Stroock is admitted only for Theorem 5.4 convergence in law of dyadic linear approximations under its bounded admissible-domain conditions, with \(\sigma\in C^2\) uniformly Lipschitz and \(b\) uniformly Lipschitz. The static-projection and sector-approximation routes are not admitted (EXSRC-9ad8645433f6d2bd).
- Lundström–Önskög remains on hold: the globally uniform full spatial Sobolev-norm condition is unresolved; no application to a static triangle is admitted (EXSRC-b3368137b121a91d).

## A proof line can fail without refuting the theorem

For Atar–Burdzy's 2004 manuscript, the printed fourth-moment estimate in Lemma 1 fails if read for all continuous adapted inputs: with an interior linear path, the two sides scale as \(t^4\) and \(Ct^5/5\). This blocks that printed line as a universal construction estimate. It does not disprove the main theorem. The submitted bounded use derives a separate smooth-unit-disk mirror construction by product-domain reflected-SDE cutoffs; it does not extend that repair to general lip domains or polygon corners (wave08 delta (project review provenance)).
