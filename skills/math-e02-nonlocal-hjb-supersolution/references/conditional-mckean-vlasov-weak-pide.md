# Conditional weak Fokker--Planck PIDE with common noise

Use this component only to pass from a specified conditional McKean--Vlasov jump SDE to its weak, test-function formulation.  It is not a density theorem or a nonsmooth HJB verification rule.

## Certified conditional statement

Let `B1` be the common Brownian motion, independent of the idiosyncratic noises and jump measures, and let
`mu_t = Law(X_t | F_t^B1)`.  The caller must supply a well-defined SDE, predictable coefficients, and the integrability and domain conditions needed for jump Itô's formula.  For every bounded `C^2` test function for which the generator terms are integrable, the source derives

```
<mu_t, phi> = <mu_0, phi>
  + integral_0^t <mu_s, A0 phi> ds
  + integral_0^t <mu_s, A1 phi> dB1_s.
```

Here `A0` contains the drift, diffusion, and compensated jump generator, while `A1` is the common-noise first-order operator.  This is a distributional identity; use it only after writing the caller's truncation and compensation convention into `A0`.

For a jump displacement `gamma`, use the pushforward definition

```
<mu^(gamma), g> = integral g(x + gamma) mu(dx).
```

No absolute-continuity relation between `mu^(gamma)` and `mu` follows.  In particular, translating a point mass by a nonzero vector gives a mutually singular point mass.  The source's assertion of automatic absolute continuity immediately after (3.3) is false and is not part of this component.

## Verification boundary

The displayed weak identity is obtained in the source by jump Itô calculus, conditional expectation onto the common-noise filtration, and Fourier uniqueness of distributions.  It imports the jump Itô theorem rather than reproving its domain or integrability conditions.  Before relying on it, establish for the supplied model:

- the conditional-expectation and stochastic-integral projection identities;
- all jump-integrability, localization, and generator-domain conditions;
- a separately stated uniqueness theorem if uniqueness of the PIDE is needed.

Do not infer a density equation, absolute continuity, a viscosity comparison theorem, or an HJB result from this weak identity.  The source itself assumes, rather than proves, uniqueness in the jump setting; its smooth-feedback HJB argument has additional Dynkin and smooth-maximizer assumptions.

## Provenance

- N. Agram, B. Øksendal and A. Proske, *Stochastic Fokker--Planck PIDE for conditional McKean--Vlasov jump diffusions and applications to optimal control*, arXiv:2110.02193v4 (2023), Theorem 3.3 and proof, physical pp. 7--11; uniqueness discussion p. 12.
- Primary record: <https://arxiv.org/abs/2110.02193>.
