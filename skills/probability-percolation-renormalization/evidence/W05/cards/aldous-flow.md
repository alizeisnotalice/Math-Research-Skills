# aldous-flow — Maximum disjoint oriented paths

**Reading status:** `partial_read`; the author-hosted problem webpage and its conjecture/heuristic were read. A separately downloaded Aldous–Diaconis journal scan has blank text pages and is not treated as read evidence.

**Reference:** David Aldous, “A Discrete Hammersley Process as an Extreme Case of Oriented Percolation Flows,” author-hosted research note, [webpage](https://www.stat.berkeley.edu/~aldous/Research/OP/hammersley_flow.html), date not stated; local HTML snapshot `papers/W05/hammersley-flow-note.html`.

## What the note says

It defines \(V(n,p)\), the maximum number of edge-disjoint oriented open paths in the square model, and states existence of a limiting flow value \(v(p)\) with \(V(n,p)/(2n)\to v(p)\) in \(L^1\). It asks whether

\[
1-v(p)\sim\sqrt{2(1-p)}\quad\text{as }p\uparrow1.
\]

The note explicitly flags interchanging the large-box and near-one limits as the obstacle. Its heuristic covers closed edges by oriented paths, replaces rare closed edges by a Poisson process of rate approximately \(2(1-p)\), and appeals to Hammersley longest-increasing-subsequence scaling. This is a heuristic only; it supplies no uniform error estimate or proof of the asymptotic.

## Research interface

For A030, the needed bridge is a bound uniform jointly in box scale and \(1-p\), strong enough to pass from finite-square flow to the \(p\uparrow1\) limit. Finite enumeration or numerical extrapolation can test constants at finite n but cannot justify that interchange.
