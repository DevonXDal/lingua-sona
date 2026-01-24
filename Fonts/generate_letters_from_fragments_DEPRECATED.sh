#!/usr/bin/env bash

mkdir -p Letters

for c in Glyphs/Fragment/Consonants/*.png; do
  cname=$(basename "$c" .png)

  for v in Glyphs/Fragment/Vowels/*.png; do
    vname=$(basename "$v" .png)

    convert "$c" "$v" -compose over -composite "Letters/${cname//C_NEGATION/-}${vname//V_NEGATION/-}.png"
  done
done

