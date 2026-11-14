% Exact symbolic coefficient checks for L06_B6.
% This checks algebra only; it is not a proof of either paper's theorem.
outDir = fileparts(mfilename('fullpath'));

% Lacoin, Theorem 1.3 against the cited p_c expansion. With epsilon=1/2,
% the order-(2d)^(-3) coefficient gap is 3 log(2)-2 > 0.
epsilonChoice = sym(1)/2;
thresholdCoefficient = 2 + 3*log(sym(2)) - epsilonChoice;
pcCoefficient = sym(7)/2;
lacoinGap = simplify(thresholdCoefficient - pcCoefficient);
lacoinGapDecimal = double(vpa(lacoinGap, 16));
assert(isAlways(lacoinGap > 0));
assert(abs(lacoinGapDecimal - (3*log(2)-2)) < 1e-14);

% Hara-Slade-Sokal, Eqs. (2.31), (2.34): compare the tau=2, k=0
% prefactor with the tau=0, k=0 lower bound.
syms d positive
factorTau2ToTau0 = simplify((2*d - 1)^2/(2*d*(2*d - 2)));
factorMinusOne = simplify(factorTau2ToTau0 - 1);
assert(isAlways(factorMinusOne == 1/(2*d*(2*d - 2))));

gapText = char(lacoinGap);
factorText = char(factorTau2ToTau0);
factorDiffText = char(factorMinusOne);
summary = sprintf(['Local symbolic checks (MATLAB Symbolic Math Toolbox)\n' ...
    'P31: epsilon=1/2; threshold-minus-pc coefficient = %s = %.15g\n' ...
    'P41: tau2/tau0 algebraic factor = %s = 1 + %s\n' ...
    'These checks corroborate coefficient algebra only; they are not theorem proofs.\n'], ...
    gapText, lacoinGapDecimal, factorText, factorDiffText);

fid = fopen(fullfile(outDir, 'coefficient_checks.txt'), 'w');
assert(fid >= 0);
fprintf(fid, '%s', summary);
fclose(fid);

result = struct();
result.tool = 'local MATLAB Symbolic Math Toolbox';
result.script = 'verify_asymptotic_coefficients.m';
result.check_p31 = struct('source', 'SAW-P31, Theorem 1.3; p_c expansion on physical p.3', ...
        'epsilon', '1/2', ...
        'theorem_threshold_order_2d_minus3_coefficient', char(thresholdCoefficient), ...
        'pc_order_2d_minus3_coefficient', char(pcCoefficient), ...
        'difference', gapText, ...
        'difference_decimal', lacoinGapDecimal, ...
        'verified', true, ...
        'limit', 'Coefficient comparison plus the cited O(d^-4) expansion gives a nonempty interval for sufficiently large d; it does not compute an explicit dimension threshold.');
result.check_p41 = struct('source', 'SAW-P41, Eqs. (2.31) and (2.34)', ...
        'tau2_to_tau0_bound_factor', factorText, ...
        'factor_minus_one', factorDiffText, ...
        'verified', true, ...
        'limit', 'Exact algebraic consistency check only; it is not a proof of either Green-function inequality.');
jsonText = jsonencode(result, 'PrettyPrint', true);
fid = fopen(fullfile(outDir, 'coefficient_checks.json'), 'w');
assert(fid >= 0);
fprintf(fid, '%s\n', jsonText);
fclose(fid);

fprintf('%s', summary);
