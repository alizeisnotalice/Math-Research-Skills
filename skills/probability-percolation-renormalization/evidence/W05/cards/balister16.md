# balister16 — Subcritical U-bootstrap percolation

**Reading status:** `fulltext_read`; complete 27-page article read (PDF pp. 1–27). The main theorem, update-family definitions, multiscale barrier/triangle-cover proof, symmetric special case, and open-problem discussion were followed in the text. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** Paul Balister, Béla Bollobás, Michał Przykucki, and Paul Smith, “Subcritical U-Bootstrap Percolation Models Have Non-Trivial Phase Transitions,” *Transactions of the AMS* 368(10) (2016), 7385–7411, DOI [10.1090/tran/6586](https://doi.org/10.1090/tran/6586), arXiv [1311.5883](https://arxiv.org/abs/1311.5883). Local PDF SHA-256: `7eff74194c26a771125ef87b41a2a68d949c52c1b1402788f71e44b1419fe9d2`.

## Model and theorem

An update family `U={X_1,…,X_m}` is a finite collection of finite nonempty subsets of `Z²\{0}`. Starting from an iid Bernoulli-`p` infected set `A`, a site `x` is added if `X_i+x` is already infected for some rule `X_i`; write `[A]` for the eventual closure. The stable set `S(U)` consists of directions whose discrete half-plane remains closed. In two dimensions, “subcritical” means every open semicircle intersects the interior of `S(U)`, equivalently there are three strongly stable directions whose convex hull contains the origin in its interior.

Theorem 1 (PDF p. 4) proves, for every subcritical finite update family,

\[
\mathbb P_p(0\in[A])\longrightarrow0\quad(p\downarrow0),
\]

and hence `p_c(Z²,U)>0`; it further states `p_c(Z²,U)=1` iff `S(U)=S¹`. Combined with the preceding Bollobás–Smith–Uzzell classification that critical and supercritical families have `p_c=0`, Corollary 2 (PDF p. 4) characterizes `p_c>0` exactly by subcriticality. This is a positivity/nontriviality result for two-dimensional update families, not an exponential infection-time tail.

## Proof mechanism and limitations

The proof chooses three strongly stable directions with a positive linear dependence and constructs slightly perturbed finite triangles that remain `U`-closed. A multiscale tiling of `Z²` uses rapidly growing square scales `Δ_i`, declares squares good when smaller bad squares are sufficiently isolated, and constructs thick healthy barriers through good squares. Inductively, each bad square nested in a good square is enclosed by a robust triangle; the triangle family is nested or well separated, contains every eventually infected site, and has probability tending to zero of covering the origin as `p↓0`. The first-moment/renormalization bound then rules out percolation at small `p`. The main technical work is the barrier construction and the triangular-cover theorem (Theorem 6, §5, PDF pp. 15–22); the paper separately gives the easier oriented-percolation coupling for symmetric families in §6.

For the directed triangular bootstrap example, Corollary 3 (PDF pp. 4–5) gives a very small positive lower bound and an oriented-site-percolation upper bound; the authors report a computer-experiment estimate only as heuristic and warn that such predictions have historically been inaccurate. Do not promote that estimate to theorem. The proof depends on the stable-direction geometry and multiscale barriers, so neither the theorem nor its constants transfer to other dimensions, random hosts, synchronous graph-bootstrap edge infection, or a generic `q_c`-to-exponential-decay claim.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/balister16`).
