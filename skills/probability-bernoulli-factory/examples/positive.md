# Positive example: a one-step finite event

Given two iid tosses of a `p`-coin, output 1 exactly when the first toss is heads and the second is tails. The output probability is

`p(1-p)`.

This is a finite deterministic-depth event with unnormalized degree-2 Bernstein coefficients `(a_0,a_1,a_2)=(0,1,0)`. It uses exactly two input tosses, so its event degree is at most 2. The example illustrates Wästlund's finite-event coefficient criterion; it does not illustrate a random stopping-time factory or establish a general `N(d)` bound.
