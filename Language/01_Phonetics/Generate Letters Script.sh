#!/usr/bin/env bash

mkdir -p Letters

for c in Glyphs/Consonants/*.png; do
  cname=$(basename "$c" .png)

  for v in Glyphs/VowelsAndClusters/*.png; do
    vname=$(basename "$v" .png)

    convert "$c" "$v" -compose over -composite "Letters/${cname}-${vname}.png"
  done
done

