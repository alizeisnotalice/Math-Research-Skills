% Finite evidence only for the L06_B4 full-text cards.
% 1) Recompute the two smallest positive real roots in Lindorfer's
%    Grandparent-graph bridge generating-function calculation.
% 2) Enumerate rooted SAWs up to length 10 in a finite radius-10 3-regular
%    tree ball. Because every rooted SAW in a tree is non-backtracking and
%    cannot turn into an unused branch without revisiting an ancestor, these
%    counts agree with the infinite-tree rooted counts for n <= 10.
% These computations do not prove the cited infinite-graph theorems.

outDir = fileparts(mfilename('fullpath'));

polyInc = [8 -8 10 -8 1];        % 1 - 8x + 10x^2 - 8x^3 + 8x^4
polyDec = [1 -1 3 -4 1];         % 1 - 4x + 3x^2 - x^3 + x^4
rInc = roots(polyInc);
rDec = roots(polyDec);
rInc = sort(real(rInc(abs(imag(rInc)) < 1e-10 & real(rInc) > 0)));
rDec = sort(real(rDec(abs(imag(rDec)) < 1e-10 & real(rDec) > 0)));
betaInc = 1 / rInc(1);
betaDec = 1 / rDec(1);


R = 10;
N = 1 + 3 * (2^R - 1);
parent = zeros(N,1);
depth = zeros(N,1);
next = 2;
frontier = 1;
for d = 0:R-1
    newFrontier = [];
    for v = frontier
        if d == 0
            nChildren = 3;
        else
            nChildren = 2;
        end
        for k = 1:nChildren
            w = next;
            next = next + 1;
            parent(w) = v;
            depth(w) = d + 1;
            newFrontier(end+1) = w; %#ok<AGROW>
        end
    end
    frontier = newFrontier;
end
assert(next == N+1);
adj = cell(N,1);
for v = 2:N
    p = parent(v);
    adj{v}(end+1) = p;
    adj{p}(end+1) = v;
end
counts = walkCount(1, 0, 1, adj, R);
expected = [1; (3 * 2.^(0:R-1))'];
assert(isequal(counts, expected));
% Capture the actually computed values explicitly; MATLAB diary is not used.
resInc = polyval(polyInc,rInc(1));
resDec = polyval(polyDec,rDec(1));
diffInc = abs(betaInc - 6.64993);
diffDec = abs(betaDec - 3.10380);
lines = { ...
    sprintf('Increasing-bridge smallest positive root: %.14f; reciprocal: %.12f; residual: %.3g', rInc(1), betaInc, resInc), ...
    sprintf('Decreasing-bridge smallest positive root: %.14f; reciprocal: %.12f; residual: %.3g', rDec(1), betaDec, resDec), ...
    sprintf('Absolute differences from article rounded values 6.64993, 3.10380: %.3g, %.3g', diffInc, diffDec), ...
    sprintf('3-regular tree rooted SAW counts n=0..10: %s', mat2str(counts')), ...
    'Checked exact finite counts against c_0=1 and c_n=3*2^(n-1), 1<=n<=10.', ...
    'Scope: finite computation only; the asymptotic tree value 2 follows from the displayed closed form, not from finite samples alone.'};
textPath = fullfile(outDir, 'finite_math_check.txt');
fid = fopen(textPath, 'w');
assert(fid >= 0, 'Could not open explicit MATLAB text-result artifact.');
for j = 1:numel(lines)
    fprintf(fid, '%s\n', lines{j});
    fprintf(1, '%s\n', lines{j});
end
assert(fclose(fid) == 0, 'Could not close MATLAB text-result artifact.');

result = struct();
result.execution = 'Actually evaluated by local MATLAB MCP run_matlab_file';
result.scope = 'Finite numerical/combinatorial consistency only; not proof of any asymptotic theorem.';
result.increasing_bridge = struct('polynomial_coefficients_descending', polyInc, 'smallest_positive_real_root', rInc(1), 'reciprocal', betaInc, 'residual', resInc, 'paper_rounded_value', 6.64993, 'absolute_difference_from_rounded_value', diffInc);
result.decreasing_bridge = struct('polynomial_coefficients_descending', polyDec, 'smallest_positive_real_root', rDec(1), 'reciprocal', betaDec, 'residual', resDec, 'paper_rounded_value', 3.10380, 'absolute_difference_from_rounded_value', diffDec);
result.tree_enumeration = struct('graph', 'radius-10 ball of the 3-regular tree', 'radius', R, 'counts_n0_to_n10', counts', 'closed_form_checked', 'c_0=1; c_n=3*2^(n-1) for 1<=n<=10', 'exact_for_these_lengths', true);
jsonPath = fullfile(outDir, 'finite_math_check.json');
fid = fopen(jsonPath, 'w');
assert(fid >= 0, 'Could not open explicit MATLAB JSON-result artifact.');
jsonText = jsonencode(result);
fprintf(fid, '%s\n', jsonText);
assert(fclose(fid) == 0, 'Could not close MATLAB JSON-result artifact.');

function counts = walkCount(v, depth, visited, adj, R)
    counts = zeros(R+1,1);
    counts(depth+1) = 1;
    if depth == R
        return
    end
    for w = adj{v}
        if ~ismember(w, visited)
            counts = counts + walkCount(w, depth+1, [visited w], adj, R);
        end
    end
end
