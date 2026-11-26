# Odd folded-window certificate for tensor products

Source: *Tensor products of Mycielskians of odd cycles with odd wheels and with extended Mycielskians of odd cycles are not word-representable*, version 2 (12 Nov 2026), physical pp. 3--6 of 9. Local SHA-256: `8e76ce77af955bc6674149c8733a2d856f70ab771c6a8f385404f3bd19094f39`.

## Certified finite kernel

For the labelled `F9` and `F11` graphs of physical p. 4, independently enumerate all `2^9` and `2^11` orientations. Retain an orientation exactly when it has property (P): for every directed path `a -> c -> d -> b` whose endpoints are adjacent, both shortcut edges `a-d` and `c-b` exist.  The resulting input/output five-edge-state constraints form a bipartite graph on 32 states. The independent replay reports 72 accepted `F9` orientations, 44 accepted `F11` orientations, 56 union constraints, and colouring SHA-256 `0b800be2dc876e8adfa6100a3a6b727507ce6374411c1b02f213e9ddf405d0a8`. Thus every permitted `F9` or `F11` window reverses its colour.

## Word-to-(P) implication

Let a word represent a graph and orient every edge from the letter occurring first. For an oriented path `a -> c -> d -> b` with `a` adjacent to `b`, each prefix has

`alpha=#a-#c`, `beta=#c-#d`, `gamma=#d-#b`, and `delta=#a-#b` in `{0,1}`.

The identities `alpha+beta=delta-gamma` and `beta+gamma=delta-alpha` force both prefix differences `#a-#d` and `#c-#b` into `{0,1}`. Their first letters occur in the displayed direction order, so the two pairs alternate and hence are edges of the represented graph. This proves (P) without the paper's Lean claim.

## Fold and odd closure

Let `3 <= k < K` be odd, `K >= 5`, and let `H` be either `mu_k` or `mu'_k`. Define the printed fold `phi: Z_K -> Z_k` by `phi(i)=i` for `i<k`, then alternately `k-2,k-1`. In `H x mu'_K`, put `R=(w,w)`, `T_i=(v_phi(i),v_i)`, and `S_i=(u_phi(i),u_i)`.

Directly checking the factor adjacencies shows that each ordered seven-vertex window `(R,T_i,T_{i+1},T_{i+2},S_i,S_{i+1},S_{i+2})` induces exactly `F9` or `F11`: the only variable pair is the symmetric pair `T_i S_{i+2}`, `T_{i+2} S_i`; when present both give `F11`, otherwise `F9`. Distinctness follows from the second coordinates because `K>=5`. The output five edges of window `i` are, in order, the input five edges of window `i+1`. Therefore a word representation would force a two-colour flip at every one of the `K` windows. Since `K` is odd, returning to window zero would reverse its colour, a contradiction.

This establishes the source's Theorem 3 route for `mu_k x mu'_K` and `mu'_k x mu'_K`, within the explicit definitions above. It does not certify the separate wheel-product theorem, or claims about external Lean builds.

## Reproduction

~~~sh
python3 -B scripts/verify_window_coloring.py
python3 -B scripts/replay_fold_windows.py --family mu --k 3 --K 5
python3 -B scripts/replay_fold_windows.py --family muext --k 5 --K 7
~~~
