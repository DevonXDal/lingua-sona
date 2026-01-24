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
    "CHAI","CHEI","CHOI","CHAU","CHOU",
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

GlyphOrderLetters = (
    CORE_CV
    + V_INITIAL
    + C_FINAL-
    + CVV
    + VV_INITIAL
    + NONCORE_CV
    + NONCORE_CVV
    + NONCORE_FINAL
)

for i in GlyphOrderLetters:
    print(f"{i} \n")


