# Scoped reference. Quintic Gepner numerical lattice

Source: OpenAI, *A Gepner stability condition on every smooth quintic threefold*, pinned [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Gepner-stability-condition-on-every-smooth-quintic-threefold-September-24-2026/paper.pdf), SHA-256 `f70b73596fffb0689874c768d3975cb8e16cbdede231c21baef0707ab1898f49`, physical pp. 3--6.

For a smooth complex quintic, represent a numerical class as `(r,c,d,e)` with the normalized Chern-character coordinates of (2.1).  The source gives the exact tensor-by-`O(1)` update

`(r,c,d,e) -> (r, c+r, d+c+r/2, e+d+c/2+r/6)`.

The indicated twist then gives the displayed matrix `M` on this four-dimensional numerical space, with `det(zI-M)=z^4+z^3+z^2+z+1`.  The normalized eigencharge for `lambda=exp(2*pi*i/5)` is

`Z(r,c,d,e)/5 = ((lambda-1)/5)r + (t0^2/2-5/6+i*t0/2)c + (-1/2+i*t0)d-e`,

where `t0=(1/2)cot(pi/5)`, and `Im Z/(5t0)=d+c/2+u r`, `u=(5-sqrt(5))/10`.

Use this only after the caller has supplied the quintic numerical-lattice conventions and the autoequivalence action.  The source's stability condition, tilts, slicing, support property, and slope inequality are not finite linear-algebra certificates.
