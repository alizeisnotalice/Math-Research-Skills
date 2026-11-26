# Exact positive and negative checks

From the skill directory:

```sh
python3 -B scripts/height_residual.py \
  --g11 '4/(1+x*x+y*y)^2' --g12 0 --g22 '4/(1+x*x+y*y)^2' \
  --z '(x*x+y*y-1)/(x*x+y*y+1)'
```

This is the unit round sphere in stereographic coordinates and returns status
`zero`.  The same Euclidean coordinate metric with `z='x*y'` returns
`nonzero`, since the Hessian determinant is \(-1\) while \(K=0\).
