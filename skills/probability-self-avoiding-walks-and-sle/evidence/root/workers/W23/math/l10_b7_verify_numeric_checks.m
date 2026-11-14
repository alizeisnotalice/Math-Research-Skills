% Numerical cross-checks for fully read sources SAW-P46 and SAW-P49.
% These computations check quoted finite-dimensional formulas only; they
% are not proofs of the papers' asymptotic or graph-theoretic theorems.

format long g;

% SAW-P49, p. 22: H(7,3) recurrence matrix from the proof of Theorem 1.
A73 = [2 1 0 2; 2 2 2 0; 2 1 0 1; 2 2 1 0];
ev73 = eig(A73);
lambda73 = max(real(ev73(abs(imag(ev73)) < 1e-10)));
residual73 = norm(A73 * ones(4,1) - lambda73 * ones(4,1)); %#ok<NASGU>
% Use a corresponding eigenvector residual, since the all-ones vector is not
% asserted to be an eigenvector.
[V73,D73] = eig(A73);
[~,i73] = max(real(diag(D73)));
vec73 = V73(:,i73);
residual73 = norm(A73*vec73 - lambda73*vec73, 2);

% SAW-P49, p. 23: H(4,5) recurrence matrix in the proof of Theorem 1.
A45 = [1 0 2; 1 0 1; 2 1 0];
ev45 = eig(A45);
lambda45 = max(real(ev45(abs(imag(ev45)) < 1e-10)));
[V45,D45] = eig(A45);
[~,i45] = max(real(diag(D45)));
vec45 = V45(:,i45);
residual45 = norm(A45*vec45 - lambda45*vec45, 2);

% SAW-P46, p. 2: exact Fisher-lattice relation
% x^(-3)+x^(-4) = 1/(2+sqrt(2)), with x>1.
muHex = sqrt(2 + sqrt(2));
f = @(x) x.^(-3) + x.^(-4) - muHex.^(-2);
muFisher = fzero(f, [1 3]);
residualFisher = abs(f(muFisher));

% SAW-P46, p. 10: inverse-recurrence derivative at the fixed point.
alpha = (sqrt(5) - 1) / 2;
inverseDerivative = 1 / (2*alpha + 3*alpha^2);

fprintf('P49 H(7,3) largest eigenvalue: %.12f\n', lambda73);
fprintf('P49 H(7,3) eigenpair residual: %.3e\n', residual73);
fprintf('P49 H(4,5) largest eigenvalue: %.12f\n', lambda45);
fprintf('P49 H(4,5) eigenpair residual: %.3e\n', residual45);
fprintf('P46 hex Fisher connective constant root: %.12f\n', muFisher);
fprintf('P46 defining-equation residual: %.3e\n', residualFisher);
fprintf('P46 inverse-recurrence derivative at fixed point: %.12f\n', inverseDerivative);
fprintf('Evidence type: numerical checks of transcribed finite formulas, not proofs.\n');
