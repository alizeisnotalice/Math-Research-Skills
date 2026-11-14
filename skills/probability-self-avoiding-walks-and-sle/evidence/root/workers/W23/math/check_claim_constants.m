% Numerical consistency checks for honeycomb constants and polygon thresholds.
% No Lacoin/Z^2 numerical bound is evaluated here: the exact square-lattice
% connective constant mu_2 and a proof-admissible N0 are not supplied.
mu_honeycomb = sqrt(2 + sqrt(2));
xc_honeycomb = 1 / mu_honeycomb;
parafermion_mu = 2 * cos(pi / 8);
square_threshold = 1 / (2 * (1 + 8 * 29));
honeycomb_threshold = 1 / (2 * (1 + 2 * 10));
checks = struct();
checks.mu_honeycomb = mu_honeycomb;
checks.xc_honeycomb = xc_honeycomb;
checks.honeycomb_mu_times_xc = mu_honeycomb * xc_honeycomb;
checks.honeycomb_parafermion_identity_difference = parafermion_mu - mu_honeycomb;
checks.square_epsilon_threshold = square_threshold;
checks.honeycomb_epsilon_threshold = honeycomb_threshold;
checks.lacoin_numeric_instantiation = 'not computed: requires square-lattice mu_2 and theorem-admissible N0';
checks.interpretation = 'Floating-point consistency only for honeycomb identities and source-derived epsilon arithmetic. It is not a proof; no Z^2 quenched/annealed value was computed.';
out = fullfile(pwd, 'check_claim_constants_results.txt');
fid = fopen(out, 'w');
cleanup = onCleanup(@() fclose(fid));
fields = fieldnames(checks);
for k = 1:numel(fields)
    value = checks.(fields{k});
    if isnumeric(value)
        fprintf(fid, '%s=%.17g\n', fields{k}, value);
    else
        fprintf(fid, '%s=%s\n', fields{k}, value);
    end
end
fprintf('%s\n', out);
