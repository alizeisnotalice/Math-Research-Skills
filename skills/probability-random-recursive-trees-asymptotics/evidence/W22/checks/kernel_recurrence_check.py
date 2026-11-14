"""Reproducible finite checks for W22 source cards; numerical evidence only."""
from fractions import Fraction
from math import log, pi
from pathlib import Path
import mpmath as mp

OUT = Path(__file__).with_suffix('.txt')
mp.mp.dps = 40

def H(n):
    return sum(1.0/k for k in range(1, n+1))

lines = []
lines.append('W22 local math checks (not proofs)')
lines.append('Runtime: Python fractions + mpmath 1.3.0; exact rational finite checks and float recurrence evaluation.')
lines.append('')
# Exact normalization of q(m,i).
for m in [2, 3, 5, 10, 25, 50]:
    hm = sum((Fraction(1, k) for k in range(1, m)), Fraction(0))
    total = sum((Fraction(m, 2) / (hm*i*(m-i)) for i in range(1, m)), Fraction(0))
    assert total == 1
lines.append('Beta split kernel q(m,i)=m/[2 h_(m-1) i(m-i)] exact rational row sums: m=2,3,5,10,25,50 all equal 1.')
lines.append('Identity used: 1/[i(m-i)]=(1/i+1/(m-i))/m.')
# Reverse harmonic descent row sums.
for i in range(2, 31):
    # Exact finite N telescoping identity; the omitted tail tends to zero as N -> infinity.
    N = 5000
    hn_i = sum(1.0/k for k in range(1, N-i+1))
    hn = sum(1.0/k for k in range(1, N))
    hi = H(i-1)
    partial = (hn_i - hn + hi) / hi
    assert abs(partial - 1.0) < 0.01
p1 = float(6/mp.pi**2 * mp.zeta(2))
assert abs(p1-1) < 1e-35
lines.append('RT003 upward chain row masses: i=1 sums to 6/pi^2*zeta(2)=1; for each i=2,...,30, the telescoping partial sum through j=5000 differs from 1 by <0.01.')
lines.append('Exact identity: sum_(j=i+1)^N 1/[(j-1)(j-i)]=[H_(N-i)-H_(N-1)+H_(i-1)]/(i-1); limit gives h_(i-1)/(i-1).')
lines.append('')
# Evaluate the exact recurrences from RT002 eqs. (2.3), (2.18), (2.41), (2.43).
N = 1000
h = [0.0]*(N+1)
for n in range(1,N+1): h[n] = h[n-1] + 1/n
dm=[0.0]*(N+1); dv=[0.0]*(N+1); lm=[0.0]*(N+1); lv=[0.0]*(N+1)
for n in range(2,N+1):
    denom=h[n-1]
    dm[n]=(1.0+sum(dm[k]/(n-k) for k in range(1,n)))/denom
    dv[n]=sum((dv[k]+(dm[n]-dm[k])**2)/(n-k) for k in range(1,n))/denom
    lm[n]=1.0+sum(lm[k]/(n-k) for k in range(1,n))/denom
    lv[n]=-1.0+sum((lv[k]+(lm[n]-lm[k])**2)/(n-k) for k in range(1,n))/denom
z2=float(mp.zeta(2)); z3=float(mp.zeta(3))
Ad=1/z2; Vd=2*z3/(z2**3); Al=1/(2*z2); Vl=2*z3/(3*z2**3)
lines.append(f'RT002 recurrence check to n={N}, computed from source equations (2.3),(2.18),(2.41),(2.43) by direct float sums. Theorem leading constants: D mean {Ad:.12f}, D variance/log n {Vd:.12f}; L mean/log^2 n {Al:.12f}, L variance/log^3 n {Vl:.12f}.')
lines.append(' n | E[D_n] - (1/zeta(2))log n | Var(D_n)/log n | E[L_n]/log^2 n | Var(L_n)/log^3 n')
for n in [10,100,1000]:
 lines.append(f'{n:4d} | {dm[n]-Ad*log(n): .9f} | {dv[n]/log(n): .9f} | {lm[n]/log(n)**2: .9f} | {lv[n]/log(n)**3: .9f}')
lines.append('These finite-n values illustrate convergence only and do not establish any asymptotic theorem.')
lines.append('')
# Exact symbolic algebra check of the GW variance formula for leaf toll in Poisson(1) GW.
e=mp.e
mu=1/e
cross=mu*(1-mu)
var_f=mu*(1-mu)
gamma2=2*cross-var_f-mu**2
expected=1/e-2/e**2
assert abs(gamma2-expected) < mp.mpf('1e-35')
lines.append('RT020 Theorem 1.5 formula, Poisson(1) GW and f(T)=1{|T|=1}: mu=1/e, E[f(T)(F(T)-|T|mu)]=(1/e)(1-1/e), Var f=(1/e)(1-1/e), hence gamma^2=1/e-2/e^2 = '+mp.nstr(gamma2,14)+'.')
lines.append('This checks only substitution into the printed formula; it does not verify the conditioned-GW CLT or imply a Beta-splitting representation.')
OUT.write_text('\n'.join(lines)+'\n')
print(OUT.read_text())
