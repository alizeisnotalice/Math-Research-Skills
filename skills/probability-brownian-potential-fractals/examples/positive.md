# Positive cases

These examples show what the admitted sources support when their exact assumptions and stopping rules are carried into the claim.

## Large-packet disconnection

Take n independent planar Brownian arms with arbitrary starts on the unit circle, each stopped at its own first hit of radius R. Let non-disconnection mean that 0 remains in the unbounded component of the complement. For M0196 Proposition 1, use the connector F_(R+1), strict sausage witnesses with positive clearance, and ordinary first-hit stopping times. First send n to infinity with R, epsilon and alpha fixed; then epsilon decreases to zero; then R grows. The admitted result is eta_n/n -> 1/2 for the radius exponent (time exponent eta_n/2). It is not an exact finite-n formula. See PR-58f59904e178 in the source register.

## Brownian-excursion restriction for a vertical slit

For a vertical slit attached to the real line at a>0 with height h>0, the admitted Brownian-excursion avoidance example gives Phi_A' (0)=a/sqrt(a^2+h^2). This is the derivative of the normalized conformal map in the Brownian-excursion restriction statement. It is not an SLE(8/3) construction or a frontier-dimension result. See PR-2a6cfc3818b2.

## Local Brownian loop-erasure density

In the unit disk, let complex Brownian coordinates have variance t, use the positive normalized Poisson kernel Q_0 for exit at 1, and take an independent radial SLE2 from 1 toward 0. For fixed disjoint Jordan separators sigma_1 and sigma_2 surrounding 0, with sigma_2 enclosing sigma_1, the accepted two-time commutation lemmas give a bounded stopped change of measure at the corresponding first hits. This preserves both marginals for that fixed separator pair. Stop there; the finite-family extension and global loop-erasure conclusions are not included. See PR-1018a43b4e34.

## Rectangle reflection order and the first Neumann mode

For D=(0,1)x(0,2) with normal reflection, Atar’s rectangle result uses the same Brownian driver, primitive face normals +/-e_1 and +/-e_2, and the exact closed-cone conditions to preserve coordinatewise order. Its explicit first positive mode is phi(x,y)=-cos(pi y/2): the eigenvalue of -Delta is pi^2/4, so the standard reflected-Brownian generator Delta/2 gives mode decay pi^2/8. This supplies an exact rectangle comparison; it does not construct an acute-triangle coupling or its meeting-time tail. See EXSRC-cd55a9e0f1e0c2d0.

## Disk noncoalescence and joint boundary event

For fixed unequal starts in the closed unit disk, the admitted same-driver synchronous normal-reflection pair in EXSRC-62f2ce007b957ddb never meets at finite time, even though its spatial distance has limsup exponential rate at most -1. Thus P(T>t)=1 for every finite t in this specified coupling. The separate EXSRC-ef5251d44e6ca12e theorem says the pair almost surely reaches the product boundary; in rotating coordinates the event is y=0 and x^2+z^2=1. This joint location does not say that the two original regulator measures charge the same times. Spatial contraction and joint boundary contact do not imply finite coalescence or overlapping regulator mass.

## Deterministic pursuit

Under the bounded CAT(0), uniform exterior-sphere and interior-cone assumptions of PR-455d793d0df2, the deterministic Proposition 17 bounds uniform epsilon/2 capture for a unit-speed lion pursuing a measurable man control whose actual speed is u<=1. Keep u in the cosine estimate; do not replace the deterministic problem by a Brownian driver or promote this proposition to the paper’s stochastic theorems.
