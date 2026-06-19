# Industry Pattern Libraries

Domain-specific playbooks layered on top of `design_patterns.md`. The 8 Laws still
govern everything here — these libraries only bias **which patterns, motifs, and
colors** to reach for so the mark reads as native to the industry. Each entry gives:
visual language, go-to construction patterns, motif vocabulary, color direction,
matching showcase styles, and do/don't.

All examples use `viewBox="0 0 100 100"`, `currentColor`, the numeric defaults from
`design_patterns.md` (stroke 3, dot 2.5–4, spacing 9).

---

## 1. AI / Intelligence

**Visual language:** systematic, generative, "emergent from data". Order that
implies computation, not decoration.

**Go-to patterns** (from `design_patterns.md`):
- Concentric dots with opacity falloff (model layers / attention).
- Node networks — dots joined by curved edges (graphs / embeddings).
- Dot-matrix fill of a silhouette (a shape *made of* data points).

**Motif vocabulary:** neuron/node, particle field converging to a focal point,
token grid, soft orbit. Avoid literal robots, brains, or circuit-board clichés.

**Color direction:** single ink. If hue is wanted: indigo/Klein blue, or a
cool→warm pair expressed only via the showcase background, not the mark.

**Showcase styles:** `fluid`, `aura`, `clinical`, `iridescent`.

```svg
<!-- Particle field converging to a focal node (AI) -->
<svg viewBox="0 0 100 100" fill="currentColor">
  <circle cx="50" cy="50" r="4"/>
  <g opacity="0.85">
    <circle cx="36" cy="40" r="2.6"/><circle cx="64" cy="40" r="2.6"/>
    <circle cx="40" cy="64" r="2.6"/><circle cx="62" cy="62" r="2.6"/>
  </g>
  <g opacity="0.3">
    <circle cx="26" cy="30" r="2.2"/><circle cx="74" cy="32" r="2.2"/>
    <circle cx="28" cy="72" r="2.2"/><circle cx="72" cy="74" r="2.2"/>
    <circle cx="50" cy="22" r="2.2"/><circle cx="50" cy="80" r="2.2"/>
  </g>
  <g stroke="currentColor" stroke-width="1.6" opacity="0.4" fill="none">
    <path d="M36 40 Q50 38 50 50"/><path d="M64 40 Q50 38 50 50"/>
    <path d="M40 64 Q46 56 50 50"/><path d="M62 62 Q54 56 50 50"/>
  </g>
</svg>
```

**Do:** let structure emerge from many small units. **Don't:** gradients, glow,
3D "AI sphere" renders, lightning bolts.

---

## 2. 船舶智能化 / Maritime Intelligence (Smart Shipping)

**Visual language:** stable, navigational, fluid-meets-structure. The mark should
feel **seaworthy** — weighty and balanced — while signalling sensing/automation.

**Go-to patterns:**
- Line systems as **waves/curves** clipped into a shape (sea + horizon).
- Geometry + line accent: a stable hull/hexagon crossed by a heading line.
- Node network as a **route/waypoint** path (curved edges between 2–3 nodes).
- Arc segment as a radar/sonar sweep (rounded cap, Law 8).

**Motif vocabulary:** bow/hull silhouette (abstracted to 2 strokes), heading
vector, waypoint chain, radar sweep, horizon line, compass tick. Avoid literal
anchors, steering wheels, or detailed ships.

**Color direction:** single ink; if hue: deep navy or teal. Maritime trust reads in
restraint, not in blue gradients.

**Showcase styles:** `void`, `swiss` (navy), `clinical`, `spotlight`.

```svg
<!-- Abstract bow + heading vector + waypoint (maritime intelligence) -->
<svg viewBox="0 0 100 100" fill="none" stroke="currentColor"
     stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
  <!-- hull/bow: two strokes meeting -->
  <path d="M28 62 L50 50 L72 62"/>
  <!-- waterline / horizon -->
  <path d="M24 70 H76" opacity="0.35"/>
  <!-- heading vector to waypoint -->
  <path d="M50 50 L50 28"/>
  <circle cx="50" cy="26" r="3.2" fill="currentColor" stroke="none"/>
</svg>
```

**Do:** keep a strong horizontal base (stability at sea). **Don't:** tilt the whole
mark, add waves as decoration, draw a recognizable boat.

---

## 3. 智能座舱 / Smart Cockpit (Intelligent Cabin)

**Visual language:** human-centric, ambient, HMI/screen-native. Rounded, calm,
"interface you live inside". Closer to product-UI than to industrial.

**Go-to patterns:**
- Rounded-rect dot grid (a display / pixel field).
- UI-container framing: a rounded enclosure holding a focal element (a screen).
- Concentric arcs as an **ambient HUD** (driver-centric, one focal point).
- Capsules along a path (controls / airflow / motion in cabin).

**Motif vocabulary:** rounded screen frame, occupant-centric arc, dashboard
horizon, soft pill controls, gaze/focus point. Avoid literal cars, steering
wheels, or dashboards.

**Color direction:** single ink; if hue: warm graphite or a calm cyan accent.
Cockpit = comfort + clarity, so favor generous rounding and light weight.

**Showcase styles:** `ui`, `frosted`, `aura`, `iridescent`.

```svg
<!-- Occupant-centric ambient HUD inside a rounded screen (smart cockpit) -->
<svg viewBox="0 0 100 100" fill="none" stroke="currentColor"
     stroke-width="3.2" stroke-linecap="round">
  <!-- rounded screen frame -->
  <rect x="22" y="30" width="56" height="40" rx="12" opacity="0.35"/>
  <!-- ambient arcs centered on the occupant focal point -->
  <path d="M38 56 A14 14 0 0 1 62 56"/>
  <path d="M32 58 A22 22 0 0 1 68 58" opacity="0.5"/>
  <!-- focal point (occupant) -->
  <circle cx="50" cy="58" r="3.2" fill="currentColor" stroke="none"/>
</svg>
```

**Do:** round generously, keep one calm focal point. **Don't:** sharp corners,
literal vehicle parts, dense detail (it must read on a small HMI badge).

---

## Cross-industry quick map

| Industry | Reach for | Avoid | Showcase |
|----------|-----------|-------|----------|
| AI | concentric dots, node networks, dot-matrix fill | robots, brains, circuits | fluid, aura, clinical, iridescent |
| 船舶智能化 | wave/line systems, bow+vector, radar arc | anchors, wheels, real ships | void, swiss(navy), clinical, spotlight |
| 智能座舱 | rounded grids, UI container, ambient arcs | cars, dashboards, sharp corners | ui, frosted, aura, iridescent |

When the brand spans two domains (e.g. AI + maritime), pick the **base pattern**
from the primary domain and borrow **one motif** from the secondary — never blend
both vocabularies into one busy mark (Law 1).
