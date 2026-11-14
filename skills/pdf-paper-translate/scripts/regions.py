#!/usr/bin/env python3
"""通用「图区域」识别 + 区域整体渲染。

单栏论文的插图常由大量小矢量路径组成（没有外框），用 get_image_info 抓不到。
本工具把「所有绘图路径 ∪ 位图 bbox」按邻近间隙做连通聚类，得到图区域，
再整块渲染成 PNG —— 这样坐标轴、刻度、标注、线稿全部保真。

用法：
    python regions.py <原文.pdf> <页码1based> [gap]     # 只列出聚类
    python regions.py <原文.pdf> <页码1based> --render <输出目录> <前缀> [gap]
"""
import os
import sys
import json
import fitz


def clusters(pg, gap=8.0, min_area=400.0):
    items = []
    for d in pg.get_drawings():
        r = d["rect"]
        if r.width <= 0.3 and r.height <= 0.3:
            continue
        items.append(fitz.Rect(r))
    for i in pg.get_image_info(xrefs=True):
        items.append(fitz.Rect(i["bbox"]))
    # 迭代合并
    boxes = [fitz.Rect(b) for b in items]
    changed = True
    while changed:
        changed = False
        out = []
        for b in boxes:
            for k, o in enumerate(out):
                if b.intersects(o + (-gap, -gap, gap, gap)):
                    out[k] = o | b
                    changed = True
                    break
            else:
                out.append(b)
        boxes = out
    boxes = [b for b in boxes if b.width * b.height >= min_area]
    boxes.sort(key=lambda b: (round(b.y0 / 10), b.x0))
    return boxes


def main():
    pdf = sys.argv[1]
    page = int(sys.argv[2]) - 1
    render = "--render" in sys.argv
    if render:
        k = sys.argv.index("--render")
        outdir, prefix = sys.argv[k + 1], sys.argv[k + 2]
        rest = [a for a in sys.argv[k + 3:] if a.replace(".", "").isdigit()]
        gap = float(rest[0]) if rest else 8.0
    else:
        gap = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
        outdir = prefix = None

    doc = fitz.open(pdf)
    pg = doc[page]
    bs = clusters(pg, gap)
    print(f"页 {page+1}  共 {len(bs)} 个图区域（gap={gap}）")
    table = []
    if render:
        os.makedirs(outdir, exist_ok=True)
    for i, b in enumerate(bs):
        name = f"{prefix}{i+1}"
        y_ff = pg.rect.height - b.y0 - b.height
        print(f"  {name:6s} ({b.x0:6.1f},{b.y0:6.1f})-({b.x1:6.1f},{b.y1:6.1f}) "
              f"w={b.width:6.1f} h={b.height:6.1f}  y_ff={y_ff:6.1f}")
        table.append({"name": name, "x": round(b.x0, 1), "y_top": round(b.y0, 1),
                      "w": round(b.width, 1), "h": round(b.height, 1),
                      "y_ff": round(y_ff, 1)})
        if render:
            pix = pg.get_pixmap(clip=b, dpi=600)
            pix.save(os.path.join(outdir, name + ".png"))
    if render and table:
        with open(os.path.join(outdir, f"{prefix}_regions.json"), "w") as f:
            json.dump(table, f, ensure_ascii=False, indent=1)
    doc.close()


if __name__ == "__main__":
    main()
