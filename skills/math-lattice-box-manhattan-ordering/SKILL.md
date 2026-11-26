---
name: math-lattice-box-manhattan-ordering
description: Exhaustively optimize or validate a Manhattan-length ordering of all points in a small integer box.
---

# Finite lattice-box Manhattan ordering

Use this skill for boxes having at most nine points. It enumerates every ordering, reports the exact maximum, and evaluates the source's centred-coordinate identity for a supplied maximizer.

```sh
python3 -B scripts/check_box.py --sides 2,3
```

This is a finite certificate only. It does not certify the source's formula for arbitrary side lengths, its inflation construction, or any imported coordinatewise upper bound.

## 文献复核采用的构件

- [Source note: centred-coordinate identity](references/lattice-box-centering.md)
