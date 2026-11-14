% Exact finite enumeration of the one-step SAWs in Z^2.
% This checks the finite-size boundary case cited in W23S007; it is not
% evidence for the asymptotic theorem or a substitute for its proof.
steps = [1 0; -1 0; 0 1; 0 -1];
n = 1;
v = 1/2;
epsilon = 0.1; % Any positive epsilon makes exp(-epsilon*n) strictly less than 1.
maxDisplacement = sqrt(sum(steps.^2, 2));
event = maxDisplacement >= v*n;
probability = sum(event) / numel(event);
bound = exp(-epsilon*n);
fprintf('d=2, n=%d, v=%g: exact one-step event probability = %.0f\n', n, v, probability);
fprintf('Illustrative epsilon=%g gives exp(-epsilon*n)=%.12f\n', epsilon, bound);
fprintf('Strict inequality fails: %d\n', probability > bound);
