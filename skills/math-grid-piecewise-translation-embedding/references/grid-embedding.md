# Strict finite-cell comparison

## Statement

Fix a finite collection of square cells in finitely many tracks of a common
grid.  If `source` and `target` are duplicate-free cell lists and
\(|\mathrm{source}|<|\mathrm{target}|\), there is a cellwise translation
embedding of the union of source cells into the union of target cells.

This is the combinatorial final step of Lemma 3.1 (physical pp. 6--7) of
*An infinite finitely presented simple amenable group*, OpenAI, 23 September
2026, pinned PDF SHA-256
`810ff1d8e0901a21d4cb9075a3dc4716716ebfd75f2279583b335bdfdf43f5f0`,
[official pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-Infinite-Finitely-Presented-Simple-Amenable-Group-September-23-2026/paper.pdf).

## Independent finite proof

Order both finite lists lexicographically and pair the \(i\)-th source cell
with the \(i\)-th target cell.  The target cells are distinct, so this is
injective.  For a source cell with lower-left grid coordinates \((x,y)\) and
target cell \((x',y')\), translation by \((x'-x,y'-y)\) maps the whole square
onto that target square; the track label is changed as recorded.  The finite
union of these maps is well-defined because source cells are disjoint, and its
images are disjoint because targets are distinct.  At least one target cell is
unused by strict inequality.

The paper supplies the non-finite bridge: for its Boolean polygon algebra,
sufficient refinement makes the count of source-intersecting squares smaller
than the count of target-contained squares, using its boundary estimates.  The
checker intentionally accepts only that already-refined finite datum.  It does
not verify those estimates, an atomless Boolean algebra, the allowed
translation ring, arbitrary polygon input, or equality-area cases.
