# Continued-fraction limsup formulas

Source: Jonathan Sondow, *Irrationality Measures, Irrationality Bases, and a Theorem of Jarnik*, arXiv:math/0406300v1, physical pp.4–6, SHA-256 `537c120ed1ce44e5bf5fd65e7bbc4084707198970dbf95773e229ec920adaf3c`.

For an irrational number with simple continued fraction partial quotients `b_n` and convergent denominators `q_n`, Theorem 1 records

\[
\mu=1+\limsup_n\frac{\log b_{n+1}}{\log q_n},\qquad
\log\beta=\limsup_n\frac{\log b_{n+1}}{q_n}.
\]

Use the denominator recurrence `q_{n+1}=b_{n+1}q_n+q_{n-1}` with certified input data. These formulas diagnose supplied approximants; they do not establish them for Euler's constant.
