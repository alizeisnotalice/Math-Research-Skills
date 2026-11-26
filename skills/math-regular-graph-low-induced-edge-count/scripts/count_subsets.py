#!/usr/bin/env python3
"""Exact small-graph induced-edge enumerator."""
import argparse, json

def parse_edges(raw, n):
    out = set()
    for item in raw:
        u, v = item
        if not (0 <= u < n and 0 <= v < n) or u == v:
            raise ValueError('edge endpoint out of range or loop')
        edge = tuple(sorted((u, v)))
        if edge in out:
            raise ValueError('duplicate edge')
        out.add(edge)
    return sorted(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--graph-json', required=True, help='JSON object with n and edges')
    ap.add_argument('--budget', type=int, required=True)
    a = ap.parse_args()
    g = json.loads(a.graph_json)
    n = g['n']; edges = parse_edges(g['edges'], n)
    if n < 0 or a.budget < 0:
        raise SystemExit('n and budget must be nonnegative')
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1; deg[v] += 1
    count = 0
    for mask in range(1 << n):
        induced = sum(((mask >> u) & 1) and ((mask >> v) & 1) for u, v in edges)
        count += induced <= a.budget
    print(json.dumps({'n': n, 'edges': edges, 'degree_sequence': deg, 'regular': len(set(deg)) <= 1, 'budget': a.budget, 'count': count, 'enumerated_subsets': 1 << n}))

if __name__ == '__main__':
    main()
