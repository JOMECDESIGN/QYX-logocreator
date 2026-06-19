#!/usr/bin/env python3
"""Generate high-end logo showcase images with an AI image model.

Provider is pluggable via env (.env / .env.example):
    IMAGE_PROVIDER = gemini | together | openai-compatible
    IMAGE_MODEL    = <model id for that provider>

The logo PNG is sent as a reference; the model composes it onto a professional
background described in references/background_styles.md. The logo is flattened to
a single ink color (white on dark styles, black on light styles).

Usage:
    python scripts/generate_showcase.py logo.png --name "Acme" --style void
    python scripts/generate_showcase.py logo.png --name "Acme" --all-styles
    python scripts/generate_showcase.py logo.png --name "Acme" --desc "AI database"

Output: output/<name>_<style>.png  (16:9, ~2K)
"""
import argparse
import base64
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:  # dotenv optional
    pass

# style key -> (is_dark, prompt fragment). Keep in sync with background_styles.md.
STYLES: dict[str, tuple[bool, str]] = {
    "void": (True, "Absolute black (#000000) background with extremely fine "
                   "silver/white high-contrast micro-noise and faint distant starlight at the edges."),
    "frosted": (True, "Deep titanium gray (#1a1c1e) with organic dust texture and one large, "
                      "low-saturation cold gray-blue light halo."),
    "fluid": (True, "Deep purple / Klein blue base with dark orange (right) and dark blue (left) "
                    "slowly interweaving like fluid."),
    "spotlight": (True, "Warm carbon gray with physical studio lighting and a soft vignette."),
    "analog": (True, "One solid vibrant color field (orange) with a metallic shimmer overlay of "
                     "gold dust and mica powder."),
    "matrix": (True, "Black base with a glowing dot-matrix pattern and subtle CRT scanline artifacts."),
    "editorial": (False, "Off-white (#f4f1ea) paper with fine grain, humanistic independent-magazine feel."),
    "iridescent": (False, "Light silver-gray with soft holographic iridescent sheen through frosted glass."),
    "aura": (False, "Warm cream with blurred low-saturation pastel blobs dissolving into warm white."),
    "clinical": (False, "Pure white (#ffffff) with a large softbox from the top creating a smooth "
                        "gray-white gradient."),
    "ui": (False, "Clean light gradient with a frosted-glass container card holding the logo."),
    "swiss": (False, "100% pure solid deep vintage green, zero effects, flat Swiss style."),
}


def build_prompt(name: str, desc: str, style_key: str) -> str:
    is_dark, bg = STYLES[style_key]
    ink = "pure white" if is_dark else "solid black"
    desc_line = f" The product is: {desc}." if desc else ""
    return (
        "Create a professional brand showcase image, 16:9, high resolution.\n"
        f"Background: {bg}\n"
        "Place the provided reference logo CENTERED, flattened to a single "
        f"{ink} color (preserve its exact shapes; do not redraw or add detail). "
        "Generous negative space around the logo. The logo stays the clear focal point.\n"
        f'Add small, tasteful Swiss-grid caption micro-text in a corner: the brand name "{name}"'
        f" and a short tagline.{desc_line}\n"
        "No watermarks, no extra logos, no gibberish text beyond the caption."
    )


def load_logo_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


# --- providers -------------------------------------------------------------

def gen_gemini(prompt: str, logo: Path, model: str) -> bytes:
    from google import genai  # type: ignore
    from google.genai import types  # type: ignore

    cfg = {"api_key": os.environ["GEMINI_API_KEY"]}
    if os.environ.get("GEMINI_BASE_URL"):
        cfg["http_options"] = types.HttpOptions(base_url=os.environ["GEMINI_BASE_URL"])
    client = genai.Client(**cfg)

    contents = [
        prompt,
        types.Part.from_bytes(data=logo.read_bytes(), mime_type="image/png"),
    ]
    resp = client.models.generate_content(model=model, contents=contents)
    for part in resp.candidates[0].content.parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            return part.inline_data.data
    raise RuntimeError("Gemini returned no image data")


def gen_together(prompt: str, logo: Path, model: str) -> bytes:
    from together import Together  # type: ignore

    client = Together(api_key=os.environ["TOGETHER_API_KEY"])
    # Together image models are text-to-image; the logo is described, not attached.
    resp = client.images.generate(
        prompt=prompt, model=model, width=1344, height=768, n=1,
        response_format="b64_json",
    )
    return base64.b64decode(resp.data[0].b64_json)


def gen_openai_compatible(prompt: str, logo: Path, model: str) -> bytes:
    from openai import OpenAI  # type: ignore

    client = OpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ.get("OPENAI_BASE_URL") or None,
    )
    resp = client.images.generate(
        model=model, prompt=prompt, size="1792x1024", n=1,
    )
    item = resp.data[0]
    if getattr(item, "b64_json", None):
        return base64.b64decode(item.b64_json)
    # URL fallback
    import requests

    return requests.get(item.url, timeout=60).content


PROVIDERS = {
    "gemini": gen_gemini,
    "together": gen_together,
    "openai-compatible": gen_openai_compatible,
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate AI logo showcase images.")
    ap.add_argument("logo", type=Path, help="logo PNG (reference)")
    ap.add_argument("--name", required=True, help="brand name for caption")
    ap.add_argument("--desc", default="", help="optional product description")
    ap.add_argument("--style", default="void", choices=sorted(STYLES),
                    help="single background style")
    ap.add_argument("--all-styles", action="store_true", help="render all 12 styles")
    ap.add_argument("--out", type=Path, default=Path("output"))
    args = ap.parse_args()

    if not args.logo.exists():
        print(f"error: {args.logo} not found", file=sys.stderr)
        return 1

    provider = os.environ.get("IMAGE_PROVIDER", "gemini")
    model = os.environ.get("IMAGE_MODEL", "gemini-2.5-flash-image-preview")
    if provider not in PROVIDERS:
        print(f"error: unknown IMAGE_PROVIDER={provider!r} "
              f"(use one of {', '.join(PROVIDERS)})", file=sys.stderr)
        return 1

    styles = sorted(STYLES) if args.all_styles else [args.style]
    args.out.mkdir(parents=True, exist_ok=True)
    safe_name = args.name.lower().replace(" ", "-")

    rc = 0
    for style in styles:
        prompt = build_prompt(args.name, args.desc, style)
        try:
            data = PROVIDERS[provider](prompt, args.logo, model)
        except KeyError as e:
            print(f"error: missing env var {e} for provider {provider}", file=sys.stderr)
            return 1
        except Exception as e:  # surface, continue with other styles
            print(f"  [{style}] failed: {e}", file=sys.stderr)
            rc = 2
            continue
        dest = args.out / f"{safe_name}_{style}.png"
        dest.write_bytes(data)
        print(f"  [{style}] -> {dest}")

    return rc


if __name__ == "__main__":
    raise SystemExit(main())
