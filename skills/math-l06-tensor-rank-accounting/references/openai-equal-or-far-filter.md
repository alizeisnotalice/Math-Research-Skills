# Equal-or-far finite-field filter

OpenAI, *The logarithmic exponent of integer multiplication on tapes*, physical p.8, SHA-256 `238c2cb21352a0fa6aeb2d694fa9a8cae5fae8f0186897222f1c6b911f69daff`.

For an odd prime `p`, alphabet size `q`, and inner Hamming distance `0 <= d <= 2p-1`, use the element `P0(d)=1-d^(p-1)` in `F_p`. Fermat's theorem makes it one exactly for `d=0` or `d=p`, and zero otherwise. The source expands `d` as coordinate-inequality indicators to obtain its stated bounded-term tensor-rank accounting, then gives a binary-prefix rectangle labeling for ordered distinct symbols.

Run `scripts/check_equal_or_far_filter.py p q` to exhaustively verify this finite filter at small parameters. This check does not calculate the manuscript's tape layout, rectangle incidence asymptotics, or multiplication exponent.

## 固定来源

- 物理页 8。Finite-field equal-or-far filter and rectangle-label construction. SHA-256 `238c2cb21352a0fa6aeb2d694fa9a8cae5fae8f0186897222f1c6b911f69daff`。[The logarithmic exponent of integer multiplication on tapes](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-logarithmic-exponent-of-integer-multiplication-on-tapes-November-24-2026/paper.pdf)
