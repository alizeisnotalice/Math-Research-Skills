# A25 bounded crossover-code replay

Source reviewed: local arXiv:2610.41622v1, *Lowered crossover points of
Anthropic's subexponential 3-SAT algorithm*; physical pp.1, 50, and 54--56
of the reviewed 56-page PDF. The paper links a public MIT-licensed repository
of scripts and recorded outputs.

This review made a shallow checkout of the repository at observed commit
`7b5611921a0467fd0a1662254174b5a275a558b2`. That is an observation of the
remote at review time, not a claim that this commit is the paper's source
revision. With Python 3.13, NumPy 2.5.4, SciPy 1.18.1, PyYAML 6.0.3, and
mpmath 1.3.0 already available, two bounded runs were made:

- `python -B calc/r122b_expansion.py 3 4` reproduced the first four recorded
  lines: two positive finite cases obeyed the displayed expansion identity,
  while both swapped-kernel negative controls failed it.
- `python -B calc/r123_chr_check.py` completed the script's exact finite range
  check through 24000 and its stated sampled analytic-range calculation.

These executions are evidence only for those source-code/model instances.
They do not prove the paper's crossover estimates, validate the imported
literature inequalities or schedules, establish the Anthropic recursion, or
imply an ETH conclusion. A paper-version replay needs an immutable matching
revision and an audit of every upstream premise.
