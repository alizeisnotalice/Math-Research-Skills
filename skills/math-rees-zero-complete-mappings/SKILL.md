---
name: math-rees-zero-complete-mappings
description: Verify the explicit even-index complete mapping of a finite Rees 0-matrix semigroup over Z/2Z with identity diagonal.
---

# Rees 0-matrix complete mappings

For an even index count `N`, this checker builds the source's explicit complete mapping on `M^0(Z/2Z,H,H,P)` for a supplied sandwich matrix over `x,0,1`, where `x` denotes a zero product and the diagonal entries are the group identity `0`. It verifies that both the map and `x -> x f(x)` are bijections.

```sh
python3 -B scripts/check_even_index.py --matrix '0,1;1,0'
```

This checks the additive rank-two quotient only. It does not construct Brauer diagrams, lift through the alternating group, classify principal factors, or invoke Hall--Paige.

## 文献复核采用的构件

- [Source note: even-index Rees construction](references/rees-even-index-complete-map.md)
