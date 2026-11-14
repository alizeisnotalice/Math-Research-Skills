import fitz, re, os, json
import numpy as np

PDF = '2026PRA.pdf'
OUT = 'figs'
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
DPI = 300
ZOOM = DPI / 72.0

records = []
for pno in range(doc.page_count):
    page = doc[pno]
    blocks = page.get_text('blocks')
    caps = []
    for b in blocks:
        t = b[4].strip()
        m = re.match(r'^FIG\.\s*(\d+)\.', t)
        if m:
            caps.append((int(m.group(1)), fitz.Rect(b[:4])))
    if not caps:
        continue
    pix = page.get_pixmap(dpi=DPI, colorspace=fitz.csGRAY)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)

    for fnum, crect in caps:
        cx0, cx1 = int(crect.x0 * ZOOM), int(crect.x1 * ZOOM)
        cy0 = int(crect.y0 * ZOOM)
        cx0 = max(0, cx0); cx1 = min(pix.width, cx1)
        strip = img[:, cx0:cx1]
        ink = (strip < 200).sum(axis=1)   # ink per row

        # scan upward from caption top: first find ink, then keep going up
        y = cy0 - 1
        # skip blank gap between figure and caption
        while y > 0 and ink[y] == 0:
            y -= 1
        bottom = y
        # now walk up, tolerating internal gaps up to GAP_TOL rows
        GAP_TOL = int(0.055 * DPI)   # ~4 pt
        gap = 0
        top = y
        while y > 0:
            if ink[y] == 0:
                gap += 1
                if gap > GAP_TOL:
                    break
            else:
                gap = 0
                top = y
            y -= 1
        # trim margins
        top = max(0, top - int(0.02 * DPI))
        bottom = min(pix.height, bottom + int(0.02 * DPI))
        rect = fitz.Rect(cx0, top, cx1, bottom) / ZOOM
        records.append(dict(page=pno + 1, fig=fnum, rect=list(rect)))

json.dump(records, open('figs/fig_boxes.json', 'w'), indent=1)
for r in records:
    print(r['page'], r['fig'], [round(v, 1) for v in r['rect']])
