# Finite rationality test for a Mahler function

For a proved homogeneous Mahler equation

\[
 a_0(z)F(z)+a_1(z)F(z^k)+\cdots+a_d(z)F(z^{k^d})=0,
\]

Bell--Coons give a finite exact test for whether the *function* is rational.  By Bezivin's theorem this decides function transcendence in the source setting.  It does not prove transcendence or irrationality of an individual value \(F(\alpha)\).

Run `scripts/mahler_transcendence_test.py` with exact coefficient lists for the `a_i` (low-degree first) and exact Taylor coefficients of `F`.  The script computes the source bound `kappa`, constructs the prescribed finite Hankel matrix, and uses rational row reduction.  A full-rank output certifies that the given finite data pass the source's rationality obstruction.  An input shorter than the theorem's required prefix is rejected.

Before treating that output as a source-theorem application, independently establish all of these global facts.

1. The functional equation holds as a formal/analytic identity for the stated `F`.
2. The supplied Taylor coefficients really are those of that solution.
3. The source's hypotheses (in particular `k >= 2`, polynomial coefficients, and any needed convergence statement) hold.
4. If the intended claim concerns `F(alpha)`, separately prove the Mahler specialization hypotheses.  In the standard relation-lifting theorem, `alpha` must be algebraic with `0 < |alpha| < 1` and its full orbit must avoid singularities.

The program computes the finite matrix from the submitted prefix and checks those coefficient identities for which the prefix provides data. The corresponding formal identity and the identification of the prefix with the intended solution are additional mathematical inputs.

## Sources and scope

- Bell--Coons, *Transcendence tests for Mahler functions*, local [arXiv:1511.07530v1](https://arxiv.org/abs/1511.07530v1), pp. 1–6. The published edition is *Proc. Amer. Math. Soc.* **145** (2017), no. 3, 1061–1070, as listed in the [AMS volume contents](https://www.ams.org/journals/proc/2017-145-12/proc-145-12-print-matter.pdf).  The universal test combines their rational degree bound with a finite Hankel rank computation.  The test data and the bound used by the script are transcribed from Figure 2 and the proof on pp. 4--6.
- Adamczewski--Faverjon, *A new proof of Nishioka's theorem in Mahler's method*, C. R. Math. 361 (2023), 1011--1028, DOI 10.5802/crmath.458, pp. 1--4.  This supplies relation lifting at regular algebraic orbit points.  It is a global theorem, not something the finite rank calculation verifies.

The paper on relation lifting is formally published.  Its publisher record and local HAL text agree on title, authors, volume, year, and pages.  The local test never claims value transcendence.
