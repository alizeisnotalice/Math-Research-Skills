% A040 finite-chain check; exploratory numeric evidence, not a proof.
% Random-scan heat-bath kernel P = (1/n) sum_v K_v, with each K_v
% resampling spin v from its conditional zero-field Ising law.

outdir = fileparts(mfilename('fullpath'));
if ~exist(outdir, 'dir'), mkdir(outdir); end
rng(375, 'twister');

% Reproduce the fixed-time single-spin monotonicity failure from Shirai
% (2010), using its path P_3 and x_e = 2 J_e parametrization.
syms z real
x1 = sym(28); x3 = sym(14);
q12 = sinh(x1) / (1 + cosh(x1));
q21 = sinh(x1) / (cosh(x1) + cosh(z));
q23 = sinh(z) / (cosh(x1) + cosh(z));
q32 = sinh(z) / (cosh(z) + cosh(x3));
q34 = sinh(x3) / (cosh(z) + cosh(x3));
q43 = sinh(x3) / (1 + cosh(x3));
Q = sym(zeros(4));
Q(1,2) = q12; Q(2,1) = q21; Q(2,3) = q23;
Q(3,2) = q32; Q(3,4) = q34; Q(4,3) = q43;
Qlazy = sym(3)/4 * eye(4) + sym(1)/4 * Q;
spinMean = (Qlazy^3 * ones(4,1));
shiraitMean = vpa(subs(spinMean(2), z, 14), 50);
shiraitDerivative = vpa(subs(diff(spinMean(2), z), z, 14), 50);

% Independently build all 16 configurations symbolically to check that the
% four-dimensional invariant linear-spin reduction matches the full kernel.
[fullMean, fullDerivative] = symbolicFullChainAtShiraiPoint();

% Exhaust every connected labelled simple graph up to four vertices.
% For each edge, hold other positive couplings fixed and scan that edge.
grid = [0 0.1 0.4 1 2 4];
gapChecks = 0; graphCount = 0; testedEdges = 0;
positiveIncrementCount = 0;
maxPositiveGapIncrement = -Inf;
worst = struct('n', [], 'edges', [], 'edge_index', [], 'J_at_record', [], ...
    'J_left', [], 'J_right', [], 'gap_left', [], 'gap_right', []);
for n = 2:4
    allEdges = nchoosek(1:n, 2);
    m = size(allEdges, 1);
    for mask = 1:(2^m - 1)
        keep = logical(bitget(mask, 1:m));
        edges = allEdges(keep, :);
        if ~isConnected(n, edges), continue; end
        graphCount = graphCount + 1;
        for e = 1:size(edges,1)
            J = 0.2 + 1.8*rand(size(edges,1),1);
            values = zeros(size(grid));
            for k = 1:numel(grid)
                J(e) = grid(k);
                values(k) = spectralGap(n, edges, J);
                gapChecks = gapChecks + 1;
            end
            testedEdges = testedEdges + 1;
            increments = diff(values);
            positiveIncrementCount = positiveIncrementCount + sum(increments > 1e-10);
            [inc, idx] = max(increments);
            if inc > maxPositiveGapIncrement
                maxPositiveGapIncrement = inc;
                worst = struct('n', n, 'edges', edges, 'edge_index', e, ...
                    'J_at_record', J(:).', 'J_left', grid(idx), ...
                    'J_right', grid(idx+1), 'gap_left', values(idx), ...
                    'gap_right', values(idx+1));
            end
        end
    end
end

% Seeded sample of connected five-vertex graphs, including trees and graphs
% with cycles. This is a search sample, not an exhaustive n=5 result.
n = 5; sampleCount = 12;
for sample = 1:sampleCount
    edges = randomConnectedGraph(n);
    for e = 1:size(edges,1)
        J = 0.2 + 1.8*rand(size(edges,1),1);
        values = zeros(size(grid));
        for k = 1:numel(grid)
            J(e) = grid(k);
            values(k) = spectralGap(n, edges, J);
            gapChecks = gapChecks + 1;
        end
        testedEdges = testedEdges + 1;
        increments = diff(values);
        positiveIncrementCount = positiveIncrementCount + sum(increments > 1e-10);
        [inc, idx] = max(increments);
        if inc > maxPositiveGapIncrement
            maxPositiveGapIncrement = inc;
            worst = struct('n', n, 'edges', edges, 'edge_index', e, ...
                'J_at_record', J(:).', 'J_left', grid(idx), ...
                'J_right', grid(idx+1), 'gap_left', values(idx), ...
                'gap_right', values(idx+1));
        end
    end
end

result = struct();
result.generated_utc = char(datetime('now', 'TimeZone', 'UTC', ...
    'Format', 'yyyy-MM-dd HH:mm:ss'' UTC'''));
result.engine = 'MATLAB R2026b Update 1; double precision eig for gaps; Symbolic Math Toolbox vpa(50) for Shirai derivative';
result.kernel = 'P=(1/n) sum_v K_v, random-site discrete-time heat-bath, zero field';
result.gap_clock = 'gap_P=1-lambda_2(P); per-site-rate-one CT gap=n*gap_P';
result.scan_scope = 'all connected labelled simple graphs n=2,3,4; 12 seeded connected n=5 samples; fixed other edge couplings, varied one edge over [0,0.1,0.4,1,2,4]';
result.connected_graphs_exhaustive_n2_to_n4 = graphCount;
result.sampled_n5_graphs = sampleCount;
result.varied_edges = testedEdges;
result.spectral_gap_evaluations = gapChecks;
result.maximum_adjacent_gap_increment = maxPositiveGapIncrement;
result.positive_increment_count_above_1e_10 = positiveIncrementCount;
result.worst_increment_record = worst;
result.shirai_path_P3 = struct('x_edges_2J', [28 14 14], ...
    'vertex', 2, 'time_steps', 3, 'mean_at_point_vpa50', char(shiraitMean), ...
    'derivative_d_mean_d_x2_vpa50', char(shiraitDerivative), ...
    'full_16_state_mean_at_point_vpa50', char(fullMean), ...
    'full_16_state_derivative_d_mean_d_x2_vpa50', char(fullDerivative), ...
    'reduction_derivative_difference_vpa50', char(vpa(fullDerivative-shiraitDerivative,50)));
result.interpretation = 'Numerical checks only. No finite scan proves the arbitrary-graph edgewise gap conjecture.';

% The main scan was used as a directional falsification search. Record the
% maximal numerical violation; spectral eigensolvers have finite precision.
jsonText = jsonencode(result, 'PrettyPrint', true);
fid = fopen(fullfile(outdir, 'a040_scan.json'), 'w');
assert(fid >= 0, 'Could not open result file for writing.');
fprintf(fid, '%s\n', jsonText);
fclose(fid);

fprintf('Shirai point t=3 mean (vpa50): %s\n', char(shiraitMean));
fprintf('Shirai point d/dx2 (vpa50): %s\n', char(shiraitDerivative));
fprintf('Full 16-state derivative (vpa50): %s\n', char(fullDerivative));
fprintf('Full minus reduced derivative (vpa50): %s\n', char(vpa(fullDerivative-shiraitDerivative,50)));
fprintf('Exhaustive n<=4 connected graphs: %d; n=5 sampled graphs: %d\n', graphCount, sampleCount);
fprintf('Varied edges: %d; spectral gap evaluations: %d\n', testedEdges, gapChecks);
fprintf('Maximum adjacent gap increment: %.16g\n', maxPositiveGapIncrement);
fprintf('Saved %s\n', fullfile(outdir, 'a040_scan.json'));

function connected = isConnected(n, edges)
    seen = false(1,n); seen(1) = true;
    changed = true;
    while changed
        changed = false;
        for e = 1:size(edges,1)
            u = edges(e,1); v = edges(e,2);
            if seen(u) && ~seen(v), seen(v) = true; changed = true; end
            if seen(v) && ~seen(u), seen(u) = true; changed = true; end
        end
    end
    connected = all(seen);
end

function edges = randomConnectedGraph(n)
    edges = zeros(n-1,2);
    for v = 2:n
        edges(v-1,:) = [randi(v-1), v];
    end
    allEdges = nchoosek(1:n,2);
    for k = 1:size(allEdges,1)
        edge = allEdges(k,:);
        if rand < 0.22 && ~ismember(sort(edge), sort(edges,2), 'rows')
            edges(end+1,:) = edge; %#ok<AGROW>
        end
    end
    edges = sortrows(sort(edges,2));
end

function gap = spectralGap(n, edges, J)
    P = heatbathKernel(n, edges, J);
    N = size(P,1);
    spins = spinTable(n);
    energy = zeros(N,1);
    for e = 1:size(edges,1)
        energy = energy + J(e) * spins(:,edges(e,1)) .* spins(:,edges(e,2));
    end
    pi = exp(energy - max(energy)); pi = pi / sum(pi);
    rootPi = sqrt(pi);
    S = (rootPi .* P) ./ rootPi';
    eigenvalues = sort(eig((S+S')/2), 'descend');
    gap = 1 - eigenvalues(2);
end

function P = heatbathKernel(n, edges, J)
    spins = spinTable(n);
    N = size(spins,1); P = zeros(N,N);
    for a = 0:N-1
        for v = 1:n
            localField = 0;
            for e = 1:size(edges,1)
                u = edges(e,1); w = edges(e,2);
                if u == v, localField = localField + J(e)*spins(a+1,w); end
                if w == v, localField = localField + J(e)*spins(a+1,u); end
            end
            probPlus = 1/(1 + exp(-2*localField));
            plusState = double(bitset(uint32(a), v, 1)) + 1;
            minusState = double(bitset(uint32(a), v, 0)) + 1;
            P(a+1,plusState) = P(a+1,plusState) + probPlus/n;
            P(a+1,minusState) = P(a+1,minusState) + (1-probPlus)/n;
        end
    end
end

function spins = spinTable(n)
    N = 2^n; spins = zeros(N,n);
    for a = 0:N-1
        spins(a+1,:) = 2*double(bitget(uint32(a),1:n))-1;
    end
end

function [meanValue, derivative] = symbolicFullChainAtShiraiPoint()
    syms x1 x2 x3 real
    xs = [x1 x2 x3]; edges = [1 2; 2 3; 3 4]; n = 4; N = 16;
    spins = sym(zeros(N,n));
    for a = 0:N-1
        spins(a+1,:) = 2*sym(bitget(uint32(a),1:n))-1;
    end
    P = sym(zeros(N));
    for a = 0:N-1
        for v = 1:n
            localXField = sym(0);
            for e = 1:3
                u = edges(e,1); w = edges(e,2);
                if u == v, localXField = localXField + xs(e)*spins(a+1,w); end
                if w == v, localXField = localXField + xs(e)*spins(a+1,u); end
            end
            probPlus = 1/(1 + exp(-localXField));
            plusState = double(bitset(uint32(a), v, 1)) + 1;
            minusState = double(bitset(uint32(a), v, 0)) + 1;
            P(a+1,plusState) = P(a+1,plusState) + probPlus/n;
            P(a+1,minusState) = P(a+1,minusState) + (1-probPlus)/n;
        end
    end
    f = P^3 * spins(:,2);
    meanValue = vpa(subs(f(N), [x1 x2 x3], [28 14 14]), 50);
    derivative = vpa(subs(diff(f(N),x2), [x1 x2 x3], [28 14 14]), 50);
end

