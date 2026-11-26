#!/usr/bin/env python3
import argparse,json
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--matrix',required=True); a=ap.parse_args()
 def entry(x): return None if x == 'x' else int(x)
 P=[[entry(x) for x in row.split(',')] for row in a.matrix.split(';')]; n=len(P)
 if n==0 or n%2 or any(len(r)!=n or x not in (None,0,1) for r in P for x in r) or any(P[i][i] != 0 for i in range(n)): raise SystemExit('matrix must be even square over x,0,1 with diagonal 0')
 # H=Z/n, L(i,l)=i+l; delta(l)=l+n/2; t is 0 then 1 on its delta partner.
 t=lambda x: 0 if x<n//2 else 1
 elems=['0']+[(i,b,l) for i in range(n) for b in range(2) for l in range(n)]
 def f(x):
  if x=='0': return x
  i,b,l=x; mu=(i+l)%n
  return (l,1,mu) if b==(1+t(mu))%2 else (l,0,(mu+n//2)%n)
 def mult(x,y):
  if x=='0' or y=='0': return '0'
  i,a,l=x; j,b,m=y
  return '0' if P[l][j] is None else (i,(a+P[l][j]+b)%2,m)
 images=[f(x) for x in elems]; products=[mult(x,f(x)) for x in elems]
 out={'index_size':n,'map_bijective':len(set(images))==len(elems),'product_map_bijective':len(set(products))==len(elems)}
 print(json.dumps(out,sort_keys=True))
 if not all(out.values()): raise SystemExit('complete-map verification failed')
if __name__=='__main__': main()
