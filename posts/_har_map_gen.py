#!/usr/bin/env python3
"""Generate the HAR map (posts/_har_map.html) — an inline, theme-aware SVG.

Log-log scatter: x = HAR_savings, y = HAR_risk (log10 hours/year, US national
scale, illustrative log bins from public anchors). Diagonal risk_share bands
carry the action posture (negotiate / strategic / secure supply).

Regenerate:  python3 posts/_har_map_gen.py
"""
import math

# (name, log10 savings h/yr, log10 risk h/yr, posture, public anchor for tooltip)
DATA = [
    ("Hip & knee implants",       8.0, 4.5, "leverage",  "huge spend, notorious price dispersion; deep multi-vendor pool"),
    ("Stents & cardiac rhythm",   7.5, 5.5, "leverage",  "high-dollar devices, contract-tier dispersion; several vendors"),
    ("Exam & surgical gloves",    6.8, 5.2, "leverage",  "commodity volume; deep pool outside pandemic conditions"),
    ("IV saline & solutions",     5.9, 7.3, "secure",    "2017 Baxter/Hurricane Maria shortage; gates most inpatient care"),
    ("Iodinated contrast media",  6.1, 7.1, "secure",    "2022 Shanghai lockdown shortage; gates CT-guided diagnosis"),
    ("Blood culture bottles",     5.0, 6.8, "secure",    "2024 supplier disruption; gates sepsis diagnosis"),
    ("Platinum chemotherapies",   4.5, 7.0, "secure",    "2023 cisplatin/carboplatin shortage; curative-intent, few substitutes"),
    ("Heparin",                   5.5, 6.5, "secure",    "single raw-material origin; 2008 contamination crisis"),
    ("Dialysis consumables",      6.3, 6.5, "strategic", "life-sustaining recurring therapy; concentrated supply"),
    ("Infusion pumps & sets",     6.5, 6.2, "strategic", "2022 pump/set shortages; moderate dispersion, moderate fragility"),
]

# Per-point label placement: (anchor, dx, dy)
LABEL = {
    "Hip & knee implants":      ("end", -11, 4),
    "Stents & cardiac rhythm":  ("end", -11, 4),
    "Exam & surgical gloves":   ("start", 11, 4),
    "IV saline & solutions":    ("end", -11, 1),
    "Iodinated contrast media": ("start", 11, 10),
    "Blood culture bottles":    ("start", 11, -6),
    "Platinum chemotherapies":  ("start", 11, 4),
    "Heparin":                  ("end", -11, 4),
    "Dialysis consumables":     ("end", -11, -4),
    "Infusion pumps & sets":    ("start", 11, 8),
}

POSTURE = {
    "leverage":  dict(var="c1", label="NEGOTIATE — savings-dominated"),
    "strategic": dict(var="c3", label="STRATEGIC — judgment call"),
    "secure":    dict(var="c2", label="SECURE SUPPLY — risk-dominated"),
}

# Plot geometry
W, H = 780, 600
ML, MR, MT, MB = 74, 22, 30, 58
PW, PH = W - ML - MR, H - MT - MB
X0, X1 = 4.0, 8.6          # log10 savings range
Y0, Y1 = 3.9, 7.9          # log10 risk range
D = math.log10(9)          # risk_share 0.9 / 0.1 boundary offset (~0.954)


def X(s): return ML + (s - X0) / (X1 - X0) * PW
def Y(r): return MT + (Y1 - r) / (Y1 - Y0) * PH


def poly(pts):
    return " ".join(f"{X(s):.1f},{Y(r):.1f}" for s, r in pts)


sup = {4: "10⁴", 5: "10⁵", 6: "10⁶", 7: "10⁷", 8: "10⁸"}

parts = []
parts.append("""<style>
.har-map { --hm-ink:#073642; --hm-muted:#657b83; --hm-grid:#e4dcc3; --hm-ring:#fdf6e3;
           --hm-c1:#2a78d6; --hm-c2:#1baf7a; --hm-c3:#c98500;
           --hm-b1:rgba(42,120,214,0.08); --hm-b2:rgba(27,175,122,0.08); --hm-b3:rgba(201,133,0,0.07); }
.quarto-dark .har-map, [data-bs-theme="dark"] .har-map {
  --hm-ink:#eee8d5; --hm-muted:#93a1a1; --hm-grid:#0f4a5a; --hm-ring:#073642;
  --hm-c1:#3987e5; --hm-c2:#199e70; --hm-c3:#c98500;
  --hm-b1:rgba(57,135,229,0.16); --hm-b2:rgba(25,158,112,0.16); --hm-b3:rgba(201,133,0,0.14); }
.har-map text { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }
.har-map .pt:hover circle { stroke-width: 3; }
</style>
""")
parts.append(f'<svg class="har-map" viewBox="0 0 {W} {H}" role="img" '
             f'aria-label="HAR map: savings hours versus risk hours for ten product families" '
             f'style="max-width:100%;height:auto;">')

# --- posture bands (clipped to plot rect) ---
sec = [(X0, X0 + D), (Y1 - D, Y1), (X0, Y1)]                                  # r > s + D
lev = [(Y0 + D, Y0), (X1, Y0), (X1, X1 - D)]                                  # r < s - D
mid = [(X0, Y0), (Y0 + D, Y0), (X1, X1 - D), (X1, Y1), (Y1 - D, Y1), (X0, X0 + D)]
parts.append(f'<polygon points="{poly(sec)}" fill="var(--hm-b2)"/>')
parts.append(f'<polygon points="{poly(lev)}" fill="var(--hm-b1)"/>')
parts.append(f'<polygon points="{poly(mid)}" fill="var(--hm-b3)"/>')

# --- grid + ticks ---
for t in range(5, 9):
    parts.append(f'<line x1="{X(t):.1f}" y1="{MT}" x2="{X(t):.1f}" y2="{MT+PH}" stroke="var(--hm-grid)" stroke-width="1"/>')
for t in range(4, 8):
    parts.append(f'<line x1="{ML}" y1="{Y(t):.1f}" x2="{ML+PW}" y2="{Y(t):.1f}" stroke="var(--hm-grid)" stroke-width="1"/>')
# axes
parts.append(f'<line x1="{ML}" y1="{MT+PH}" x2="{ML+PW}" y2="{MT+PH}" stroke="var(--hm-muted)" stroke-width="1.5"/>')
parts.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{MT+PH}" stroke="var(--hm-muted)" stroke-width="1.5"/>')
for t in range(4, 9):
    parts.append(f'<text x="{X(t):.1f}" y="{MT+PH+22}" text-anchor="middle" font-size="12" fill="var(--hm-muted)">{sup[t]}</text>')
for t in range(4, 8):
    parts.append(f'<text x="{ML-10}" y="{Y(t)+4:.1f}" text-anchor="end" font-size="12" fill="var(--hm-muted)">{sup[t]}</text>')
parts.append(f'<text x="{ML+PW/2:.0f}" y="{H-14}" text-anchor="middle" font-size="13" fill="var(--hm-ink)">HAR<tspan baseline-shift="sub" font-size="10">savings</tspan> (quality-adjusted hours / year) →</text>')
parts.append(f'<text x="20" y="{MT+PH/2:.0f}" text-anchor="middle" font-size="13" fill="var(--hm-ink)" transform="rotate(-90 20 {MT+PH/2:.0f})">HAR<tspan baseline-shift="sub" font-size="10">risk</tspan> (quality-adjusted hours / year) →</text>')

# --- risk_share midline (r = s) ---
parts.append(f'<line x1="{X(4.0):.1f}" y1="{Y(4.0):.1f}" x2="{X(7.9):.1f}" y2="{Y(7.9):.1f}" stroke="var(--hm-muted)" stroke-width="1" stroke-dasharray="5 5" opacity="0.7"/>')
parts.append(f'<text x="{X(4.85):.1f}" y="{Y(5.05):.1f}" font-size="11" fill="var(--hm-muted)" transform="rotate(-40 {X(4.85):.1f} {Y(5.05):.1f})">risk_share = 0.5</text>')

# --- band labels (text tokens + colored swatch dot: legend + direct label in one) ---
def band_label(x, y, key, anchor="start"):
    p = POSTURE[key]
    dot_dx = -9 if anchor == "start" else 9
    return (f'<circle cx="{x + dot_dx}" cy="{y - 4}" r="5" fill="var(--hm-{p["var"]})"/>'
            f'<text x="{x + (4 if anchor == "start" else -4)}" y="{y}" text-anchor="{anchor}" '
            f'font-size="12" font-weight="600" fill="var(--hm-ink)">{p["label"]}</text>')

parts.append(band_label(X(4.12) + 9, Y(7.72), "secure", "start"))
parts.append(band_label(X(8.5) - 9, Y(4.08), "leverage", "end"))
parts.append(band_label(X(8.5) - 9, Y(7.72), "strategic", "end"))

# --- points ---
for name, s, r, posture, anchor_note in DATA:
    share = 10 ** r / (10 ** r + 10 ** s)
    color = f'var(--hm-{POSTURE[posture]["var"]})'
    an, dx, dy = LABEL[name]
    tip = (f"{name}\nHAR_savings ≈ 10^{s:g} h/yr · HAR_risk ≈ 10^{r:g} h/yr"
           f"\nrisk_share ≈ {share:.2f}\n{anchor_note}")
    parts.append(
        f'<g class="pt"><title>{tip}</title>'
        f'<circle cx="{X(s):.1f}" cy="{Y(r):.1f}" r="6" fill="{color}" stroke="var(--hm-ring)" stroke-width="2"/>'
        f'<text x="{X(s)+dx:.1f}" y="{Y(r)+dy:.1f}" text-anchor="{an}" font-size="12" fill="var(--hm-ink)">{name}</text></g>')

parts.append("</svg>")

out = "/Users/jdonaldson/Projects/jjd.io/posts/_har_map.html"
with open(out, "w") as f:
    f.write("\n".join(parts) + "\n")
print(f"wrote {out}")
