function [result, report] = local_gpu(operation, inputs, options)
%LOCAL_GPU Explicit float32 Apple Metal jobs through a checked Python bridge.
% [C,R] = local_gpu("matmul", struct('a',single(A),'b',single(B)))
% [Y,R] = local_gpu("sin_exp", struct('x',single(X)))
% [S,R] = local_gpu("sum", struct('x',single(X)))
arguments
    operation (1,1) string {mustBeMember(operation,["matmul","sin_exp","sum"])}
    inputs (1,1) struct
    options.Python (1,1) string = ""
    options.AllowPrecisionLoss (1,1) logical = false
    options.ScratchDir (1,1) string = "/Volumes/data/CodexTemp/local-gpu-math"
end
assert(isunix, 'local_gpu:Platform', 'This shell wrapper supports macOS/Linux.');
assert(isfolder('/Volumes/data'), 'local_gpu:Storage', 'The data volume is not mounted.');
python = options.Python;
if strlength(python) == 0
    python = string(getenv('LOCAL_GPU_PYTHON'));
end
if strlength(python) == 0
    python = fullfile(string(getenv('HOME')), '.venvs', 'main', 'bin', 'python');
end
assert(isfile(python), 'local_gpu:Python', 'Specify an existing MPS Python with Python=path.');
if operation == "matmul"
    expected = {'a';'b'};
else
    expected = {'x'};
end
assert(isequal(sort(fieldnames(inputs)),sort(expected)), 'local_gpu:Inputs', 'Incorrect input keys.');
specs = struct;
for k = 1:numel(expected)
    name = expected{k}; a = inputs.(name);
    assert(isnumeric(a) && isreal(a) && ismatrix(a) && ~issparse(a) && ...
        ~isempty(a) && all(isfinite(a),'all'), 'local_gpu:InputType', ...
        'Inputs must be nonempty, finite, dense real numeric matrices.');
    assert(isa(a,'single') || options.AllowPrecisionLoss, 'local_gpu:Precision', ...
        'Metal bridge uses float32. Pass single inputs, or AllowPrecisionLoss=true explicitly.');
end
if ~isfolder(options.ScratchDir), mkdir(options.ScratchDir); end
jobDir = string(tempname(options.ScratchDir)); mkdir(jobDir);
cleanup = onCleanup(@() rmdir(jobDir,'s'));
requestPath = fullfile(jobDir,'request.json');
reportPath = fullfile(jobDir,'report.json');
inputPath = fullfile(jobDir,'inputs.mat');
outputPath = fullfile(jobDir,'result.mat');
save(inputPath, '-struct', 'inputs', '-v7');
for k = 1:numel(expected)
    name = expected{k};
    specs.(name) = struct('mat', char(inputPath), 'variable', name);
end
req = struct('operation',char(operation),'dtype','float32', ...
    'allow_precision_loss',true,'inputs',specs,'output_mat',char(outputPath));
fid = fopen(requestPath,'w'); assert(fid>=0);
fileCleanup = onCleanup(@() fclose(fid));
fprintf(fid,'%s',jsonencode(req)); clear fileCleanup;
bridge = fullfile(fileparts(mfilename('fullpath')),'gpu_math.py');
command = [shellQuote(python) ' ' shellQuote(bridge) ' run --request ' ...
    shellQuote(requestPath) ' --report ' shellQuote(reportPath)];
t = tic; [status, stdout] = system(command); elapsed = toc(t);
assert(isfile(reportPath), 'local_gpu:Bridge', 'Bridge produced no report: %s',stdout);
report = jsondecode(fileread(reportPath));
report.caller = 'MATLAB'; report.bridge_wall_seconds = elapsed;
if status ~= 0 || ~isfield(report,'ok') || ~report.ok
    if isfield(report,'error'), detail = report.error; else, detail = stdout; end
    error('local_gpu:Bridge', 'GPU job failed: %s',detail);
end
assert(startsWith(string(report.device),'mps'), 'local_gpu:Device','Expected MPS output.');
assert(isfield(report.result,'mat') && string(report.result.mat)==outputPath && isfile(outputPath), ...
    'local_gpu:Result','Expected the local MAT result file.');
loaded = load(outputPath,'result'); result = loaded.result;
assert(isa(result,'single'), 'local_gpu:Dtype','Expected a single precision result.');
% Result bytes have been loaded; temporary files are removed on function return.
report.result = rmfield(report.result, {'mat','variable'});
report.result.transport = 'temporary MAT-v5, loaded and removed';
end

function q = shellQuote(value)
s = char(value);
assert(~any(s==char(0)), 'local_gpu:Path','NUL is not valid in paths.');
q = [char(39), strrep(s,char(39),[char(39),char(34),char(39),char(34),char(39)]), char(39)];
end
