"""Numerically evaluate one feasible 1D family for the B167 objective.

p_d = He_d / sqrt(d!), so for Z~N(0,1), E[p_d]=0 and Var(p_d)=1.
The resulting values are upper bounds on the infimum, not sharpness evidence.
"""
from math import factorial, pi, sqrt, exp
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_hermitenorm

records=[]
for d in range(1,13):
    roots=np.polynomial.hermite_e.hermeroots([0.0]*d+[1.0])
    if np.max(np.abs(np.imag(roots))) > 1e-10:
        raise ArithmeticError(f"nonreal computed Hermite root beyond tolerance for d={d}")
    scale=sqrt(factorial(d))
    def integrand(x):
        p=eval_hermitenorm(d,x)/scale
        return (abs(p)-1.0)**2 * exp(-x*x/2.0)/sqrt(2*pi)
    cuts=[-np.inf,*sorted(float(np.real(r)) for r in roots),np.inf]
    value=0.0; err=0.0
    for a,b in zip(cuts[:-1],cuts[1:]):
        v,e=quad(integrand,a,b,epsabs=2e-11,epsrel=2e-11,limit=250)
        value+=v; err+=e
    records.append({'degree':d,'objective':value,'estimated_abs_quad_error':err,'sqrt_degree_times_objective':sqrt(d)*value})

out={
 'input':'Z standard normal; p_d(Z)=He_d(Z)/sqrt(d!), d=1,...,12.',
 'normalization':'Probabilists Hermite polynomial He_d; E[p_d]=0 and Var[p_d]=1.',
 'method':'SciPy adaptive quadrature of (|p_d|-1)^2 times standard normal density, split at all real Hermite roots.',
 'records':records,
 'interpretation':'Each value is a numerical feasible-point upper bound on the one-dimensional infimum for that degree. It is not a lower bound, does not show asymptotic optimality, and does not determine the all-dimensional sharp constant.',
}
p=Path(__file__).with_name('b167_hermite_candidate_scan.json')
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
