# Generalized ABC recurrence finite interface

Source: `EXT-0395`, arXiv:2606.27885v1, physical pp. 1--3 and 9--14 (15 pages total), SHA-256 `1e8245043fbc88458e615014b4968ec7d6076733611e18c8f5766165acbd7aa8`.

The source studies the two-sided recurrence associated with

\[
\pi_U(X)=X\prod_{j=1}^{q-1}(X-P_j(U))+1.
\]

The included interface accepts a fixed, caller-supplied monic specialization and its (q) initial values.  A unit constant coefficient permits exact backwards propagation; it reports all equal absolute values in the requested finite radius.  The example is merely a toy specialization, not a source instance selected to meet its theorem hypotheses.

The source's assertion of at most two sufficiently large common values remains unadopted: its constants are not explicit in the supplied version and the proof requires specialization/irreducibility, root-separation, Galois and nonzero logarithmic-form conditions before the Matveev step.
