#!/usr/bin/env python3
import argparse,json,itertools
DATA={'g1':[(0,1),(0,2),(0,4),(0,6),(1,3),(2,3),(2,5),(4,5),(4,7),(6,7)],'g2':[(0,2),(0,3),(0,6),(1,2),(2,5),(3,4),(3,5),(6,7)]}
def dist(n,E,subset=None):
 V=set(range(n)) if subset is None else set(subset); d=[[99]*n for _ in range(n)]
 for v in V:d[v][v]=0
 for u,v in E:
  if u in V and v in V:d[u][v]=d[v][u]=1
 for k in V:
  for i in V:
   for j in V:d[i][j]=min(d[i][j],d[i][k]+d[k][j])
 return d
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--example',choices=DATA,required=True); a=ap.parse_args(); E=DATA[a.example]; n=8; d=dist(n,E); D=max(max(r) for r in d); tri=[sum((d[x][y],d[x][z],d[y][z])) for x in range(n) for y in range(x,n) for z in range(y,n)]; T=max(tri)
 triples=[[x,y,z] for x in range(n) for y in range(x,n) for z in range(y,n) if d[x][y]+d[x][z]+d[y][z]==T]
 peripheral=[v for v in range(n) if max(d[v])==D]
 median=all(sum(1 for z in range(n) if d[u][z]+d[z][v]==d[u][v] and d[u][z]+d[z][w]==d[u][w] and d[v][z]+d[z][w]==d[v][w])==1 for u in range(n) for v in range(n) for w in range(n))
 dh=True
 for mask in range(1,1<<n):
  V=[v for v in range(n) if mask>>v&1]; dd=dist(n,E,V)
  if max(dd[i][j] for i in V for j in V)<99 and any(dd[i][j]!=d[i][j] for i in V for j in V): dh=False
 out={'example':a.example,'diameter':D,'triameter':T,'triametral_triples':triples,'peripheral':peripheral,'median':median,'distance_hereditary':dh}
 print(json.dumps(out,sort_keys=True))
 if not median: raise SystemExit('median check failed')
if __name__=='__main__':main()
