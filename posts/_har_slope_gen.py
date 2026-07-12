#!/usr/bin/env python3
"""Generate the rank-flip slopegraph (posts/_har_slope.html) — inline theme-aware SVG.

Left column: the ten families ranked by spend (proxy: HAR_savings magnitude).
Right column: the same families ranked by total HAR. Lines connect each family's
two positions; colour = posture. Risk-dominated (green) families rise, savings-
dominated (blue) fall — the metric's contribution made visible in one glance.

Regenerate:  python3 posts/_har_slope_gen.py
"""

# (name, log10 savings h/yr, log10 risk h/yr, posture)  — same anchors as _har_map_gen.py
DATA = [
    ("Hip & knee implants",            8.0, 4.5, "leverage"),
    ("Stents & cardiac rhythm devices", 7.5, 5.5, "leverage"),
    ("Exam & surgical gloves",         6.8, 5.2, "leverage"),
    ("Infusion pumps & sets",          6.5, 6.2, "strategic"),
    ("Dialysis consumables",           6.3, 6.5, "strategic"),
    ("Iodinated contrast media",       6.1, 7.1, "secure"),
    ("IV saline & solutions",          5.9, 7.3, "secure"),
    ("Heparin",                        5.5, 6.5, "secure"),
    ("Blood culture bottles",          5.0, 6.8, "secure"),
    ("Platinum chemotherapies",        4.5, 7.0, "secure"),
]

POSTURE = {"leverage": "c1", "strategic": "c3", "secure": "c2"}

# spend rank = descending HAR_savings; HAR rank = descending total HAR (10^s + 10^r)
spend_rank = {d[0]: i + 1 for i, d in
              enumerate(sorted(DATA, key=lambda d: -d[1]))}
har_rank = {d[0]: i + 1 for i, d in
            enumerate(sorted(DATA, key=lambda d: -(10 ** d[1] + 10 ** d[2])))}

W, H = 820, 560
MT, MB = 74, 26
XL, XR = 262, 558              # left / right column x
PH = H - MT - MB
STEP = PH / 9                  # 10 ranks, rank 1 at top


def Y(rank):
    return MT + (rank - 1) * STEP


parts = []
parts.append("""<style>
.har-slope { --hs-ink:#073642; --hs-muted:#657b83; --hs-grid:#e4dcc3; --hs-ring:#fdf6e3;
             --hs-c1:#2a78d6; --hs-c2:#1baf7a; --hs-c3:#c98500; }
.quarto-dark .har-slope, [data-bs-theme="dark"] .har-slope {
  --hs-ink:#eee8d5; --hs-muted:#93a1a1; --hs-grid:#0f4a5a; --hs-ring:#073642;
  --hs-c1:#3987e5; --hs-c2:#199e70; --hs-c3:#c98500; }
.har-slope text { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }
.har-slope .row { opacity: 0.9; }
.har-slope .row:hover { opacity: 1; }
.har-slope .row:hover line { stroke-width: 3.5; }
</style>
""")
parts.append(f'<svg class="har-slope" viewBox="0 0 {W} {H}" role="img" '
             f'aria-label="Slopegraph: product families re-ranked from spend order to HAR order" '
             f'style="max-width:100%;height:auto;">')

# column headers
parts.append(f'<text x="{XL}" y="{MT-34}" text-anchor="end" font-size="13" '
             f'font-weight="700" fill="var(--hs-ink)">RANKED BY SPEND</text>')
parts.append(f'<text x="{XL}" y="{MT-18}" text-anchor="end" font-size="11" '
             f'fill="var(--hs-muted)">what procurement sees</text>')
parts.append(f'<text x="{XR}" y="{MT-34}" text-anchor="start" font-size="13" '
             f'font-weight="700" fill="var(--hs-ink)">RANKED BY HAR</text>')
parts.append(f'<text x="{XR}" y="{MT-18}" text-anchor="start" font-size="11" '
             f'fill="var(--hs-muted)">what HAR surfaces</text>')

# column guide lines
parts.append(f'<line x1="{XL}" y1="{MT-6}" x2="{XL}" y2="{MT+PH+6}" '
             f'stroke="var(--hs-grid)" stroke-width="1"/>')
parts.append(f'<line x1="{XR}" y1="{MT-6}" x2="{XR}" y2="{MT+PH+6}" '
             f'stroke="var(--hs-grid)" stroke-width="1"/>')

for name, s, r, posture in DATA:
    sr, hr = spend_rank[name], har_rank[name]
    col = f"var(--hs-{POSTURE[posture]})"
    yl, yr = Y(sr), Y(hr)
    parts.append(f'<g class="row"><title>{name}: spend #{sr} → HAR #{hr}</title>')
    parts.append(f'<line x1="{XL}" y1="{yl:.1f}" x2="{XR}" y2="{yr:.1f}" '
                 f'stroke="{col}" stroke-width="2"/>')
    parts.append(f'<circle cx="{XL}" cy="{yl:.1f}" r="5" fill="{col}" '
                 f'stroke="var(--hs-ring)" stroke-width="1.5"/>')
    parts.append(f'<circle cx="{XR}" cy="{yr:.1f}" r="5" fill="{col}" '
                 f'stroke="var(--hs-ring)" stroke-width="1.5"/>')
    parts.append(f'<text x="{XL-14}" y="{yl+4:.1f}" text-anchor="end" font-size="12.5" '
                 f'fill="var(--hs-ink)">{sr}. {name}</text>')
    parts.append(f'<text x="{XR+14}" y="{yr+4:.1f}" text-anchor="start" font-size="12.5" '
                 f'fill="var(--hs-ink)">{hr}. {name}</text>')
    parts.append('</g>')

# legend — colour encodes posture, not direction (see caption for the movement)
lg = [("c2", "risk-dominated"), ("c1", "savings-dominated"),
      ("c3", "strategic")]
lx = XL - 6
ly = MT + PH + 22
xo = 0
for var, lab in lg:
    parts.append(f'<circle cx="{lx+xo}" cy="{ly-4}" r="5" fill="var(--hs-{var})"/>')
    parts.append(f'<text x="{lx+xo+9}" y="{ly}" font-size="11.5" '
                 f'fill="var(--hs-muted)">{lab}</text>')
    xo += 20 + len(lab) * 6.6 + 14

parts.append("</svg>")

out = "/Users/jdonaldson/Projects/jjd.io/posts/_har_slope.html"
with open(out, "w") as f:
    f.write("\n".join(parts) + "\n")
print(f"wrote {out}")
