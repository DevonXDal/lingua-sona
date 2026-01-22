import fontforge
import sys
import os

# ---------------- CONFIG ----------------
FONT_NAME   = sys.argv[1]
STYLE_NAME  = sys.argv[2]
SVG_DIR     = sys.argv[3]
OUTPUT_DIR  = sys.argv[4]
PUA_START   = int(sys.argv[5], 16)  # e.g. E300

EM_SIZE     = 1024
ASCENT      = 800
DESCENT     = 224

# ----------------------------------------

font = fontforge.font()
font.fontname   = FONT_NAME.replace(" ", "")
font.familyname = FONT_NAME
font.fullname   = f"{FONT_NAME} {STYLE_NAME}"

font.em = EM_SIZE
font.ascent = ASCENT
font.descent = DESCENT

font.encoding = "UnicodeFull"

codepoint = PUA_START

svgs = sorted(f for f in os.listdir(SVG_DIR) if f.lower().endswith(".svg"))

for svg in svgs:
    glyph_name = os.path.splitext(svg)[0]
    g = font.createChar(codepoint, glyph_name)

    g.importOutlines(os.path.join(SVG_DIR, svg))
    g.correctDirection()
    g.removeOverlap()
    g.simplify()
    g.left_side_bearing  = 100
    g.right_side_bearing = 100
    g.width = 1024

    codepoint += 1

# ---- Metadata ----
font.copyright = "Copyright © Lingua Sona Project"
font.appendSFNTName("English (US)", "License", "SIL Open Font License 1.1")
font.appendSFNTName("English (US)", "License URL", "https://openfontlicense.org")
font.appendSFNTName("English (US)", "Designer", "Devon X. Dalrymple et al.")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---- Export ----
font.generate(os.path.join(OUTPUT_DIR, f"{FONT_NAME}-{STYLE_NAME}.ttf"))
font.generate(os.path.join(OUTPUT_DIR, f"{FONT_NAME}-{STYLE_NAME}.otf"))
font.generate(os.path.join(OUTPUT_DIR, f"{FONT_NAME}-{STYLE_NAME}.woff"))
font.generate(os.path.join(OUTPUT_DIR, f"{FONT_NAME}-{STYLE_NAME}.woff2"))

font.close()
print(f"✔ Built {FONT_NAME}-{STYLE_NAME}")

