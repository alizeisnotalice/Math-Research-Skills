---
name: math-grid-piecewise-translation-embedding
description: Certify a finite cellwise translation embedding between two strict-size subsets of a specified square cell grid. Use after a geometric argument has supplied an allowable common grid; it does not polygonize sets or prove a general equidecomposition theorem.
---

# Finite grid piecewise-translation embedding

Use this interface when the geometric part of a strict-comparison argument has
already reduced two sets to finite unions of cells of one specified square grid.
The checker constructs and verifies a one-to-one list of cell translations from
`source` into `target` whenever the listed source has strictly fewer cells.

The input is JSON with positive integers `side` and `tracks`, and `source` and
`target` lists of cells `[track, x, y]`, where
`0 <= track < tracks` and `0 <= x,y < side`.  Each list must have no repeated
cell.  Run:

```sh
python3 scripts/check_grid_embedding.py examples/strict-positive.json
```

An output translation applies only to its one source cell.  Thus the output is
a finite piecewise translation, not a single global translation.  The input
cell grid is an external geometric certificate: this skill does **not** check
that arbitrary polygons were correctly subdivided, that a grid belongs to a
specified algebra, or that a translation remains admissible after changing
the grid.

Strict cardinality is essential.  Equality is deliberately rejected, even
when a bijection happens to exist; use a separately justified equal-area
equidecomposition argument for that situation.  The finite proof and source
boundary are in [the comparison note](references/grid-embedding.md).
