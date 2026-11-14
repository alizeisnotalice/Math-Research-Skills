"""Exact symbolic cross-checks for two L11 batch02 source statements.

These calculations check identities and a literal standalone reading only;
they do not replace the source proofs or settle C019's intended scope.
"""

import sympy as sp


def main() -> None:
    x, y, z = sp.symbols("x y z", positive=True)
    image = (
        x**2 + 2 * x * y,
        y**2 + 2 * y * z,
        z**2 + 2 * z * x,
    )
    product_ratio = sp.factor(sp.prod(image) / (x * y * z))
    assert sp.expand(sum(image) - (x + y + z) ** 2) == 0
    assert sp.expand(
        (x + 2 * y) + (2 * x + z) + (y + 2 * z) - 3 * (x + y + z)
    ) == 0

    # The literal, standalone subset inequalities in the printed C019 Thm 3.4
    # permit A=0 in dimension 2, whereas a symmetrized row-stochastic matrix
    # has total entry sum 2. This does not decide whether U1 is an intended
    # standing restriction in the source.
    A0 = sp.zeros(2)
    subsets = [(), (0,), (1,), (0, 1)]
    subset_sums = [sum(A0[i, j] for i in alpha for j in alpha) for alpha in subsets]
    T = sp.Matrix([[sp.Rational(1, 3), sp.Rational(2, 3)],
                    [sp.Rational(1, 4), sp.Rational(3, 4)]])
    row_stochastic = all(sum(T[i, j] for j in range(2)) == 1 for i in range(2))
    symmetrized_total = sp.simplify(sum((T + T.T) / 2))

    print("SymPy", sp.__version__)
    print("C013 sum(V_coordinates)=", sp.factor(sum(image)))
    print("C013 phi(Vx)/phi(x)=", product_ratio)
    print("C013 three positive factors sum=3*(x+y+z)")
    print("C019 A=0 subset sums in dimension 2=", subset_sums)
    print("C019 example T is row-stochastic=", row_stochastic)
    print("C019 sum( (T+T^T)/2 )=", symmetrized_total)
    print("Scope limit: literal-statement check only; intended U1 standing hypothesis remains for R02 review.")


if __name__ == "__main__":
    main()
