#!/usr/bin/env python3
"""Convert an SVG logo to PNG.

Default backend is cairosvg. If cairosvg fails to install (it needs the system
`cairo` library), you can switch CONVERTER to "resvg" (pip install resvg-py) or
"playwright" (pip install playwright && playwright install chromium) — both avoid
the cairo system dependency.

Usage:
    python scripts/svg_to_png.py logo.svg logo.png --size 1024
    python scripts/svg_to_png.py logo.svg tiny.png --size 16     # legibility test
    python scripts/svg_to_png.py logo.svg white.png --color "#FFFFFF"  # set ink
"""
import argparse
import re
import sys
from pathlib import Path

CONVERTER = "cairosvg"  # "cairosvg" | "resvg" | "playwright"


def apply_ink(svg: str, color: str | None) -> str:
    """Replace currentColor with an explicit ink color (for dark/light backdrops)."""
    if not color:
        return svg
    return svg.replace("currentColor", color)


def convert_cairosvg(svg: str, out: Path, size: int) -> None:
    import cairosvg  # type: ignore

    cairosvg.svg2png(
        bytestring=svg.encode("utf-8"),
        write_to=str(out),
        output_width=size,
        output_height=size,
    )


def convert_resvg(svg: str, out: Path, size: int) -> None:
    from resvg_py import svg_to_png  # type: ignore

    data = svg_to_png(svg_string=svg, width=size, height=size)
    out.write_bytes(data)


def convert_playwright(svg: str, out: Path, size: int) -> None:
    from playwright.sync_api import sync_playwright  # type: ignore

    html = (
        f'<body style="margin:0">'
        f'<div style="width:{size}px;height:{size}px">{svg}</div></body>'
    )
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": size, "height": size})
        page.set_content(html)
        page.locator("div").screenshot(path=str(out), omit_background=True)
        browser.close()


CONVERTERS = {
    "cairosvg": convert_cairosvg,
    "resvg": convert_resvg,
    "playwright": convert_playwright,
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Convert SVG logo to PNG.")
    ap.add_argument("svg", type=Path, help="input .svg file")
    ap.add_argument("png", type=Path, help="output .png file")
    ap.add_argument("--size", type=int, default=1024, help="output px (square)")
    ap.add_argument("--color", default=None, help="replace currentColor, e.g. #FFFFFF")
    args = ap.parse_args()

    if not args.svg.exists():
        print(f"error: {args.svg} not found", file=sys.stderr)
        return 1

    svg = apply_ink(args.svg.read_text(encoding="utf-8"), args.color)

    # Ensure a viewBox exists so scaling is predictable.
    if "viewBox" not in svg:
        print("warning: SVG has no viewBox; output may scale unexpectedly",
              file=sys.stderr)

    args.png.parent.mkdir(parents=True, exist_ok=True)
    try:
        CONVERTERS[CONVERTER](svg, args.png, args.size)
    except ImportError as e:
        print(
            f"error: backend '{CONVERTER}' not installed ({e}).\n"
            f"  pip install cairosvg   (or set CONVERTER='resvg'/'playwright' "
            f"in this file)",
            file=sys.stderr,
        )
        return 2

    print(f"wrote {args.png} ({args.size}x{args.size}) via {CONVERTER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
