# Finite zero-loop honeycomb boundary flux

## Certified statement

Let D be a finite simply connected union of equilateral triangles with simple polygonal boundary, and let a be an inward boundary port. Use the zero-loop honeycomb walk convention of the source. For an exiting self-avoiding path γ:a→b, let |γ| be its number of visited triangles and W(γ) its signed turn from the inward direction at a to the outward direction at b. Put

\[
\lambda=\pi/8,\qquad t=3/8,\qquad
\rho=(2\cos\lambda)^{-1}.
\]

Then

\[
 \sum_{b\in\partial D}\ \sum_{\gamma:a\to b}
 \rho^{|\gamma|}e^{itW(\gamma)}=1. \tag{F}
\]

If D is convex, closing γ by the counterclockwise boundary arc gives
\(W(\gamma)=\pi-\operatorname{turn}_{\partial D}(b\to a)\in[-\pi,\pi]\).
Thus \(\cos(tW(\gamma))\geq\cos(3\pi/8)>0\), and taking real parts of (F) yields

\[
 \sum_{b,\gamma:a\to b}\rho^{|\gamma|}
 \leq \frac1{\cos(3\pi/8)}. \tag{U}
\]

## Finite proof ledger

Grow a finite rooted tree of partial paths. At a newly visited vertex, branch into the two allowed continuations with factors \(\rho e^{i\lambda}\) and \(\rho e^{-i\lambda}\). Their sum preserves incoming signed mass because \(2\rho\cos\lambda=1\). Stop a branch when it exits D or would enter an already visited vertex; finiteness of D makes this tree finite.

For a stopped collision, the newly closed cycle is simple and has a disjoint incoming stem. Planarity and the simple boundary ensure the unused continuation at the collision is exterior to that cycle. Reversing the new cycle preserves \(\rho^{|\gamma|}\), pairs collisions without fixed points, and changes the relevant winding increment between \(+4\pi/3\) and \(-4\pi/3\). Their total phase is

\[
 e^{it(4\pi/3)}+e^{-it(4\pi/3)}
 = 2\cos(\pi/2)=0.
\]

All collision leaves therefore cancel. The remaining leaves are exactly the exiting self-avoiding paths, proving (F). Convexity is used only for the turning interval needed for (U).

## Mandatory scope gates

- Keep the triangle-domain, boundary-port, zero-loop, ρ, and phase conventions exactly as above.
- Do not replace the finite cancellation with a positive probability law: individual complex summands are signed.
- Do not use (F) to infer transfer convergence, a finite-size rate, a strip exponent, a bridge estimate, or an infinite-volume identity. Those require additional inputs from the source family.
- For a nonconvex boundary, (F) still has its stated finite scope, but (U) is unavailable without a separately proved phase lower bound.

## Finite input audit

Before applying (F), retain a finite combinatorial embedding: the list of triangular faces, oriented edge incidences, and the marked boundary half-edge. Check that the face adjacency is connected, every interior edge has two incident faces, boundary edges form one simple oriented cycle, and the embedded triangle complex has Euler characteristic one. These finite checks establish the disk/single-boundary hypotheses used by the collision pairing. For (U), also check that every successive oriented boundary turn is nonnegative and at most π; this is a finite convex-polygon test. The walk enumeration must stop before a repeated vertex and assign zero to a completed loop. A different loop fugacity, port normalization, or winding convention is outside this certificate.

## Source check

OpenAI, Critical strip-crossing mass on the honeycomb lattice, fixed openai/math@3344da59991ed94f9ba711217b29c1d760badfa6, SHA-256 33e92f50d83f53439caa07ff0f71472694dc67d6d7c573e28cad30294b3eb1c0, physical PDF pp. 3–4, Lemma 2.1. The local source proof was checked against the extracted physical pages: its finite branching, cycle-reversal cancellation, convex-boundary turning interval, and final unsigned estimate are the only adopted material.
