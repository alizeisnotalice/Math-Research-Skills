> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see review index (historical project reference; target is outside the runtime package).

# PGEL-006 — Synchronization of Kuramoto Oscillators in Dense Networks

## Identity and reading record

Jianfeng Lu and Stefan Steinerberger, “Synchronization of Kuramoto Oscillators in Dense Networks,” arXiv:1911.12336v2 (17 Apr 2020), DOI [10.1088/1361-6544/ab9baa](https://doi.org/10.1088/1361-6544/ab9baa); [official arXiv record](https://arxiv.org/abs/1911.12336). The local PDF front page matches this title, author list, and v2. It has 13 physical pages and SHA-256 841b88e00295b691598e044b59778f22355f7f9b6f6c254f2797e74936c82688. Reader L14 read physical pp. 1–13 in order, including the complete proof and references. Section coverage and rendered formula-page evidence are recorded in ../reading_coverage.json. No matching accepted canonical full-read record was found by exact title, arXiv identifier, or PDF hash. R05 helper-stage review passed; mother hash binding is pending.

## Model and theorem

The paper studies a connected simple undirected graph with adjacency entries \(a_{ij}=a_{ji}\in\{0,1\}\), \(a_{ii}=0\). Its objective is
\[
f(\theta)=\sum_{i,j=1}^n a_{ij}\cos(\theta_i-\theta_j).
\]
Global maximizers are the synchronized phases, up to common rotation. Under the ODE \(\dot\theta_i=-\sum_j a_{ij}\sin(\theta_i-\theta_j)\), local maxima of \(f\) correspond to stable local minima of the associated flow energy.

**Theorem (unnumbered, abstract and physical p. 2).** If every vertex has degree at least \(0.7889(n-1)\), then \(f\) has no nonglobal local maximum. The degree condition is deterministic; the theorem is about this unweighted positive undirected graph model.

## Proof chain and checked details

1. At a local maximum, the Hessian condition gives
   \[
   \sum_{i,j}a_{ij}\cos(\theta_i-\theta_j)(w_i-w_j)^2\ge 0
   \quad\text{for every }w\in\mathbb R^n.
   \]
   The cited Ling–Xu–Bandeira cone proposition says that if an order-parameter angle \(\theta_r\) satisfies \(|\sin(\theta_i-\theta_r)|<1/\sqrt2\) for every \(i\), all phases coincide (up to rotation). The source’s earlier bound is
   \[
   \|r\|^2\ge \bigl(2\mu-\tfrac32\bigr)n^2+2(1-\mu)n,\qquad
   \|r\|\,|\sin(\theta_i-\theta_r)|\le (1-\mu)n,
   \]
   where \(r=\sum_j e^{i\theta_j}\) and \(\mu=d_{\min}/(n-1)\). This is the baseline criterion, not by itself the improved threshold.

2. For a candidate nonglobal local maximum the authors write the missing-edge deficit as
   \[
   \sum_{i\ne j}(1-a_{ij})\left|\cos(\theta_i-\theta_j)-\cos^2(\theta_i-\theta_j)\right|
   =(2-\alpha)(1-\mu)(n-1)n.
   \]
   If \(\alpha>0.0537\), the baseline argument already excludes a nonglobal maximum at the target density. It remains to treat \(0\le\alpha\le0.0537\).

3. For any \(\varepsilon\ge\alpha\), at least \((1-\alpha/\varepsilon)n\) vertices are \(\varepsilon\)-good, meaning their row sum of the absolute cosine deficit is at least \((2-\varepsilon)(1-\mu)(n-1)\). For \(\varepsilon<\delta<1\), each such vertex has at least \((1-\mu)(n-1)(1-\varepsilon/\delta)\) non-neighbors whose absolute cosine deficit is at least \(2-\delta\). Trigonometry bounds the corresponding sine by
   \[
   s_\delta=\frac1{\sqrt2}\sqrt{\sqrt{9-4\delta}-3+2\delta}.
   \]
   Combining this with the first-order condition and the order-parameter lower bound places every good vertex within an angle \(\varphi\) of one of two opposing cones; the outlier fraction is at most \(\alpha/\varepsilon\). The source’s displayed definition of \(\varphi\) is retained in the p. 6–7 render.

4. Let \(\gamma_1 n,\gamma_2 n\) be the good vertices in the two cones, with \(\gamma_2\ge\gamma_1\). The order-parameter lower bound forces a lower bound on \(\gamma_2\) (equation (8), physical p. 8). Test the Hessian quadratic form with \(w=1\) in the left cone, \(w=-1\) in the right cone, and \(w=v\) on outliers. The cross-cone edges contribute negatively; optimizing \(v=(\gamma_1-\gamma_2)/(\gamma_1+\gamma_2)\) bounds the outlier contribution. Equations (11)–(13) then give a contradiction whenever the angle and cone-size inequalities in Step 5 hold (physical pp. 8–12).

5. The paper chooses \(\varepsilon=0.5,\delta=0.88\) and reports an “easy (mathematica) check” over \(0\le\alpha\le0.0537\), \(0.788897\le\mu\le0.794\). It gives margins \(<0.46<1/2\), \(<-0.05<0\), and a final gap \(>0.004\). This is the authors’ reported parameter check; the paper supplies no interval certificate, so the numerical parameter verification is not promoted here to an independently proved claim.

## Reusable method and transfer boundary

Reusable for positive undirected dense-graph landscapes: combine (i) a second-order Hessian test, (ii) a rank/order-parameter lower bound, (iii) a good-vertex/outlier decomposition driven by near-equality in the missing-edge bound, and (iv) a cone-separating Hessian test vector. The exact method is model-specific: the sign of each cross-cone contribution uses \(a_{ij}\ge0\) and the cosine of phase differences; a signed edge can reverse that sign. This is not a C118 signed-graph theorem. For C118 it is only a proof-design pattern: one still needs a uniform signed-Hessian certificate and a probability bound controlling all phase configurations.
