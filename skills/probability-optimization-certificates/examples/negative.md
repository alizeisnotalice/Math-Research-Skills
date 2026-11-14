# Negative example: decimal solver status is not a proof

Suppose a floating-point solver reports “optimal” and returns a primal point with a small equality residual and a dual point with a small negative multiplier. Those values do not certify feasibility or optimality: the residual may be nonzero, the multiplier sign may be wrong, and the apparent gap may be smaller than rounding error. Recheck exact rational data with exact arithmetic or enclose each operation rigorously; otherwise label the result exploratory.

Likewise, do not claim strong duality for an SDP solely because both solvers return similar objective values. Verify the relevant qualification (or use a justified facial-reduction/extended-dual result), primal and dual feasibility, and attainment requirements. Even an exact finite optimum says nothing by itself about a sequence of problems as `n→∞`.
