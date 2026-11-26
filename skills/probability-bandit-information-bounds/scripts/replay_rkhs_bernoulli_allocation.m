% Replay the three-arm direct Bernoulli example with base MATLAB.
q = linspace(0.7, 1, 3001);
bernoulliKL = @(p, x) p .* log(p ./ x) + (1 - p) .* (log1p(-p) - log1p(-x));
arm2 = bernoulliKL(0.3, q);
arm3 = bernoulliKL(0.5, (0.7 + q) / 2);

% Equality at the left endpoint is the limit of admissible strict alternatives.
d2 = arm2(1);
d3 = arm3(1);
left = 49 * 21^5;
right = 9 * 25^5;
assert(left < flintmax && right < flintmax && left > right);
assert(all(diff(arm2) >= 0) && all(diff(arm3) >= 0));
assert(abs(d2 - (2 / 5) * log(7 / 3)) < 1e-14);
assert(abs(d3 - log(25 / 21) / 2) < 1e-14);
eta2 = 1 / d2;
cost = (2 / 5) * eta2;
assert(abs(cost - 1 / log(7 / 3)) < 1e-14);

result = struct('matlab', version, 'grid_points', length(q), ...
    'd2_at_tie', d2, 'd3_at_tie', d3, 'eta2', eta2, 'eta3', 0, ...
    'cost', cost, 'integer_inequality', [left, right]);
disp(jsonencode(result));
