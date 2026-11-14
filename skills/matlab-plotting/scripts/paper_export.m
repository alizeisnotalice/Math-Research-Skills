function result = paper_export(fig, basePath, options)
%PAPER_EXPORT Save a Figure as PNG, PDF, FIG, and optionally SVG.
% Call with the entire figure, so legends and tiled layouts are included.
arguments
    fig (1,1) matlab.ui.Figure
    basePath (1,1) string
    options.Resolution (1,1) double {mustBePositive} = 300
    options.ContentType (1,1) string {mustBeMember(options.ContentType,["vector","image","auto"])} = "vector"
    options.SVG (1,1) logical = false
    options.Overwrite (1,1) logical = false
    options.Padding (1,1) double {mustBeNonnegative} = 6
end
extensions = [".png", ".pdf", ".fig"];
if options.SVG, extensions(end+1) = ".svg"; end
paths = basePath + extensions;
if ~options.Overwrite && any(isfile(paths))
    error('matlabPlotting:Exists', 'Output exists; choose another name or explicitly enable Overwrite.');
end
parent = fileparts(basePath);
if strlength(parent) > 0 && ~isfolder(parent), mkdir(parent); end
if options.SVG && verLessThan('matlab', '25.1')
    error('matlabPlotting:Version', 'SVG via exportgraphics requires R2025a or later.');
end
drawnow;
margin = {};
if ~verLessThan('matlab', '25.1')
    margin = {'Padding', options.Padding, 'Units', 'points'};
end
exportgraphics(fig, paths(1), 'Resolution', options.Resolution, 'BackgroundColor', 'white', margin{:});
exportgraphics(fig, paths(2), 'ContentType', options.ContentType, ...
    'Resolution', options.Resolution, 'BackgroundColor', 'white', margin{:});
savefig(fig, paths(3));
if options.SVG
    exportgraphics(fig, paths(4), 'BackgroundColor', 'white', margin{:});
end
for k = 1:numel(paths)
    entry = dir(paths(k));
    assert(~isempty(entry) && entry.bytes > 0, 'matlabPlotting:EmptyExport', 'Missing or empty export: %s', paths(k));
end
result = struct('files', paths, 'resolution', options.Resolution, 'pdf_content_type', options.ContentType);
end
