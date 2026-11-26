# Contract and proof for the purity local-factor check

## Certificate contract

The JSON checker accepts a finite exact witness, not a representation constructor.

- `residue_cardinality` is the integer \(Q\ge2\).
- `kernel_inertia_in_m0` is an external attestation that the displayed local-factor space \((\ker N)^{I_k}\) lies in \(M_0V\), for a valid Weil–Deligne representation with finite inertial image.  The checker rejects `false`; it cannot derive this inclusion from a matrix dump.
- Each `graded_spectrum` record has a unique `label`, an integer monodromy degree `degree`, and `modulus_squared`, a non-negative rational string.  It represents one Frobenius eigenvalue on \(\operatorname{Gr}^M_jV\).  The checker verifies \(|c|^2=Q^j\) exactly and verifies \(\dim\operatorname{Gr}^M_jV=\dim\operatorname{Gr}^M_{-j}V\) by counts.
- `local_factor_labels` is the multiset of Frobenius eigenvalues on the already-computed local-factor space.  Each label must occur no more often than in the graded spectrum and must have degree at most zero.  Repeated labels encode multiplicity.

Thus the input must come with exact algebraic-number norm/modulus proofs and an independently verified monodromy filtration.  Decimal approximations, an asserted eigenvalue list without an exact witness, or a non-semisimple numerical matrix are outside the interface.

## Reusable proof

Let \(M_\bullet V\) be the monodromy filtration centered at zero.  For a Jordan chain of length \(d+1\), its bottom vector has degree \(-d\), hence \(\ker N\subset M_0V\).  Taking inertia invariants preserves this containment.  Weight-zero purity says that a Frobenius eigenvalue on \(\operatorname{Gr}^M_jV\) has modulus \(Q^{j/2}\).  Every eigenvalue \(c\) on \((\ker N)^{I_k}\), being in the spectrum of \(M_0V\), therefore satisfies \(|c|\le1\).  If \(\operatorname{Re}s>0\), then \(|Q^{-s}c|<1\), so each factor \(1-Q^{-s}c\) is nonzero.  This proves holomorphy and nonvanishing of the displayed local factor.

The defining isomorphisms \(N^j:\operatorname{Gr}^M_jV\simeq\operatorname{Gr}^M_{-j}V\) give equal dimensions in degrees \(j\) and \(-j\).  Hence
\[
 |\det r(\operatorname{Fr})|
 =Q^{\frac12\sum_j j\dim\operatorname{Gr}^M_jV}=1.
\]
This is Lemma 3.2 of the source, with the local-factor convention made explicit.

## Source and boundary

K. S. Kedlaya, W. Sawin, A. S. S. Tamas-Gyöngyösi, *Temperedness at ramified places for globally generic exceptional groups*, pinned OpenAI/math commit `3344da59991ed94f9ba711217b29c1d760badfa6`, Lemma 3.2, local PDF p. 8 (PDF page 8), 5 October 2026.  The source is a preprint; no independent journal version was identified in the candidate record.

The result is conditional on valid Weil–Deligne and purity inputs.  It does not prove those hypotheses, does not infer them from approximate eigenvalues, and does not prove the paper's global all-ramified-place temperedness result.
