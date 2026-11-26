# Successor-colour reachability on an edge deletion

Use a finite simple graph \(G\), an edge \(xy\), a proper \(k\)-colouring \(\phi\)
of \(G-xy\) with \(\phi(x)=\phi(y)\), and a cyclic permutation \(\sigma\) of its
\(k\ge3\) colours. Orient the permitted arcs \(u\to v\) on \(G-xy\) by
\(\phi(v)=\sigma(\phi(u))\). The checker constructs paths \(x\leadsto y\) and
\(y\leadsto x\), or returns a proper colouring of \(G\).

For either source vertex let \(R\) be its reachable set. If the other
endpoint is outside \(R\), replace \(\phi\) by \(\sigma\circ\phi\) on \(R\).
Edges within \(R\) stay properly coloured since \(\sigma\) is injective.
An edge leaving \(R\) can become monochromatic only if it originally carried
a successor arc, contradicting closure of \(R\). The endpoints of \(xy\)
now differ. Thus an independently certified non-\(k\)-colourable \(G\) forces
mutual reachability for every such \(\sigma\). That reachability gives a
directed closed walk through each endpoint. A shortest returning walk
through that endpoint is a cycle, and its length is divisible by \(k\)
because its colours advance under \(\sigma\).

The interface uses the successor-digraph paragraph and the first part of
Lemma 4 in Horace Dong, *Critical graphs with the fewest cycles of length 0
modulo k*, local physical page 3, SHA-256
`6485685e4afb9b06f4688fa1dc11f34dedd9ab5f96ed41491995551a5407d53b`.
Kim and Picollelli use the same reachability operation in Definition 2.1 and
Theorem 2.2. [Fixed version of the cited Kim–Picollelli article](https://doi.org/10.37236/12623)

For the stronger source conclusion that the cycles found have length
exactly \(k\), supply the equality-saturation hypothesis and the separate
Lemma 2. The cited Choi–Sieniawski arXiv v1 Lemmas 5 and 6 give the two
sides of the saturation count. For the other global cases, the degree
\(k\) construction is Kim–Picollelli Theorem 2.4 and the rooted
admissible-path theorem is Gao–Huo–Liu–Ma Theorem 3.1. [Choi–Sieniawski
v1](https://arxiv.org/abs/2611.13580v1) · [Gao–Huo–Liu–Ma journal version](https://doi.org/10.1093/imrn/rnaa324)

Run the two bundled inputs from the skill directory.

~~~sh
python3 -B scripts/check_successor_colour_paths.py examples/successor-k5.json
python3 -B scripts/check_successor_colour_paths.py examples/successor-recolour.json
~~~

The first input uses \(K_5\) and reports the two directed paths from the
source colour cycle. The second uses a single edge and returns a proper
recolouring. Mutual reachability for one input does not establish a
chromatic lower bound or an equality classification.
