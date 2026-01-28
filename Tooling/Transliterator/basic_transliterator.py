import tkinter as tk
from tkinter import ttk
from tkinter import font
import pyperclip

# Unicode starting points
LETTER_UNICODE_START = 0xE000
NUMBER_UNICODE_START = 0xE300

# Mapping data from Lingua Sona core tables 
CORE_CV = [
    # P
    "PA","PE","PI","PO","PU","PAH","PON","POOO",
    # B
    "BA","BE","BI","BO","BU","BAH","BON","BOOO",
    # T
    "TA","TE","TI","TO","TU","TAH","TON","TOOO",
    # D
    "DA","DE","DI","DO","DU","DAH","DON","DOOO",
    # K
    "KA","KE","KI","KO","KU","KAH","KON","KOOO",
    # G
    "GA","GE","GI","GO","GU","GAH","GON","GOOO",
    # M
    "MA","ME","MI","MO","MU","MAH","MON","MOOO",
    # N
    "NA","NE","NI","NO","NU","NAH","NON","NOOO",
    # F
    "FA","FE","FI","FO","FU","FAH","FON","FOOO",
    # V
    "VA","VE","VI","VO","VU","VAH","VON","VOOO",
    # S
    "SA","SE","SI","SO","SU","SAH","SON","SOOO",
    # SH
    "SHA","SHE","SHI","SHO","SHU","SHAH","SHON","SHOOO",
    # L
    "LA","LE","LI","LO","LU","LAH","LON","LOOO",
    # W
    "WA","WE","WI","WO","WU","WAH","WON","WOOO",
    # Y (formerly J in Latin sense)
    "YA","YE","YI","YO","YU","YAH","YON","YOOO",
    # H
    "HA","HE","HI","HO","HU","HAH","HON","HOOO",
    # CH
    "CHA","CHE","CHI","CHO","CHU","CHAH","CHON","CHOOO",
]

V_INITIAL = [
    "-A","-E","-I","-O","-U","-AH","-ON","-OOO"
]

C_FINAL = [
    "P-","B-","T-","D-","K-","G-",
    "M-","N-",
    "F-","V-","S-","SH-",
    "L-","W-","Y-","H-","CH-"
]

CVV = [
    # P
    "PAI","PEI","POI","PAU","POU",
    # B
    "BAI","BEI","BOI","BAU","BOU",
    # T
    "TAI","TEI","TOI","TAU","TOU",
    # D
    "DAI","DEI","DOI","DAU","DOU",
    # K
    "KAI","KEI","KOI","KAU","KOU",
    # G
    "GAI","GEI","GOI","GAU","GOU",
    # M
    "MAI","MEI","MOI","MAU","MOU",
    # N
    "NAI","NEI","NOI","NAU","NOU",
    # F
    "FAI","FEI","FOI","FAU","FOU",
    # V
    "VAI","VEI","VOI","VAU","VOU",
    # S
    "SAI","SEI","SOI","SAU","SOU",
    # SH
    "SHAI","SHEI","SHOI","SHAU","SHOU",
    # L
    "LAI","LEI","LOI","LAU","LOU",
    # W
    "WAI","WEI","WOI","WAU","WOU",
    # Y
    "YAI","YEI","YOI","YAU","YOU",
    # H
    "HAI","HEI","HOI","HAU","HOU",
    # CH
    "CHAI","CHEI","CHOI","CHAU","CHOU"
]

VV_INITIAL = ["-AI","-EI","-OI","-AU","-OU"]

NONCORE_CV = [
    # Z (meta / classifier)
    "ZA","ZE","ZI","ZO","ZU","ZAH","ZON","ZOOO",
    # R
    "RA","RE","RI","RO","RU","RAH","RON","ROOO",
    # J (affricate)
    "JA","JE","JI","JO","JU","JAH","JON","JOOO",
    # TH
    "THA","THE","THI","THO","THU","THAH","THON","THOOO",
]

NONCORE_CVV = [
    # Z
    "ZAI","ZEI","ZOI","ZAU","ZOU",
    # R
    "RAI","REI","ROI","RAU","ROU",
    # J
    "JAI","JEI","JOI","JAU","JOU",
    # TH
    "THAI","THEI","THOI","THAU","THOU",
]

NONCORE_FINAL = ["Z-","R-","J-","TH-"]

def build_latin_to_unicode():
    mapping = {}
    cp = LETTER_UNICODE_START

    ordered_symbols = (
        CORE_CV
        + V_INITIAL
        + C_FINAL
        + CVV
        + VV_INITIAL
        + NONCORE_CV
        + NONCORE_CVV
        + NONCORE_FINAL
    )

    for sym in ordered_symbols:
        if sym in mapping:
            raise ValueError(f"Duplicate symbol in glyph order: {sym}")
        mapping[sym] = chr(cp)
        cp += 1

    return mapping

LATIN_TO_UNICODE = build_latin_to_unicode()

# Numbers block is separate and explicit
LATIN_TO_UNICODE["0"]   = chr(NUMBER_UNICODE_START)       # E300
LATIN_TO_UNICODE["000"] = chr(NUMBER_UNICODE_START + 1)   # E301

for i, d in enumerate("123456789", start=2):
    LATIN_TO_UNICODE[d] = chr(NUMBER_UNICODE_START + i)

HEX_DIGITS = ["HEX_A","HEX_B","HEX_C","HEX_D","HEX_E","HEX_F"]
for i, h in enumerate(HEX_DIGITS, start=11):
    LATIN_TO_UNICODE[h] = chr(NUMBER_UNICODE_START + i)

# Invert mapping for reverse transliteration
UNICODE_TO_LATIN = {v: k for k, v in LATIN_TO_UNICODE.items()}

SORTED_SYMBOLS = sorted(
    LATIN_TO_UNICODE.keys(),
    key=len,
    reverse=True
)


# --- GUI App ---
class LinguaSonaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lingua Sona Latin<->Glyph Converter")

        self.preferred_fonts = ["LinguaSona Sans", "Noto Sans", "Liberation Sans", "Arial", "sans-serif"]
        self.available_fonts = font.families()

        for pf in self.preferred_fonts:
            if pf in self.available_fonts:
                self.active_font = pf
                break
        else:
            self.active_font = "sans-serif"

        self.input_label = ttk.Label(root, text="Input (Latin or Glyphs):")
        self.input_label.pack(pady=2)

        self.input_text = tk.Text(root, height=5, font=(self.active_font, 16))
        self.input_text.pack(fill='x', padx=10)
        self.input_text.bind("<KeyRelease>", self.update_output)

        self.output_label = ttk.Label(root, text="Output:")
        self.output_label.pack(pady=2)

        self.output_text = tk.Text(root, height=5, font=(self.active_font, 16), state='disabled')
        self.output_text.pack(fill='x', padx=10)

        self.copy_button = ttk.Button(root, text="Copy Output", command=self.copy_output)
        self.copy_button.pack(pady=5)

    def is_glyph_text(self, s):
        return any(0xE000 <= ord(c) <= 0xF8FF for c in s)


    def update_output(self, event=None):
        raw = self.input_text.get("1.0", tk.END).strip()
        if not raw:
            self.set_output("")
            return

        if self.is_glyph_text(raw):
            out = self.transliterate_unicode_to_latin(raw)
        else:
            out = self.transliterate_latin_to_unicode(raw)

        self.set_output(out)

    def transliterate_latin_to_unicode(self, text):
        tokens = text.upper().split()
        out = []

        for token in tokens:
            i = 0
            glyphs = []
            token_len = len(token)

            while i < token_len:
                matched = False

                for sym in SORTED_SYMBOLS:
                    if token.startswith(sym, i):
                        glyphs.append(LATIN_TO_UNICODE[sym])
                        i += len(sym)
                        matched = True
                        break

                if not matched:
                    # --- graceful recovery ---
                    # mark unknown char, advance ONE position only
                    glyphs.append("[?]")   # replacement char
                    i += 1

            out.append(''.join(glyphs))

        return ' '.join(out)



    def transliterate_unicode_to_latin(self, text):
        return ' '.join(UNICODE_TO_LATIN.get(ch, f"[{ch}]") for ch in text)

    def set_output(self, text):
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state='disabled')

    def copy_output(self):
        pyperclip.copy(self.output_text.get("1.0", tk.END).strip())


if __name__ == '__main__':
    root = tk.Tk()
    app = LinguaSonaApp(root)
    root.mainloop()

