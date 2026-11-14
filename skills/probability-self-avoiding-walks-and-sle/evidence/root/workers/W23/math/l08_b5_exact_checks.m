% Exact/algebraic checks for L08_B5 reading cards.
% These checks verify transcribed constants and parameter algebra only;
% they do not prove the paper's probabilistic/combinatorial theorems.
nu = sym(3)/2;
alpha = simplify(nu/(2*nu-1));
claimedPower = simplify((nu-1)/(2*nu-1));
leftPower = simplify(alpha*(nu-1)/nu);
rightPower = simplify(1-alpha);
p16ok = isAlways(leftPower == rightPower);
margin = vpa(sym(5)/3-log(sym(4)),30);
p18positive = isAlways(margin > 0);
rootTwo = sqrt(sym(2));
xcSquared = simplify(1/(2+rootTwo));
p24bulk = isAlways(simplify((2*cos(sym(pi)/8))^2-(2+rootTwo)) == 0);
yc = simplify(1/(1-2*xcSquared));
p24surface = isAlways(simplify(yc-(1+rootTwo)) == 0);

result.P16_corollary_parameter_check.input_nu = char(nu);
result.P16_corollary_parameter_check.optimized_alpha_nu_over_2nu_minus_1 = char(alpha);
result.P16_corollary_parameter_check.claimed_n_power = char(claimedPower);
result.P16_corollary_parameter_check.alpha_times_nu_minus_1_over_nu = char(leftPower);
result.P16_corollary_parameter_check.one_minus_alpha = char(rightPower);
result.P16_corollary_parameter_check.identity_verified = p16ok;
result.P18_proof_exponential_margin.five_over_three_minus_log_four_decimal = char(margin);
result.P18_proof_exponential_margin.positive_at_30_digit_precision = p18positive;
result.P18_proof_exponential_margin.meaning = 'Numerical check of the strict margin used after the exact proof compares log(4) with 5/3.';
result.P24_honeycomb_constants.twice_cos_pi_over_eight_squared_equals_2_plus_sqrt2 = p24bulk;
result.P24_honeycomb_constants.xc_squared = char(xcSquared);
result.P24_honeycomb_constants.one_over_1_minus_2xc_squared = char(yc);
result.P24_honeycomb_constants.critical_y_equals_1_plus_sqrt2 = p24surface;
result.scope_note = 'Finite exact symbolic/algebra and numerical arithmetic checks only; none establishes a probabilistic or combinatorial theorem.';
assert(p16ok && p18positive && p24bulk && p24surface);
outPath = fullfile(fileparts(mfilename('fullpath')), 'l08_b5_exact_checks.json');
fid = fopen(outPath,'w');
assert(fid >= 0, 'Could not open result JSON for writing');
fwrite(fid, jsonencode(result,'PrettyPrint',true), 'char');
fwrite(fid, newline, 'char');
fclose(fid);
disp(jsonencode(result,'PrettyPrint',true));
