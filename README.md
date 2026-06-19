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

## Development

A SessionStart hook (`.claude/hooks/session-start.sh`, registered in
`.claude/settings.json`) runs the project checks at the start of every Claude Code
web session and reports results without blocking. Run them manually any time:

```bash
.claude/hooks/session-start.sh        # all checks at once
python3 -m py_compile scripts/*.py    # python syntax
```

The checks are: **python syntax** (`scripts/*.py`), **HTML embedded-JS syntax**
(`assets/*.html`, via node), and **background-style key parity** between
`references/background_styles.md` and the `STYLES` dict in
`scripts/generate_showcase.py`.

When extending the skill, keep the invariants the checks enforce:

| Change | Keep in sync |
|--------|--------------|
| Add a showcase style | `references/background_styles.md` **and** `STYLES` in `generate_showcase.py` (key-parity check) |
| Add a CSS/WebGL shader | `SHADERS` in both `assets/*.html`, plus the 12→6 `ALIAS` map in `showcase_template.html` |
| Add an industry | a new section in `references/industry_patterns.md` + its cross-industry quick-map row |
| Change the methodology | `references/design_patterns.md` is the source of truth; mirror any numeric change into the SKILL.md self-check |

> The hook only takes effect for new sessions once `.claude/` is merged into the
> repo's default branch.

## Credits
Reimplementation inspired by the open-source
[op7418/logo-generator-skill](https://github.com/op7418/logo-generator-skill),
with a pluggable image provider and a zero-dependency CSS/WebGL showcase path added.
