% Bounded numerical cross-check for BBDM equation (1), d=r=2.
% This checks the reported integral numerically; it does not prove the theorem.
format long g
beta1 = @(u) (u + sqrt(4.*u - 3.*u.^2))./2;
g1 = @(z) -log(beta1(-expm1(-z)));
% Avoid evaluating the integrable logarithmic singularity exactly at z=0.
cutoff = 1e-10;
lambda_numeric = integral(g1, cutoff, Inf, 'AbsTol', 1e-11, 'RelTol', 1e-11);
lambda_exact = pi^2/18;
% Check the positive-root identity beta_1(u)^2 = u beta_1(u)+u(1-u).
u_check = [1e-6, 0.01, 0.2, 0.75, 1.0];
b_check = beta1(u_check);
root_residual = max(abs(b_check.^2 - u_check.*b_check - u_check.*(1-u_check)));
fprintf('cutoff = %.12g\n', cutoff);
fprintf('lambda integral over [cutoff, Inf] = %.15g\n', lambda_numeric);
fprintf('pi^2/18 = %.15g\n', lambda_exact);
fprintf('absolute difference = %.6g\n', abs(lambda_numeric-lambda_exact));
fprintf('max beta_1 positive-root residual on finite sample = %.6g\n', root_residual);
