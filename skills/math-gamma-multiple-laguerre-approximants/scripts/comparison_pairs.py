"""Compare the Aptekarev and Rivoal gamma recurrence baselines."""
import argparse
from fractions import Fraction
import json


def aptekarev(n, a, b, c):
    return (
        (128*n**3 + 40*n*n - 82*n - 45)*c
        - n*n*(256*n**3 - 240*n*n + 64*n - 7)*b
        + n*n*(n - 1)**2*(16*n + 1)*a
    ) / (16*n - 15)


def rivoal(n, a, b, c):
    return (
        (n + 3)*(8*n + 11)*(24*n*n + 145*n + 215)*c
        - (8*n + 27)*(24*n**3 + 105*n*n + 124*n + 25)*b
        + (n + 2)**2*(8*n + 19)*(8*n + 27)*a
    ) / ((n + 3)**2*(8*n + 11)*(8*n + 19))


ROUTES = {
    "aptekarev": (aptekarev, 2, (0, 2, 31), (1, 3, 50)),
    "rivoal": (rivoal, 0, (-1, 4, Fraction(77, 4)), (1, 7, Fraction(65, 2))),
}


def sequence(step, start, initials, end):
    values = list(map(Fraction, initials))
    for n in range(start, start + max(0, end - 2)):
        values.append(step(n, *values[-3:]))
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("route", choices=ROUTES)
    parser.add_argument("n", nargs="+", type=int)
    args = parser.parse_args()
    if min(args.n) < 0:
        parser.error("n must be nonnegative")
    step, start, p0, q0 = ROUTES[args.route]
    p = sequence(step, start, p0, max(args.n))
    q = sequence(step, start, q0, max(args.n))
    print(json.dumps([
        {"n": n, "p": str(p[n]), "q": str(q[n]),
         "ratio": str(p[n]/q[n]) if q[n] else None}
        for n in args.n
    ], indent=2))


if __name__ == "__main__":
    main()
