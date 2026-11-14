% Exact Gaussian-moment diagnostic for the W12-027 Theorem 1.4 transcription.
% This tests scalar Brownian special cases only; it is not a proof of the theorem.
t = 2;
p = 2;

% With scalar integrand H=c, X_t=c B_t and E|B_t|^2=t, E|B_t|^4=3t^2.
c = 1;
lhs_original = c^2 * t;
rhs_original = (2*p - 1) * c^2 * t;
lhs_wrong_moment = 3 * c^4 * t^2;
rhs_card_at_c1 = (2*p - 1) * c^(2*p) * t;

% Keep the second moment on the left but incorrectly raise the integrand
% Schatten-p norm to p: choose c=1/2 so the scaling error is visible.
c = 1/2;
lhs_wrong_integrand = c^2 * t;
rhs_wrong_integrand = (2*p - 1) * c^(2*p) * t;

assert(lhs_original <= rhs_original);
assert(lhs_wrong_moment > rhs_card_at_c1);
assert(lhs_wrong_integrand > rhs_wrong_integrand);

out_path = fullfile(fileparts(mfilename('fullpath')), 'maitre_2025_thm14_scalar_diagnostic.out');
fid = fopen(out_path, 'w');
cleanup = onCleanup(@() fclose(fid));
fprintf(fid, 'Scalar Brownian exact-moment diagnostic (p=%d, t=%g)\n', p, t);
fprintf(fid, 'Original theorem: E|B_t|^2 = %.6g <= RHS %.6g: true\n', lhs_original, rhs_original);
fprintf(fid, 'Erroneous 2p-moment substitution at c=1: %.6g <= %.6g: false\n', lhs_wrong_moment, rhs_card_at_c1);
fprintf(fid, 'Erroneous p-th-power integrand at c=1/2: %.6g <= %.6g: false\n', lhs_wrong_integrand, rhs_wrong_integrand);
fprintf('Scalar Brownian exact-moment diagnostic (p=%d, t=%g)\n', p, t);
fprintf('Original theorem: E|B_t|^2 = %.6g <= RHS %.6g: true\n', lhs_original, rhs_original);
fprintf('Erroneous 2p-moment substitution at c=1: %.6g <= %.6g: false\n', lhs_wrong_moment, rhs_card_at_c1);
fprintf('Erroneous p-th-power integrand at c=1/2: %.6g <= %.6g: false\n', lhs_wrong_integrand, rhs_wrong_integrand);
