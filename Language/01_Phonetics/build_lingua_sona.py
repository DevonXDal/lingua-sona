# =======================================
# Builds all letters and numbers for thin, regular, and bold. It does this for their italic forms as well. Using glyphs for the consonants and vowels first.
# Not gonna lie, I took two looks at this and said "screw this, let's have ChatGPT write me this."
# =======================================
import subprocess
from pathlib import Path
import itertools
import tempfile
import shutil
import xml.etree.ElementTree as ET
import copy

# --------------------
# CONFIG
# --------------------
INKSCAPE = "inkscape"  # must be in PATH on Windows/Linux

PROJECT = Path("./Glyphs/InkscapeProject.svg")

FRAG = Path("./Glyphs/Fragments")
LETTERS = Path("./Glyphs/Letters")
NUMBERS = Path("./Glyphs/Numbers")

CANVAS_SIZE = 1024
PNG_SIZE = 512

BASE_STROKE = 5
REG_STROKE = 10     # or 15 if you prefer
BOLD_STROKE = REG_STROKE * 2
ITALIC_SHEAR = 0.212  # ~12°

CONSONANTS = ["B","CH","D","F","G","H","J","K","L","M","N","P","S","SH","T","W","Z"]
VOWELS = ["A","AH","AI","AU","E","EI","I","O","OI","ON","OOO","OU","U"]
C_NEG = "C_NEGATION"
V_NEG = "V_NEGATION"

NUMERAL_IDS = [
    "0","1","2","3","4","5","6","7","8","9",
    "HEX_A","HEX_B","HEX_C","HEX_D","HEX_E","HEX_F","000"
]

# --------------------
# UTILITIES
# --------------------
def run(cmd):
    subprocess.run(cmd, check=True)

def export_object(obj_id: str, out_svg: Path):
    run([
        INKSCAPE,
        str(PROJECT),
        "--export-area-page", # This preserves the canvas area rather than cropping
        f"--export-id={obj_id}",
        "--export-id-only",
        f"--export-filename={out_svg}"
    ])

def export_png(svg: Path, png: Path):
    run([
        INKSCAPE,
        str(svg),
        f"--export-width={PNG_SIZE}",
        f"--export-filename={png}"
    ])

def set_stroke_width(svg_root, width):
    for el in svg_root.iter():
        style = el.attrib.get("style")
        if style and "stroke-width" in style:
            parts = style.split(";")
            parts = [
                f"stroke-width:{width}px" if p.startswith("stroke-width") else p
                for p in parts
            ]
            el.attrib["style"] = ";".join(parts)

def apply_italic(svg_root):
    for el in svg_root.iter():
        if el.tag.endswith("g"):
            t = el.attrib.get("transform", "")
            el.attrib["transform"] = f"{t} skewX(12)"

def merge_svgs(left: Path, right: Path, out: Path):
    t1 = ET.parse(left)
    t2 = ET.parse(right)

    r1 = t1.getroot()
    r2 = t2.getroot()

    for child in list(r2):
        r1.append(copy.deepcopy(child))

    ET.ElementTree(r1).write(out, encoding="utf-8", xml_declaration=True)

def styled_export(src_svg: Path, dst_dir: Path, stroke, italic):
    tree = ET.parse(src_svg)
    root = tree.getroot()

    set_stroke_width(root, stroke)
    if italic:
        apply_italic(root)

    dst_svg = dst_dir / src_svg.name
    dst_png = dst_dir / (src_svg.stem + ".png")

    tree.write(dst_svg, encoding="utf-8", xml_declaration=True)
    export_png(dst_svg, dst_png)

# --------------------
# PHASE 1 — EXPORT FRAGMENTS
# --------------------
for d in ["Consonants","Vowels","Negations","Numbers"]:
    (FRAG/d).mkdir(parents=True, exist_ok=True)

for c in CONSONANTS:
    export_object(c, FRAG/"Consonants"/f"{c}.svg")

for v in VOWELS:
    export_object(v, FRAG/"Vowels"/f"{v}.svg")

export_object(C_NEG, FRAG/"Negations"/"C_NEGATION.svg")
export_object(V_NEG, FRAG/"Negations"/"V_NEGATION.svg")

for n in NUMERAL_IDS:
    export_object(n, FRAG/"Numbers"/f"{n}.svg")

# --------------------
# PHASE 2 — COMPOSITE LETTERS (THIN)
# --------------------
tmp = Path(tempfile.mkdtemp())
letters_thin = tmp / "Letters"
letters_thin.mkdir()

lefts = CONSONANTS + [C_NEG]
rights = VOWELS + [V_NEG]

for l, r in itertools.product(lefts, rights):
    if l == C_NEG and r == V_NEG:
        continue

    left_svg = (
        FRAG/"Consonants"/f"{l}.svg"
        if l != C_NEG else FRAG/"Negations"/"C_NEGATION.svg"
    )
    right_svg = (
        FRAG/"Vowels"/f"{r}.svg"
        if r != V_NEG else FRAG/"Negations"/"V_NEGATION.svg"
    )

    out = letters_thin / f"{l}-{r}.svg"
    merge_svgs(left_svg, right_svg, out)

# --------------------
# PHASE 3 — STYLE EXPORT
# --------------------
STYLES = {
    "Thin": BASE_STROKE,
    "Regular": REG_STROKE,
    "Bold": BOLD_STROKE
}

for base, target in [
    (letters_thin, LETTERS),
    (FRAG/"Numbers", NUMBERS)
]:
    for name, stroke in STYLES.items():
        for italic in (False, True):
            folder = target / (("Italic" if italic else "") + name)
            folder.mkdir(parents=True, exist_ok=True)

            for svg in base.glob("*.svg"):
                styled_export(svg, folder, stroke, italic)

shutil.rmtree(tmp)

print("✔ Lingua Sona build complete (SVG + PNG, all styles, cross‑platform).")



