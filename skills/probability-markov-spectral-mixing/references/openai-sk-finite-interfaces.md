# OpenAI SK finite interfaces

These are conditional interfaces from the cited drafts.  They are not a
spectral-gap, cutoff, or worst-start mixing certificate.

## Balanced-cut pruning for typical starts

For a finite reversible continuous-time chain with strictly positive `pi`,
exit-rate bound `R`, `0<epsilon<1/3`, and certified cut flux
`Q(S,S^c)>B` for every `epsilon<=pi(S)<=1-epsilon`, the draft states

`sum_x pi(x) ||P_T(x,.)-pi||_TV <= sqrt(2 R H(pi)/B) / sqrt(T) + 2 epsilon`.

Keep the quantifier on balanced cuts and the `pi`-average: this is neither a
conductance bound for all cuts nor a worst-start estimate.

Source: *A typical-start upper bound for low-temperature SK Glauber dynamics*,
SHA-256 `a4a9ccfe1526c056978ba2bf9bd482e78438115e8116c2a525082f2027cfa690`,
physical pp. 19--20, Lemma 8; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/paper.pdf).

## Scalar relative-Gaussian entropy guard

For `0<j<1`, `s>0`, a law `P` with finite second moment, and
`s >= j E_P[tanh(Y)^2]`, define `q=E_P[tanh(Y)^2]`,
`b=1-q`, `a=E_P[(Y-d)tanh(Y)]`, and `S=s+jq`.  The claimed usable lower
bound is

`D(P || N(d,s)) >= j (a-s b)^2 / (2 s S)`.

Require finite relative entropy before invoking an equality clause; do not
reinterpret this scalar inequality as an SK spectral-gap proof.

Source: *A spectral gap throughout the high-temperature Sherrington–Kirkpatrick
phase*, SHA-256 `d1eccdc9781a9cf3ea3ff54891d8288f8ab77fad5be4f539c6ddae1d67a98bb6`,
physical p. 22, Lemma 4.1; [pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/main.pdf).
