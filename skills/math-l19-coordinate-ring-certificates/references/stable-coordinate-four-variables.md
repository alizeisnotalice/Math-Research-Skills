# Stable coordinate in four variables

Source: *A stable coordinate that is not a coordinate in four variables*, SHA
`52d49d150cf01ef08c0eb878d1fde75b17125437a276a9616b4df7f1adeedcaa`,
physical pp. 4--5.

This is an auxiliary reference for exactly the displayed presentation. After
adjoining `w`, the locally nilpotent derivation has `Delta(H)=p` and fixes `p`,
so `exp(w Delta)` transports `H` to `H+p w`. The coordinate substitution uses
`x_0=s^2-u^2` and
`L=x_0^2 F-(1+2 s x_0)J`,
`N=(1-2s x_0)F+4s^2J`.
Its coefficient matrix has determinant one, with inverse
`F=4s^2L+(1+2s x_0)N` and
`J=-(1-2s x_0)L+x_0^2N`.

From the skill directory, the Python launcher selects SymPy and records the exact check.

```sh
python3 -B ../python-math/scripts/run_math.py --require sympy --workdir .   scripts/check_stable_coordinate_substitution.py --case positive
``` It does not prove that an arbitrary
presentation is stably polynomial, nor does it decide coordinate status before
or after adjoining variables.

## 固定来源

- 物理页 4, 5。Equations (2.4)--(2.12), Proposition 2.2 and the determinant-one coordinate change after adjoining w. SHA-256 `52d49d150cf01ef08c0eb878d1fde75b17125437a276a9616b4df7f1adeedcaa`。[A stable coordinate that is not a coordinate in four variables](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/stable-coordinate-four-variables.pdf)
