---
name: math-free-group-presentation-traces
description: 核验有限 Andrews–Curtis 自由群表示轨迹，以及已给成员关系时的带并自由积正规形见证。
---

# Free-group transformations and group word certificates

Use this skill to replay a supplied finite trace on an ordered pair of relators in the free group on `x,y`.  The checker applies free reduction after every move, enforces the source move set, and replays the inverse trace from the final presentation.

```sh
python3 scripts/check_ac_trace.py examples/right-multiply-reduction.json
python3 scripts/check_ac_trace.py examples/conjugate-reduction.json
```

The output certifies only the supplied finite trace and ordered target.  It does not search for a reduction, prove that an arbitrary balanced presentation is trivial, validate any competition record, or turn a bounded exploration into a general non-existence result.

Read [the trace contract](references/thakur-ac-trace-contract.md) before interpreting a replay.

## 文献复核采用的构件

- [Amalgamated-word witness: verified scope](references/amalgam-word-source.md)
