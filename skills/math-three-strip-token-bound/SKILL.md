---
name: math-three-strip-token-bound
description: Certify the finite three-strip/token boundary bound for a sequence of equal-cardinality planar threshold cuts with matched exchanges; not a halving-line asymptotic solver.
---

# Three-strip token boundary certificate

Use this skill for a finite sequence \(M_0,\ldots,M_m\) of equal-size subsets
of a labelled planar point set, when every state is an exact strict linear cut
and every one-step loss is paired bijectively with a one-step gain.  It
certifies the local conclusion

\[
 \#\bigl((A\cap B)\setminus(S_{c_0}\cup S_{c_-}\cup S_{c_+})\bigr)\leq 2C_B,
\]

where \(A=\bigcup_i(M_{i-1}\triangle M_i)\), \(C_B\) is the number of
chosen transfers crossing the boundary of the supplied bounded region, and
the three strips have half-width \(3D\theta\).  It is a finite lemma for an
already supplied cut sequence, rather than an algorithm for finding the
sequence or bounding the number of its participants.

1. Encode every coordinate, normal, threshold, \(D\), and \(\theta\) as an
   exact rational string.  The checker requires each normal to have squared
   norm one, the cuts to reproduce every listed \(M_i\) with strict
   inequalities, and every matching to be precisely the loss--gain
   bijection.
2. State the bounded region by the IDs marked `inside`; it need not be
   represented geometrically, but every inside point must satisfy
   \(\lVert x\rVert\le D\).  This is the only property of \(B\) used by the
   finite lemma.
3. Run `scripts/check_three_strip.py certificate.json`.  A successful
   calculation is an exact certificate of the stated finite inequality.
   Read [the proof and interface](references/finite-three-strip.md) before
   using it in a limiting or packing argument.

Do not infer the planar halving-line power saving, a strip mass estimate, or
the compactness/three-foliation step from this finite check.  Those require
additional measure and geometric hypotheses outside this skill.
