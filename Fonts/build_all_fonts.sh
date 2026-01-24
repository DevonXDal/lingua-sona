#!/bin/bash

STYLES=("Thin" "Regular" "Bold" "ThinItalic" "RegularItalic" "BoldItalic")

for style in "${STYLES[@]}"; do
  BASE="./Base/NotoSans-$style.ttf"
  # If not using 'Italic' prefix for filename, adjust accordingly
  if [[ "$style" == *Italic ]]; then
    BASE="./Base/NotoSans-${style}.ttf"
  fi

  echo "🔧 Building $style..."
  python3 build_font.py \
    "$BASE" \
    "LinguaSona Sans" \
    "$style" \
    "Glyphs/Letters/$style" \
    "Glyphs/Numbers/$style" \
    "Final"
done

echo "✅ All fonts built and merged!"

