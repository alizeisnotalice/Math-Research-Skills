# Casoratian identity for a supplied order-two recurrence

Source: Marc Chamberland and Armin Straub, *Apéry Limits: Experiments and
Proofs*, arXiv:2011.03400v1 (6 November 2020), local physical PDF pp. 9--10,
equations (12)--(14); illustrative integral/linear-form discussion is on p.12.
The exact local source is
`07_Irrationality_Transcendence_Compendium/PDF/EXT-0558_Ap-ry-Limits-Experiments-and-Proofs.pdf`,
SHA-256
`3390126ece668d5dba1d13a63bfbc6c8d7da822b69770613a3a4ba1b3ee5f963`.

For a monic order-`d` recurrence the source gives the Casoratian propagation
law.  Its `d=2` specialization (p.9, equation (14)) expresses a second
solution from a nonzero first solution and the propagated Casoratian.  Written
in this tool's unnormalised convention

\[
 a_nx_{n+1}=b_nx_n+c_nx_{n-1},
\]

direct substitution gives

\[
 W_n=u_nv_{n+1}-u_{n+1}v_n=-\frac{c_n}{a_n}W_{n-1}.
\]

If `u_n u_{n+1}` is nonzero, division gives the consecutive quotient identity.
Both are finite algebraic identities; neither source nor this implementation
identifies a quotient limit, supplies denominator/integrality bounds, or proves
irrationality of any Apéry limit or Euler's constant.

The Delannoy example of local pp.2--3 has
\((n+1)x_{n+1}=3(2n+1)x_n-nx_{n-1}\), `A_0=1,A_1=3`,
`B_0=0,B_1=1`.  It yields `W_n=1/(n+1)` and is included solely as an exact
finite regression fixture.

[刊载版，American Mathematical Monthly 128(9) (2021), 811–824](https://doi.org/10.1080/00029890.2021.1962153)
