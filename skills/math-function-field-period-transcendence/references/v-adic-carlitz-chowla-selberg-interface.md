# Finite-place Carlitz period admission

Source checked: Chieh-Yu Chang, Fu-Tsun Wei, and Jing Yu, *v-adic periods of Carlitz motives and Chowla--Selberg formula revisited*, arXiv:2407.15024v3 (2025), physical pp. 1--6 and 39--47 of the local copy.

## Admissible input

Supply a finite place `v` of `F_q(theta)`, its degree, a positive integer `ell`, and the source's CM Carlitz motive together with its stated good-reduction data. Construct the displayed global de Rham basis and the crystalline and de Rham modules. The comparison isomorphism and the required motivic-Galois-dimension statement must be independently available for the exact motive; they are not certified by a numerical gamma evaluation.

## Callable conclusion

With those data, Theorems 1.2.1--1.2.3 give the finite-place crystalline--de Rham period action in terms of the source's `v`-adic arithmetic gamma values. Theorem 1.4.1 states the resulting transcendence degree for the indicated rational arguments as

```text
ell - gcd(ell, deg(v)).
```

Use this only with the source's arithmetic gamma normalization and the supplied comparison/motivic hypotheses. The proof route explicitly passes through product expansions, comparison, switching `v` and infinity, and a motivic-Galois dimension calculation; none may be dropped.

## Stop conditions

Do not apply this card to the classical Euler gamma function, Euler's constant, a general p-adic period, or an unconstructed motive. Missing good reduction, basis conventions, comparison isomorphism, or Galois-dimension input leaves the conclusion conditional rather than established.
