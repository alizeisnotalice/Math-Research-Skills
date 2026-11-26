#!/usr/bin/env python3
import argparse,json
from fractions import Fraction
H=[1,9,28,42,39,22,7,1]; A=[1,10,36,65,75,57,28,8,1]; B=[1,10,36,64,66,41,14,2]
def add(a,b): return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def mul(a,b):
 r=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]+=x*y
 return r
def scale_x(a):return [0]+a
def ev(a,x):return sum(c*x**i for i,c in enumerate(a))
def poly(word):
 z=u=[1]
 for c in reversed(word):
  p={'A':A,'B':B,'O':[1]}[c]; q={'A':scale_x(H),'B':scale_x(H),'O':[0,1]}[c]
  z,u=add(mul(p,z),mul(q,u)),mul(p,z)
 return z
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--family',type=int,required=True); a=ap.parse_args()
 if a.family<1:raise SystemExit('family must be positive')
 vals=[]
 for j in range(a.family+1):
  p=poly('A'*j+'B'*(a.family-j)); vals.append([ev(p,Fraction(-1,10)),ev(p,Fraction(-1,6))])
 out={'m':a.family,'values_at_minus_1_10':[str(x[0]) for x in vals],'values_at_minus_1_6':[str(x[1]) for x in vals],'strictly_decreases_at_minus_1_10':all(vals[i][0]>vals[i+1][0] for i in range(a.family)),'strictly_increases_at_minus_1_6':all(vals[i][1]<vals[i+1][1] for i in range(a.family))}
 print(json.dumps(out,sort_keys=True))
 if not out['strictly_decreases_at_minus_1_10'] or not out['strictly_increases_at_minus_1_6']:raise SystemExit('sign-separation check failed')
if __name__=='__main__':main()
