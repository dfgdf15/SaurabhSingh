#!/bin/bash
# Regenerate all 4 dossier PDFs (Dark/Sakura x A4/Letter) per PRD recipe.
set -e
TMP=/tmp/pdfgen; mkdir -p $TMP; OUT=/app/frontend/public
COMPACT='<style>@media print{tbody td{padding:6.5px 10px !important}.seclabel{margin:12px 0 6px !important}.hero{padding:18px 20px 16px !important}}</style>'

gen() { # $1 src html  $2 base name
  # A4
  sed '/@import/d' "$1" > $TMP/a4.html
  google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$OUT/$2.pdf" "file://$TMP/a4.html" 2>/dev/null
  # Letter
  sed -e '/@import/d' -e 's/size:A4/size:Letter/' "$1" > $TMP/lt.html
  printf '%s' "$COMPACT" >> $TMP/lt.html
  google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$OUT/$2-Letter.pdf" "file://$TMP/lt.html" 2>/dev/null
}

gen /app/saurabh-master-chart.html        SAURABH-Master-Chart-Dark
gen /app/saurabh-master-chart-sakura.html SAURABH-Master-Chart-Sakura

python - <<'EOF'
import fitz
for f in ["Dark","Dark-Letter","Sakura","Sakura-Letter"]:
    p="/app/frontend/public/SAURABH-Master-Chart-%s.pdf"%f
    d=fitz.open(p); print(f, "->", d.page_count, "pages,", round(len(open(p,'rb').read())/1024), "KB")
EOF
