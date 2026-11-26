#!/usr/bin/env python3
"""Exact finite check for F=x+F(x^p) over F_p."""
import argparse

def is_prime(p):
    if p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d += 1
    return True

def is_power_of_p(n, p):
    if n < 1:
        return False
    while n % p == 0:
        n //= p
    return n == 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prime', type=int, required=True)
    ap.add_argument('--cutoff', type=int, required=True)
    args = ap.parse_args()
    if not is_prime(args.prime):
        raise SystemExit('prime must be prime')
    if args.cutoff < 0:
        raise SystemExit('cutoff must be nonnegative')
    a = [0] * (args.cutoff + 1)
    for n in range(1, args.cutoff + 1):
        a[n] = 1 if n == 1 else (a[n // args.prime] if n % args.prime == 0 else 0)
    bad = [n for n in range(1, args.cutoff + 1) if a[n] != int(is_power_of_p(n, args.prime))]
    print({'prime': args.prime, 'cutoff': args.cutoff, 'support': [n for n in range(1, args.cutoff + 1) if a[n]], 'exact_window': not bad})
    if bad:
        raise SystemExit('recurrence/support mismatch')

if __name__ == '__main__':
    main()
