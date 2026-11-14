# HUTCH2020TUP — indistinguishability of collections of USF trees

**Source:** Tom Hutchcroft, “Indistinguishability of Collections of Trees in the Uniform Spanning Forest,” *Annales de l’Institut Henri Poincaré, Probabilités et Statistiques* 56(2) (2020), 917–927, DOI 10.1214/19-AIHP988; arXiv:1810.06382v1. Complete 14-page PDF read (SHA-256 `6ae78fc7c44530c4ffb625114d4fa7011b4a0794216210be9674df4d776502b6`).

## Main theorems

Theorem 1.1 (PDF p. 3): for the USF on \mathbb{Z}^d, (d\ge5), and every (k\ge1), every tail (k)-component property is almost surely satisfied by either every ordered (k)-tuple of distinct USF components or by none. A (k)-component property is a measurable property of (k) distinct components; it is **tail** when it is unchanged by finite modifications to the forest relevant to those components and is invariant when the root chosen in any component is moved within that component.

Theorem 1.2 (PDF p. 3) gives the same all-or-none conclusion for an infinite, connected, locally finite Liouville graph whose USF components are almost surely one-ended. The theorem’s graph assumptions and the one-endedness premise matter: it is not a general conclusion for every unimodular or transitive graph. The paper notes that one-endedness of the graph follows from the other hypotheses in this setting.

## Proof chain

Section 2 (PDF pp. 4–12) proves the tuple statement. The main ingredients are WSF tail triviality (Theorem 2.1), a lazy-random-walk mixing/independence result for Liouville graphs (Theorem 2.2), and Proposition 2.3, which turns tail triviality into asymptotic independence for separated finite observations. Wilson’s algorithm supplies the coupling: move the starting locations of (k) walks far apart, expose finite initial path pieces, and use one-endedness plus finite-change stability of a tail property to identify the limiting conditional probability. Lemma 2.7 extends the resulting common probability from the chosen roots to arbitrary tuples, yielding the zero-or-one alternative in Theorem 1.1. The argument for Theorem 1.2 follows the same tail/mixing route under its Liouville and one-ended-component assumptions.

Section 3 (PDF pp. 12–13) explains why the Liouville condition is meaningful and supplies counterexample mechanisms when the hypotheses are weakened. Liouville is a property of the random walk on the graph; it is not synonymous with unimodularity.

## Reading coverage

Complete PDF read: introduction and theorems, §1 (PDF pp. 1–3); tail, mixing, and Wilson-coupling proof, §2 (pp. 4–12); limitations and examples, §3 (pp. 12–13); references (pp. 13–14). Physical PDF pages are used.

## Scope boundary

The theorem concerns tail properties of tuples of distinct USF components under its graph and end assumptions. It does not directly imply indistinguishability for minimal spanning forests, arbitrary component labels, or non-tail properties.
