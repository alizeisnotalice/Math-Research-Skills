---
name: math-free-group-presentation-traces
description: Verify a finite Andrews--Curtis trace on an ordered free-group presentation using exact free reduction and reversible move semantics; not a search engine or a decision procedure.
---

# Finite Andrews--Curtis presentation traces

Use this skill to replay a supplied finite trace on an ordered pair of relators in the free group on `x,y`.  The checker applies free reduction after every move, enforces the source move set, and replays the inverse trace from the final presentation.

```sh
python3 scripts/check_ac_trace.py examples/right-multiply-reduction.json
python3 scripts/check_ac_trace.py examples/conjugate-reduction.json
```

The output certifies only the supplied finite trace and ordered target.  It does not search for a reduction, prove that an arbitrary balanced presentation is trivial, validate any competition record, or turn a bounded exploration into a general non-existence result.

Read [the trace contract](references/thakur-ac-trace-contract.md) before interpreting a replay.
