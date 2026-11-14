function info = paper_style(fig, options)
%PAPER_STYLE Apply local publication defaults; call before and after plotting.
% Existing data colors and line styles are preserved. No global defaults change.
arguments
    fig (1,1) matlab.ui.Figure
    options.Width (1,1) double {mustBePositive} = 16
    options.Height (1,1) double {mustBePositive} = 10
    options.FontSize (1,1) double {mustBePositive} = 10
    options.FontName (1,1) string = ""
end
palette = [0 114 178; 213 94 0; 0 158 115; 204 121 167; 230 159 0; 86 180 233; 0 0 0]/255;
fonts = string(listfonts);
font = options.FontName;
if font == ""
    preferred = ["PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", "Arial Unicode MS", "Heiti SC"];
    available = preferred(ismember(lower(preferred), lower(fonts)));
    if isempty(available)
        font = "Helvetica";
        warning('matlabPlotting:Font', 'No preferred CJK font found; verify Chinese glyphs visually.');
    else
        font = available(1);
    end
elseif ~any(strcmpi(font, fonts))
    error('matlabPlotting:Font', 'Requested font is not installed: %s', font);
end
if exist('theme', 'file') == 2
    theme(fig, 'light');
end
set(fig, 'Color', 'w', 'InvertHardcopy', 'off', 'Units', 'centimeters');
pos = fig.Position;
pos(3:4) = [options.Width options.Height];
fig.Position = pos;
set(fig, 'DefaultAxesColorOrder', palette, 'DefaultAxesFontName', char(font), ...
    'DefaultAxesFontSize', options.FontSize, 'DefaultAxesLineWidth', 0.8, ...
    'DefaultLineLineWidth', 1.5, 'DefaultTextFontName', char(font));
axesList = findall(fig, 'Type', 'axes');
for k = 1:numel(axesList)
    ax = axesList(k);
    set(ax, 'FontName', char(font), 'FontSize', options.FontSize, ...
        'LineWidth', 0.8, 'Color', 'w', 'XColor', 'k', 'YColor', 'k', 'ZColor', 'k', ...
        'TickDir', 'out', 'Box', 'off', 'GridAlpha', 0.15);
end
objects = findall(fig);
for k = 1:numel(objects)
    obj = objects(k);
    if isprop(obj, 'FontName'), obj.FontName = char(font); end
    if isprop(obj, 'FontColor'), obj.FontColor = [0 0 0]; end
    if isa(obj, 'matlab.graphics.primitive.Text'), obj.Color = [0 0 0]; end
    if isa(obj, 'matlab.graphics.illustration.Legend')
        set(obj, 'TextColor', 'k', 'Color', 'w', 'Box', 'off');
    end
    if isa(obj, 'matlab.graphics.illustration.ColorBar'), obj.Color = [0 0 0]; end
end
info = struct('font', font, 'width_cm', options.Width, ...
    'height_cm', options.Height, 'font_size', options.FontSize, 'palette', palette);
end
