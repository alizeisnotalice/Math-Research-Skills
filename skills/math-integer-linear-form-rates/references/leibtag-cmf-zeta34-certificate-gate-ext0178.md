# CMF zeta(3), zeta(4) certificate admission gate

Source: Elyasheev Leibtag, Hila Barkan, Rotem Kalisch, Shachar Weinbaum,
Michael Shalyt, and Ido Kaminer, *New Directions in Irrationality*,
arXiv:2610.27799v1 (20 October 2026), local source SHA-256
`29ae9b2fddf5a5cb5ff2180b8b45e1049206d0587062beb6ecb5c5c3dd2889c2`,
physical pp. 2--3, 22--29, 61--67.

The source reports a conservative-matrix-field route to the irrationality of
every nonzero rational combination of `zeta(3)` and `zeta(4)`, and to quoted
irrationality-measure bounds.  Its arithmetic-growth arguments use exact
supplementary certificates.  The paper points to the public companion release
`RamanujanMachine/new-directions-in-irrationality`; the release README identifies
the intended Lean projects and pinned revisions, including
`meijerg_zeta3_zeta4` at `639a790897ec`.

Admission rule: do not turn a Python-notebook execution into an irrationality or
linear-independence theorem.  The release itself says that its Python execution
checks documented computational ingredients, not the complete proof.  A caller
may use the source result only after supplying all of the following evidence:

1. a successful Lean kernel check at the exact upstream revision (with its
   dependency pins and no untracked source substitution);
2. a verified source-manifest/release hash matching the checked files; and
3. the analytic assumptions exposed by the Lean guide, including any
   prime-number-theorem input used by the formalized statement.

Keep the target rational pair explicit and apply only the checked theorem's
quantifiers.  In the absence of this evidence, retain the paper as a research
lead rather than a certified linear-form input.
