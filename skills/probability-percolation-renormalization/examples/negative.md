# Negative example: threshold gap and model mismatch

**Input.** “Every 2D subcritical update family has an exponential infection-time tail for all q>q_c because Hartarsky proves exponential decay.”

**Why this inference fails.** The read theorem gives exponential one-arm decay above \(\widetilde q_c\), with \(q_c\le\widetilde q_c\); it does not establish equality for every family. Below \(\widetilde q_c\), the paper proves a polynomial lower tail for the infection time. Unless the parameter lies above \(\widetilde q_c\), or an additional theorem identifies the thresholds, the requested range q>q_c is not covered. Also verify the finite-volume event and infection-density convention.

**Another invalid upgrade.** Exhaustively checking graph-bootstrap instances for n≤6 can match \(M_{K_4}(n)=n-3\) on those sizes. It cannot prove the all-n identity; that is supplied by the source’s induction proof, not the enumeration.
