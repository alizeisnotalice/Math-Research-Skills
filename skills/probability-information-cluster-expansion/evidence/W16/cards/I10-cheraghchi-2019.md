<!-- Card created by W15 after reading the complete shared PDF; review pending. -->

# Mahdi Cheraghchi, “Capacity Upper Bounds for Deletion-type Channels”

- **Identity/version:** Journal of the ACM 66 (2019), extended from STOC 2018; arXiv:1711.01630v4. The official arXiv record and JACM DOI `10.1145/3281275` were checked. Local reader copy: `evidence/fulltexts/I10.pdf`, SHA-256 `d6b511019c184487f3f7fb9ec9c05c3e114313732f22d2ebe76b89b902ab12b3`, 79 PDF pages. W15 read pp. 1–79; no duplicate download.
- **Scope:** Analytic capacity upper bounds for D-repeat channels (each input symbol is independently repeated according to a nonnegative-integer law), with the binary deletion and Poisson-repeat channels as cases. This is a comparison source for B051, not a proof of its higher-order small-deletion expansion.

## Results and proof dependencies

1. **Mean-limited channel dual bound (Theorem 1, PDF pp. 11, 19).** For any proposed output law `Y` and real `ν₀,ν₁`, if every input `x` satisfies
   `D_KL(Y_x || Y) ≤ ν₁ E[Y_x] + ν₀`,
   then the mean-limited channel capacity is at most `ν₁ μ + ν₀`. Equality requires an input distribution inducing the selected output law and equality in the pointwise dual inequality on its support. The proof constructs the output-law-relative-entropy upper bound and applies the mean constraint; the equality characterization is an additional support condition, not automatic from dual feasibility.
2. **Reduction to mean-limited channels (Theorem 4 and Corollary 5, PDF pp. 23–27).** The D-repeat-channel argument separates run lengths into a preprocessor and a run-processor, then bounds the former using the mean-limited channel result. In the source notation, `1−p=P(D=0)`, `λ=E[D]`, and `\bar λ=E[D | D>0]`. Theorem 4 states `Cap(Ch)≤sup_{μ≥\bar λ} Cap(Ch_μ(P))/[1/p+(μ−\bar λ)/λ]`, where `Ch_μ(P)` receives positive integer input `1+x` and outputs `\bar D ⊕ D^{⊕x}`. Corollary 5 states `Cap(Ch)≤sup_{μ≥0} Cap(Ch_μ(D))/[1/p+μ/λ]`. The latter is more convenient but may lose sharpness when the nonzero repetition distribution has substantial entropy. These bounds apply to the stated independent-repeat channel construction, not arbitrary variable-length channels.
3. **Poisson-repeat (Theorems 10 and 17, PDF pp. 32 and 40).** A digamma-family dual output law yields the mean-limited Poisson bound. Combining it with Corollary 5 gives a Poisson-repeat capacity upper bound, with the two source-specified candidate laws and their normalizers. The reported limiting constant near `d→1` is obtained by numerical optimization; it is not a closed-form exact capacity.
4. **Deletion channel (Theorems 26, 34, 35, 38; PDF pp. 47, 57–63).** Inverse-binomial and truncated inverse-binomial dual distributions yield explicit parameterized bounds. Theorem 35 gives
   `C(d) ≤ (1−d) sup_q [−μ(q) log q − log y₀(q)]/[1+μ(q)]`.
   For `d≥1/2`, the source derives the explicit golden-ratio bound `(1−d)log₂ φ`; the extension to `d<1/2` uses a stated convexity assumption for the explicit line. Theorem 38 gives `C(d)≤1−(1−O(d))h(d)/2 = 1−h(d)/2+o(d)` as `d→0` (bits per channel use), with the source's inverse-binomial choice. Preserve the source log/capacity-unit convention when using Theorem 35; Theorem 38 explicitly reports bits.

## What this does not establish

These are upper bounds, not an exact capacity formula. They do not identify a third or later coefficient in the `d→0` expansion, prove convergence of an infinite series, or justify an interchange between a supremum over stationary inputs and a small-`d` limit. The dual distributions and their feasibility conditions must be retained when reusing the bounds.

## Full-text coverage

See `evidence/W16/reading_coverage.json#I10`: PDF pp. 1–79, including introduction/model, the mean-limited duality and multiple-use reduction, D-repeat reduction, Poisson and binomial constructions, deletion bounds, discussion, references, and appendices A–B.
