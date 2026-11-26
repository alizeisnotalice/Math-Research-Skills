# O43 / GD1998 swirl: bounded exact reduction audit

Source under review: supplied 31-page preprint, SHA-256
`a38af23a5873e7671ecf0bcd7f3d4c45851c67689a7551ae0e51203ba166fe95`,
physical pp. 4--5 (definitions (1)--(3)); pp. 17 and 25--29 (unresolved
sonic-layer spectrum and claimed external software/tests).

## Adoptable component: exact coordinate-differentiation contract

Fix `0 < h < 1/100`, `D = 1/2-h`, `tau = 1-t`, and define `q=q(t,z)>0`
implicitly by

```
tau = q(1-eta^2),   eta = z q^{-D},   X = r^2/(2q).
```

On any local branch for which `L = 1-2h eta^2 != 0`, and for every smooth
`f(X,eta)`, direct implicit differentiation gives

```
partial_t(q^b f) = q^(b-1) L^(-1) [-b f + D eta f_eta + X f_X],
partial_z(q^b f) = q^(b-D) L^(-1) [2b eta f + (1-eta^2) f_eta - 2eta X f_X].
```

This is a local exact chain-rule identity, not an asymptotic Navier--Stokes
reduction.  Its only branch condition is `L != 0`; under the stated paper
range it is positive for `|eta| <= 1`.

The associated derivative data follow from the implicit equation:

```
q_t = -L^(-1),       q_z = 2 eta q^(1-D) L^(-1),
X_t = X(qL)^(-1),    eta_t = D eta(qL)^(-1),
X_z = -2 eta X q^(-D)L^(-1),
eta_z = q^(-D)(1-eta^2)L^(-1).
```

`verify_similarity_operators.py` uses SymPy on three nontrivial polynomial
profiles and three distinct rational powers `b`; all four residuals per case
are exactly zero.  It also checks that the coefficient from differentiating
the implicit `q` relation is precisely `L`.

## Excluded claims

No claim is adopted about the leading-order profile equations (4), the
neglected `O(q^(2h))` terms, any computed branch/fold, the manufactured test,
the heat-exterior implementation, or spectral/nonlinear stability.  In
particular the source itself says the moderate-inflow/strong-swirl sonic-line
eigenvalues do not converge with axial resolution; that remains open.

Use the source branch conditions before any profile equation. The identity follows by differentiating the scalar relation q - z^2 q^(2h) = 1-t and substituting the resulting q derivatives into X and eta.

~~~sh
python3 -B scripts/verify_similarity_operators.py
~~~
