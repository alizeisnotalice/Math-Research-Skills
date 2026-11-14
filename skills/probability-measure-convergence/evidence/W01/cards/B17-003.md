# B17-003 — Thomas G. Kurtz, “The Yamada-Watanabe-Engelbert theorem for general stochastic equations and inequalities” (2007), version-family dependency

## Identity and scope

- *Electronic Journal of Probability* 12 (2007), paper 33, pp. 951–965; DOI [10.1214/EJP.v12-431](https://doi.org/10.1214/EJP.v12-431).
- Local file: complete 15-page article; title/author/venue/pages/DOI match the first page and references. SHA-256: `7dad2706b8719609a6b9e6bd5059b9bd7f4eed287683cc9d2985938c15e5603a`.
- Full physical pages 1–15 were read, including the entire appendix and references. Rendered and visually inspected pp. 7 and 9 for the compatibility lemma and Theorem 3.14.
- This paper is a full-text-read **dependency document**, not an independent source-count item: Kurtz 2014, p. 1, identifies that article as an “essentially a rewrite” and 2014 cites 2007 again for the randomization factor lemma. The 2007/2014 pair contributes at most one independent work pending version-family audit.

## Relevant statements and version comparison

Section 2 (pp. 3–6) treats simple equations `Γ(X,Y)=0` on Polish spaces. Proposition 2.10 (pp. 5–6) states equivalence of pointwise uniqueness, the per-law variant, joint uniqueness in law, and uniqueness in law in this equation setting. The proof of uniqueness-in-law ⇒ pointwise uniqueness does not follow from convexity alone: given two solutions `(X₁,Y)` and `(X₂,Y)`, it chooses a measurable `f` separating them with positive probability and sets `X` equal to whichever of `X₁,X₂` has the larger `f`-value. Since `Γ(Xᵢ,Y)=0` pointwise, this measurable pasting still satisfies `Γ(X,Y)=0`, while its `f(X)=max(f(X₁),f(X₂))` law differs from either candidate law. The source says on p. 6 that if the equation is replaced by an arbitrary convex set of joint laws with fixed input marginal, all results except Proposition 2.10 continue to hold; there only (a)⇔(b), (a)⇒(c), and (c)⇒(d) remain. Thus the full equivalence uses the equation model’s pasting closure and cannot be inferred for a general convex law set. This is not the theorem for an arbitrary compatible process law.

Section 3 defines temporal compatibility in Definition 3.1 (p. 6) by the conditional-expectation identity, and its general compatibility structure in Definition 3.3 (p. 6). Lemma 3.2 (p. 6; continued p. 7) prints the statement that compatibility is equivalent to every `F^Y`-martingale being an `F^{X,Y}`-martingale. The 2014 paper explicitly corrects this: only compatibility ⇒ the martingale condition holds in general; the reverse implication needs a separate partial-compatibility/uniqueness argument. Do **not** transfer the 2007 “iff” as a general theorem or interface.

**Theorem 3.14 (pp. 9–10).** Assuming the nonempty compatible solution-law set `S_{Γ,C,ν}`, it equates (a) pointwise uniqueness for compatible solutions and (b) joint uniqueness in law for compatible solutions plus existence of a strong compatible solution. This older theorem is stated inside the compatible, convex-law framework set up in §3. Kurtz 2014 Theorem 1.5 (pp. 3–4) instead gives a more abstract equivalence for arbitrary constraint sets without convexity or compatibility; §2 compatibility lemmas then connect that result to classical SDE settings. These scopes must not be conflated.

Appendix Lemmas A.1–A.2 (pp. 13–14) provide the measurable randomization and factorization steps used in the 2014 proof: a joint law with fixed input marginal can be sampled as `F(Y,ξ)`; if two independent-randomizer realizations agree a.s., their common value is measurable in `Y`.

## Coverage and migration limit

The full section map (front matter/introduction, §2, §3, examples, Appendix A, references) is in `../reading_coverage.json#sources.B17-003`. Use the 2007 article only to identify the earlier formulation and a cited technical lemma. Where it conflicts with the explicit 2014 correction, use the corrected 2014 statement and preserve the fact that 2007 printed the false iff. Review status: pending.
