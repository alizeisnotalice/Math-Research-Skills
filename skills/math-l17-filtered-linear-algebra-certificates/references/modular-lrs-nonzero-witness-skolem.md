# Finite modular nonzero witness for an integer LRS

For an integer recurrence \(u_{n+d}=a_{d-1}u_{n+d-1}+\cdots+a_0u_n\), a
claimed modulus \(m\ge2\) witness that \(u_n\not\equiv0\pmod m\) for all
\(n\ge0\) is decidable by finite state enumeration. Reduce the order-\(d\)
companion state modulo \(m\), iterate it until its first repeated state, and
check the first coordinate of every state in the finite orbit. Determinism then
makes the orbit ultimately periodic, so this exactly proves or refutes the
given witness for the stated one-sided LRS.

`check_lrs_modular_witness.py` implements this finite check with integer
arithmetic. It does **not** find a witnessing modulus, prove the Skolem
conjecture, handle a bi-infinite recurrence without an invertibility argument,
or turn absence modulo one modulus into an unconditional answer when no witness
is supplied. This is the finite checker needed by the modular-witness portions
of the Skolem sources.
