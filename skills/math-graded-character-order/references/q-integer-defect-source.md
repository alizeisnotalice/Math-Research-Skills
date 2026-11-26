# q-integer defect coefficient: verified scope

Source: Suvrit Sra, *The q-Foulkes problem I: A fusion inequality for Macdonald plethysms*,
v1 author preprint (local SHA-256 `02b122b396de6202bb7e74d56ca43e1c057f6cf2a921c2d8645e68e95cae158f`),
physical pp. 17–18, Lemma B.4.

The source defines a standard-character defect coefficient through
`C_{r,m}=([r]_q[m]_q-[rm]_q)/(1-q)` and displays its nonnegative finite expansion
`[r]_q sum_{j=1}^{m-1} q^j[j(r-1)]_q`.  This helper checks exactly that elementary polynomial
identity.

Its interpretation as a coefficient of `D_{mu,m}` uses the Macdonald evaluation formula,
Garsia–Haiman and fusion constructions.  The preprint's global fusion and q-Foulkes claims are
outside this helper's certificate.
