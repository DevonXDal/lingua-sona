#!/usr/bin/env bash
set -e

SVG="./Glyphs/InkscapeProject.svg"

OUT_CON="./Glyphs/Fragments/Consonants"
OUT_VOW="./Glyphs/Fragments/Vowels"
OUT_NUM="./Glyphs/Fragments/Numbers"

mkdir -p "$OUT_CON" "$OUT_VOW" "$OUT_NUM"

# -------------------------------
# Helper: export a list of IDs
# -------------------------------
export_ids () {
  local TARGET_DIR="$1"
  shift
  for id in "$@"; do
    inkscape "$SVG" \
      --export-id="$id" \
      --export-id-only \
      --export-filename="$TARGET_DIR/$id.svg"
  done
}

# -------------------------------
# Consonants
# -------------------------------
CONSONANTS=(
  B CH D F G H J K L M N P S SH T W Z
)

export_ids "$OUT_CON" "${CONSONANTS[@]}"

# -------------------------------
# Vowels & clusters
# -------------------------------
VOWELS=(
  A AHW AI AU
  E EI
  I
  O OI ON OOO OU
  U
)

export_ids "$OUT_VOW" "${VOWELS[@]}"

# -------------------------------
# Numbers / Hex
# -------------------------------
NUMBERS=(
  0 1 2 3 4 5 6 7 8 9
  HEX_A HEX_B HEX_C HEX_D HEX_E HEX_F
  000
)

export_ids "$OUT_NUM" "${NUMBERS[@]}"

echo "✔ All Lingua Sona fragments exported as SVG."

