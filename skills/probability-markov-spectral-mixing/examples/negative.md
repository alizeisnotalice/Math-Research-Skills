# Negative example: invalid static-to-dynamic transfer

> FKG association in a stationary ferromagnetic Ising measure, even when applicable, does not imply that increasing one J_uv increases every fixed-time spin expectation or orders the spectral gap on every graph. GKS/GHS are not admitted source routes in this candidate.

This is invalid. FKG orders stationary increasing observables; it is not a theorem about finite-time semigroup expectations or the second eigenvalue. Shirai proves the fixed-time single-spin assertion can fail on a graph containing a length-3 path. That counterexample does not itself contradict spectral-gap monotonicity. To prove a gap claim, fix the clock and control the changing Dirichlet form and variance (or the relevant eigenvalue branch) directly.

> For an arbitrary finite reversible discrete-time chain, `k>0` (or a positive Poincaré gap below eigenvalue `+1`) automatically gives geometric total-variation mixing.

This ignores the bottom of the spectrum: the simple random walk on a connected bipartite graph can have eigenvalue `−1`, and a nearly bipartite chain can mix slowly despite a good upper-endpoint bound. Use an absolute-gap bound, odd-return paths, an odd-flow comparison, or verify laziness/nonnegative spectrum. Continuous-time Poissonization has a different spectral decay formula and a specified jump-rate normalization.

> Diaconis–Stroock Proposition 6 gives `β₁≤1−h²` for every finite reversible ergodic chain, so that sharper upper bound may always be used.

The paper prints this inequality, but its §3C proof gives only `β₁≤1−h²/2`; moreover an exact four-state reversible, irreducible and aperiodic kernel violates the printed `h²` version. Use the proof-supported factor `1/2` unless independent review finds a missing hypothesis or correction. The exact cut enumeration and eigenvalue comparison are recorded in `evidence/W04/numerical/s027_cheeger_printed_bound_audit.json`.

## Missing hypotheses in the newly matched baseline sources

- W04S013's persistence estimate starts from `pi(·|Psi)` and uses a continuous-time generator with the stated site rate. A point start inside `Psi`, a multi-site event, an event whose exit rate exceeds one without rescaling, or discrete-time eigenvalues placed directly into the exponential does not meet this premise.
- W04S014's sufficient norm condition is clock- and orientation-specific. A failed `||R||_1<1` check does not prove slow mixing, and scan time is counted in whole scans rather than single updates.
- W04S015's accepted censoring comparison uses an exogenous schedule at a fixed stationary law and the source's monotone heat-bath hypotheses. Its initial-law premise is a top state or increasing `mu0/pi`; it does not certify state-adaptive schedule choice or arbitrary initial distributions.
- W04S016 is an all-plus, zero-field, ferromagnetic, uniform random-site lower bound for sufficiently large `n`, with specific LPW/Nacu inputs. It is not a bound for every start, field, or update clock.
- W04S018 uses odd `n` and a global-spin-flip quotient. The scalar chain alone supplies only the upper comparison; the accepted lower comparison uses the source conditional update and the separately derived `c/n` bound.
- W04S019's tree criterion is sufficient, not necessary. Failure of `gamma*kappa*b<1` does not establish slow mixing, and the row does not admit an entropy or log-Sobolev conclusion.
- W04S020 depends on critical two-dimensional RSW/FK and the stated block comparison. It does not transfer to general graphs or higher dimensions, and the exponent `C` is unspecified.

The exact conditions and proof dependencies for all 37 currently accepted works are in the linked 37-work accepted-use register（本机附件：`references/accepted_scope_register.md`）. All 30 original baseline works now have a matched high-scoped use, but only within the exact row interfaces in the register; whole-entry approval remains pending.

- W04S021's shared barrier coupling controls a local approximation under its torus/core/collar scales; it does not itself imply SSM-to-cutoff or arbitrary-boundary replacement.
- W04S022 requires a finite-cube density with real symmetric `0≤J<I` and the conditional-variance heat-bath form. The retained proof uses its named localization inputs and loose `T≤Tr J` bound; it does not extend to non-PSD or norm-large `J`.
- W04S023 requires the source's pinwise spectral-independence premises on feasible pinnings. Do not replace them by an unpinned-only condition or promote the exact `κ` route into the excluded final degree-dependent constant.
- W04S024 needs the minimum over all feasible pinned chains and the original `n`-coordinate clock, where frozen coordinates still count as holds. Dropping either changes the comparison.
- W04S025 is for a fixed `theta` and the order-statistic inner chain. It does not establish convergence of the outer nonlinear map or classify stationary laws for all `j,k`.

## Missing-condition examples for the final five source rows

- **Aldous (W04S028):** a periodic discrete-time chain cannot be inserted into the continuous-time Proposition 8 estimate by replacing `t` with a number of steps; the source row requires its continuous-time generator/semigroup and clock.
- **Chen–Wang (W04S029):** replacing the minimum-mass cut denominator by a product-mass denominator, adding killing, or dropping the verified exit-rate bound `M` leaves the accepted inequality unsupported.
- **Dyer–Goldberg–Jerrum (W04S031):** an ordinary flow alone compares `E`; it does not rule out a negative eigenvalue near `−1`. A bipartite chain is the standard boundary example, so the odd-flow/`F` condition is needed for the lower endpoint.
- **Sambale–Sinulis (W04S032):** hard constraints with zero conditional probabilities fail the accepted positive lower bound `α₁>0`; the full-support theorem cannot be applied as stated.
- **Paulin (W04S033):** a nonstationary initial law does not meet the row's `X₁~π` premise; neither a Bernstein bound nor nonstationary variance control follows from equations (3.14)/(3.16) alone.

These are scope checks, not claims that the source proves a counterexample to an unreviewed extension.
