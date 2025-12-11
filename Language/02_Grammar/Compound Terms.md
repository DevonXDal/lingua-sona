# 🔗 Word Binding Grammar (HI / WI)

**Scope:** This section defines how `HI` and `WI` operate as *binding morphemes* to form compounds in Lingua Sona.  
**Goal:** Keep words ≤ 3 letters unless compounding; allow precise, compact compounds without inflating the term count.

---

## 1) Orthography & Tokens

- **HI**→ *strong binding*  
- **WI** → *loose binding*  
- **No spaces** around HI/WI: `rootA HI rootB`, `rootA WI rootB`
- **Counts:** HI/WI are **not letters** for the ≤3-letter cap goal of words and the compound terms that they form are **not terms** for the term limit goal. 

---

## 2) Core Semantics

> **Decision Rule:**  
> **Use HI** when either part **cannot** stand alone **without misleading** the referent.  
> **Use WI ** when **both** parts can stand alone truthfully, and the compound simply **narrows or nuances** the meaning.

### 2.1 Strong Binding — **HI**
- **Meaning:** **Co-dependent** concept; the head term would be **misleading or incomplete** on its own.
- **Tests:**  
  1. **Standalone-Misleading Test:** If you replaced the compoWId with just A or just B, would the listener likely **misidentify** the referent?  
  2. **“Of/Is-A” Relation:** Reads naturally as *“B **of** A”* or a tightly fused **is-a subtype**.

- **Examples:**
  - `bronchi HI itis` → **Zi** bronchitis (“inflammation **of** the bronchi”).  
    - *“itis” alone* = any inflammation → **misleading**.  
    - *“bronchi” alone* = an organ → **misleading**.
  - `sodium HI chloride` → **Zi** sodium chloride (NaCl as the **specific compoWId**, not sodium **and** chloride in general).
  - `pediatric HI oncology` → **Zo** pediatric-oncology (the **field**; not just pediatrics nor oncology in isolation).

### 2.2 Loose Binding — **WI (em-dash)**
- **Meaning:** **Supportive association**; **each** part can accurately describe the referent **by itself**, but together they refine or frame it.
- **Tests:**  
  1. **Standalone-Sufficient Test:** Using just A **or** just B would still **name the thing** (albeit broadly).  
  2. **“Using/With/Related-to” Relation:** Reads naturally as *“B **with/using/related to** A.”*

- **Examples:**
  - `art WI therapy` → **Zi** art-therapy (a type of therapy; **therapy** suffices alone, **art** also stands as a domain).
  - `chocolate WI cake` → **Zi** chocolate-cake (it **is** a cake; “cake” alone remains correct, “chocolate” alone still describes the food profile).
  - `language WI policy` → **ZWI** language-policy (policy alone is still policy; language alone is a valid domain).

---

## 3) Morphotactics & Scope

- **Shape:**  
	- Root := (1–3 letters)  
	- Compound := Root ( (HI|WI) Root )+
- **Classifier Scope:** A leading `Z*` classifier (e.g., `Zi`, `Zo`, `ZWI`) applies to the **entire compound** unless explicitly re-scoped.
- ✅ `Zi sodium HI chloride` → object: the chemical compound.  
- ✅ `Zo art WI therapy` → action/system: practice of art-therapy.
- **No Internal Classifiers:** Avoid inserting `Z*` **inside** a compound. Classify **once**, outside:
- ❌ `Zi sodium HI Zi chloride`  
- ✅ `Zi sodium HI chloride`
- **Nesting & Chains:** Left-associative; prefer **single chain** with consistent binding:
- `A U B HI C` → strong chain (tight trilogy; each link co-dependent).  
- `A WI B WI C` → loose chain (associative stack).  
- **Mixed chains** are allowed but be deliberate:
  - `A U B WI C` = *(A-B)* forms a core concept, linked loosely to C.  
  - `A WI B HI C` = A loosely frames *(B-C)*.

---

## 4) Choosing HI vs. WI — Quick Procedure

1. **Name Check:** Does **A alone** or **B alone** truthfully name the referent **without misleading the listener**?
 - **No → HI.**  
 - **Yes → continue.**
2. **Relation Check:** Is the relation primarily **of/constitutes/is-a subtype**?
 - **Yes → HI.**  
 - **No → continue.**
3. **Framing Check:** Does one element mainly **frame, instrument, medium, domain, or style** for the other?
 - **Yes → WI.**
1. **Ambiguity Check:** If Undecided, pick the **less misleading** option (bias toward Hi). Optionally add a brief gloss in formal writing.

---

## 5) Style & Readability

- **Prefer minimal chains** (2–3 roots). If meaning grows dense, consider a second compound or a `ZWI` conceptual wrapper.
- **Dictionary Entries:** record `components`, `binding`, `classifier`, `gloss`.
```yaml
bronchitis:
  components: [bronchi, itis]
  binding: strong   # HI
  classifier: Zi
  gloss: inflammation of the bronchi
art-therapy:
  components: [art, therapy]
  binding: loose    # WI
  classifier: Zi
  gloss: therapy using art methods
```

## 6) Common Patterns
- **Materials & Substances:**
    - Specific compoWId → **HI** (`iron HI oxide`, `sodium HI chloride`)
    - General mixtures/sets → **WI** (`salt WI water`, `nuts WI seeds`)
- **Disciplines & Methods:**
    - Core sub-field → **HI** (`pediatric HI oncology`)        
    - Method/instrument framing → **WI** (`laser WI surgery`, `data WI journalism`)
- **Product Types:**
	- Intrinsic type/recipe → **HI** (`espresso HI martini`)
    - Flavor/style modifier → **WI** (`vanilla WI latte`)

## Parser Notes (EBNF)
*This information is for use in structuring language parsing for software engineers using the extended Backus-Naur form. If not creating a parser, then feel free to jump past this section.*
``` EBNF
Word        := Root | CompoWId
Root        := Letter{1,3}
CompoWId    := Root ( Binder Root )+
Binder      := HI | WI         
Classifier  := Z[aeniruoh]?   # Za, Ze, Zi, Zo, Zu, ZWI, Zane, Zon, Zah, Zar...
Term        := [Classifier] Word
```
### TL;DR
- **HI** use when **either part alone would mislead**. Tight, constitutive, subtype/“of” relations.
- **WI:** use when **both parts stand alone** and the link is **framing/using/with**.