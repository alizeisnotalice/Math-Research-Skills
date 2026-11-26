# Certificate contract and source boundary

The source is OpenAI, *A Torsion-Free Group Algebra with Zero Divisors* (23 September 2026), pinned at `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`, [PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026/paper.pdf), SHA-256 `b9788d4579b317fa2487796338fe3413322e105950880ec5a42bc85188a36bc6`. Physical pp. 2 and 24 give the finite simultaneous-step argument.

## Input

`A` and `B` each contain nonempty `vertices` and directed `edges` of the form `[source, label, target]`. `label_inverse` must be a fixed-point-free involution. An edge with label `t` must have its reverse edge with label `label_inverse[t]`; at most one edge of a given label may leave a vertex. The script requires each underlying component to be connected, so the supplied vertices are the full rooted components relevant to the cancellation argument.

`left_labels[x]` denotes `g_x`. `right_inverse_labels[y]` denotes `h_y^{-1}` directly. `products` is a list of `[left_label, right_inverse_label, value]` rows, with exactly one value for every queried pair. It is an oracle contract, not a presentation of a group.

For every `(x,y)`, the checker forms one simultaneous edge for each common outgoing signed label. It validates that the endpoint product is the same as the initial product. It then checks that every simultaneous multigraph component has odd degree at every vertex, even cardinality, and one product value. Therefore the coefficient contribution of each component to

`(sum_x g_x)(sum_y h_y^{-1})`

is its even cardinality modulo two and is zero in F2.

## Boundary

This is only the cancellation part of the source’s construction. The source proves path-label well-definedness by coning graph components, nonzeroness through separate root separation, and torsion-freeness through asphericity (physical pp. 2–3, 21–24). None follows from this finite certificate. In particular, a successful certificate does not prove that its supplied factors are nonzero or that its multiplication oracle is a torsion-free group.
