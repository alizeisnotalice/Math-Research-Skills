# Tribonacci dominant-root height gate

For the recurrence with characteristic polynomial
\[
\Psi(X)=X^3-X^2-X-1
\]
and its positive real root \(\alpha\), set
\[
g(\alpha)=\frac{\alpha}{\Psi'(\alpha)}.
\]
This narrow reference supplies exact height data usable as an input to a
linear-form lower-bound calculation.  It does not prove a Diophantine
classification.

Using \(\alpha^3=\alpha^2+\alpha+1\), direct reduction gives
\[
 g(\alpha)=\frac{-4-3\alpha+5\alpha^2}{22}.
\]
Eliminating \(\alpha\) yields the primitive polynomial
\[
44X^3-2X-1.
\]
It has no rational root, hence is the minimal polynomial.  Its three roots
all have modulus below one, so
\[
h(g(\alpha))=\frac{\log 44}{3}.
\]

Source: *Tribonacci numbers that are palindromic concatenations of two
distinct repdigits*, arXiv:2610.15770v1, physical pp.2–3, equations (2)–(5)
and Lemma 2.1; local source SHA-256
`84379b3f99020ae4ec816f81f791ddc503be5db45dfd35492ebca5b898a11667`.

The present review independently checked the inverse identity in
\(\mathbb Q[X]/(\Psi)\) and obtained resultant
\(242(44X^3-2X-1)\).  This is only a normalization/height gate.  A use of it
still requires a specified Binet error, nonvanishing of the particular
logarithmic form, field-degree/height bounds for every other factor, a valid
reduction certificate, and any finite search.
