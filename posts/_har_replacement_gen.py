#!/usr/bin/env python3
"""Generate the 'replacement level moves' diagram (posts/_har_replacement.html).

Two states of the same product (a saline bag). Normal market: a deep pool of
substitute suppliers, so value-over-replacement ~ 0 and the product is cheap.
Stressed market (hurricane / lockdown / recall): the pool collapses, the same
product's value-over-replacement explodes without the product changing at all.
This is the post's core claim — criticality is exposure to replacement-level
collapse — given a picture.

Regenerate:  python3 posts/_har_replacement_gen.py
"""
import math

W, H = 760, 300
CY = 138
LEFT_CX, RIGHT_CX = 150, 610
POOL_R = 78          # radius of the ring of substitutes
SUB_R = 13           # substitute node radius
PROD_R = 22          # central product node radius
N_SUB = 7

parts = []
parts.append("""<style>
.har-repl { --hr-ink:#073642; --hr-muted:#657b83; --hr-grid:#e4dcc3; --hr-ring:#fdf6e3;
            --hr-prod:#c98500; --hr-sub:#1baf7a; --hr-gone:#b9482f; --hr-arrow:#657b83; }
.quarto-dark .har-repl, [data-bs-theme="dark"] .har-repl {
  --hr-ink:#eee8d5; --hr-muted:#93a1a1; --hr-grid:#0f4a5a; --hr-ring:#073642;
  --hr-prod:#c98500; --hr-sub:#199e70; --hr-gone:#d0503a; --hr-arrow:#93a1a1; }
.har-repl text { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }
</style>
""")
parts.append(f'<svg class="har-repl" viewBox="0 0 {W} {H}" role="img" '
             f'aria-label="The same product with a deep substitute pool (value over replacement near zero) '
             f'versus a collapsed pool (value over replacement explodes)" '
             f'style="max-width:100%;height:auto;">')


def draw_state(cx, gone, title, sub_label):
    g = []
    g.append(f'<text x="{cx}" y="26" text-anchor="middle" font-size="13" '
             f'font-weight="700" fill="var(--hr-ink)">{title}</text>')
    for i in range(N_SUB):
        ang = -math.pi / 2 + i * 2 * math.pi / N_SUB
        sx = cx + POOL_R * math.cos(ang)
        sy = CY + POOL_R * math.sin(ang)
        # in the stressed state all but one substitute is gone
        if gone and i != 0:
            g.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{SUB_R}" fill="none" '
                     f'stroke="var(--hr-gone)" stroke-width="1.5" stroke-dasharray="3 3" opacity="0.6"/>')
            g.append(f'<line x1="{sx-7:.1f}" y1="{sy-7:.1f}" x2="{sx+7:.1f}" y2="{sy+7:.1f}" '
                     f'stroke="var(--hr-gone)" stroke-width="1.5" opacity="0.6"/>')
            g.append(f'<line x1="{sx+7:.1f}" y1="{sy-7:.1f}" x2="{sx-7:.1f}" y2="{sy+7:.1f}" '
                     f'stroke="var(--hr-gone)" stroke-width="1.5" opacity="0.6"/>')
        else:
            g.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{SUB_R}" fill="var(--hr-sub)" '
                     f'stroke="var(--hr-ring)" stroke-width="1.5"/>')
    # central product
    g.append(f'<circle cx="{cx}" cy="{CY}" r="{PROD_R}" fill="var(--hr-prod)" '
             f'stroke="var(--hr-ring)" stroke-width="2.5"/>')
    g.append(f'<text x="{cx}" y="{CY+4}" text-anchor="middle" font-size="10.5" '
             f'font-weight="700" fill="#fdf6e3">saline</text>')
    # caption under the pool
    g.append(f'<text x="{cx}" y="{CY+POOL_R+34}" text-anchor="middle" font-size="12" '
             f'fill="var(--hr-muted)">{sub_label}</text>')
    return "".join(g)


parts.append(draw_state(LEFT_CX, False, "NORMAL MARKET",
                        "deep substitute pool"))
parts.append(draw_state(RIGHT_CX, True, "SHORTAGE",
                        "pool collapses"))

# VOR readouts under each state
parts.append(f'<text x="{LEFT_CX}" y="{CY+POOL_R+56}" text-anchor="middle" font-size="13.5" '
             f'font-weight="700" fill="var(--hr-sub)">value over replacement ≈ 0</text>')
parts.append(f'<text x="{LEFT_CX}" y="{CY+POOL_R+74}" text-anchor="middle" font-size="11" '
             f'fill="var(--hr-muted)">— which is why it’s cheap</text>')
parts.append(f'<text x="{RIGHT_CX}" y="{CY+POOL_R+56}" text-anchor="middle" font-size="13.5" '
             f'font-weight="700" fill="var(--hr-gone)">value over replacement explodes</text>')
parts.append(f'<text x="{RIGHT_CX}" y="{CY+POOL_R+74}" text-anchor="middle" font-size="11" '
             f'fill="var(--hr-muted)">— same product, unchanged</text>')

# transition arrow with trigger label
ax0, ax1 = LEFT_CX + POOL_R + 40, RIGHT_CX - POOL_R - 40
parts.append(f'<defs><marker id="hr-ah" markerWidth="9" markerHeight="9" refX="6.5" refY="3" '
             f'orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="var(--hr-arrow)"/></marker></defs>')
parts.append(f'<line x1="{ax0}" y1="{CY}" x2="{ax1}" y2="{CY}" stroke="var(--hr-arrow)" '
             f'stroke-width="1.8" marker-end="url(#hr-ah)"/>')
parts.append(f'<text x="{(ax0+ax1)/2:.0f}" y="{CY-12}" text-anchor="middle" font-size="11.5" '
             f'font-style="italic" fill="var(--hr-ink)">hurricane · lockdown · recall</text>')

parts.append("</svg>")

out = "/Users/jdonaldson/Projects/jjd.io/posts/_har_replacement.html"
with open(out, "w") as f:
    f.write("\n".join(parts) + "\n")
print(f"wrote {out}")
