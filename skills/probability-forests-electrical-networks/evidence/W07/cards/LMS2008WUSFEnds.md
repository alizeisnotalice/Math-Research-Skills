# LMS2008WUSFEnds — ends of wired uniform spanning forests

**Source:** Russell Lyons, Benjamin J. Morris, and Oded Schramm, *Ends in Uniform Spanning Forests*, Electronic Journal of Probability 13, Paper 58 (2008), 1702–1725, DOI 10.1214/EJP.v13-566. Full reading of the 23-page author manuscript (version 19 May 2008; arXiv:0706.0358v2 dated 23 May 2008), PDF pp. 1–23.

## Main theorem: conductance/isoperimetric criterion

- **Proposition 5.1 (PDF pp. 13–14).** If a transient network admits a finite connected exhaustion (V_n) with a uniform positive lower bound on (C(v\leftrightarrow\infty;G\setminus V_n)) for every (v\notin V_n), and if these residual networks have conductance to infinity tending uniformly to infinity for finite sets of large total conductance, then WSF-a.s. every tree is one-ended. The proof examines the WSF(_o) one edge at a time. The effective conductance (M_n) from the exposed root cluster to infinity is a nonnegative martingale (Lemma 3.3); its boundedness plus the two uniform conductance conditions gives positive conditional probability of eventually exposing no new root-cluster edge. Thus the WSF(_o) root component is finite, and the corrected Proposition 3.1 converts this to one-endedness.
- **Theorem 6.1 and Lemma 6.2 (PDF pp. 15–16).** For κ((t)) the minimum edge-boundary conductance of finite connected sets of volume at least (t), the resistance satisfies (R(A\leftrightarrow\infty)\le\sum_{k\ge0}2/\kappa(s_k)), where (s_0=|\partial_E^\infty A|_c) and (s_{k+1}=s_k+\kappa(s_k)/2). Lemma 6.2 proves the finite-network form by taking level sets of the voltage of the unit current and bounding the voltage increments by (2/\kappa(\pi(W_k))); exhaustion gives Theorem 6.1. Lemma 6.3 (PDF pp. 16–17) constructs an exhaustion whose complements retain at least half the original profile.
- **Theorem 7.1 (PDF pp. 17–18).** If (s_0:=\inf_{s>0}\kappa(s)>0) and (\sum_{k\ge0}1/\kappa(s_k)<\infty), with (s_{k+1}=s_k+\kappa(s_k)/2), then WSF-a.s. every tree has one end. Apply Theorem 6.1 to the good exhaustion from Lemma 6.3: summability makes resistance from large sets to infinity uniformly small, establishing both hypotheses of Proposition 5.1.
- **Corollary 7.3 and Theorem 7.4 (PDF pp. 20–21).** A quasi-transitive transient network has at least cubic volume growth; the unimodular transitive isoperimetric bound gives κ((t))\(\ge c t^{2/3}\). Substitution into the recursion makes the criterion summable, proving one-ended WSF trees for quasi-transitive transient networks. Theorem 7.5 (PDF pp. 20–21) also treats bounded-degree graphs roughly isometric to hyperbolic space, with a planar-dual conclusion for the free forest in dimension two.

## Erratum that changes the proposition statement

The authors’ erratum dated 14 Mar. 2020 says the WSF and WSF(_o) definitions should use exhaustions by induced subnetworks. It corrects Proposition 3.1: replace “there do not exist two edge-disjoint infinite paths in ℑ(o) starting at (o)” by “the tree ℑ(o) has only one end.” It also corrects two typos in Lemma 3.3, including the reference to Theorem 7 of Morris, which should be Theorem 6. The criterion above uses the corrected statement. See the author-hosted [erratum](https://rdlyons.pages.iu.edu/errata/ends.pdf).

## Scope

The result concerns WSF, not WMSF. Transience of each component is not enough by itself; the profile summability or one of the corollaries is needed for the one-end conclusion.
