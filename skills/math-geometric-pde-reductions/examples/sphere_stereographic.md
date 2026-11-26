# Exact positive and negative checks

Run the example from the skill directory. The launcher selects an existing interpreter with SymPy and records the certificate output in its `stdout` log.

```sh
python3 -B ../python-math/scripts/run_math.py --require sympy --workdir . scripts/height_residual.py \
  --g11 '4/(1+x*x+y*y)^2' --g12 0 --g22 '4/(1+x*x+y*y)^2' \
  --z '(x*x+y*y-1)/(x*x+y*y+1)'
```

This is the unit round sphere in stereographic coordinates and returns status
`zero`.  The Euclidean coordinate metric `g11=g22=1, g12=0` with `z='x*y'` returns
`nonzero`, since the Hessian determinant is \(-1\) while \(K=0\).
