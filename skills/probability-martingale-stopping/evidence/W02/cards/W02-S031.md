# W02-S031 — Paul M. N. Feehan and Camelia Pop, “On the martingale problem for degenerate-parabolic partial differential operators with unbounded coefficients and a mimicking theorem for Itô processes”

## Identity and reading evidence

Local original: arXiv:1211.4636v3, dated 7 Aug 2013, 27 physical PDF pages; SHA-256 `838e89ac3ef9070a523b1211f3e1ae66afa7eafbd7f4325f94dcca2a97414c38`. All physical pages 1–27 were read. Rendered and visually inspected PDF pp. 3, 6, 12–13, 19, and 24, covering the main statement, assumptions, companion PDE theorem, and uniqueness/mimicking proof. Review remains pending.

## Martingale-problem setup and well-posedness

The state space is the half-space $H=\mathbb R^{d-1}\times(0,\infty)$. The time-inhomogeneous operator has the form

\[
\mathcal A_t v(x)=\tfrac12 x_d\sum_{i,j}a_{ij}(t,x)\,\partial_{ij}v(x)
+\sum_i b_i(t,x)\,\partial_i v(x).
\]

On canonical $C_{\rm loc}([0,\infty);\bar H)$, Definition 1.1 (PDF p. 3) requires, for every $v\in C_0^2(\bar H)$, that $v(X_t)-v(X_s)-\int_s^t\mathcal A_uv(X_u)du$ be a continuous martingale under the augmented, right-continuous canonical filtration; paths are fixed at the initial point through $s$. Theorem 1.3 states uniqueness in law for every $(s,x)\in[0,\infty)\times\bar H$ when Assumption 2.2 holds.

Assumption 2.2 (PDF p. 12) uses constants $\delta,K,\nu>0$ and $\alpha\in(0,1)$: the zeroth-order coefficient is bounded above by $K$ and the normal drift satisfies $b_d(t,x',0)\ge\nu$; near the boundary $x_d<2$, $a$ is uniformly elliptic and $a,b,c$ are bounded and locally Hölder in the cycloidal metric; away from the boundary, $x_da$ is uniformly elliptic and $x_da,b,c$ are locally Hölder in the parabolic metric. These hypotheses imply at most linear growth for $x_da,b,c$. In the martingale generator the second-order coefficient is $x_da$; the factor convention is fixed by (1.1), with the paper noting where $1/2$ is absorbed in the PDE coefficient.

Theorem 1.11 (PDF pp. 5–6) separately gives weak existence, uniqueness in law and the strong Markov property for the associated degenerate SDE under Assumption 1.8. The paper's proof route is PDE regularity: Theorem 2.5 (PDF p. 13) is recalled from companion paper [26], not proved here; it supplies a unique weighted-cycloidal Hölder solution and an a priori estimate for the degenerate parabolic equation, without a separately prescribed condition on the degenerate boundary portion.

## Proof architecture and mimicking theorem

Section 3.1 (PDF pp. 13–16) extends coefficients and proves the state-space invariance/existence steps. Section 3.2 (pp. 16–24) uses the PDE solution in a duality argument to identify one-dimensional marginals and prove uniqueness/strong Markov: because the relevant second derivatives are only controlled after multiplication by $x_d$, the proof shifts the process by $\varepsilon$, applies ordinary Itô's formula, localizes and passes $\varepsilon\downarrow0$. Time augmentation converts the inhomogeneous problem into a homogeneous one for the Markov argument.

For the mimicking result, the input is an Itô process with adapted drift $\beta$ and diffusion coefficient $\xi$ satisfying

\[
\mathbb E\int_0^t\bigl(|\beta_s|+|\xi_s\xi_s^*|\bigr)ds<\infty\quad(t\ge0),
\]

a deterministic initial point $x_0\in\bar H$, and $X_t\in\bar H$ a.s. Define measurable conditional coefficients $b(t,x)=\mathbb E[\beta_t\mid X_t=x]$ and $x_da(t,x)=\mathbb E[\xi_t\xi_t^*\mid X_t=x]$. If $(a,b)$ satisfy Assumption 2.2 and the chosen square root $\sigma$ obeys (1.8)–(1.9), Theorem 1.13 (PDF pp. 6, 24–25) says the unique weak solution of the corresponding mimicking SDE has the same one-dimensional marginals as the input process. Section 3.3 proves this by applying the conditional-expectation Itô identity to the source process and comparing the resulting backward PDE identities.

## C112 auxiliary boundary

This source is now linked as auxiliary evidence for C112 only. It provides a specialized well-posedness route for a boundary-degenerate diffusion on a half-space with inward normal drift, cycloidal/parabolic Hölder regularity and linear-growth control. It does not establish tightness, generator convergence, uniqueness or variance positivity for the separate conditioned unbounded-path model; those remain unproved interfaces.

## Limits on use

The martingale problem is tied to the specified half-space, test class, canonical usual filtration, coefficient regularity and non-explosion/moment controls. The mimicking theorem preserves one-time marginals, not path law. The needed PDE existence theorem is imported from [26], so this paper's argument depends on that companion result. `reading_coverage.json` records the complete section/appendix map.
