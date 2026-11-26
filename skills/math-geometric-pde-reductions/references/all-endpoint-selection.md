# All-endpoint representative selection

**Source.** OpenAI, *Uniqueness of tangent flows at the first singular time of embedded surface mean-curvature flow*, Lemma 2.1, PDF pp. 5–6, pinned source commit `3344da59991ed94f9ba711217b29c1d760badfa6`, SHA-256 `19b2f77a4cbfb0d5180a6456312c545da5be942f849ca7f7fad31b1af2566a8a`. The pinned PDF is [available here](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Tangent-flow-uniqueness-2026-09-24/paper.pdf).

## Transfer statement

Let `I` be an open interval. Let `mu_t` and `nu_t` be Radon measures, defined for every `t in I`. Suppose, for each nonnegative `phi in C_c^2(R^3)`, that `beta_phi in L^1_loc(I)` and that for all `a<b` in `I`

```text
mu_b(phi)-mu_a(phi) <= int_a^b beta_phi(t) dt,
nu_b(phi)-nu_a(phi)  = int_a^b beta_phi(t) dt.
```

If `mu_t=nu_t` for a.e. `t`, then the equality holds for every `t`.

## Independent proof

Subtract the second endpoint identity from the first and put `h_phi(t)=mu_t(phi)-nu_t(phi)`. The displayed inequality says precisely that `h_phi(b)<=h_phi(a)` whenever `a<b`; it is therefore nonincreasing. Let `G_phi` be the full-measure set where `mu_t=nu_t`. For each `s in I`, openness of `I` and full measure of `G_phi` give `a in G_phi` and `b in G_phi` with `a<s<b`. Thus

```text
0=h_phi(a) >= h_phi(s) >= h_phi(b)=0.
```

Hence `mu_s(phi)=nu_s(phi)` for every nonnegative compact smooth `phi` and every `s`. This class determines locally finite Radon measures (for example, approximate compactly supported continuous nonnegative functions from below and above by smooth compact functions). Therefore `mu_s=nu_s` for every `s`.

## Brakke instantiation and boundary

For the source's smooth homothetic shrinker, `beta_phi(t)=integral (grad phi dot H_nu - phi |H_nu|^2) dnu_t`. Its all-endpoint closed-slab Brakke inequality, used with a time-independent test, supplies the first endpoint inequality. The source's local `(1+|H|^2)` spacetime integrability on compact cylinders is what makes that reduction meaningful; properness and smoothness of the shrinker supply the comparison transport identity. These are independent prerequisites, not conclusions of the selection argument.

The proof fails to determine a value at an exceptional time if endpoint inequalities are unavailable there. It also fails for a test class that does not determine Radon measures, or if the smooth comparison identity has a different right-hand side. This transfer is deliberately silent on the source's subsequent tangent-flow compactness and uniqueness results.
