"""Exact free-boundary square peak counts by descending-order DP and brute force."""
from collections import Counter
from functools import lru_cache
from itertools import permutations
from math import factorial
import json
import random
from pathlib import Path


def grid_graph(n):
    N=n*n
    adj=[0]*N
    for r in range(n):
        for c in range(n):
            v=r*n+c
            for rr,cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=rr<n and 0<=cc<n:
                    adj[v] |= 1 << (rr*n+cc)
    return adj


def dp_peak_distribution(adj, peak_cap=2):
    N=len(adj)
    full=(1<<N)-1
    @lru_cache(None)
    def count(rem,k):
        if k<0: return 0
        if rem==0: return int(k==0)
        total=0
        bits=rem
        while bits:
            b=bits & -bits; bits-=b
            v=b.bit_length()-1
            is_peak=(adj[v] & rem)==adj[v]
            total += count(rem^b, k-int(is_peak))
        return total
    dist={k:count(full,k) for k in range(peak_cap+1)}
    return dist, count.cache_info().currsize


def exact_sample_order(adj, target_peaks=2, seed=20261113):
    """Sample exactly uniformly from all descending orders with target peaks.

    Each branch is selected with weight equal to its exact integer completion count.
    A fair random integer in [0,total) is the only randomness required.
    """
    N=len(adj); full=(1<<N)-1
    @lru_cache(None)
    def count(rem,k):
        if k<0: return 0
        if rem==0: return int(k==0)
        total=0; bits=rem
        while bits:
            b=bits & -bits; bits-=b; v=b.bit_length()-1
            is_peak=(adj[v] & rem)==adj[v]
            total += count(rem^b, k-int(is_peak))
        return total
    rng=random.Random(seed)
    rem=full; k=target_peaks; order=[]
    while rem:
        options=[]; total=0; bits=rem
        while bits:
            b=bits & -bits; bits-=b; v=b.bit_length()-1
            is_peak=(adj[v] & rem)==adj[v]
            w=count(rem^b,k-int(is_peak))
            if w: options.append((v,is_peak,w)); total+=w
        if total==0: raise ValueError("target peak count is infeasible")
        draw=rng.randrange(total)
        for v,is_peak,w in options:
            if draw<w:
                order.append(v); rem ^= 1<<v; k-=int(is_peak); break
            draw-=w
    return order, count(full,target_peaks)


def brute_square(n, max_peaks=2):
    N=n*n; adj=grid_graph(n)
    dist=Counter(); pair_dist=Counter()
    for order in permutations(range(N)):
        # Descending label order; selected earlier vertices have larger labels.
        remaining=(1<<N)-1
        peaks=[]
        for v in order:
            if adj[v] & remaining == adj[v]:
                peaks.append(v)
            remaining ^= 1<<v
        if len(peaks)<=max_peaks:
            dist[len(peaks)] += 1
        if len(peaks)==2:
            r1,c1=divmod(peaks[0],n); r2,c2=divmod(peaks[1],n)
            pair_dist[abs(r1-r2)+abs(c1-c2)] += 1
    return dict(dist),dict(pair_dist)


def main():
    results={}
    for n in (2,3,4):
        d,states=dp_peak_distribution(grid_graph(n),2)
        results[str(n)]={"dp_counts_k_0_to_2":d,"dp_states":states,"n_factorial":factorial(n*n)}
        if n<=3:
            brute,pair=brute_square(n)
            results[str(n)]["brute_counts_k_0_to_2"]={k:brute.get(k,0) for k in range(3)}
            results[str(n)]["brute_pair_distance_counts_given_exactly_2"]={str(k):v for k,v in sorted(pair.items())}
            results[str(n)]["dp_matches_brute"] = all(d[k]==brute.get(k,0) for k in range(3))
    sample_order,total=exact_sample_order(grid_graph(3),2)
    remaining=(1<<9)-1; peaks=[]
    for v in sample_order:
        if grid_graph(3)[v] & remaining == grid_graph(3)[v]: peaks.append(v)
        remaining ^= 1<<v
    results["exact_sampler_demo"]={"seed":20261113,"descending_order_vertices_0_based":sample_order,
                                   "peak_vertices_0_based":peaks,"peak_count":len(peaks),
                                   "exact_target_total":total}
    out=Path(__file__).with_name("verification_results.json")
    out.write_text(json.dumps(results,indent=2,sort_keys=True)+"\n")
    print(json.dumps(results,indent=2,sort_keys=True))

if __name__=="__main__": main()
