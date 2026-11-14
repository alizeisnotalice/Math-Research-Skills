# Positive pattern: preserve the variance budget

For a martingale with centered increments bounded by one, set S_n=ΣΔS_k and V_n=ΣVar(ΔS_k|F_{k−1}). If the event is that S crosses a before V exceeds b, Freedman Theorem 1.6 gives P(exists n:S_n≥a,V_n≤b)≤exp(−a²/(2(a+b))). Apply only after verifying the filtration, centering, increment bound and predictable variance.

Exact enumeration for a symmetric random walk at N=4 found P(max_{k≤4}S_k≥2)=3/8. With a=2,b=4 the coarse bound is exp(−1/3)=0.716531310574. The script and output are in evidence/W02/examples/. The computation checks one finite case; the proof is the cited theorem card.

For a separate sub-Gaussian line crossing, enumerate 12-step Rademacher paths with a=b=1/2 and V_k=k. The exact finite-horizon probability of ever crossing S_k≥a+bV_k is 69/128=0.5390625, below Howard et al.'s all-time bound exp(−2ab)=0.606530659713. See `evidence/W02/examples/s006_rademacher_line_crossing.py` and its output. This verifies only the finite case and does not prove the general bound.

For S007, the exact five-step symmetric-walk probability of ever reaching level 3 is 7/32=0.21875. With [S]_k≤5, V=0 and λ=3/5, the displayed normalizer is numerically 0.990183783462 and the variance-budget bound is exp(−9/10)=0.406569659741. The script is `evidence/W02/examples/batch4_martingale_checks.py`; this checks one finite instance only.

For the C207 mapping, SymPy evaluates S024's sharp scalar component constant at p=4 as cot(π/8)=1+√2≈2.4142. The d=4 componentwise estimate gives at best 2cot(π/8)≈4.8284. This illustrates the dimension-loss gap and proves no exact vector constant; see the saved batch-4 output.


For a family of stochastic convolutions in a 2-smooth Banach space, first record $D$, the progressive γ-radonifying integrands, contractive semigroups and time horizon. Then use Cox–van Winden Theorem 3.1 with the countable weight $\sqrt{p+\log j}$. For their discrete martingale version, check conditional symmetry and retain the different weights $p+\log j$ for the increment maximum and $\sqrt{p+\log j}$ for the conditional-square sum. See W02-S025 and its rendered theorem page p. 10.

For a finite-grid stopping dual, normalize the martingale to start at zero, compute the Snell envelope and its Doob martingale, then state whether the candidate is weakly or surely optimal. S029's randomized strictness theorem needs independent centered ξ_j supported on $(-\infty,1]$ with a joint continuous density positive at 1; it is not an arbitrary perturbation argument.


For A007, use Aldous only as a conditional process-convergence step. If a model proof has already produced real-valued (D)-martingales with f.d.d. convergence to a continuous limit and UI at each fixed time, Proposition 1.2 yields (J_1) convergence. If the target process is not a martingale, verify Proposition 2.2's full stopping-time (Gamma) condition instead. The model must establish these hypotheses itself.
