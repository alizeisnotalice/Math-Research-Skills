#!/usr/bin/env python3
"""Exact scalar replay of the prefix-state chunk-to-letter construction."""
from __future__ import annotations
import argparse, json
from fractions import Fraction

def fail(msg):
    print(json.dumps({'ok': False, 'error': msg})); raise SystemExit(2)

def main():
    p=argparse.ArgumentParser(); p.add_argument('fixture'); args=p.parse_args()
    d=json.load(open(args.fixture)); alphabet=d['alphabet']; labels=d['labels']; maxlen=d['max_length']
    if not alphabet or len(set(alphabet)) != len(alphabet) or any(not isinstance(a,str) or len(a)!=1 for a in alphabet): fail('alphabet must be distinct one-character symbols')
    if not isinstance(maxlen,int) or maxlen<0: fail('max_length must be nonnegative')
    if any(not isinstance(x['word'],str) or not x['word'] or any(c not in alphabet for c in x['word']) for x in labels): fail('each label word must be nonempty over alphabet')
    weights={}
    for x in labels: weights[x['word']]=weights.get(x['word'],Fraction(0))+Fraction(x['weight'])
    prefixes={''}
    for w in weights: prefixes.update(w[:i] for i in range(1,len(w)))
    states=sorted(prefixes,key=lambda z:(len(z),z)); pos={s:i for i,s in enumerate(states)}; n=len(states)
    trans={a:[[Fraction(0) for _ in states] for _ in states] for a in alphabet}
    for s in states:
        for a in alphabet:
            u=s+a
            if u in prefixes: trans[a][pos[s]][pos[u]] += 1
            if u in weights: trans[a][pos[s]][pos['']] += weights[u]
    def automaton(word):
        v=[Fraction(0)]*n; v[pos['']]=1
        for a in word: v=[sum(v[i]*trans[a][i][j] for i in range(n)) for j in range(n)]
        return v[pos['']]
    def chunk(word):
        f=[Fraction(0)]*(len(word)+1); f[0]=1
        for i in range(1,len(word)+1): f[i]=sum(f[i-len(w)]*c for w,c in weights.items() if i>=len(w) and word[i-len(w):i]==w)
        return f[-1]
    words=['']
    for _ in range(maxlen): words += [w+a for w in list(words) if len(w)<maxlen for a in alphabet]
    bad=[w for w in words if automaton(w)!=chunk(w)]
    if bad: fail('prefix automaton mismatch at '+bad[0])
    print(json.dumps({'ok':True,'states':states,'checked_words':len(words),'labels':len(weights)}))
if __name__=='__main__': main()
