# TIMAR2006FMSF — ends of free minimal spanning forests

**Source:** Ádám Timár, *Ends in Free Minimal Spanning Forests*, Ann. Probab. 34(3) (2006), 865–869, DOI 10.1214/009117906000000025. Full six-page paper read; local PDF `evidence/fulltexts/TIMAR2006FMSF.pdf`.

## Theorem 1.2 (PDF pp. 2–5)

If (G) is a transitive unimodular graph and FMSF\((G)\ne\)WMSF\((G)\), then every FMSF tree has infinitely many ends a.s. If the forests agree, the theorem makes no claim about the ends.

The paper uses iid continuous uniform edge labels. (p_c<p_u) is equivalent to FMSF\(≠\)WMSF in the stated transitive unimodular setting (Lemma 2.1, invoking LPS Proposition 3.6). WMSF trees have one end in that setting, by the cited LPS theorem.

## Proof chain

1. Suppose a “lonely” FMSF tree is also a WMSF tree with positive probability; choose (p\in(p_c,p_u)).
2. Choose a finite path joining two distinct infinite (p)-clusters so one endpoint lies in the lonely tree and no inner vertex is incident to its relevant (p)-cluster part.
3. Raise labels on edges incident to inner path vertices but outside the path above (p). The finite-label-change lemma changes the MSF only finitely; weak insertion tolerance plus the no-isolated-end lemma rules out the modified tree absorbing another (p)-cluster tree while retaining the lonely end.
4. Lower all labels on the chosen path below (p). Those edges now lie in FMSF; the path joins the two infinite (p)-cluster trees. The resulting FMSF tree either has finitely many ends, contradicting the invariant mass-transport argument, or infinitely many ends with the original lonely end isolated, contradicting Lemma 2.2.
5. The MTP lemma used here says an invariant random forest on a transitive unimodular graph cannot assign a finite nonempty vertex subset equivariantly to one of its disjoint infinite vertex sets. An infinite-ended invariant tree has no isolated end.

## Relevance and gap

This proves an end-number conclusion under unimodularity, not full component indistinguishability. It does not settle B068, which asks to remove unimodularity for quasi-transitive graphs. The book’s Theorem 11.15 gives a related but different proof in a broader quasi-transitive unimodular formulation; see the book card.
