import sympy as sp

# Exact two-state sanity check for Seneta (1988), equation (3).
# It illustrates the finite-chain sensitivity inequality only; it is not a proof of it.
P = sp.Matrix([[sp.Rational(3, 4), sp.Rational(1, 4)],
                [sp.Rational(1, 4), sp.Rational(3, 4)]])
P_tilde = sp.Matrix([[sp.Rational(17, 20), sp.Rational(3, 20)],
                      [sp.Rational(1, 4), sp.Rational(3, 4)]])
E = P_tilde - P

def stationary_row(M):
    a, b = sp.symbols("a b")
    sol = sp.solve([a*M[0,0] + b*M[1,0] - a, a+b-1], [a,b], dict=True)[0]
    return sp.Matrix([[sol[a], sol[b]]])

pi = stationary_row(P)
pi_tilde = stationary_row(P_tilde)
tau1 = sp.Rational(1, 2) * max(sum(abs(P[i,j]-P[k,j]) for j in range(2))
                               for i in range(2) for k in range(2))
row_error = max(sum(abs(E[i,j]) for j in range(2)) for i in range(2))
l1_difference = sum(abs((pi_tilde-pi)[0,j]) for j in range(2))
bound = row_error / (1-tau1)
assert pi == sp.Matrix([[sp.Rational(1,2), sp.Rational(1,2)]])
assert pi_tilde == sp.Matrix([[sp.Rational(5,8), sp.Rational(3,8)]])
assert tau1 == sp.Rational(1,2)
assert row_error == sp.Rational(1,5)
assert l1_difference == sp.Rational(1,4)
assert l1_difference <= bound == sp.Rational(2,5)
print("P=", P)
print("P_tilde=", P_tilde)
print("pi=", pi, "pi_tilde=", pi_tilde)
print("tau_1(P)=", tau1, "||E||_row=", row_error)
print("||pi_tilde-pi||_1=", l1_difference, "bound=", bound)
print("Exact inequality holds in this example; this is a sanity check, not the general theorem proof.")
