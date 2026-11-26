---
name: math-cycle-type-likelihood-bounds
description: Compare two supplied finite cycle-type laws under an explicit iid observation model, with Hellinger affinity and Bayes-error bounds.
---

# Cycle-type likelihood bounds

Use this skill when a finite alphabet of cycle types and two fully specified probability laws are already available. It computes the Hellinger affinity and the two-sided Bayes-error bounds for a stated number of iid observations.

The result is conditional on the supplied laws and iid model. In particular, it does not certify that factorization patterns at selected finite primes are independent Chebotarev samples, identify a Galois group, validate sampled group profiles, or give a finite-prime error guarantee.

Run `scripts/compare_cycle_type_profiles.py` on the two exact probability profiles and a list of observation labels. Only its length enters the equal-prior risk bound. The script preserves radical expressions and prints decimal approximations only for inspection. Read [the source scope](references/chebotarev-cycle-likelihood-scope.md) when using it with factorization data.
