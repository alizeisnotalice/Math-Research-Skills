<!-- Reader: W15; complete 55-page combined corrected reprint read; review pending. -->
# Claude E. Shannon (1948), “A Mathematical Theory of Communication”

- **Identity and copy read:** *Bell System Technical Journal* 27 (1948), July installment pp. 379–423 and October installment pp. 623–656; DOI [10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x). Read copy: [MIT-hosted combined corrected reprint](https://web.mit.edu/6.441/spring05/reading/shannon1948.pdf), 55 physical PDF pages, SHA-256 6e4e3411984f3edf99dbfe8b941cb5e8a321379ff0cae6ae5c1f592ad8882ca8. The first page explicitly identifies the corrected reprint as combining the July and October 1948 installments. The DOI record is associated with the July installment; this card describes the actual combined copy read.
- **Reader and extent:** W15 read physical PDF pp. 1–55, including appendices and end matter. Formula/theorem pages were rendered and visually checked, including pp. 3–4, 11, 13–14, 16–17, 20–26, 28–31, 38–47, 50–51, and 54–55. Complete section coverage is in evidence/W16/reading_coverage.json.

## Statements and proof routes used here

### Entropy of finite-alphabet sources

Section 6 and Appendix 2 (PDF pp. 10–12, 29) motivate and derive, up to a positive choice-of-units constant $K$,
\[
H(p_1,\ldots,p_m)=-K\sum_i p_i\log p_i.
\]
The derivation assumes continuity in the probabilities, maximality at equiprobability, and additivity/composition for successive choices; Appendix 2 first handles rational probabilities and then invokes continuity. Theorem 3 (§7, PDF pp. 13–14) gives the entropy-rate typical-sequence statement for the finite-state ergodic Markov source defined in §§4–5: for every $\epsilon,\delta>0$, sufficiently long sequences have probability at least $1-\epsilon$ of satisfying
\[
\left|N^{-1}\log p^{-1}-H\right|<\delta.
\]
The proof in Appendix 3 (PDF pp. 14–15, 30) counts transitions in an ergodic finite-state graph and bounds the sequence log-probability by the empirical transition frequencies. Theorem 4 identifies the exponential size of the high-probability set; Theorems 5–6 give block/conditional-entropy approximations converging to the source entropy.

### Discrete channels and asymptotic coding

- **Noiseless channel, Theorem 9 (§9, PDF pp. 16–17):** for a discrete source with entropy $H$ bits per source symbol and a noiseless channel of capacity $C$ bits/s, the output can be encoded at any source-symbol rate below $C/H$; a greater rate cannot be achieved. The proof uses the typical-source set and variable-length arithmetic coding. For a block $s$, the codeword length is between $\log_2 p(s)^{-1}$ and $1+\log_2 p(s)^{-1}$; the normalized expected overhead therefore vanishes with block length. This is an asymptotic existence/average-rate result, not a modern finite-block error exponent.
- **Noisy channel capacity (§12, PDF pp. 20–22):** Shannon defines equivocation $H_y(x)$ and rate $R=H(x)-H_y(x)=I(X;Y)$, then capacity $C=\max_{P_X} I(X;Y)$ over admissible input sources. In the binary symmetric example on p. 20, crossover probability 0.01 leaves equivocation approximately 0.081 bits/symbol and rate 0.919 bits/symbol.
- **Theorem 11 (§13, PDF pp. 22–24):** for a discrete source of entropy rate $H$ and a discrete channel of capacity $C$, if $H\le C$, codes can make error frequency/equivocation arbitrarily small; if $H>C$, equivocation can be reduced to $H-C+\epsilon$, and not below $H-C$. The proof first classifies long input/output sequences into high-probability sets of approximate cardinalities $2^{TH(x)}$, $2^{TH(y)}$, with about $2^{TH_y(x)}$ plausible causes per output. Randomly assigning messages to channel inputs shows collision probability tends to zero below $C$. For $H>C$, sending only $C$ bits/s leaves the stated excess uncertainty. The source explicitly notes that this is an existence proof and does not give a practical explicit code construction.
- **Theorem 12 (§14, PDF p. 25):** if $N(T,q)$ is the maximum size of a duration-$T$ signal subset, used with equal prior probabilities and decoded by the most-probable-cause rule with error at most $q$, then $\lim_{T\to\infty}\log N(T,q)/T=C$ for fixed $q\notin\{0,1\}$. This is an asymptotic fixed-error criterion.

### Continuous ensembles and channels

The source distinguishes differential entropy, which changes under a coordinate transformation by the expected log-Jacobian and may be negative, from information rate/capacity differences, which are coordinate invariant (PDF pp. 38–43). Theorems 14–15 concern band-limited function ensembles: a linear filter changes entropy rate by the band average of $\log |Y(f)|^2$; for independent ensembles, the entropy power of their sum lies between the sum of their entropy powers and the sum of their average powers (PDF pp. 39–41). These are statements for the continuous function-ensemble model used there.

For an additive channel $Y=X+N$ with $X$ and $N$ independent, Theorem 16 (PDF p. 43) gives $R=H(Y)-H(N)$, hence $C=\max_{P_X}[H(Y)-H(N)]$ subject to the input constraints. Theorem 17 (PDF pp. 43–44) states the average-power white-thermal-noise formula $C=W\log((P+N)/N)$; the text gives bits/s as $W\log_2(1+P/N)$. For arbitrary perturbing noise, Theorem 18 (PDF pp. 44–45) bounds capacity using average noise power $N$ and entropy power $N_1$:
\[
W\log\frac{P+N_1}{N_1}\le C\le W\log\frac{P+N}{N_1}.
\]
Theorem 20 (PDF pp. 46–47) is explicitly under a **peak** constraint: on p. 46 the theorem defines $S$ as the peak allowed transmitter power (the preceding §26 formulation, p. 45, bounds the instantaneous signal amplitude by $\sqrt S$). For white thermal noise of average power $N$, it gives $C\ge W\log\{2S/(\pi e^3N)\}$; for sufficiently large $S/N$ it gives $C\le W\log\{[(2/(\pi e))S+N]/N\}(1+\epsilon)$ with arbitrarily small $\epsilon>0$. As $S/N\to0$, if the band starts at zero, $C/[W\log(1+S/N)]\to1$ (PDF p. 47). Keep this distinct from Theorem 17 (PDF p. 43), whose constraint is **average** transmitter power $P$ and whose white-noise formula is $C=W\log((P+N)/N)=W\log(1+P/N)$. The peak- and average-power symbols and hypotheses are not interchangeable.

### Continuous-source fidelity and data processing

Theorems 21–23 (§§28–29, PDF pp. 50–51) treat a band-limited source with a fidelity functional. Theorem 21 says a source rate $R_1$ at target fidelity is communicable over capacity $C$ when $R_1\le C$, and not when $R_1>C$. For a white-noise source of bandwidth $W_1$, power $Q$, and allowed mean-square error $N$, Theorem 22 gives $R=W_1\log(Q/N)$; for a general band-$W_1$ source, Theorem 23 bounds $R$ between $W_1\log(Q_1/N)$ and $W_1\log(Q/N)$, where $Q_1$ is the source entropy power. Appendix 7 (PDF pp. 54–55) defines information rate by measurable partitions and proves that postprocessing a received signal cannot increase information rate: $R(X,V)\le R(X,Y)$ when $V$ is obtained from $Y$ (including the probabilistic-channel formulation).

## Relevance and transfer limits

This is foundational information-theory background for B051: it clarifies entropy rate, mutual information, channel capacity, coding limits, and the distinction between differential entropy and invariant information quantities. The direct B051 evidence remains Kanoria–Montanari I03; Shannon proves no small-deletion expansion, higher-order coefficient, all-orders series, or convergence radius. The finite-state source AEP and 1948 continuous-channel theorems cannot be applied to a stationary-input deletion channel without verifying their source/channel assumptions, and they do not justify interchanging an input-law supremum with a small-deletion limit.

