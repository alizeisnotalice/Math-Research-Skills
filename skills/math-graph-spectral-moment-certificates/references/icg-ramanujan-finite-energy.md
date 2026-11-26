# Source note: finite integral-circulant energy

Source: *Maximal energy of integral circulant graphs of order \(p^a q^b\) when one prime is 3 or one exponent is at most 2*, author manuscript v3 (9 Nov 2026), physical p. 5 of 33.  Local SHA-256: `84620c31de933ee0dd8ba6efffe042a60ec1cd8901e178f08bb87446aa1f78b0`.

The source presents a weighted Ramanujan-transform expression for the energy of an integral circulant graph.  The accompanying asset retains a narrower, independently reconstructed finite check.  For an explicitly supplied `n` and proper-divisor set `D`, it constructs the adjacency matrix of

`ICG_n(D) = Cay(Z/nZ, {r : gcd(r,n) in D})`,

computes `lambda_t = sum_{d in D} c_(n/d)(t)` using the elementary integer Ramanujan formula, and checks the second and fourth spectral moments directly from the adjacency matrix.  The residue-class decomposition `r=d u`, `gcd(u,n/d)=1` independently explains the closed sum.

It does **not** certify a Jiang--Yang matrix formula, a maximizing divisor set, any symbolic prime/exponent family, Lean artifact, or a general extremal theorem.

~~~sh
python3 -B scripts/check_icg_ramanujan_energy.py --n 45 --divisors 1,3,5
~~~
