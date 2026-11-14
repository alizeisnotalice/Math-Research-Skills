> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see review index (historical project reference; target is outside the runtime package).

# PGEL-005 — Sufficiently dense Kuramoto networks are globally synchronizing

## Identity and reading record

- Martin Kassabov, Steven H. Strogatz, and Alex Townsend. Source read: arXiv:2105.11406v1 (submitted 24 May 2021), [official arXiv record](https://arxiv.org/abs/2105.11406); published DOI recorded by D02: [10.1063/5.0057659](https://doi.org/10.1063/5.0057659). This card describes the exact 6-page arXiv author version, not a line-by-line journal comparison.
- Local PDF: `../pdfs/PGEL-005.pdf`; SHA-256 `cb25a266410f4be91663f2ba0e515164fb55e1c3170a83bd5b8984cbfad9223d`.
- Strict PDF parse, page count, and hash checked. Read all 6 physical pages, including the full discussion and references. Rendered PDF p. 5 to verify Lemma 4 and Theorem 5, including the strict threshold. Coverage is in `../reading_coverage.json`.
- Review pending.

## Model and threshold

The model is the homogeneous Kuramoto system on an arbitrary simple undirected graph with symmetric positive unit edge weights and no self-loops; identical intrinsic frequencies are removed by a rotating frame. Let \(d_{\min}\) be the minimum degree and \(\mu=d_{\min}/(n-1)\). The paper introduces loops for proof convenience and writes \(\widetilde\mu=(\mu(n-1)+1)/n\); adding a self-loop to each vertex does not change the ODE. “Globally synchronizing” means convergence to in-phase synchrony from almost every initial phase, not from every initial condition.

**Theorem 5 (PDF p. 5).** In the looped convention, if \(\widetilde\mu>3/4\), then the only stable equilibrium is the all-in-phase state. Equivalently, in the original loopless convention the sufficient strict condition is
\[
\mu>\frac{3n/4-1}{n-1}=\frac{3n-4}{4(n-1)}.
\]
This gives the asymptotic critical-connectivity upper bound \(\mu_c\le3/4\). At finite \(n\), retain the strict inequality above; do not replace it by \(\mu\ge3/4\) without checking the integer degree condition.

## Proof dependency and limits

Lemma 1 bounds the missing-edge contribution using equilibrium and nonnegative Hessian diagonal entries; Corollary 2 says a stable state with \(\rho_1>\sqrt2(1-\widetilde\mu)\) must be synchronous. A moment inequality then relates \(\rho_1\) and \(\rho_2\). Lemma 3 supplies a lower bound on \(\lvert\rho_2\rvert\); Lemma 4 proves \(\lvert\rho_2\rvert\ge1/2\) when \(\widetilde\mu>3/4\). Combining this with the moment inequality gives \(\rho_1^2\ge1/8>2(1-\widetilde\mu)^2\), so Corollary 2 applies. The saved SymPy calculation verifies the exact algebraic conversion between the looped and loopless strict thresholds; it is not a substitute for this proof.

The theorem is deterministic and applies to every graph meeting the minimum-degree condition; it is not itself a random-graph theorem. The paper explains that a sequence of twisted states with multiple zero eigenvalues makes improvement by this style of linear stability analysis difficult. Section VI gives only a rough, explicitly non-rigorous sketch of possible four-cluster patterns just below \(0.75\); it does not prove that such patterns exist. The cited lower bound \(0.6838<\mu_c\) is prior work, not proved here. This source concerns positive undirected coupling only; it does not transfer to signed or oriented models.
