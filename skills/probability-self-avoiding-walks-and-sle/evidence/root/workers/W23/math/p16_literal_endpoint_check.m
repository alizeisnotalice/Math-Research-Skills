% Exact finite-step audit for the literal n=m=1 endpoint in SAW-P16 (d=2).
% Enumerate all one-step nearest-neighbour paths; retain those that are
% bridges with unique initial minimum and endpoint maximum in coordinate 2.
steps = [1 0; -1 0; 0 1; 0 -1];
bridgeCount = 0;
eventCount = 0;
bridgeSteps = zeros(0,2);
eventSteps = zeros(0,2);
for j = 1:size(steps,1)
    endpoint = steps(j,:);
    heights = [0; endpoint(2)];
    isBridge = (sum(heights == min(heights)) == 1) && (heights(end) == max(heights));
    inEvent = isBridge && heights(end) >= 1;
    if isBridge
        bridgeCount = bridgeCount + 1;
        bridgeSteps(end+1,:) = endpoint; %#ok<SAGROW>
    end
    if inEvent
        eventCount = eventCount + 1;
        eventSteps(end+1,:) = endpoint; %#ok<SAGROW>
    end
end
assert(bridgeCount == 1 && eventCount == 1);
result.dimension = 2;
result.length_n = 1;
result.height_m = 1;
result.candidate_nearest_neighbour_steps = steps;
result.bridge_steps = bridgeSteps;
result.event_steps = eventSteps;
result.b1 = bridgeCount;
result.event_count = eventCount;
result.event_fraction = eventCount / bridgeCount;
result.literal_source_bound_if_positive_phi1 = '1 <= exp(-phi(1))';
result.contradiction = 'For every phi(1)>0, exp(-phi(1))<1, while the exact left side is 1.';
result.scope = 'Finite literal-input counterexample only. It does not refute the separately stated asymptotic qualitative Theorem 1.2 and does not supply a repaired quantitative hypothesis.';
outPath = fullfile(fileparts(mfilename('fullpath')), 'p16_literal_endpoint_check.json');
fid = fopen(outPath,'w');
assert(fid >= 0, 'Could not open result JSON for writing');
fwrite(fid, jsonencode(result,'PrettyPrint',true), 'char');
fwrite(fid, newline, 'char');
fclose(fid);
disp(jsonencode(result,'PrettyPrint',true));
