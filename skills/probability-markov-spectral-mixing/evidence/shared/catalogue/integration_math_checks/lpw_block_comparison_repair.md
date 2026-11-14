# Independent conditional-variance repair for the block comparison

Scope: finite graph with n>=1 vertices, maximum degree Delta, zero-field Ising
law pi(sigma) proportional to exp(beta sum_edges sigma_u sigma_v), finite beta>=0.
Single-site heat bath chooses a vertex uniformly; block heat bath chooses uniformly
among b blocks covering all vertices. Let M be maximum block size and Mstar the
maximum number of blocks containing one vertex. Both gaps use the same pi and
discrete update conventions. This is not a statement about different stationary
measures, hard constraints, unbounded fields, or changed clocks.

Root inspected LPW physical pp.239–240 (printed223–224). The displayed congestion
estimate contains 2(n/b) M Mstar 4^M exp(2 beta Delta(M+1)); the next simplification
does not justify dropping 2 and replacing 4^M by4. This observation alone does
not refute the stated theorem. The following is an independent proof under the
specified heat-bath assumptions, awaiting independent R02 review.

For a block B of size m and a fixed outside configuration, write mu for its
strictly positive conditional law and nu for uniform measure on its m-bit cube.
Let a=min(mu/nu), A=max(mu/nu). Then

    Var_mu f <= A Var_nu f.

For an edge of the cube, the single-site conditional-variance coefficient is
mu(x)mu(y)/(mu(x)+mu(y)); it is at least a times the corresponding coefficient
for nu, because both mu(x),mu(y)>=a 2^{-m} and the harmonic mean is increasing
in each argument. Consequently

    sum_i E_mu Var_mu(f | all coordinates other than i)
       >= a sum_i E_nu Var_nu(f | all coordinates other than i)
       >= a Var_nu f.

The last inequality is product-measure variance tensorization (equivalently the
uniform m-site heat-bath spectral gap1/m). For completeness, expand f in the
orthonormal Walsh basis chi_A of the uniform cube: Var_nu f is the sum of squared
coefficients over nonempty A, whereas sum_i E_nu Var_i f is the same sum with
each squared coefficient multiplied by |A|. This proves the inequality directly
for every real f; no Boolean influence normalization is involved. Thus

    Var_mu f <= (A/a) sum_i E_mu Var_i f.

Only edges touching B change energy. There are at most Delta m such edges, and
each edge product can change by at most2. Therefore the oscillation of log density
is at most2 beta Delta m, uniformly in the outside configuration, and
A/a<=exp(2 beta Delta m). Averaging the preceding bound over outside spins gives

    E_pi Var_B f <= exp(2 beta Delta M) sum_{i in B} E_pi Var_i f.

Empty blocks contribute zero. With E_single=(1/n)sum_i E_pi Var_i and
E_block=(1/b)sum_B E_pi Var_B, summing and using multiplicity at most Mstar yields

    E_block <= (n/b) Mstar exp(2 beta Delta M) E_single
            <= M Mstar exp(2 beta Delta M) E_single,

since coverage implies n<=bM. Taking the Rayleigh quotient at a single-site gap
minimizer proves

    gamma_block <= M Mstar exp(2 beta Delta M) gamma_single.

For M>=1 and beta>=0 this coefficient is no larger than LPW's stated
4 M^2 Mstar exp(2 beta Delta(M+1)). Hence the stated comparison has this alternative
proof, without treating the printed arithmetic simplification as established.

The adjacent Python/SymPy code checks a harmonic-mean algebra identity and the
uniform heat-bath spectrum for m=1..4. Those finite checks support consistency;
the variance and energy arguments above supply the general proof.
