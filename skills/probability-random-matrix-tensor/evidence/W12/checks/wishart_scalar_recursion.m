% Scalar p=1 check of the Wishart Stein moment recursion, Theorem 3.1.
alphaW = 2.5;
sigma2W = 1.7;
nW = 4;
recursionW = 1;
degreeW = nW;
while degreeW > 0
    recursionW = recursionW * sigma2W * (alphaW + 2*(degreeW-1));
    degreeW = degreeW - 1;
end
closedFormW = sigma2W^nW * prod(alphaW + 2*(0:nW-1));
relativeErrorW = abs(recursionW-closedFormW)/closedFormW;
resultFileW = fopen('wishart_scalar_recursion.out', 'w');
assert(resultFileW >= 0, 'Unable to open result file.');
fprintf(resultFileW, 'recursion = %.15g\nclosed form = %.15g\nrelative error = %.3g\n', ...
    recursionW, closedFormW, relativeErrorW);
fclose(resultFileW);
fprintf('recursion = %.15g\nclosed form = %.15g\nrelative error = %.3g\n', ...
    recursionW, closedFormW, relativeErrorW);
