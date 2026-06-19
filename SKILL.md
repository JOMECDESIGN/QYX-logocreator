---
name: logo-generator
description: >
  Generate professional SVG logos and high-end showcase images. Use when the user
  wants to: (1) Create a logo or icon for a product/brand, (2) Generate logo design
  concepts from product information, (3) Produce professional logo showcase
  presentations with multiple background styles, (4) Export logos in various formats
  (SVG, PNG), or (5) Iterate on logo designs with different visual styles. Supports
  geometric patterns, dot-matrix designs, line systems, node networks, and mixed
  compositions. Showcase images are rendered either with a pure-CSS/WebGL pipeline
  (zero external dependencies) or with an AI image model (Gemini / Together / any
  OpenAI-compatible endpoint) across 12 professional background styles.
---

# Logo Generator

Generate **professional, scalable SVG logos** and **high-end showcase images**.

The logo itself is authored as **hand-written SVG code** following the design
methodology in `references/design_patterns.md` — no text-to-image model is used to
draw the mark. Image models are only used (optionally) to render showcase
backgrounds.

## Workflow

Follow these five phases. Do not skip Phase 1.

### Phase 1 — Information Gathering
Ask a **small, focused** set of questions (never an interrogation):
- Product / brand name (required — it may appear in the mark).
- Industry / domain.
- One-sentence core concept or value.
- Style preference (geometric, dot-matrix, line, organic, minimal…) and any
  must-have / must-avoid elements.
- Primary color preference (or "you decide").

If the user already gave enough, skip straight to Phase 2.

### Phase 2 — Pattern Matching & SVG Generation
1. Read `references/design_patterns.md` and pick **distinct construction patterns**.
2. Generate **at least 6 variants** that differ across pattern type, density,
   symmetry, weight, and complexity — not 6 versions of one idea.
3. Every SVG uses `viewBox="0 0 100 100"`, is centered around (50, 50), uses
   `currentColor` (single ink), `<defs>` + `<use>` for repeated elements, and
   opacity (0.1–0.4) instead of extra colors.
4. **Self-check each variant** against the 8 design laws before showing it
   (see Self-Check below). Discard any that fail.
5. Show all variants inline (render the SVG) with a one-line rationale each.

### Phase 3 — Iteration & Refinement
Narrow to the user's preferred 1–2 directions. Adjust concrete parameters:
spacing, rotation, stroke weight, dot radius, negative-space cut, color.

### Phase 4 — High-End Showcase Generation
1. Convert the chosen SVG to PNG:
   `python scripts/svg_to_png.py logo.svg logo.png --size 1024`
2. Generate showcase images. Two paths:
   - **CSS path (default, zero dependency):** open `assets/showcase_template.html`,
     inject the SVG, pick a background style, screenshot. No API key needed.
   - **AI path:** `python scripts/generate_showcase.py logo.png --name "Brand" --all-styles`
     Renders the logo into 12 professional backgrounds (16:9, 2K) via the
     configured image provider. See `references/background_styles.md`.

### Phase 5 — Delivery
Package and hand off: editable **SVG**, production **PNG**, the **showcase images**,
and (optionally) an interactive HTML showcase. Offer a short brand note
(suggested colors, clear-space, min-size).

## Key Design Principles (8 Laws)
See `references/design_patterns.md` for full detail. In brief:
1. Extreme simplicity — 1–2 core elements max.
2. Generous negative space — 40–50% of the canvas stays empty.
3. Precise proportions — stroke 2.5–4, dot radius 2–8, spacing ≥8–12 (in 100×100).
4. Visual tension through asymmetry.
5. Restraint over decoration — no gradients, no shadows.
6. Single focal point.
7. Structural stability — strokes < 2.5 feel fragile.
8. Rounded negative-space cuts — sharp cuts feel accidental.

## Self-Check (run before showing any logo)
- [ ] 1–2 core elements only?
- [ ] ≥40% negative space?
- [ ] Stroke ≥2.5, consistent weights?
- [ ] One clear focal point?
- [ ] Single ink via `currentColor` (opacity for depth)?
- [ ] Still legible mentally at 16×16? (`scripts/svg_to_png.py logo.svg t.png --size 16`)

## Technical Notes
- SVG: semantic `<g>` grouping, reusable `<defs>`/`<use>`, `<clipPath>` for masking.
- Showcase (AI path) needs provider config in `.env` (see `.env.example`).
  Provider is pluggable: `gemini` (default), `together`, or any
  `openai-compatible` image endpoint — set `IMAGE_PROVIDER` and `IMAGE_MODEL`.
- Showcase (CSS path) needs nothing — it renders in a browser.

## Common Patterns
Reusable starting points (full library in `references/design_patterns.md`):
- **Concentric dots** — rings of circles around center, radius/opacity falloff.
- **Geometric + line accent** — a clean shape cut or crossed by a single line system.
- **Node network** — dots as nodes joined by curved edges.
- **Dot-matrix fill** — a geometric silhouette filled with a dot grid.

## Troubleshooting
- `cairosvg` install fails → it needs the system `cairo` lib; install it, or switch
  the converter to `resvg`/Playwright (see `scripts/svg_to_png.py` header).
- AI showcase 401/403 → check `.env` key and that your account can call `IMAGE_MODEL`.
- Logo looks busy → you broke Law 1 or 2; reduce to 1–2 elements, add negative space.
