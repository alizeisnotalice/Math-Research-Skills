# Divergence-form residual repair

For a supplied smooth positive pair \((A,\rho)\), a real smooth function
\(u\), positive contravariant tensor \(I\), and volume divergence
\(\operatorname{div}_\mu\), put

\[
r=\operatorname{div}_\mu(A\,du)+k^2\rho u,
\quad D=u^2+I(du,du),
\quad F=-r/D.
\]

If \(D>0\), define

\[
\delta A=FuI,
\qquad
\delta\rho=k^{-2}\{Fu-\operatorname{div}_\mu(FIdu)\}.
\]

The product rule gives

\[
\operatorname{div}_\mu(\delta A\,du)+k^2\delta\rho\,u
=F\{I(du,du)+u^2\}=-r.
\]

Thus the corrected pair has \(u\) as an exact eigenfunction whenever its two
coefficients remain positive. This is an algebraic repair identity. It does
not construct a residual, establish the derivative estimates needed to make
the correction small, or imply a nodal construction.

The source is OpenAI, *Power-law violations of Yau's nodal upper bound*,
Lemma 5.3 and equation (5.18), physical pp. 27--28, fixed local SHA-256
`b8b6757d7a3a49d70e4cd367848cc017f777403acf72d18337c70cbfc2a410c7`.
The relevant primary version is [the pinned OpenAI PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/paper.pdf).

`scripts/check_divergence_residual_repair.py` gives a narrower executable
certificate on one interval in a one-dimensional coordinate chart with
\(d\mu=dx\). It accepts rational polynomial data, verifies the identity using
exact symbolic rational arithmetic, and uses exact Bernstein coefficients to
certify strict positivity of \(A,\rho,I,D\) and the corrected coefficients.
The Bernstein gate is sufficient, and can reject a positive rational function
when its selected representation has mixed Bernstein coefficients.

从本技能目录运行下列命令，输出日志包含 `corrected_residual`。环境选择器加载实际已有的 SymPy。

```sh
python3 -B ../python-math/scripts/run_math.py --require sympy --workdir . \
  scripts/check_divergence_residual_repair.py examples/divergence-residual-repair-positive.json
```
