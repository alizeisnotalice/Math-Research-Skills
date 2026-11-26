# Chaise Longue: algebraic matching quotient

## Source and audit

- Rafael Amichis Luengo, *The Chaise Longue Theorem*, v12, 4 October 2026, 82 pages; local-source SHA-256 `1334d04bfd19dfeca0593a9fdedb31c1dae747915e493922862f7c1c7e56c056`.
- Status in the source: unrefereed public preprint. The public repository reports a Lean project and automated builds, but this review did not pin a revision, obtain a trusted build environment, or replay a build. Therefore no machine-checking claim is promoted beyond the source report.

## Scoped algebraic statement

The source labels its topology-free core `Main Theorem'`: for the precise Degtyarev--Shimada group ring `R`, its full family of matching generators `psi_J`, and the source count `Q_k(m)`, it asserts for every `m >= 3` and `k >= 1` that

`R / (psi_J : J in J)`

is free abelian of rank `m^(2k+1) - Q_k(m)`. Its proof route is characteristic-by-characteristic: compare the quotient dimensions in prime characteristic with the characteristic-zero rank and rule out torsion. The even-degree branch uses the printed odd-box/interlaced-down-set result and the full matching family; replacing that family is outside the theorem's scope.

## Boundary of use

Treat this statement as a caller-certified lemma unless the exact source definitions, all finite ideal/dimension steps, and (when wanted) a pinned Lean build have been independently checked. It is not a proof of the geometric identification between the group-ring quotient and Fermat homology. The source itself reserves that bridge to the cited work of Pham and Degtyarev--Shimada.

## Follow-up needed for proof-level deployment

Pin the public repository revision, record Lean and Mathlib versions, rebuild its declared target, and compare the elaborated theorem statement with the caller's `R`, `psi_J`, matching family, and `Q_k(m)`. Independently audit the Pham and Degtyarev--Shimada hypotheses before deriving a topological or integral-Hodge result.
