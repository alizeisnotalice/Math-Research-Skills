# Positive example: infer only the known order

Let $p$ satisfy B167’s assumptions and put $f=\operatorname{sgn}p$, $\delta=\|p-f\|_2^2$. If $\delta\le1/4$, variance transfer gives $\operatorname{Var}(f)\ge1/4$. The Hermite-tail theorem at degree $d$ then gives $\delta\ge c/\sqrt d$, since every degree-at-most-$d$ polynomial is orthogonal to Hermite levels above $d$. If $\delta>1/4$, the same order follows after reducing the absolute constant. This is a lower-order bound $\Omega(d^{-1/2})$, not the sharp leading constant.
