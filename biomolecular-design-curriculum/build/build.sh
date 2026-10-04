#!/bin/zsh
setopt NULL_GLOB
set -e
# directory holding the numbered source parts (defaults to this script's own directory)
D="${D:-$(cd "$(dirname "$0")" && pwd)}"
OUT="${OUT:-$(cd "$D/.." && pwd)}"
mkdir -p "$OUT"

# --- generated sections (regenerate every build so they cannot drift) ---
python3 "$D/gen_hours.py" "$D" "$D/05_hours.md"


python3 - "$D" <<'PY'
import sys, pathlib
d = pathlib.Path(sys.argv[1])
parts = sorted(p for p in d.glob("[0-9][0-9]_*.md"))
out = "\n\n".join(p.read_text().rstrip() for p in parts)
(d/"full.md").write_text(out + "\n")
print("parts:", len(parts), "| words:", len(out.split()))
PY

python3 "$D/gen_index.py" "$D/full.md" "$D/96_appendix_index.md"
# reassemble so the index is included
python3 - "$D" <<'PY'
import sys, pathlib
d = pathlib.Path(sys.argv[1])
parts = sorted(p for p in d.glob("[0-9][0-9]_*.md"))
out = "\n\n".join(p.read_text().rstrip() for p in parts)
(d/"full.md").write_text(out + "\n")
print("final parts:", len(parts), "| words:", len(out.split()))
PY

pandoc "$D/full.md" -o "$D/full.html" \
  --standalone --toc --toc-depth=2 \
  --metadata title="The Biomolecular Design Curriculum" \
  --metadata subtitle="Third Edition — every computational method for proteins, DNA and RNA, the AI research upstream of it, and the engineering that makes it fast" \
  --metadata author="A self-study curriculum" \
  --metadata date="October 4, 2026" \
  --css style.css --resource-path="$D"

python3 - "$D" <<'PY'
import sys, pathlib
d = pathlib.Path(sys.argv[1])
html = (d/"full.html").read_text()
css = (d/"style.css").read_text()
html = html.replace('<link rel="stylesheet" href="style.css" />', f"<style>\n{css}\n</style>")
(d/"full.html").write_text(html)
PY

"${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT/Biomolecular_Design_Curriculum.pdf" \
  "file://$D/full.html" 2>/dev/null

python3 -c "
import re
d=open('$OUT/Biomolecular_Design_Curriculum.pdf','rb').read()
print('pages:', len(re.findall(rb'/Type\s*/Page[^s]', d)))
"
ls -lh "$OUT/Biomolecular_Design_Curriculum.pdf"
