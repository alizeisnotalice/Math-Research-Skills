---
name: math-differential-operator-minimization
description: Minimize a supplied rational-coefficient differential operator for a specified formal solution, after certifying the Ore factor, degree-bound and initial-series subroutines.
---

# Differential-operator minimization

Use this skill for a formal solution \(S\in\mathbb Q[[z]]\) of a supplied operator
\(L\in\mathbb Q[z]\langle\partial_z\rangle\), when the question is the least order
of an operator annihilating that particular solution. This is different from factoring
\(L\) without its selected solution.

Supply the indicial roots at zero, enough exact initial coefficients to identify \(S\),
and a certified degree bound for every requested right-factor order. Apply the source
algorithm only with exact series extension, approximant bases, and greatest common
right divisors in the Ore algebra. Its terminal residual test must cover the required
initial data. The result is a minimal annihilator for the specified solution.

For an E-function value, keep the minimization output separate from the subsequent
desingularization and algebraic-value procedure. A minimal differential equation alone
does not decide whether an E-function takes an algebraic value.

Read [the source contract](references/ext0270-operator-minimization.md) before
using the algorithm.
