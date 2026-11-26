# Source note: decomposition lengths

Source: *The decomposition lengths of a numerical semigroup form an interval*, author manuscript (20 Nov 2026), physical pp. 1--5 of 9. Local SHA-256: `528fe7e19805ae7af8a83eb6c88d437e0413b0d764c439e942ca74b1dd4299c9`.

The source defines an irredundant decomposition as an intersection of irreducible numerical oversemigroups (p. 1), gives the special-gap cover criterion (p. 3), and proves its normalizing exchange route on pp. 4--5.  The asset below independently uses only the definitions: finite gap sets encode all oversemigroups, and direct finite enumeration determines the irredundant lengths for a caller-supplied semigroup.  It does not adopt the universal theorem or its cited special-gap and irreducibility characterizations.

Run:

~~~sh
python3 -B scripts/check_lengths.py --gaps 1,2,3,5,6,7
~~~

The checker uses the empty intersection convention for an empty gap set and
reports a length-zero decomposition in that case.
