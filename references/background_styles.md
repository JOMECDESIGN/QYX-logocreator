# Showcase Background Styles

12 professional backdrops for presenting a finished logo. Each entry is a building
block for the AI showcase prompt (`scripts/generate_showcase.py`) and maps to a
CSS/WebGL preset (`assets/`). The logo is always the focal point — backgrounds stay
restrained (except the intentionally bold ones).

**Logo ink rule:** on **dark** styles render the logo **white**; on **light**
styles render it **black** (`scripts/generate_showcase.py` does this automatically).
Layout follows a Swiss grid: logo centered or on a thirds line, with small caption
micro-text (brand name + a short tag) in a corner.

Each style below provides: `key` (CLI value), palette, texture/lighting, and the
brand mood it fits.

---

## Dark styles

### 1. THE VOID — `void`
- **Palette:** absolute black `#000000`.
- **Texture:** extremely fine, high-contrast silver/white micro-noise; faint
  distant "starlight" at the edges.
- **Mood:** infinite, premium, serious. Tech / security / infra.

### 2. FROSTED HORIZON — `frosted`
- **Palette:** deep titanium gray `#1a1c1e`.
- **Texture:** organic dust; one large, low-saturation cold gray-blue light halo.
- **Mood:** premium design tools, studios.

### 3. FLUID ABYSS — `fluid`
- **Palette:** deep purple / Klein blue base.
- **Texture:** dark orange (right) and dark blue (left) slowly interweaving.
- **Mood:** AI, data viz, generative products.

### 4. STUDIO SPOTLIGHT — `spotlight`
- **Palette:** warm carbon gray.
- **Texture:** physical studio lighting simulation; soft vignette.
- **Mood:** editorial, considered, human.

### 5. ANALOG LIQUID — `analog`
- **Palette:** one solid vibrant color (orange / blue / lime).
- **Texture:** metallic shimmer overlay — gold dust flow, mica powder.
- **Mood:** bold creative tools, consumer.

### 6. LED MATRIX — `matrix`
- **Palette:** black base, single accent glow.
- **Texture:** glowing dot-matrix pattern; subtle CRT scanline artifacts.
- **Mood:** cyberpunk, hardware, dev tools.

---

## Light styles

### 7. EDITORIAL PAPER — `editorial`
- **Palette:** off-white `#f4f1ea`.
- **Texture:** fine paper grain.
- **Mood:** humanistic, independent-magazine, craft brands.

### 8. IRIDESCENT FROST — `iridescent`
- **Palette:** light silver-gray.
- **Texture:** soft holographic/iridescent sheen through frosted glass.
- **Mood:** tech / hardware, modern.

### 9. MORNING AURA — `aura`
- **Palette:** warm cream.
- **Texture:** blurred, low-saturation pastel blobs dissolving into warm white.
- **Mood:** approachable AI, wellness, consumer.

### 10. CLINICAL STUDIO — `clinical`
- **Palette:** pure white `#ffffff`.
- **Texture:** large softbox from top/side → smooth gray-white gradient.
- **Mood:** data-driven, medical, precise.

### 11. UI CONTAINER — `ui`
- **Palette:** clean light gradient.
- **Texture:** a frosted-glass card/container holding the logo (product UI feel).
- **Mood:** SaaS, interactive digital products.

### 12. SWISS FLAT — `swiss`
- **Palette:** 100% solid color — deep vintage green, rich burgundy, or classic navy.
- **Texture:** none. Zero effects.
- **Mood:** established, classic, confident.

---

## Selection guidance

| Brand vibe | Suggested styles |
|------------|------------------|
| Tech / security / infra | void, matrix, iridescent |
| AI / data | fluid, aura, clinical |
| Creative / consumer | analog, editorial, swiss |
| SaaS / product | ui, clinical, frosted |
| Premium / design | frosted, spotlight, editorial |

`--all-styles` renders all 12 so the user can choose.
