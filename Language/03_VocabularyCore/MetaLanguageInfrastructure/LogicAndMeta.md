# Logic & Meta-Language Infrastructure

## Executive Summary of Terms Within

This file defines the **logical and meta-linguistic control structures** of Lingua Sona.

These terms are used to:
- Express **formal logic** (negation, conjunction, disjunction)
- Express **conditional reasoning** (if / then / else)
- Express **iteration and control flow** (for / while / until)
- Support **mathematics, proofs, algorithms, and programming-adjacent syntax**
- Enable **meta-language discussion** about rules, statements, and processes

All terms in this file are intended to be:
- **Atomic**
- **Short (1–3 letters)**
- **Classifier-neutral by default**
- **Safe for reuse in compound terms via `HI` and `WI`**

⚠️ **Note:** Translations are semantic approximations, not guarantees of cultural or contextual equivalence.

---

## Terms

### ¬IF¬ — (Sona Script)

#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-1  
**Affective Primitive Used:** None 

#### Definition
Introduces a **conditional premise**.

Evaluates a statement whose truth determines whether a consequence applies.

> If X is true, then Y applies.

#### Language Translations

| English | Spanish | French | Chinese (Simplified) | German | Japanese | Arabic (MSA) | Portuguese (Brazil) | Swahili |
|--------|---------|--------|----------------------|--------|----------|--------------|---------------------|---------|
| if | si | si | 如果 | wenn | もし | إذا | se | ikiwa |

#### With Context Classifiers

| Classifier | Combined Meaning |
|-----------|-----------------|
| Zo | to condition / to test |
| Zooo | conditional logic |
| Zon | the word itself |

---

### ¬ETO — (Sona Script)

#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-2  
**Affective Primitive Used:** None 
#### Definition
Marks the **result or consequence** of a satisfied condition.

Used only in relation to a prior conditional premise.

> IF X, THEN Y.

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| then | entonces | alors | 那么 | dann | なら | ثم | então | basi |

---

### SINAU — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-3  
**Affective Primitive Used:** None 

#### Definition
Introduces the **alternative branch** when a conditional premise is not satisfied.

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| else | si no | sinon | 否则 | sonst | それ以外 | وإلا | senão | vinginevyo |

---

### NI — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-4  
**Affective Primitive Used:** None 

#### Definition
Logical negation.

Inverts the truth value of a statement.

> NOT X → X is false.

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| not | no | ne…pas | 不 | nicht | ない | ليس | não | si |

#### With Context Classifiers

| Classifier | Combined Meaning |
|-----------|-----------------|
| Zu | negated / false |
| Zooo | negation (concept) |

---

### ¬E — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-5 
**Affective Primitive Used:** None 


#### Definition
Logical conjunction.

All linked statements must be true.

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| and | y | et | 和 | und | と | و | e | na |

---

### ¬OU — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-6
**Affective Primitive Used:** None 

#### Definition
Logical inclusive disjunction.

At least one linked statement must be true.

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| or | o | ou | 或 | oder | または | أو | ou | au |

---

### NOU — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-7
**Affective Primitive Used:** None 

#### Definition
Logical **exclusive disjunction**.

Exactly one statement must be true — not both.

> (A OR B) AND NOT (A AND B)

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| exclusive or | o exclusivo | ou exclusif | 异或 | exklusives oder | 排他的論理和 | أو حصري | ou exclusivo | au pekee |

---

### FO — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-8
**Affective Primitive Used:** None 

#### Definition
Introduces **bounded iteration**.

Used when the range or count of repetition is known.

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| for | para | pour | 对于 | für | 〜のために | من أجل | para | kwa |

---

### WAKA — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-9
**Affective Primitive Used:** None 

#### Definition
Introduces **conditional repetition**.

Repeats as long as a condition remains true.

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| while | mientras | tant que | 当…时 | während | 〜の間 | بينما | enquanto | wakati |

---

### ¬ATE — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-10  
**Affective Primitive Used:** None 

#### Definition
Introduces **terminal repetition**.

Repeats until a condition becomes true.

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| until | hasta | jusqu’à | 直到 | bis | まで | حتى | até | hadi |

---

### FEI — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-11  
**Affective Primitive Used:** None 

#### Definition
Marks an **action or execution block**.

Used in procedural descriptions, algorithms, and instructions.

#### Language Translations

| English | Spanish | French | Chinese | German | Japanese | Arabic | Portuguese | Swahili |
|--------|---------|--------|---------|--------|----------|--------|------------|---------|
| do | hacer | faire | 做 | tun | する | افعل | fazer | fanya |

---

### WITO — (Sona Script)
#### Quick Details
**Term ID:** LS-MetaLanguageInfrastructure__LogicAndMeta-12
**Affective Primitive Used:** None 

#### Definition
Marks the **output or produced value** of a logical or procedural process.

#### Language Translations

| English | Spanish  | French    | Chinese | German      | Japanese | Arabic | Portuguese | Swahili |
| ------- | -------- | --------- | ------- | ----------- | -------- | ------ | ---------- | ------- |
| return  | devolver | retourner | 返回      | zurückgeben | 戻す       | إرجاع  | retornar   | rudisha |

---

## Compound
### ¬E HI NI  - (Sona Script)
#### Quick Details
**Term ID:** Compound
**Affective Primitive Used:** None 

#### Definition
Logical **exclusive disjunction**.

None to one of the two may be true. Not both.

>  NOT (A AND B)

| English  | Spanish        | French            | Chinese (Simplified) | German            | Japanese            | Arabic (MSA)        | Portuguese (Brazil) | Swahili            |
| -------- | -------------- | ----------------- | -------------------- | ----------------- | ------------------- | ------------------- | ------------------- | ------------------ |
| Not Both | no ambos       | pas les deux      | 不同时为真           | nicht beide       | 両方ではない        | ليس كلاهما          | não ambos           | si zote mbili      |

## Notes for Designers

- These terms are **Tier-0 infrastructure**
- They are expected to be:
  - Extremely frequent
  - Semantically stable
- Phonetic and glyph assignment should prioritize:
  - Visual simplicity
  - Auditory distinction
  - Zero collision with numbers, evidentials, or classifiers
- Once chosen, these roots should be considered **frozen**
