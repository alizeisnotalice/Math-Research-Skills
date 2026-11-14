#!/usr/bin/env python3
"""通用版面探测：对任意原文 PDF 输出复刻所需的全部几何/字体数据。

用法：
    python probe.py <原文.pdf> [首页...末页]

输出：
  1) 页面尺寸
  2) 每页的「栏」判定（行首 x 直方图 → 栏位/栏宽）
  3) 正文字号 / 行距 / 字体（按栏统计众数）
  4) 标题层级（按字号从大到小列出典型行）
  5) 图区域（描边矩形框 ∪ 位图 bbox），可直接作为「区域整体渲染」的 clip
  6) 首页文本块 bbox（用于复刻题名区）
"""
import sys
import collections
import fitz


def mode(seq, k=3):
    return collections.Counter(seq).most_common(k)


def probe(path, pages=None):
    doc = fitz.open(path)
    n = doc.page_count
    pages = pages or list(range(min(n, 12)))
    print(f"### {path}")
    print(f"总页数={n}")
    sizes = {(round(p.rect.width), round(p.rect.height)) for p in doc}
    print(f"页面尺寸集合={sorted(sizes)}")
    for pno in pages:
        pg = doc[pno]
        print(f"\n===== p{pno+1}  ({pg.rect.width:.0f}x{pg.rect.height:.0f}) =====")

        # --- 行级数据 ---
        lines = []
        for b in pg.get_text("dict")["blocks"]:
            if b["type"] != 0:
                continue
            for l in b["lines"]:
                if not l["spans"]:
                    continue
                txt = "".join(s["text"] for s in l["spans"]).strip()
                if not txt:
                    continue
                lines.append({
                    "x0": round(l["bbox"][0], 1), "y0": round(l["bbox"][1], 1),
                    "x1": round(l["bbox"][2], 1), "y1": round(l["bbox"][3], 1),
                    "sz": round(l["spans"][0]["size"], 1),
                    "font": l["spans"][0]["font"], "txt": txt,
                })

        # --- 栏判定：把 x0 按 6bp 归并，取计数 >= 5 的簇 ---
        buckets = collections.Counter(round(l["x0"] / 6) * 6 for l in lines)
        cand = sorted([x for x, c in buckets.items() if c >= 5])
        cols, used = [], set()
        for x in cand:
            if x in used:
                continue
            grp = [y for y in cand if abs(y - x) <= 12 and y not in used]
            for y in grp:
                used.add(y)
            cols.append(x)
        print(f"  栏位候选 x = {cols}")
        for cx in cols:
            sel = [l for l in lines if abs(l["x0"] - cx) <= 12]
            if len(sel) < 5:
                continue
            wid = max(l["x1"] for l in sel) - cx
            ys = sorted({l["y0"] for l in sel})
            dif = [round(ys[i + 1] - ys[i], 1) for i in range(len(ys) - 1)]
            dif = [d for d in dif if 5 < d < 20]
            print(f"    x={cx:4d} 行数={len(sel):3d} 右界≈{cx + wid:6.1f} 有效宽≈{wid:6.1f} "
                  f"主字号={mode([l['sz'] for l in sel], 2)} 主行距={mode(dif, 2)} "
                  f"主字体={mode([l['font'].split('+')[-1] for l in sel], 2)}")

        # --- 标题层级 ---
        big = sorted({l["sz"] for l in lines}, reverse=True)[:6]
        for s in big:
            ex = [l for l in lines if l["sz"] == s][:2]
            for e in ex:
                print(f"    字号{s:5.1f} x={e['x0']:6.1f} y={e['y0']:6.1f} "
                      f"{e['font'].split('+')[-1][:18]:18s}| {e['txt'][:56]}")

        # --- 图区域 ---
        rects = []
        for d in pg.get_drawings():
            r = d["rect"]
            if r.width > 40 and r.height > 40:
                rects.append((round(r.x0, 1), round(r.y0, 1), round(r.x1, 1), round(r.y1, 1), d["type"]))
        imgs = [(round(i["bbox"][0], 1), round(i["bbox"][1], 1),
                 round(i["bbox"][2], 1), round(i["bbox"][3], 1)) for i in pg.get_image_info(xrefs=True)]
        if rects:
            print(f"    描边框 {len(rects)} 个:")
            for r in rects:
                print(f"      ({r[0]:6.1f},{r[1]:6.1f})-({r[2]:6.1f},{r[3]:6.1f}) "
                      f"w={r[2]-r[0]:6.1f} h={r[3]-r[1]:6.1f} type={r[4]}")
        if imgs:
            print(f"    位图 {len(imgs)} 个:")
            for r in imgs:
                print(f"      ({r[0]:6.1f},{r[1]:6.1f})-({r[2]:6.1f},{r[3]:6.1f}) "
                      f"w={r[2]-r[0]:6.1f} h={r[3]-r[1]:6.1f}")
    doc.close()


if __name__ == "__main__":
    p = sys.argv[1]
    rng = [int(v) - 1 for v in sys.argv[2:]] if len(sys.argv) > 2 else None
    probe(p, rng)
