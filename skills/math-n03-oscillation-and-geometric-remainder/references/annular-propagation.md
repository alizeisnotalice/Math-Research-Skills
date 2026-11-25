# Two-circle propagation for a nonnegative auxiliary energy

OpenAI, *Local smoothing for the Euclidean wave equation*, PDF p. 21, Lemma 6.1. Local SHA-256 9ca156c552f2d940528f7131716326ef0d67a5829e723e1d294d74560c8636ff. This is the source lemma interface, with a checked potential example. [Versioned manuscript index](https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6)

Take \(0<b<1/4\), \(b\le r\le1\), and \(D=\log(3/b)\). The input is a smooth nonnegative energy \(E(T,\tau)\) on \(\mathbb R_T\times\{\tau\in\mathbb R^2:b\le|\tau|\le3\}\) with \(\Delta_{T,\tau}E\le V(|\tau|)E\) in the interior and \(V\ge0\) continuous. Verify both
\[
\int_b^3 s\log(s/b)V(s)\,ds\le M,\qquad
\sup_{1/2\le s\le3/2}V(s)\le M .
\]
For the mean \(H(T,s)\) over the circle of radius \(s\) in the auxiliary \(\tau\) variables, the lemma gives
\[
H(0,r)\ge c(M)\frac{\log(r/b)}{D^2}\int_1^2 H(T,b)\,dT .
\]
The PDE and comparison are in the auxiliary variables. In the wave application, the bounds linking \(H(0,2b)\) to input size and \(H(T,b)\) to the desired norm are separate steps (PDF pp. 18 and 23). At \(r=2b\) the logarithmic factor is of order \(D^{-2}\); this interface retains the loss.

For a candidate potential \(V(s)=A s^{-2} e^{-cs/h}\) with \(A,c>0\) fixed and \(b=2Kh\) for fixed \(K>0\), use \(s=by\). The first integral is at most \(A\int_1^\infty (\log y)y^{-1}e^{-2cKy}\,dy\le A e^{-2cK}/(2cK)\) because \(\log y\le y\). The second bound is at most \(4A\). This checks only the potential budget; the differential inequality for \(E\) and norm comparisons must come from the specific model.
