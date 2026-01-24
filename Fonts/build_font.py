import fontforge
import sys, os

BASE_FONT     = sys.argv[1]
FONT_NAME     = sys.argv[2]
STYLE_NAME    = sys.argv[3]
LETTER_DIR    = sys.argv[4]
NUMBER_DIR    = sys.argv[5]
OUTPUT_DIR    = sys.argv[6]

LETTER_START  = 0xE000
NUMBER_START  = 0xE300

font = fontforge.open(BASE_FONT)

font.fontname   = FONT_NAME.replace(" ", "")
font.familyname = FONT_NAME
font.fullname   = f"{FONT_NAME} {STYLE_NAME}"

font.em     = 1024
font.ascent = 800
font.descent = 224

CORE_CV = [
    # P
    "PA","PE","PI","PO","PU","PAH","PON","POOO",
    # T
    "TA","TE","TI","TO","TU","TAH","TON","TOOO",
    # K
    "KA","KE","KI","KO","KU","KAH","KON","KOOO",
    # M
    "MA","ME","MI","MO","MU","MAH","MON","MOOO",
    # N
    "NA","NE","NI","NO","NU","NAH","NON","NOOO",
    # F
    "FA","FE","FI","FO","FU","FAH","FON","FOOO",
    # S
    "SA","SE","SI","SO","SU","SAH","SON","SOOO",
    # SH
    "SHA","SHE","SHI","SHO","SHU","SHAH","SHON","SHOOO",
    # L
    "LA","LE","LI","LO","LU","LAH","LON","LOOO",
    # W
    "WA","WE","WI","WO","WU","WAH","WON","WOOO",
    # J
    "JA","JE","JI","JO","JU","JAH","JON","JOOO",
    # H
    "HA","HE","HI","HO","HU","HAH","HON","HOOO",
    # G
    "GA","GE","GI","GO","GU","GAH","GON","GOOO",
    # CH
    "CHA","CHE","CHI","CHO","CHU","CHAH","CHON","CHOOO",
]

V_INITIAL = [
    "-A","-E","-I","-O","-U","-AH","-ON","-OOO"
]

C_FINAL = [
    "P-","T-","K-","M-","N-","F-","S-","SH-",
    "L-","W-","J-","H-","G-","CH-"
]

CVV = [
    # P
    "PAI","PEI","POI","PAU","POU",
    # T
    "TAI","TEI","TOI","TAU","TOU",
    # K
    "KAI","KEI","KOI","KAU","KOU",
    # M
    "MAI","MEI","MOI","MAU","MOU",
    # N
    "NAI","NEI","NOI","NAU","NOU",
    # F
    "FAI","FEI","FOI","FAU","FOU",
    # S
    "SAI","SEI","SOI","SAU","SOU",
    # SH
    "SHAI","SHEI","SHOI","SHAU","SHOU",
    # L
    "LAI","LEI","LOI","LAU","LOU",
    # W
    "WAI","WEI","WOI","WAU","WOU",
    # J
    "JAI","JEI","JOI","JAU","JOU",
    # H
    "HAI","HEI","HOI","HAU","HOU",
    # G
    "GAI","GEI","GOI","GAU","GOU",
    # CH
    "CHAI","CHEI","CHOI","CHAU","CHOU"
]

VV_INITIAL = ["-AI","-EI","-OI","-AU","-OU"]

NONCORE_CV = [
    "ZA","ZE","ZI","ZO","ZU","ZAH","ZON","ZOOO",
    "BA","BE","BI","BO","BU","BAH","BON","BOOO",
    "DA","DE","DI","DO","DU","DAH","DON","DOOO",
]

NONCORE_CVV = [
    "ZAI","ZEI","ZOI","ZAU","ZOU",
    "BAI","BEI","BOI","BAU","BOU",
    "DAI","DEI","DOI","DAU","DOU",
]

NONCORE_FINAL = ["Z-","B-","D-"]

NUMBERS=["0", "000", "1", "2", "3", "4", "5", "6", "7", "8", "9", "HEX_A", "HEX_B", "HEX_C", "HEX_D", "HEX_E", "HEX_F"]

GlyphOrderLetters = (
    CORE_CV
    + V_INITIAL
    + C_FINAL
    + CVV
    + VV_INITIAL
    + NONCORE_CV
    + NONCORE_CVV
    + NONCORE_FINAL
)

def import_glyphs(directory, start_codepoint, numbers_are_used):
    codepoint = start_codepoint
    setToUse = GlyphOrderLetters
    if numbers_are_used:
        setToUse = NUMBERS
    if not os.path.exists(directory):
        print(f"⚠ Skipping missing folder: {directory}")
        return
    for name in setToUse:
        svg = f"{name}.svg"
        g = font.createChar(codepoint, name)
        g.importOutlines(os.path.join(directory, svg))
        g.correctDirection()
        g.removeOverlap()
        g.simplify()
        g.left_side_bearing  = 100
        g.right_side_bearing = 100
        g.width = 1024
        codepoint += 1

# Import both sets
import_glyphs(LETTER_DIR, LETTER_START, False)
import_glyphs(NUMBER_DIR, NUMBER_START, True)

# Metadata
font.copyright = "Copyright © Lingua Sona Project"
font.appendSFNTName("English (US)", "License", "SIL Open Font License 1.1")
font.appendSFNTName("English (US)", "Designer", "Devon X. Dalrymple et al.")

os.makedirs(OUTPUT_DIR, exist_ok=True)
base = os.path.join(OUTPUT_DIR, f"{FONT_NAME}-{STYLE_NAME}")
font.generate(f"{base}.ttf")
font.generate(f"{base}.otf")
font.generate(f"{base}.woff")
font.generate(f"{base}.woff2")
font.close()

print(f"✔ Final merged font built: {FONT_NAME}-{STYLE_NAME}")

