# Certified stochastic box-mass enclosure

For a fixed parameter, use a caller-certified disjoint family of inner boxes,
boundary boxes and a directed mass enclosure. Sum their exact rational masses.
The inner total is a lower bound for the satisfaction probability. If the
boundary boxes cover the unresolved part inside the truncation region and the
specified `outside_mass` bounds the satisfaction mass beyond it, their total
added to the inner mass is a local upper bound.

The checker only verifies nonnegative rational mass bookkeeping. It cannot
establish interval containment, disjointness, the box-mass oracle, or a global
optimization guarantee. Its lower bound is also a lower bound for a maximum
over a domain only after the supplied parameter is feasible.

Physical pp. 5--7 of Li--Wu--Xia--Yang--Zhan, *Solving Stochastic
Constraints by Oracle-based Gradient Descent and Interval Arithmetic*,
arXiv:2604.17275v1, give the inner/boundary construction. Their displayed
upper enclosure omits a tail term while the preceding construction truncates
the random domain. This interface therefore requires `outside_mass`, with zero
permitted only when the caller certifies that no satisfaction mass lies outside
the covered region.

Run `python3 scripts/check_stochastic_box_mass_enclosure.py
examples/stochastic-box-mass-positive.json`. A mass overflow exits with status 2.
