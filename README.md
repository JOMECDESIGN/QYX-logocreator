# QYX Logo Creator — a Claude Code Skill

Generate **professional, scalable SVG logos** and **high-end showcase images**,
straight from Claude Code.

Unlike text-to-image logo tools, the logo here is authored as **hand-written SVG**
following an explicit design methodology — so it's vectors, infinitely scalable,
editable, and consistent in mono / dark / light. AI image models are used only
(optionally) to render photoreal **showcase backgrounds**; a zero-dependency
CSS/WebGL path is also included.

## What you get
- **6+ distinct SVG logo variants** per request, each obeying 8 design laws.
- **SVG + PNG** export (`scripts/svg_to_png.py`).
- **12 professional showcase backgrounds** via AI (`scripts/generate_showcase.py`)
  **or** zero-dependency WebGL/CSS (`assets/`).

## Install (as a skill)
```bash
npx skills add https://github.com/JOMECDESIGN/QYX-logocreator.git
```
Then in Claude Code, just ask: *"Make me a logo for …"* — the `logo-generator`
skill activates automatically (or invoke `/logo-generator`).

## Setup (only for export / AI showcase)
```bash
pip install -r requirements.txt
cp .env.example .env   # fill in only if you use the AI showcase path
```
The **logo generation itself needs no API key** — it's authored SVG.

## Showcase paths
| Path | Command | Needs |
|------|---------|-------|
| CSS / WebGL (default) | open `assets/showcase_template.html?bg=void&name=Brand` | nothing, offline |
| AI image model | `python scripts/generate_showcase.py logo.png --name Brand --all-styles` | `.env` provider key |

The AI path is **provider-pluggable** via `.env`:
`IMAGE_PROVIDER = gemini | together | openai-compatible` (Jimeng / Tongyi / self-hosted).

## Layout
```
SKILL.md                 # skill definition + 5-phase workflow
references/               # ★ the methodology (the real value)
  design_patterns.md      #   8 laws + construction pattern library
  industry_patterns.md    #   AI / 船舶智能化 / 智能座舱 playbooks
  background_styles.md    #   12 showcase backgrounds
  webgl_backgrounds.md    #   6 dynamic CSS/WebGL backgrounds
  brand_guidelines.md     #   brand spec output (palette/clear-space/min-size)
scripts/
  svg_to_png.py           # SVG -> PNG (cairosvg / resvg / playwright)
  generate_showcase.py    # AI showcase, pluggable provider
assets/
  showcase_template.html  # single-image interactive stage
  background_library.html # all backgrounds, grid preview
  brand_sheet_template.html # one-page brand spec sheet
```

## Credits
Reimplementation inspired by the open-source
[op7418/logo-generator-skill](https://github.com/op7418/logo-generator-skill),
with a pluggable image provider and a zero-dependency CSS/WebGL showcase path added.
