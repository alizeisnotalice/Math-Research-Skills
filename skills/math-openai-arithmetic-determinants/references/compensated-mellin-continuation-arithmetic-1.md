# Compensated Mellin continuation contract

Source SHA-256: `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7` (199 physical pages; Wave 4 index checked). Physical p.5 gives the common-continuation contract, p.71 isolates the principal row and factor `H_eta`, and p.85 assembles the strict `Re(s)>11/12` conclusion.

The source's continuation mechanism compares a normalized character sum with a Mellin integral containing `1/L_F(s,eta)`, after deletion of finitely many Euler factors and multiplication by a holomorphic factor bounded away from zero. Both a direct bound and a power-saving comparison must have positive margins independent of the target character; fixed-character constants and thresholds may depend on it. For the principal-row normalization, it defines `H_eta(s)` and chooses the finite enlargement of `S` so that `sup_{Re(s)>7/8}|H_eta(s)-1|<=1/2` (equation (10.2)).

At p.85 it records the 11/12 assembly from the stated low/high bounds, with target-independent positive losses. Use this only as an explicit checklist for a supplied continuation proof; it does not certify a zero-free region merely from a numerical character-sum experiment.

## 固定来源

- 物理页 5, 71, 85。Proof overview (p.5), principal-row normalization (p.71), and Theorem 3.1 assembly (p.85) SHA-256 `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`。[The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $`\Re s\gt 7/8`$ ](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
