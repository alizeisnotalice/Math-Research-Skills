from collections import Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import json
import sympy as sp

OUT = Path(__file__).with_suffix('.json')

def is_tree_preorder(ds):
    pending = 1
    for j, d in enumerate(ds):
        pending += d - 1
        if pending == 0:
            return j == len(ds) - 1
        if pending < 0:
            return False
    return False

def fringe_degree_words(ds):
    out=[]
    n=len(ds)
    for start in range(n):
        pending=1
        word=[]
        for d in ds[start:]:
            word.append(d)
            pending += d-1
            if pending==0:
                out.append(tuple(word))
                break
            if pending<0:
                raise AssertionError('invalid preorder sequence')
    return out

def valid_preorders(multiset):
    # The small examples have repeated values; set(permutations) gives each
    # distinct degree sequence once, as required by uniformity over T_n.
    return [ds for ds in sorted(set(permutations(multiset))) if is_tree_preorder(ds)]

# RT029 exact formula (3.2) for a degree-profile tree and a fixed fringe type.
multiset=[0,0,1,1,2]
trees=valid_preorders(multiset)
target=(2,0,0)  # root with two leaf children
observed=Fraction(sum(fringe_degree_words(ds).count(target) for ds in trees), len(trees))
n=5
count_profile=Counter(multiset)
target_profile=Counter(target)
falling=lambda a,k: sp.factorial(a)//sp.factorial(a-k) if a>=k else 0
formula=Fraction(n * falling(count_profile[0], target_profile[0]) * falling(count_profile[2], target_profile[2]), falling(n, len(target)))

# RT030 exact size-count first and second factorial moment identities (5.3)-(5.4).
# Size 2 has only the ordered path with degree word (1,0).
m=2
path=(1,0)
obs_size_mean=Fraction(sum(sum(len(w)==m for w in fringe_degree_words(ds)) for ds in trees), len(trees))
# Eq. (5.3): n/m times the probability a without-replacement size-m sample
# has sum degrees m-1. Enumerate labelled permutations to preserve multiplicity.
labelled=list(range(n))
deg={0:0,1:0,2:0}
values=[0,0,1,1,2]
deg={i:values[i] for i in range(n)}
all_orderings=list(permutations(labelled, m))
prob_sum=Fraction(sum(sum(deg[i] for i in q)==m-1 for q in all_orderings), len(all_orderings))
formula_size_mean=Fraction(n,m)*prob_sum
# Eq. (5.4), r=2: probability of two consecutive disjoint blocks each
# satisfying sum(degree)=m-1, under ordered sampling without replacement.
r=2
all_orderings4=list(permutations(labelled, r*m))
prob_two_blocks=Fraction(sum(
    sum(deg[i] for i in q[:m])==m-1 and sum(deg[i] for i in q[m:])==m-1
    for q in all_orderings4), len(all_orderings4))
coef=Fraction(n * falling(n-r*m+m-1, r-1), m**r)
formula_size_fact2=coef*prob_two_blocks
obs_size_fact2=Fraction(sum(
    (lambda k: k*(k-1))(sum(len(w)==m for w in fringe_degree_words(ds)))
    for ds in trees), len(trees))

# RT038: verify the exact mean recurrence for uniform binary fragmentation.
x,y=sp.symbols('x y', positive=True, real=True)
mean_trial=2*x-1
rhs=sp.simplify(1 + 2/x*sp.integrate(2*y-1,(y,1,x)))
phi=sp.simplify(2/(1+sp.Symbol('z')))
z=sp.symbols('z')
root=sp.solve(sp.Eq(phi,1),z)
alpha=sp.simplify(-sp.diff(phi,z).subs(z,1))

result={
 'scope':'Exact finite enumerations and a symbolic recurrence check; diagnostics only, not asymptotic theorem proofs.',
 'RT029_lemma_3_1':{
   'degree_profile':dict(count_profile),'valid_preorder_trees':len(trees),'target_preorder_degrees':list(target),
   'mean_by_uniform_exact_enumeration':str(observed),'source_formula_exact':str(formula),'equal':observed==formula,
   'per_tree_counts':[fringe_degree_words(ds).count(target) for ds in trees]},
 'RT030_eq_5_3_and_5_4':{
   'degree_profile':dict(count_profile),'m':m,'uniform_tree_count':len(trees),
   'size_count_mean_by_tree_enumeration':str(obs_size_mean),'size_count_mean_eq_5_3':str(formula_size_mean),
   'mean_equal':obs_size_mean==formula_size_mean,
   'size_count_second_factorial_moment_by_tree_enumeration':str(obs_size_fact2),
   'eq_5_4_coefficient':str(coef),'two_block_sample_probability':str(prob_two_blocks),
   'eq_5_4_second_factorial_moment':str(formula_size_fact2),'second_factorial_moment_equal':obs_size_fact2==formula_size_fact2},
 'RT038_uniform_binary_fragmentation':{
   'candidate_mean_m(x)':str(mean_trial),'renewal_rhs':str(rhs),'identity_holds_for_x_ge_1':sp.simplify(rhs-mean_trial)==0,
   'phi(z)':str(phi),'characteristic_roots':[str(v) for v in root],'alpha':str(alpha),'recurrence_used':'m(x)=1+2∫_{1/x}^1 m(xu)du; m(y)=0 for y<1.'}
}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
