# WebGL / CSS Dynamic Backgrounds

Reference for the **zero-dependency showcase path**: animated backgrounds rendered
in the browser (no image model, no API key). Used by `assets/background_library.html`
and `assets/showcase_template.html`. The logo is overlaid centered; export by
screenshot or headless capture.

Each background is a GLSL **fragment shader** receiving uniforms:
- `u_resolution` (vec2) — canvas size in px
- `u_time` (float) — seconds since start, for animation
- `u_mouse` (vec2) — normalized cursor position (0–1)

All backgrounds respond to the mouse: ripples emanate from the cursor, fluid
distortion follows it, with exponential decay for a natural feel. Animation targets
60 FPS via `requestAnimationFrame`; the canvas resizes to device pixel ratio.

---

## The 6 shaders

### 1. `void` — Deep Space
Absolute black with procedural starlight noise; a faint radial glow drifts. Cursor
adds a soft ripple. Maps to the **THE VOID** still style.

### 2. `aurora` — Fluid Aurora
Layered sine-distorted color fields (blue↔orange) flowing slowly. Mouse warps the
flow field. Maps to **FLUID ABYSS**.

### 3. `mesh` — Gradient Mesh
Smooth multi-stop gradient mesh with gentle low-frequency motion; pastel on light
or jewel tones on dark (seeded). Maps to **MORNING AURA** / **FROSTED HORIZON**.

### 4. `matrix` — LED Matrix
A grid of glowing dots with per-cell phase; brightness pulses; subtle scanlines.
Cursor brightens nearby cells. Maps to **LED MATRIX**.

### 5. `iridescent` — Frosted Iridescence
Thin-film interference colors over a frosted blur; hue shifts with angle/mouse.
Maps to **IRIDESCENT FROST**.

### 6. `swiss` — Solid Field
A single flat color (seeded: green / burgundy / navy), no animation. The disciplined
default. Maps to **SWISS FLAT**.

---

## Color theming
Several shaders accept a **seed** to pick a palette so repeated renders vary while
staying on-brand. Pass the logo's primary color in to tint `aurora`, `mesh`, and
`iridescent` toward the brand hue.

## Capture / export
1. Open `assets/showcase_template.html?bg=void&name=Brand`.
2. Inject the logo SVG (it reads `?logo=` or a drop zone).
3. Screenshot the 16:9 stage, or use a headless browser:
   `npx playwright screenshot --viewport-size=1920,1080 "file://…showcase_template.html?bg=void" out.png`

This path needs **no API key** and works offline — recommended as the default,
with the AI path (`generate_showcase.py`) reserved for photoreal/material backdrops.
