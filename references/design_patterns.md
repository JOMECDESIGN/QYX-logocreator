# Logo Design Patterns — Construction Library & Laws

This is the **core methodology**. When generating logos, treat the 8 Laws as
non-negotiable constraints and use the pattern library as building blocks. All
coordinates assume `viewBox="0 0 100 100"`, centered on (50, 50).

---

## Part 0 — The 8 Design Laws (non-negotiable)

1. **Extreme Simplicity.** 1–2 core elements maximum. If you can remove an
   element and the idea survives, remove it. Memorable = reducible.
2. **Generous Negative Space.** 40–50% of the canvas stays empty. Void is an
   active design element, not leftover space.
3. **Precise Proportions.** Stroke width **2.5–4**. Dot radius **2–8**. Minimum
   spacing between elements **8–12**. Keep weights consistent within one mark.
4. **Visual Tension Through Asymmetry.** Avoid perfect symmetry; a deliberate
   offset, rotation, or break creates energy.
5. **Restraint Over Decoration.** No gradients, no drop shadows, no bevels.
   Every element must justify its existence.
6. **Single Focal Point.** The eye should land in exactly one place first.
7. **Structural Stability.** Marks need visual weight — dense line systems or
   solid shapes. Strokes thinner than 2.5 feel fragile and "unfinished".
8. **Rounded Negative-Space Cuts.** When cutting a notch/gap into a shape, round
   the inner corners (`stroke-linejoin="round"`, rounded paths). Sharp accidental
   corners read as a mistake.

### One-ink rule
Use a **single ink color** via `currentColor`. Create depth with **opacity**
(0.1–0.4 for supporting/background elements, 1.0 for the primary element) — never
by introducing extra hues. This keeps the mark reproducible in mono, on dark, on
light, and at any size.

---

## Part 1 — Fundamental Elements

### 1.1 Dot-Matrix Systems
- **Concentric dots:** rings of circles around (50,50); radius and/or opacity
  decay outward. Calm, systematic, "data/AI" feel.
- **Grid (rounded-rect dots):** an N×N matrix of small rounded squares; remove or
  resize cells to form a glyph or gradient.
- **Capsules along a path:** equal capsules following a curve (motion, flow).
- **Hexagons / honeycomb:** tessellated hexes; structural, "infra/security".

```svg
<!-- Concentric dots: opacity falloff from center -->
<svg viewBox="0 0 100 100" fill="currentColor">
  <circle cx="50" cy="50" r="4"/>
  <g>
    <circle cx="50" cy="34" r="3" opacity="0.8"/>
    <circle cx="66" cy="50" r="3" opacity="0.8"/>
    <circle cx="50" cy="66" r="3" opacity="0.8"/>
    <circle cx="34" cy="50" r="3" opacity="0.8"/>
  </g>
  <g opacity="0.35">
    <circle cx="50" cy="22" r="2.5"/><circle cx="78" cy="50" r="2.5"/>
    <circle cx="50" cy="78" r="2.5"/><circle cx="22" cy="50" r="2.5"/>
  </g>
</svg>
```

### 1.2 Geometric Shapes
- **Concentric circles / arcs** — orbit, target, lens.
- **Arc segments** — a ring with a deliberate gap (Law 8: rounded ends via
  `stroke-linecap="round"`).
- **Boolean cuts** — subtract a circle from a square to suggest a letter or void.
- **Polygon compositions** — triangle/hexagon as a stable base.

```svg
<!-- Ring with rounded gap + offset accent dot (asymmetry, Law 4) -->
<svg viewBox="0 0 100 100" fill="none" stroke="currentColor"
     stroke-width="3.2" stroke-linecap="round">
  <path d="M50 22 A28 28 0 1 1 24 64"/>
  <circle cx="50" cy="50" r="3.5" fill="currentColor" stroke="none"/>
</svg>
```

### 1.3 Line Systems
- **Horizontal fill in a mask** — equal-spaced lines clipped to a circle/shape
  (venetian-blind effect); weight via line count.
- **Waves / curves** — a few parallel curves; restraint is key.
- **Spiral** — single continuous spiral; motion + focus to center.

```svg
<!-- Equal lines clipped to a circle -->
<svg viewBox="0 0 100 100">
  <defs><clipPath id="c"><circle cx="50" cy="50" r="30"/></clipPath></defs>
  <g clip-path="url(#c)" stroke="currentColor" stroke-width="3.2">
    <line x1="20" y1="38" x2="80" y2="38"/>
    <line x1="20" y1="50" x2="80" y2="50"/>
    <line x1="20" y1="62" x2="80" y2="62"/>
  </g>
</svg>
```

### 1.4 Node Networks
Dots as nodes joined by **curved** edges (quadratic paths). Suggests
connection, graphs, relationships. Keep ≤5 nodes (Law 1/2).

---

## Part 2 — Advanced Combinations

- **Dot-matrix fill of a silhouette** — define a shape, fill only its interior
  with a dot grid (use `<clipPath>`); the silhouette reads from afar, the texture
  rewards a closer look.
- **Node grid** — a regular dot grid with a few highlighted, connected nodes.
- **Outline-only geometry** — compose entirely from strokes (no fills) for a
  light, technical mark; respect stroke ≥2.5.
- **Layered composition** — a faint large background element (opacity 0.12–0.2)
  behind a bold foreground; depth without color or shadow.

```svg
<!-- Dot-matrix filling a circular silhouette -->
<svg viewBox="0 0 100 100" fill="currentColor">
  <defs>
    <clipPath id="disc"><circle cx="50" cy="50" r="30"/></clipPath>
    <circle id="d" r="2.4"/>
  </defs>
  <g clip-path="url(#disc)">
    <!-- 7x7 grid, spacing 9, origin 14 -->
    <use href="#d" x="23" y="23"/><use href="#d" x="32" y="23"/><use href="#d" x="41" y="23"/>
    <use href="#d" x="50" y="23"/><use href="#d" x="59" y="23"/><use href="#d" x="68" y="23"/>
    <use href="#d" x="32" y="32"/><use href="#d" x="41" y="32"/><use href="#d" x="50" y="32"/>
    <use href="#d" x="59" y="32"/><use href="#d" x="50" y="41"/><use href="#d" x="50" y="50"/>
  </g>
</svg>
```

---

## Part 3 — Letter / Symbol Integration

- **Geometric abstraction of a letter** — reduce the initial to its skeleton, then
  rebuild from the chosen pattern language (a "K" as two crossing line systems).
- **Dot-matrix lettering** — form the initial out of the dot grid so the symbol
  and the mark share one visual language.
- **Counter as concept** — use the letter's enclosed space (counter) as the
  negative-space focal point.

Always keep the letter readable at small size; if in doubt, abstract less.

---

## Part 4 — Generating 6 Distinct Variants

Do **not** produce 6 versions of one concept. Spread the set across these axes:

| Axis | Pull the variants apart by… |
|------|-----------------------------|
| Pattern type | pure geometry / dot-matrix / line system / node network / mixed / layered |
| Density | sparse vs. dense |
| Symmetry | radial-symmetric vs. deliberately asymmetric |
| Weight | light outline vs. solid heavy |
| Complexity | single element vs. shape+accent |

A good default set of 6:
1. Pure geometry (ring + gap + accent).
2. Concentric dots (systematic).
3. Line system in a mask (textured).
4. Node network (connection).
5. Dot-matrix silhouette (mixed).
6. Letterform abstraction (brand-specific).

Run the **Self-Check** (in `SKILL.md`) on each before presenting.

---

## Quick reference — numeric defaults (100×100 viewBox)

- Stroke width: **3** (range 2.5–4)
- Dot radius: **2.5–4** (hero dot up to 8)
- Element spacing: **9** (range 8–12)
- Safe margin from edges: **≥18** (keeps ≥40% negative space)
- Background/support opacity: **0.12–0.35**
- Corner rounding: `stroke-linecap="round"`, `stroke-linejoin="round"`
