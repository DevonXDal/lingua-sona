#!/bin/bash
# Run all font styles through FontForge's script
# === GENERATED WITH CHATGPT TO HASTEN THE PROCESS - IN ADDITION TO ITS PYTHON FILE ===

# Styles to build
STYLES=("Thin" "Regular" "Bold" "ItalicThin" "ItalicRegular" "ItalicBold")
PUA_START="E300"
OUTPUT_DIR="Fonts"

mkdir -p "$OUTPUT_DIR"

# LETTERS
for style in "${STYLES[@]}"; do
  echo "⏳ Building LinguaSona-$style ..."
  fontforge -lang=py -script build_font.py \
    "LinguaSona" "$style" "Glyphs/Letters/$style" "$OUTPUT_DIR" "$PUA_START"
done

# NUMBERS
for style in "${STYLES[@]}"; do
  if [ -d "Glyphs/Numbers/$style" ]; then
    echo "⏳ Building LinguaSonaNumbers-$style ..."
    fontforge -lang=py -script build_font.py \
      "LinguaSonaNumbers" "$style" "Glyphs/Numbers/$style" "$OUTPUT_DIR" "$PUA_START"
  fi
done

echo "🎉 All fonts built."

