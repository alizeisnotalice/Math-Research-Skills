# Smooth bilinear strips: finite-model scope gate

Source: F. Bernicot, *On the boundedness for the bilinear quadratic functional
given by arbitrary strips*, arXiv:2606.22134v1, Theorem 1.1, Proposition 2.1,
Theorems 2.5--2.6, and Theorem 6.2 (physical pp. 3--7 and 14--17).

The source concerns a **bilinear** square function with smooth cutoffs adapted
to pairwise-disjoint strip intervals.  Whitney decomposition reduces the
smooth problem to well-distributed strips; wave-packet expansion then reduces
it to a finite tri-tile trilinear form.  For a well-distributed strip family,
each tri-tile frequency square meets at most one strip, which is the required
bookkeeping invariant.

The source theorem is conditional on its localization construction: for
`alpha=1/2-1/r>0`, the local size/energy estimates and the cited localization
yield a restricted weak-type bound with factor `|S|^(3 alpha/2)` in the stated
strict local-L2 neighborhood.  The decisive localization is explicitly
delegated to Benea--Bernicot (2016), and has not been independently recovered
in this package.

Therefore this is a scope gate only.  Do not use it as a scalar Rubio de
Francia theorem, a nonsmooth-cutoff theorem, a cardinality-uniform estimate,
or a substitute for proving the row/column localization premise.
