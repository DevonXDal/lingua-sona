# 🔗 Dash Binding Grammar (U / UN)

**Scope:** This section defines how **U** (en-dash) and **UN** (em-dash) operate as *binding morphemes* to form compounds in Lingua Sona.  
**Goal:** Keep words ≤ 3 letters unless compounding; allow precise, compact compounds without inflating the term count.

---

## 1) Orthography & Tokens

- **U** = **en-dash** → *strong binding*  
- **UN** = **em-dash** → *loose binding*  
- **No spaces** around U/UN: `rootA U rootB`, `rootA UN rootB`
- **Counts:** U/UN are **not letters** for the ≤3-letter cap goal of words and the compound terms that they form are **not terms** for the term limit goal. 
- **PUA Forms:** When used purely as binders, prefer the dash glyphs **U / UN**.  
  - Acceptable but **less preferred**: the explicit vowel forms `¬u` and `¬un` (for manuscripts or when disambiguation is needed).

---

## 2) Core Semantics

> **Decision Rule:**  
> **Use U (en-dash)** when either part **cannot** stand alone **without misleading** the referent.  
> **Use UN (em-dash)** when **both** parts can stand alone truthfully, and the compound simply **narrows or nuances** the meaning.

### 2.1 Strong Binding — **U (en-dash)**
- **Meaning:** **Co-dependent** concept; the head term would be **misleading or incomplete** on its own.
- **Tests:**  
  1. **Standalone-Misleading Test:** If you replaced the compound with just A or just B, would the listener likely **misidentify** the referent?  
  2. **“Of/Is-A” Relation:** Reads naturally as *“B **of** A”* or a tightly fused **is-a subtype**.

- **Examples:**
  - `bronchi U itis` → **Zi** bronchitis (“inflammation **of** the bronchi”).  
    - *“itis” alone* = any inflammation → **misleading**.  
    - *“bronchi” alone* = an organ → **misleading**.
  - `sodium U chloride` → **Zi** sodium chloride (NaCl as the **specific compound**, not sodium **and** chloride in general).
  - `pediatric U oncology` → **Zo** pediatric-oncology (the **field**; not just pediatrics nor oncology in isolation).

### 2.2 Loose Binding — **UN (em-dash)**
- **Meaning:** **Supportive association**; **each** part can accurately describe the referent **by itself**, but together they refine or frame it.
- **Tests:**  
  1. **Standalone-Sufficient Test:** Using just A **or** just B would still **name the thing** (albeit broadly).  
  2. **“Using/With/Related-to” Relation:** Reads naturally as *“B **with/using/related to** A.”*

- **Examples:**
  - `art UN therapy` → **Zi** art-therapy (a type of therapy; **therapy** suffices alone, **art** also stands as a domain).
  - `chocolate UN cake` → **Zi** chocolate-cake (it **is** a cake; “cake” alone remains correct, “chocolate” alone still describes the food profile).
  - `language UN policy` → **Zun** language-policy (policy alone is still policy; language alone is a valid domain).

---

## 3) Morphotactics & Scope

- **Shape:**  
	- Root := (1–3 letters)  
	- Compound := Root ( (U|UN) Root )+
- **Classifier Scope:** A leading `Z*` classifier (e.g., `Zi`, `Zo`, `Zun`) applies to the **entire compound** unless explicitly re-scoped.
- ✅ `Zi sodium U chloride` → object: the chemical compound.  
- ✅ `Zo art UN therapy` → action/system: practice of art-therapy.
- **No Internal Classifiers:** Avoid inserting `Z*` **inside** a compound. Classify **once**, outside:
- ❌ `Zi sodium U Zi chloride`  
- ✅ `Zi sodium U chloride`
- **Nesting & Chains:** Left-associative; prefer **single chain** with consistent binding:
- `A U B U C` → strong chain (tight trilogy; each link co-dependent).  
- `A UN B UN C` → loose chain (associative stack).  
- **Mixed chains** are allowed but be deliberate:
  - `A U B UN C` = *(A-B)* forms a core concept, linked loosely to C.  
  - `A UN B U C` = A loosely frames *(B-C)*.

---

## 4) Choosing U vs. UN — Quick Procedure

1. **Name Check:** Does **A alone** or **B alone** truthfully name the referent **without misleading the listener**?
 - **No → U.**  
 - **Yes → continue.**
2. **Relation Check:** Is the relation primarily **of/constitutes/is-a subtype**?
 - **Yes → U.**  
 - **No → continue.**
3. **Framing Check:** Does one element mainly **frame, instrument, medium, domain, or style** for the other?
 - **Yes → UN.**
4. **Ambiguity Check:** If undecided, pick the **less misleading** option (bias toward **U**). Optionally add a brief gloss in formal writing.

---

## 5) Style & Readability

- **Prefer minimal chains** (2–3 roots). If meaning grows dense, consider a second compound or a `Zun` conceptual wrapper.
- **Dictionary Entries:** record `components`, `binding`, `classifier`, `gloss`.
```yaml
bronchitis:
  components: [bronchi, itis]
  binding: strong   # U
  classifier: Zi
  gloss: inflammation of the bronchi
art-therapy:
  components: [art, therapy]
  binding: loose    # UN
  classifier: Zi
  gloss: therapy using art methods
```

## 6) Common Patterns
- **Materials & Substances:**
    - Specific compound → **U** (`iron U oxide`, `sodium U chloride`)
    - General mixtures/sets → **UN** (`salt UN water`, `nuts UN seeds`)
- **Disciplines & Methods:**
    - Core sub-field → **U** (`pediatric U oncology`)        
    - Method/instrument framing → **UN** (`laser UN surgery`, `data UN journalism`)
- **Product Types:**
	- Intrinsic type/recipe → **U** (`espresso U martini`)
    - Flavor/style modifier → **UN** (`vanilla UN latte`)

## Parser Notes (EBNF)
*This information is for use in structuring language parsing for software engineers using the extended Backus-Naur form. If not creating a parser, then feel free to jump past this section.*
``` EBNF
Word        := Root | Compound
Root        := Letter{1,3}
Compound    := Root ( Binder Root )+
Binder      := U | UN         # dash tokens
Classifier  := Z[aeniruoh]?   # Za, Ze, Zi, Zo, Zu, Zun, Zane, Zon, Zah, Zar...
Term        := [Classifier] Word
```
### TL;DR
- **U (en-dash):** use when **either part alone would mislead**. Tight, constitutive, subtype/“of” relations.
- **UN (em-dash):** use when **both parts stand alone** and the link is **framing/using/with**.