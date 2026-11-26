# Trace-cone alignment and approximate-intertwining reference

**Source.** *The trace cone classifies Razak–Jacelon stabilizations*, OpenAI (25 September 2026), physical pp. 8, 28, and 59–60, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026/The-trace-cone-classifies-Razak-Jacelon-stabilizations-September-25-2026.pdf), SHA-256 `9cf38a67706f91fa455d81f1b60ed1c2bc9c591dacb0f36cbf17c17fb7e81bca`.

For a positive element, the source records the rank-cut and trace formulas
\[
 d_\tau(a)=\sup_{\varepsilon>0}d_\tau((a-\varepsilon)_+),\qquad
 \tau(a)=\int_0^{\|a\|}d_\tau((a-t)_+)\,dt.
\]
For finitely many positive tests \((s_i,\gamma_i)\) with finite designated ranks, equal pullbacks permit a unitary \(u\in U(M_2(C)^{\sim})\) for which
\[
 (\gamma_i\otimes\operatorname{Tr}_2)\bigl(|u(p(s_i)\oplus0)u^*-(q(s_i)\oplus0)|^2\bigr)<\delta.
\]
The theorem-level endgame chooses summable tolerances \(\varepsilon_n\), alternately conjugates maps so that the two composition errors on growing finite sets are below \(\varepsilon_n\), and takes point-norm limits.  Use this as a certificate template: give the finite test lists, each tolerance, each unitary adjustment, and the summable error ledger.  Its trace-cone/Cuntz-semigroup hypotheses and the required unitary-alignment result must be checked independently.
