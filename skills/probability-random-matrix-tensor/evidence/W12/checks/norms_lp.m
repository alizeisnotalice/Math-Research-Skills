% Finite numerical checks for distinct matrix norms at p=4.
% Numerical corroboration only; exact arguments are in norms_lp-proof.md.
N = 2000001;
theta = linspace(0, 2*pi, N+1);
theta(end) = [];
raw = [cos(theta(:)), sin(theta(:))];
x = raw ./ sum(abs(raw).^4, 2).^(1/4);
A = diag([1,-1]);
I = eye(2);
symA = max(abs(sum((x*A).*x, 2)));
fullA = max(sum(abs(x*A).^(4/3), 2).^(3/4));
symI = max(sum((x*I).*x, 2));
fprintf('grid points: %d\n', N);
fprintf('diag(1,-1), symmetric diagonal l4 norm: %.12f (exact 1)\n', symA);
fprintf('diag(1,-1), full bilinear l4 injective norm: %.12f (exact sqrt(2)=%.12f)\n', fullA, sqrt(2));
fprintf('I_2, symmetric diagonal l4 norm: %.12f (exact sqrt(2)=%.12f)\n', symI, sqrt(2));
fprintf('I_2, Euclidean spectral norm: %.12f (exact 1)\n', norm(I,2));
