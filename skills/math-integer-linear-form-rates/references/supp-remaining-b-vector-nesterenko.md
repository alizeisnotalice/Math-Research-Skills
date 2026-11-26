# Scoped reference. Vector Nesterenko criterion

Source: Stéphane Fischler, *Nesterenko's linear independence criterion for vectors*, local arXiv:1202.2279v2 SHA-256 `7c90baa0d46fdba5d0dabceeed1284cfd35aa4ca56b163efc2337a234f5c4d1e`, physical pp. 1--2.  The formal version was verified as *Monatshefte für Mathematik* **177** (2015), 397--419, DOI [10.1007/s00605-015-0769-9](https://doi.org/10.1007/s00605-015-0769-9), whose published metadata identifies the same vector criterion.

Let `1<=k<=p-1`, `e_1,...,e_k in R^p`, pairwise distinct `tau_j>0`, and increasing positive integers `Q_n` with `Q_(n+1)=Q_n^(1+o(1))`.  If integer-coefficient forms `L_n` have `|L_n(e_j)|=Q_n^(-tau_j+o(1))` for every `j`, and maximal coefficient at most `Q_n^(1+o(1))`, then every rational subspace containing all `e_j` has dimension at least `k+sum_j tau_j`.

This is an asymptotic transfer theorem.  Apply it only after proving the integer coefficient bound and each exact rate, including pairwise-distinct exponents; finite numerical samples and common/undistinguished exponents do not meet its interface.
