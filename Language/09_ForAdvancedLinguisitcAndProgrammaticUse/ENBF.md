############################################################
# LINGUA SONA – FORMAL GRAMMAR (EBNF SPECIFICATION v1.0)
# Authors: Devon X. Dalrymple & Mira (Custom ChatGPT Instance v4o & v5.1)
############################################################


############################################################
# 1. PHONOLOGY – LETTER SYSTEM
############################################################

LETTER = CV | CVV | "¬" V | C "¬" | "¬" VV ;

CV      = C V ;
CVV     = C VV ;

C       = "P" | "T" | "K" | "M" | "N" | "F" | "S" | "SH" | "L" | 
          "W" | "Y" | "H" | "G" | "CH" | "Z" | "B" | "D" ;

V       = "A" | "E" | "I" | "O" | "U" | "AH" | "ON" | "OOO" ;

VV      = "AI" | "EI" | "OI" | "AU" | "OU" ;


############################################################
# 2. MORPHOLOGY – ROOTS, COMPOUNDS, TERMS
############################################################

ROOT = LETTER , LETTER? , LETTER? ;

BINDER = "HI" | "WI" ;

COMPOUND = ROOT , { BINDER , ROOT } ;

WORD = ROOT | COMPOUND ;


############################################################
# 3. CLASSIFIERS (PREFIXES)
############################################################

CLASSIFIER =
      "Za"    |   # person / actor
      "Ze"    |   # place
      "Zi"    |   # object
      "Zo"    |   # action/verb stem
      "Zu"    |   # adjective/quality
      "Zooo"  |   # concept/idea
      "Zaw"   |   # time/temporal
      "Zoi"   |   # collective/group
      "Zon"   |   # meta/word-as-word
      "Z¬"        # negation/null-classifier
;

TERM = [CLASSIFIER] , WORD ;


############################################################
# 4. NUMBERS – FULL SYSTEM
############################################################

# 4.1 Digits (0–10)
DIGIT =
      "HO" | "UN" | "TU" | "TI" | "KO" |
      "FI" | "SE" | "SAI" | "WO" | "NU" | "TE"
;

# 4.2 Tens (multiplicative)
TENS = DIGIT , "_TE" ;

# 4.3 Hundreds
HUNDREDS = DIGIT , "_HE" ;

# 4.4 Thousand packets (10^3)
THOUSAND_PACKET = "HOOO" ;

# 4.5 Magnitudes (million, billion…)
MAGNITUDE = DIGIT , "_HI_" , THOUSAND_PACKET ;

# 4.6 Chunk (hundreds, tens, units)
CHUNK =
      [ DIGIT , "_HE" ] ,
      [ "WI" , DIGIT , "_TE" ] ,
      [ "WI" , DIGIT ]
;

# 4.7 Full number
NUMBER =
      [ "Z¬" ] ,
      { CHUNK , MAGNITUDE } ,
      CHUNK
;

# 4.8 Decimals
DECIMAL = NUMBER , "¬E" , NUMBER ;

# 4.9 Fractions
FRACTION = NUMBER , "PO" , NUMBER ;

# 4.10 Ordinals
ORDINAL = "ZU" , NUMBER ;


############################################################
# 5. PHRASES
############################################################

NOUN_PHRASE = TERM ;

OBJECT_PHRASE = NOUN_PHRASE ;

ADVERBIAL_PHRASE =
      TERM
    | NUMBER
    | DECIMAL
    | FRACTION
;

VERB_PHRASE =
      "Zo" , WORD ,
      [ OBJECT_PHRASE ] ,
      [ ADVERBIAL_PHRASE ]
;


############################################################
# 6. EVIDENTIALITY (MANDATORY IN STATEMENTS)
############################################################

EVIDENTIAL =
      [ "Z¬" ] ,      # negated = opinion / belief / common sense
      EVID_WORD ,
      SOURCE?
;

EVID_WORD = WORD ;   # you define FOH/MEH/TIH/etc. in lexicon

SOURCE = TERM | NUMBER | WORD ;


############################################################
# 7. SENTENCES (SVO ORDER)
############################################################

SENTENCE =
      NOUN_PHRASE ,
      VERB_PHRASE ,
      EVIDENTIAL
;

############################################################
# 8. QUESTIONS (USING KOI)
############################################################

# KOI follows the entire statement.
QUESTION =
      SENTENCE ,
      "KOI"
;


############################################################
# 9. SIMPLE RESPONSES
############################################################

RESPONSE = WORD | DIGIT | "UN" | "HO" | "WO" ;


############################################################
# 10. TOP-LEVEL UTTERANCE
############################################################

UTTERANCE =
      SENTENCE
    | QUESTION
    | RESPONSE
;
