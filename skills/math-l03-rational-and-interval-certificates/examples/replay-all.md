Run this source-specific interval replay with the pinned `python-flint` interpreter:

```sh
python3 scripts/replay_section7_bounds.py --all
```

It must print 24 `match=True` rows, one for every (k=6,10,ldots,98).  It neither runs nor replaces the repository's Sage/Pari modular and Thue computations.
