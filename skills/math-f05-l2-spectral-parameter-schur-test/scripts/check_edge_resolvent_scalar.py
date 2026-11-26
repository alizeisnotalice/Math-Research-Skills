#!/usr/bin/env python3
"""Exact scalar N=2 replay of the p.39 edge-resolvent contract."""
import json,sys
from fractions import Fraction as F
from pathlib import Path
def main(path):
 d=json.loads(Path(path).read_text()); b=[F(x) for x in d['B']]; a=F(d['a']); bs=F(d['b_sq']); rs=F(d['rho_sq'])
 if len(b)!=2 or any(abs(x)>a for x in b): raise ValueError('declared individual norm bound fails')
 if b[0]*b[0]+b[1]*b[1]>bs: raise ValueError('declared projected square-sum bound fails')
 if abs(b[0]*b[1])>rs: raise ValueError('declared edge spectral-radius bound fails')
 m2=max(a*a,bs,rs); lhs=(b[0]+b[1])**2
 if lhs>9*m2: raise ValueError('conclusion bound fails')
 print('verified: scalar N=2 edge contract')
try: raise SystemExit(main(sys.argv[1]))
except (IndexError,ValueError) as e: print('rejected: '+str(e),file=sys.stderr); raise SystemExit(2)
