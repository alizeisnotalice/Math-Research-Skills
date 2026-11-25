#!/usr/bin/env python3
"""Finite exact checks for L16; no asymptotic claim is tested here."""

from __future__ import annotations

from math import gcd, prod


def primes_upto(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if all(n % d for d in range(2, int(n**0.5) + 1))]


def root_count_mod_power(p: int, k: int) -> int:
    modulus = p**k
    return sum((n * n + 1) % modulus == 0 for n in range(modulus))


def check_finite_sieve() -> None:
    # f(n)=n^2+1, k=2; this verifies only the fixed-Y CRT identity.
    X, Y, k = 100, 5, 2
    selected_primes = primes_upto(Y)
    Q = prod(p**k for p in selected_primes)
    allowed = [a for a in range(Q) if all((a * a + 1) % (p**k) for p in selected_primes)]
    local_allowed = prod(p**k - root_count_mod_power(p, k) for p in selected_primes)
    assert len(allowed) == local_allowed
    by_classes = sum(1 for n in range(X + 1, 2 * X + 1) if n % Q in set(allowed))
    direct = sum(
        1
        for n in range(X + 1, 2 * X + 1)
        if all((n * n + 1) % (p**k) for p in selected_primes)
    )
    assert by_classes == direct
    print(f"finite CRT sieve: Q={Q}, allowed_classes={len(allowed)}, A_{Y}({X})={direct}")


def check_kummer_congruence() -> None:
    # In p == 1 (mod q), X^q-a has q roots iff a^((p-1)/q)=1 mod p.
    cases = ((2, 3), (2, 5), (3, 5))
    for a, q in cases:
        checked = 0
        split_primes: list[int] = []
        for p in primes_upto(199):
            if p in (q,) or a % p == 0 or p % q != 1:
                continue
            congruence = pow(a, (p - 1) // q, p) == 1
            roots = sum(pow(x, q, p) == a % p for x in range(p))
            assert (roots == q) == congruence
            checked += 1
            if congruence:
                split_primes.append(p)
        assert checked > 0 and all(gcd(a, p * q) == 1 for p in split_primes)
        print(f"Kummer finite check a={a}, q={q}: split-test primes<200 = {split_primes}")


if __name__ == "__main__":
    check_finite_sieve()
    check_kummer_congruence()
    print("passed: finite identities only; no tail, zero-free region, or density theorem checked")
