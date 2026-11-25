# Labelled Poisson witness lower tail

Use this component when a finite family of certificates is chosen before sampling a Poisson point process, and a certificate is an injective assignment of process points to labelled measurable slots. It bounds the event that every certificate fails.

## Checked source

OpenAI, *Translative covering densities of order \(n\log n\)*, 23 September 2026, Lemma 6.1, Proposition 6.2, and Lemma 6.3, PDF pp. 16–20. The audited local document has SHA-256 `2944d4b3135b4d794626b13db292b869dfc58b4668a29f194e8fbcb542290a3e`. Its pinned official copy is [OpenAI math commit `3344da59991ed94f9ba711217b29c1d760badfa6`](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/paper.pdf).

The result is a reusable probabilistic component from the cited covering construction. It does not transfer the paper’s geometric cap, covering-density, or asymptotic conclusions.

## Formal interface

Let \((\Omega,\mu)\) be a finite nonatomic standard Borel measure space and let \(\Pi\) be a Poisson process of intensity \(\mu\). Take a finite nonempty index set \(A\). For each \(\alpha\in A\), take a finite nonempty **labelled** slot set \(I_\alpha\), and measurable slot sets \(E_{\alpha i}\subseteq\Omega\) with

\[
\lambda_{\alpha i}:=\mu(E_{\alpha i})>0,
\qquad
\nu_\alpha:=\prod_{i\in I_\alpha}\lambda_{\alpha i}.
\]

Let \(Z_\alpha\) count injective maps from \(I_\alpha\) to the points of \(\Pi\), with the point assigned to \(i\) lying in \(E_{\alpha i}\). A partial matching \(M\) from \(I_\alpha\) to \(I_\beta\) is a set of pairs with no repeated coordinate. Define

\[
D_{\alpha\beta}
=\nu_\alpha\nu_\beta
 \sum_{\substack{M\text{ a partial matching}\\M\ne\varnothing}}
 \prod_{(i,j)\in M}
 \frac{\mu(E_{\alpha i}\cap E_{\beta j})}
 {\lambda_{\alpha i}\lambda_{\beta j}}.
\]

Then

\[
\mathbb E Z_\alpha=\nu_\alpha,
\qquad
\operatorname{Cov}(Z_\alpha,Z_\beta)=D_{\alpha\beta},
\]

and

\[
\mathbb P\{Z_\alpha=0\text{ for every }\alpha\in A\}
\le
\exp\!\left[-
\frac{(\sum_{\alpha\in A}\nu_\alpha)^2}
{2\sum_{\alpha,\beta\in A}D_{\alpha\beta}}
\right].
\]

The denominator is positive. For \(D_{\alpha\alpha}\), the full identity matching contributes \(\nu_\alpha\).

## Application rules

1. Fix the finite witness family and all slot sets before exposing \(\Pi\). This inequality does not justify adaptively choosing a witness after seeing process points.
2. Keep indices distinct when two slots or two witness types use equal sets. The injection count is ordered by these labels, and it contains no factorial normalization for repeated sets.
3. Treat an empty slot list as a deterministic certificate before applying the result. The stated interface requires nonempty lists and positive slot intensities.
4. Compute the full diagram sum when feasible. For a cross bound, set
   \[
   \rho_{\alpha\beta}=
   \sum_{i\in I_\alpha,\,j\in I_\beta}
   \frac{\mu(E_{\alpha i}\cap E_{\beta j})}
   {\lambda_{\alpha i}\lambda_{\beta j}}.
   \]
   Then \(D_{\alpha\beta}\le\nu_\alpha\nu_\beta(e^{\rho_{\alpha\beta}}-1)\). If every cross-slot intersection has measure zero, then \(D_{\alpha\beta}=0\).
5. The finite nonatomic assumption is used to partition the space into cells of arbitrarily small positive mass. For atomic spaces, derive a discrete indexed inequality directly instead of invoking this passage.

## Proof record

For independent Bernoulli coordinates and an indexed family of nonempty coordinate supports \((H_i)\), including repeated supports, Lemma 6.1 gives

\[
\mathbb P(Y=0)\le
\exp\!\left(-\frac{m^2}{2\Delta_*}\right),
\quad
m=\mathbb EY,
\quad
\Delta_*=
\sum_{H_i\cap H_j\ne\varnothing}\mathbb E(I_iI_j).
\]

The sum is ordered and includes diagonal pairs. Harris correlation gives the preliminary avoidance bound. Adding an independent private Bernoulli factor of parameter \(m/\Delta_*\) to every index yields the displayed bound. This preserves repeated indices.

For the Poisson process, form the Boolean atoms of all slots and partition each positive-mass atom into cells of mass at most \(\delta\). Their occupancy indicators are independent Bernoulli variables. Retain every internally injective assignment of cells to labelled slots. For a pair of assignments, the complete set of equal occupied cells is a unique partial matching. As \(\delta\downarrow0\), the finite mean tends to \(\sum_\alpha\nu_\alpha\), and its indexed dependency sum tends to \(\sum_{\alpha,\beta}D_{\alpha\beta}\). The probability that any cell contains two or more Poisson points is at most \(\frac12\sum_C\mu(C)^2\le\frac12\delta\mu(\Omega)\), so the cell injections and point injections agree in the limit.

For the self diagrams, the source gives a sharper slotwise product bound. The cross estimate above follows by dropping matching restrictions and using \(1+x\le e^x\).

## Exact finite check

Take \(\Omega=[0,3/2]\) with Lebesgue intensity and one witness type with labelled slots

\[
E_1=[0,1],\qquad E_2=[1/2,3/2].
\]

Both slot intensities equal one, so \(\nu=1\). The four one-edge matchings contribute \(1,1,1/2,1/2\), and the two full matchings contribute \(1,1/4\). Hence \(D=17/4\). An injective witness fails exactly when one slot is empty, or when the sole process point lies in the overlap. Thus

\[
\mathbb P(Z=0)=2e^{-1}-\tfrac12e^{-3/2}
\approx0.6241938022686697,
\]

whereas the diagram bound is \(e^{-1/(2D)}=e^{-2/17}\approx0.8890097654027757\).

This calculation was run locally with:

```bash
/Users/zzh/.venvs/main/bin/python - <<'PY'
from decimal import Decimal, getcontext
getcontext().prec = 50
one = Decimal(1)
exact = 2 * (-one).exp() - Decimal('0.5') * (Decimal('-1.5')).exp()
d = Decimal('4.25')
bound = (-(one / (2 * d))).exp()
print(exact)
print(bound)
PY
```

It returned `0.62419380226866972872440730494091547422053644738300` and `0.88900976540277566398271538258816650349544153390532`, respectively.
