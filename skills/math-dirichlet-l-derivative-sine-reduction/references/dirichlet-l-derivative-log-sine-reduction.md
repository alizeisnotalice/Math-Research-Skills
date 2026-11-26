# Even periodic Dirichlet-type data: formal log-sine reduction at `s=0`

## Source and checked proof step

T. Chatterjee and S. Dhillon, *Special values of derivatives of certain
L-functions*, arXiv:2408.13737v1 (2024), local PDF SHA-256
`7b1bc398cd412025c03077e4f6d2fd875ae540220b712a51eaee8b149487e49a`.
The local source is an arXiv v1 preprint; no formal-published version is used
by this component.

For an even algebraic-valued Dirichlet-type periodic function `f` of period
`q`, physical pp. 2--3 derive, from the Hurwitz-zeta/Lerch formula and the
Gamma reflection formula,

\[
 L'(0,f)=-\sum_{\substack{1\leq a\leq\lfloor q/2\rfloor\\(a,q)=1}}
 f(a)\log\!\left(2\sin\frac{\pi a}{q}\right). \tag{6}
\]

For a modulus having at least two distinct prime factors, physical p. 8 uses
the cyclotomic sine-product identity (14) to rewrite this as

\[
 L'(0,f)=\sum_{\substack{2\leq a\leq\lfloor q/2\rfloor\\(a,q)=1}}
 \bigl(f(a)-f(1)\bigr)\log\!\left(2\sin\frac{\pi a}{q}\right). \tag{15}
\]

The proof of Theorems 1.2 and 1.4 (physical pp. 8--9) then invokes the
independence input stated as Propositions 2.2--2.4 (physical pp. 6--7), plus
Baker's theorem.  Those external cyclotomic-unit/logarithm theorems are not
implemented or independently re-proved here.

## Exact finite component

The companion script accepts rational values on every reduced residue class,
checks the evenness condition `f(a)=f(q-a)`, and emits the exact coefficient
vectors of the formal logarithmic sums in (6), and in (15) when applicable.
It never evaluates a logarithm or decides whether the resulting linear form
vanishes.

## Scope boundary

The coefficient transform is a finite symbolic reduction.  It does not prove
analytic continuation, the source's Dirichlet-type hypotheses, the
cyclotomic sine-product identity, linear independence of logarithms, a
nonvanishing result, or transcendence.  The statements in Theorems 1.2 and
1.4 become usable only after the exact modulus restrictions and the cited
cyclotomic-logarithm inputs have been independently verified.

## Singleton residue at modulus two

At \(q=2\) the only unit is a fixed point of \(a\mapsto q-a\).
The paired display (6) counts two terms and applies for \(q>2\).
For the remaining case use
\(L(s,f)=f(1)(1-2^{-s})\zeta(s)\), giving
\(L'(0,f)=-f(1)\log 2/2\) by \(\zeta(0)=-1/2\).
The exact coefficient of the singleton \(\log(2\sin(\pi/2))\) is therefore
\(-f(1)/2\). The example \(f(1)=3\) returns \(-3/2\).
