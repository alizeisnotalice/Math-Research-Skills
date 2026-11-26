#!/usr/bin/env python3
"""Exact finite certificate for the projective-induction transport identity.

All phases are rational exponents of exp(2*pi*i*x), represented by strings
accepted by fractions.Fraction.  It deliberately handles finite Cayley tables
only: it checks the algebraic hypotheses behind Lemma 2.1, not any analytic
normality assertion for an infinite von Neumann algebra.
"""
import argparse
import json
import sys
from fractions import Fraction


def frac(value):
    return Fraction(str(value)) % 1


def phase(table, a, b):
    return frac(table.get(a, {}).get(b, "0"))


def main(path):
    data = json.load(open(path, encoding="utf-8"))
    G, L = data["gamma"], data["lambda"]
    for name, group in (("gamma", G), ("lambda", L)):
        E, one, mult = group["elements"], group["identity"], group["multiplication"]
        if one not in E or set(mult) != set(E) or any(set(mult[a]) != set(E) for a in E):
            raise ValueError(f"{name}: multiplication is not a complete Cayley table")
        if any(mult[one][a] != a or mult[a][one] != a for a in E):
            raise ValueError(f"{name}: declared identity fails")
        if any(mult[mult[a][b]][c] != mult[a][mult[b][c]] for a in E for b in E for c in E):
            raise ValueError(f"{name}: table is not associative")
    def gm(a,b): return G["multiplication"][a][b]
    def lm(a,b): return L["multiplication"][a][b]
    def gi(a): return next(x for x in G["elements"] if gm(a,x) == G["identity"] and gm(x,a) == G["identity"])
    def li(a): return next(x for x in L["elements"] if lm(a,x) == L["identity"] and lm(x,a) == L["identity"])
    D = [(g,h) for g in G["elements"] for h in L["elements"]]
    def mul(x,y): return (gm(x[0],y[0]), lm(x[1],y[1]))
    def inv(x): return (gi(x[0]),li(x[1]))
    one = (G["identity"], L["identity"])
    mu, omega = data.get("mu", {}), data.get("omega", {})
    def alpha(x,y): return (phase(mu,x[0],y[0])+phase(omega,x[1],y[1])) % 1
    if any(alpha(one,x) or alpha(x,one) for x in D):
        raise ValueError("multiplier is not normalized")
    if any((alpha(x,y)+alpha(mul(x,y),z)-alpha(y,z)-alpha(x,mul(y,z))) % 1 for x in D for y in D for z in D):
        raise ValueError("product multiplier fails the exact cocycle identity")
    A, B, delta = data["A"], data["B"], data["delta"]
    if len(set(A)) != len(A) or set(delta) != set(A) or set(delta.values()) != set(B):
        raise ValueError("delta is not a bijection A -> B")
    if any(gm(a,b) not in A for a in A for b in A) or any(lm(a,b) not in B for a in B for b in B):
        raise ValueError("A or B is not closed")
    if any(delta[gm(a,b)] != lm(delta[a],delta[b]) for a in A for b in A):
        raise ValueError("delta is not a subgroup homomorphism")
    C = [(a,delta[a]) for a in A]
    theta = data["gamma_phase"]
    if set(theta) != set(A) or frac(theta[G["identity"]]):
        raise ValueError("gamma_phase is not normalized on A")
    if any((frac(theta[a])+frac(theta[b])-frac(theta[gm(a,b)])-alpha((a,delta[a]),(b,delta[b]))) % 1 for a in A for b in A):
        raise ValueError("gamma_phase does not realize alpha restricted to the graph")
    reps = [tuple(x) for x in data["reps"]]
    if len(set(reps)) != len(reps) or any(r not in D for r in reps):
        raise ValueError("representatives are not distinct elements of Gamma x Lambda")
    cosets = [{mul(r,c) for c in C} for r in reps]
    if set().union(*cosets) != set(D) or sum(map(len,cosets)) != len(D):
        raise ValueError("representatives do not give a disjoint exhaustive left-coset system")
    def target(y):
        hits = [i for i,Q in enumerate(cosets) if y in Q]
        if len(hits) != 1: raise ValueError("ambiguous coset target")
        return hits[0]
    def corr(s,x):
        y = mul(s,reps[x]); q = target(y)
        return q, mul(mul(inv(reps[q]),s),reps[x])
    if any(c not in C for s in D for x in range(len(reps)) for _,c in [corr(s,x)]):
        raise ValueError("correction leaves graph subgroup")
    if any(mul(corr(s,target(mul(t,reps[x])))[1],corr(t,x)[1]) != corr(mul(s,t),x)[1] for s in D for t in D for x in range(len(reps))):
        raise ValueError("c(s,t x)c(t,x)=c(st,x) fails")
    def transport(s,x):
        q,c = corr(s,x)
        return q, (alpha(s,reps[x])+alpha(reps[q],c)+frac(theta[c[0]])) % 1
    if any((transport(s,target(mul(t,reps[x])))[1]+transport(t,x)[1]-transport(mul(s,t),x)[1]-alpha(s,t)) % 1 for s in D for t in D for x in range(len(reps))):
        raise ValueError("transport phase fails U_s U_t = alpha(s,t) U_st")
    changed = False
    if "alt_reps" in data:
        alt = [tuple(x) for x in data["alt_reps"]]
        if len(alt) != len(reps): raise ValueError("alt_reps has wrong length")
        old, old_cosets = reps, cosets
        def target_in(y, system):
            hits = [i for i,Q in enumerate(system) if y in Q]
            if len(hits) != 1: raise ValueError("ambiguous coset target")
            return hits[0]
        reps = alt
        cosets = [{mul(r,c) for c in C} for r in reps]
        if set().union(*cosets) != set(D) or sum(map(len,cosets)) != len(D):
            raise ValueError("alt_reps do not cover the left cosets")
        if any(alt[i] not in old_cosets[i] for i in range(len(old))):
            raise ValueError("alt_reps must preserve the supplied coset ordering")
        def old_transport(s,x):
            q=target_in(mul(s,old[x]),old_cosets)
            c=mul(mul(inv(old[q]),s),old[x])
            return q, (alpha(s,old[x])+alpha(old[q],c)+frac(theta[c[0]])) % 1
        def F(x):
            k=mul(inv(old[x]),reps[x])
            if k not in C: raise ValueError("paired alternate representative changes coset")
            return (-alpha(old[x],k)+frac(theta[k[0]])) % 1
        for s in D:
            for x in range(len(old)):
                q_new,p_new=transport(s,x)
                q_old,p_old=old_transport(s,x)
                if q_new != q_old or (F(q_new)+p_new-p_old-F(x)) % 1:
                    raise ValueError("representative-change intertwiner fails")
        changed = True
    n = int(data["dimension_n"])
    if n <= 0: raise ValueError("dimension_n must be positive")
    print(json.dumps({"status":"valid", "cosets":len(cosets), "graph_size":len(C), "dimension_M":n*(len(L)//len(B)), "dimension_N":n*(len(G)//len(A)), "representative_change_checked":changed}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="JSON finite graph-induction contract")
    try: main(parser.parse_args().input)
    except Exception as e:
        print(f"invalid: {e}", file=sys.stderr); sys.exit(2)
