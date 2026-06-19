# Brand Specification Output

After a logo is chosen (Phase 5), deliver a short **brand spec** so the mark is
usable, not just pretty. Produce these four sections. Keep them concrete and
numeric. Optionally render `assets/brand_sheet_template.html` into a one-page sheet.

---

## 1. Color palette

Derive from the single-ink mark. Provide:

- **Primary ink** — the brand color. Give HEX + RGB. (If the user had no
  preference, propose one fitting the industry: AI→indigo `#3B3BE6`, maritime→navy
  `#0E2A47`, smart cockpit→graphite `#26282B` or cyan accent `#19B5C9`.)
- **Ink on dark** — usually pure white `#FFFFFF` (logo on dark showcases).
- **Ink on light** — usually near-black `#0A0A0A`.
- **Neutrals (2)** — a light surface and a dark surface for backgrounds.
- **Tints** — the primary at opacity 35% and 12% (matches the `currentColor` +
  opacity depth system; use for supporting elements, never as a second hue).

Present as a small table:

| Role | HEX | Use |
|------|-----|-----|
| Primary ink | `#…` | the mark, key UI accents |
| On dark | `#FFFFFF` | mark on dark backgrounds |
| On light | `#0A0A0A` | mark on light backgrounds |
| Surface light | `#F4F1EA` | light backdrops |
| Surface dark | `#0A0A0A` | dark backdrops |
| Tint 35% / 12% | primary @ .35 / .12 | supporting shapes |

State a contrast note: primary ink must hit **≥4.5:1** against any surface it sits on.

## 2. Clear space (exclusion zone)

Define clear space as a fraction of the mark. Default: **clear space = 25% of the
logo's width (`x = 0.25·W`) on all sides**, and nothing else may enter that zone.

Pick a unit from the mark itself (e.g. the hero dot radius `r`, or the cap height)
and express clear space in that unit so it scales — e.g. "clear space = 2·`r`".

## 3. Minimum size

- **Digital:** minimum **24 px** height for the symbol alone (it was designed to
  survive the 16 px legibility test, so 24 px is a safe floor with margin).
- **Print:** minimum **8 mm** height.
- Below these sizes, switch to the simplest variant (drop the lowest-opacity
  supporting elements first).

Verify with: `python scripts/svg_to_png.py logo.svg t.png --size 24`.

## 4. Usage do / don't

State the rules that protect the mark:

**Do**
- Use the provided SVG; recolor only via the approved palette (single ink).
- Keep the clear space.
- Use the on-dark / on-light variant matching the background.

**Don't**
- Add gradients, shadows, outlines, or a second hue.
- Stretch, rotate, or recolor outside the palette.
- Place on a busy background or below the minimum size.
- Re-spacing or rearranging the internal elements.

---

## Output format
Deliver the spec inline as Markdown, and (if asked for a shareable asset) populate
`assets/brand_sheet_template.html`:

```
open "assets/brand_sheet_template.html?name=Brand&ink=%233B3BE6&logo=logo.svg"
```
The sheet shows: the mark on dark + light, the palette swatches, the clear-space
diagram, the minimum-size row, and the do/don't list — ready to screenshot or print.
