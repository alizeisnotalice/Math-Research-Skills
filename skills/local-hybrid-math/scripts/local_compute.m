function [result, report] = local_compute(operation, inputs, options)
%LOCAL_COMPUTE Native MATLAB CPU or an explicitly measured local Metal bridge.
% MATLAB's own CPU is included; an external Python launch is not free.
arguments
    operation (1,1) string {mustBeMember(operation,["matmul","sin_exp","sum"])}
    inputs (1,1) struct
    options.Backend (1,1) string {mustBeMember(options.Backend,["auto","cpu","mps"])} = "auto"
    options.BenchmarkGPU (1,1) logical = false
    options.AllowPrecisionLoss (1,1) logical = false
    options.Python (1,1) string = ""
end
persistent profiles;
if isempty(profiles), profiles = containers.Map('KeyType','char','ValueType','any'); end
if operation == "matmul", names={'a';'b'}; else, names={'x'}; end
assert(isequal(sort(fieldnames(inputs)),sort(names)), 'local_compute:Inputs','Incorrect input keys.');
singleInputs = true; signature = char(operation);
for k=1:numel(names)
    a=inputs.(names{k});
    assert((isa(a,'single') || isa(a,'double')) && isreal(a) && ismatrix(a) && ...
        ~issparse(a) && ~isempty(a) && all(isfinite(a),'all'), ...
        'local_compute:Type','Use finite dense real single/double arrays.');
    singleInputs = singleInputs && isa(a,'single');
    signature=[signature ':' class(a) ':' mat2str(size(a))]; %#ok<AGROW>
end
if options.Backend == "mps"
    [result,report]=local_gpu(operation,inputs,Python=options.Python,AllowPrecisionLoss=options.AllowPrecisionLoss);
    report.selection_reason='explicit Metal bridge'; return;
end
% A native CPU candidate is actual useful work, retained if the bridge loses.
computeInputs=inputs;
if ~singleInputs
    for k=1:numel(names), computeInputs.(names{k})=double(inputs.(names{k})); end
end
t=tic;
if operation=="matmul", native=computeInputs.a*computeInputs.b;
elseif operation=="sin_exp", native=sin(computeInputs.x).*exp(-computeInputs.x.^2);
else, native=sum(computeInputs.x,'all'); end
nativeSeconds=toc(t);
assert(all(isfinite(native),'all'), 'local_compute:Nonfinite', ...
    'Native CPU result overflowed or became nonfinite; revise scaling/precision.');
result=native;
report=struct('ok',true,'device','cpu','engine','MATLAB-native', ...
    'dtype',class(native),'native_cpu_seconds',nativeSeconds,'cpu_result_computed',true, ...
    'selection_reason','native CPU avoids external startup and transfer');
if options.Backend=="cpu" || (~singleInputs && ~options.AllowPrecisionLoss)
    if ~singleInputs, report.selection_reason='preserve double precision on native CPU'; end
    return;
end
runBridge=options.BenchmarkGPU;
if isKey(profiles,signature)
    prior=profiles(signature);
    runBridge=runBridge || prior.bridge_wall_seconds < 0.9*nativeSeconds;
    report.prior_bridge_wall_seconds=prior.bridge_wall_seconds;
end
if runBridge
    try
        [metal, gpuReport]=local_gpu(operation,inputs,Python=options.Python,AllowPrecisionLoss=options.AllowPrecisionLoss);
        profiles(signature)=struct('bridge_wall_seconds',gpuReport.bridge_wall_seconds);
        report.gpu_candidate=gpuReport;
        report.calibration_overhead_seconds=gpuReport.bridge_wall_seconds;
        if gpuReport.bridge_wall_seconds < 0.9*nativeSeconds
            result=metal; report.device=gpuReport.device; report.engine='Python-Metal-bridge';
            report.dtype=class(metal); report.selection_reason='measured bridge wall time wins by at least 10 percent';
        else
            report.selection_reason='native CPU wins including Python launch, MAT transfer and verification';
        end
    catch ME
        report.gpu_candidate_error=ME.message;
        report.selection_reason='auto kept native CPU; GPU candidate failed explicitly';
    end
end
end
