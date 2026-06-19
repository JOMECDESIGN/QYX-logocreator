#!/bin/bash
# SessionStart hook: install minimal deps and run the project's syntax +
# consistency checks so every Claude Code (web) session starts on a known-good base.
# Idempotent, non-interactive. Reports results but never blocks the session.
set -uo pipefail

cd "${CLAUDE_PROJECT_DIR:-$(pwd)}"

echo "== logo-generator session checks =="

# --- 1. Optional deps (best-effort; cairosvg needs system cairo) -------------
if ! python3 -c "import cairosvg" >/dev/null 2>&1; then
  echo "-- installing cairosvg (best-effort)…"
  pip install --quiet cairosvg python-dotenv >/dev/null 2>&1 \
    && echo "   cairosvg installed" \
    || echo "   cairosvg unavailable (SVG->PNG will need resvg/playwright; non-fatal)"
fi

fail=0

# --- 2. Python syntax -------------------------------------------------------
if python3 -m py_compile scripts/*.py 2>/tmp/pycerr; then
  echo "[OK]  python syntax (scripts/*.py)"
else
  echo "[FAIL] python syntax:"; sed 's/^/       /' /tmp/pycerr; fail=1
fi

# --- 3. HTML embedded JS syntax (node) --------------------------------------
if command -v node >/dev/null 2>&1; then
  for h in assets/*.html; do
    if node -e '
      const fs=require("fs");
      const s=fs.readFileSync(process.argv[1],"utf8");
      const js=[...s.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]).join("\n;\n");
      new Function(js);
    ' "$h" 2>/tmp/jserr; then
      echo "[OK]  html js syntax ($h)"
    else
      echo "[FAIL] html js syntax ($h):"; sed 's/^/       /' /tmp/jserr; fail=1
    fi
  done
else
  echo "[skip] node not found; HTML JS syntax check skipped"
fi

# --- 4. Background-style key parity -----------------------------------------
# Keys in references/background_styles.md (### headings) must match the STYLES
# dict in scripts/generate_showcase.py exactly.
md_keys=$(grep -E '^### ' references/background_styles.md | grep -oE '`[a-z]+`' | tr -d '`' | sort)
py_keys=$(python3 - <<'PY'
import re
s = open("scripts/generate_showcase.py").read()
m = re.search(r"STYLES.*?\{(.*?)\n\}", s, re.S).group(1)
print("\n".join(sorted(re.findall(r'"(\w+)":', m))))
PY
)
if [ "$md_keys" = "$py_keys" ]; then
  echo "[OK]  background-style key parity ($(echo "$py_keys" | grep -c .) styles)"
else
  echo "[FAIL] background-style key mismatch:"
  diff <(echo "$md_keys") <(echo "$py_keys") | sed 's/^/       /'; fail=1
fi

# --- summary ----------------------------------------------------------------
if [ "$fail" -eq 0 ]; then
  echo "== all checks passed =="
else
  echo "== checks reported issues (see above); session continues =="
fi

# Never block the session on check failures.
exit 0
