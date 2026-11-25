# Positive examples: check a concrete Boolean and a scoped transfer

## Exact three-bit majority noise calculation

On the uniform sign cube, let
\[
 f(x_1,x_2,x_3)=\operatorname{Maj}_3(x)=\frac{x_1+x_2+x_3-x_1x_2x_3}{2}.
\]
Its nonzero normalized Walsh coefficients are \(\hat f(\{i\})=1/2\) for \(i=1,2,3\) and \(\hat f(\{1,2,3\})=-1/2\). Thus each forced-flip influence is \(1/2\) and total influence is \(3/2\). If each bit flips independently with probability \(\delta=1/4\), then \(\rho=1-2\delta=1/2\), and
\[
 \operatorname{Stab}_{1/2}(f)=3\left(\frac14\right)\left(\frac12\right)+\left(\frac14\right)\left(\frac12\right)^3=\frac{13}{32},\qquad
 \operatorname{NS}_{1/4}(f)=\frac{1-\operatorname{Stab}_{1/2}(f)}2=\frac{19}{64}.
\]
These are exact finite identities for this function, not an asymptotic theorem. R07's exact rational enumeration checks all eight inputs and all independent flip masks.

## Exact pairwise-independent dual for three-bit majority

For \(x\in\{0,1\}^3\), let \(F(x)=1\) when at least two coordinates are 1. The even-parity law
\[
 \{000,011,101,110\}
\]
and odd-parity law
\[
 \{001,010,100,111\}
\]
are both 2-wise independent with Bernoulli-\(1/2\) marginals. Yet \(\mathbb E F\) is \(3/4\) under the even-parity law and \(1/4\) under the odd-parity law. Pointwise on the cube,
\[
 1-\sum_{i<j}(1-x_i)(1-x_j)\le F(x)\le\sum_{i<j}x_ix_j.
\]
Both product-uniform expectations are respectively \(1/4\) and \(3/4\), so these degree-2 minorant/majorant certificates match the two extremal pairwise-independent laws. This is the finite \(k=2\) LP/sandwich-duality interface admitted from BGP Proposition 4. It does not prove the source's iterated-majority Question 4. R07's exact rational check verifies the marginal laws, pointwise inequalities, and expectations.

## Gaussian \(k\)-wise PTF transfer: use the smoothed gate

For the R07-admitted Kane interface, begin with a nonnegative positive-Fourier kernel of integral one, block dimensions \(n_i\ge1\), constants \(C_i>0\), and positive even integers \(m_i\). State the directional-derivative and tail assumptions. If each polynomial coordinate \(P_{ij}\) has degree at most \(D\), use the rectangular Taylor polynomial \(T\) with block degrees below \(m_i\), and retain
\[
 R(P(Y))=\prod_i\left(1+\frac{C_i^{m_i}\lVert P_i(Y)\rVert^{m_i}}{m_i!}\right)-1.
\]
The admitted conservative sufficient condition is Gaussian \(k\)-wise independence with \(k\ge D\sum_i m_i\); then the smoothed expectation error is bounded by \(2\mathbb E R(P(Y))\) for standard-Gaussian \(k\)-wise \(X\) versus fully independent standard-Gaussian \(Y\). A sign conclusion needs an additional explicit boundary gate. Let \(h\) be a real polynomial and \(f=\operatorname{sgn}_+ h\), where \(\operatorname{sgn}_+(0)=+1\); thus \(|f|\le1\). If the closed block-radius neighborhoods meeting \(\{h=0\}\) have probabilities \(b_X,b_Y\), and the kernel tail is \(\eta\), the reviewed sign-expectation bound is
\[
 |\mathbb E f(P(X))-\mathbb E f(P(Y))|\le2\mathbb E R(P(Y))+2b_X+2b_Y+4\eta.
\]
Consequently, since \(\mathbf1_{\{h\ge0\}}=(1+f)/2\), the event-probability error is at most
\[
 |\Pr[h(P(X))\ge0]-\Pr[h(P(Y))\ge0]|\le\mathbb E R(P(Y))+b_X+b_Y+2\eta.
\]
This uses the smoothed Taylor estimate, not the literal unsmoothed display. It is a derived sufficient interface, not approval of Kane's full headline exponent, Proposition 8, an automatic small-boundary estimate, or a Boolean-cube transfer.
