# aldous95 — Hammersley’s interacting particle process and longest increasing subsequences

**Reading status:** `fulltext_read`; complete 21-page scan read visually page by page. PDFKit extraction is blank, so the theorem and formula checks were made from rendered source pages. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** David Aldous and Persi Diaconis, “Hammersley’s Interacting Particle Process and Longest Increasing Subsequences,” *Probability Theory and Related Fields* 103 (1995), 199–213, DOI [10.1007/BF01204214](https://doi.org/10.1007/BF01204214). Local PDF SHA-256: `a57f3a54dcb215b5913fb1f03e75190af3eff465570f13fdf19a7fd7dc47126c`.

## Results and proof route

For a uniform random permutation of {1,…,n}, let (L_n) be its longest increasing subsequence length. Theorem 5(a) proves

\[
n^{-1/2}\mathbb E L_n\longrightarrow 2.
\]

Theorem 5(b) gives the corresponding hydrodynamic limit for Hammersley’s particle process: at macroscopic location (at) and time (t), the local point process converges to a Poisson process of rate (a^{-1/2}). The paper represents a rate-one planar Poisson process in ([0,x]\times[0,t]) as a uniform random permutation, with (L_n) equal in distribution to the maximum number of Poisson points on an up-right path. For (g(t)=\mathbb E L^{\nearrow}(t,t)), concatenating paths gives superadditivity and (g(t)/t\to c). A process on the half-line yields (c\le2); for the reverse inequality, stationary Poisson laws on the full line, space-time interchange, and uniqueness of the stationary law force limiting rate (1), giving (c\ge2). Thus (c=2), and elementary de-Poissonization transfers the limit to (L_n).

Theorem 13 (PDF p. 16) states for the median (m_n), all (u>0) and (n\ge1),

\[
\mathbb P(L_n\ge m_n+u)\le 2e^{-u^2/(4(m_n+u))},\qquad
\mathbb P(L_n\le m_n-u)\le 2e^{-u^2/(4m_n)}.
\]

The paper only records the upper large-deviation asymptotic beyond (2\sqrt n) as anticipated and notes that the Poissonized version follows from superadditivity and Theorem 13; it explicitly does not supply the de-Poissonization details for that claim. The lower large-deviation statement below (2\sqrt n) is proved. It also derives (2\sqrt n-\mathbb E L_n\to\infty).

## Applicability boundary

This is an LIS/Hammersley-process result. Its Poisson path representation and hydrodynamic method can guide path-growth arguments, but the paper does not establish a comparison for dependent percolation paths or infection dynamics. For A030 it is auxiliary context; the finite-size/near-one estimate requested there remains open.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/aldous95`).
