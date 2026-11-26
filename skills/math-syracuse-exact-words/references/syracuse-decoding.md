# Exact 3x−1 word decoder

Let `R` be positive and odd and let `w=(a_1,...,a_d)` have positive integer
entries.  Put

\[
A=\sum_i a_i,\qquad B=\sum_{i=1}^d3^{d-i}2^{a_1+\cdots+a_{i-1}}.
\]

If `3^d` divides `2^A R+B`, define the inverse chain by `y_d=R` and
`y_{i-1}=(2^{a_i}y_i+1)/3`.  The divisibility condition forces every member
of this chain to be a positive odd integer; moreover
`v_2(3y_{i-1}-1)=a_i`, so `S_-^d(y_0)=R`, where
`S_-(x)=(3x-1)/2^{v_2(3x-1)}` on positive odd `x`.

The bundled checker recomputes the chain directly and verifies this affine
identity using Python integers.  It is a certificate for one supplied finite
word only.

## Source and audit boundary

Naoufal Al El Jaouhari, *A proof of Applegate--Lagarias Conjecture A and the
3x+1 growth exponent conjecture* (September 2026 author manuscript),
physical p. 4, Definition 2.1 and equation (2), and p. 6, Lemma 3.1.  The
paper's density and `3x+1` conclusions depend on imported manuscripts and a
claimed Lean development (pp. 1--5); this skill does not adopt them.
