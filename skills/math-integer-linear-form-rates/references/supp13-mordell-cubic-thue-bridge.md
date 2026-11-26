# Scoped reference: cubic-Thue to Mordell covariant bridge

Source: Bennett--Ghadermarzi, *Mordell's equation: a classical approach*, arXiv:1311.7077v1, local SHA-256 `f3a0ef67ce3624982110085d640116c313b780a8cc214e98d7b7fec859d9cf72`, physical p. 4.

For a binary cubic form (F) with discriminant (D), the source uses its Hessian (H) and cubic covariant (G), normalized by



\[
4H^3=G^2+27DF^2.
\]

Put (D_1=D/27), (H_1=H/9), (G_1=G/27).  If an integral pair satisfies (F(x_0,y_0)=1), (D_1\equiv0\pmod4), and the indicated parity gate holds, then

\[
X=H_1(x_0,y_0),\qquad Y=G_1(x_0,y_0)/2,\qquad k=-D_1/4=-D/108
\]

is an integral point (Y^2=X^3+k). Conversely the source associates (F(x,y)=x^3-3Xxy^2+2Yy^3) to a Mordell point and obtains discriminant (-108k).

This is a transformation gate, not a general Mordell solver. Verify the form convention, covariants, discriminant, parity, integrality, and the desired equivalence-class accounting for every instance. The source's all-|(k)|<=(10^7) enumeration depends on extra reduced-form and Thue-solving computations and is not adopted here.
