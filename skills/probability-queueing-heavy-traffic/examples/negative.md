# Missing-condition example: sampled-drift sublevel inclusion

The accepted W14-024 use card（本机附件：`cards/uses/W14-024.md`） permits Theorem 3.1 only after independently verifying its global sampled-drift, finite `W >= delta_0`, and closed-petite conditions. Its source main fluid-to-stochastic application is not admitted. In particular, `W(x) <= |x|` does not imply `{W <= kappa} subset {|x| <= kappa}`.

The exact diagnostic in the R06 script（本机附件：`examples/evidence/r06_batch03_next8_local_checks.py`） takes `|x|=3/2`, `W(x)=|x|/2=3/4`, and `kappa=1`. Then `W(x) <= kappa` holds while `|x| <= kappa` fails, so the claimed set inclusion is false. The saved result（本机附件：`examples/evidence/r06_batch03_next8_local_checks.result.json`） records this rational witness. It diagnoses the missing hypothesis in that source application; it is not a queueing-network instability example and does not invalidate the separately guarded Theorem 3.1 interface.
