function result = lacoin_strict_gap_interface(mu2Z2Upper, p, C2, mu2Evidence, C2Evidence)
% Conditional numerical interface for Lacoin's planar bond-percolation bound.
% The caller must supply a certified upper bound on the Z^2 connective
% constant and a C2 certified large enough for the
% source proof. This helper cannot certify either mathematical input.
%
% The source states, for a sufficiently large absolute C2,
%   N0 = exp(C2/(1-p)^2),
%   mu_2(p) <= 4^(-1/N0^2) * p * mu_2.
% Do not pass an arbitrary illustrative block scale as a theorem-valid N0.

if nargin ~= 5
    error('Supply mu2Z2, p, C2, and provenance strings for both certified inputs.');
end
if ~isscalar(mu2Z2Upper) || ~isfinite(mu2Z2Upper) || mu2Z2Upper <= 0
    error('mu2Z2Upper must be a positive finite certified upper bound for the square-lattice connective constant.');
end
if ~isscalar(p) || ~isfinite(p) || p <= 1/2 || p >= 1
    error('The strict planar theorem requires p in (1/2,1).');
end
if ~isscalar(C2) || ~isfinite(C2) || C2 <= 0
    error('C2 must be a positive finite proof-admissible constant.');
end
if strlength(string(mu2Evidence)) == 0 || strlength(string(C2Evidence)) == 0
    error('Record the source/certificate for mu2Z2 and proof-admissibility of C2.');
end

N0 = exp(C2 / (1 - p)^2);
factor = 4^(-1 / N0^2);
result = struct();
result.model = 'nearest-neighbour strict SAW on the Z^2 iid Bernoulli bond-percolation infinite cluster';
result.p = p;
result.mu2Z2_certified_upper_bound = mu2Z2Upper;
result.C2_input = C2;
result.N0 = N0;
result.relative_quenched_rate_factor = factor;
result.quenched_limsup_upper_bound = factor * p * mu2Z2Upper;
result.relative_gap_lower_bound = 1 - factor;
result.mu2_evidence = string(mu2Evidence);
result.C2_admissibility_evidence = string(C2Evidence);
result.warning = 'Conditional calculation only; numerical inputs and the proof-admissibility of C2 must be independently certified.';
end
