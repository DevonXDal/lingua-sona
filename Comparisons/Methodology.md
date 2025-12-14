# Comparison Methodology

This document defines the methodology used for all language comparison files in the
`Comparisons/` directory.

Its purpose is to ensure that comparisons between **Lingua Sona** and other languages,
notation systems, or structured representations are:
- fair
- repeatable
- scope-limited
- falsifiable

This methodology explicitly avoids advocacy and instead focuses on **design constraints,
intended use cases, and tradeoffs**.

---

## 1. Scope of Comparison

All comparisons are conducted within explicitly stated scopes.
A comparison **does not imply global superiority** unless explicitly stated and justified.

Primary scopes commonly evaluated include:
- structured documentation
- scientific or technical notes
- knowledge representation
- cognitive load during precision tasks
- machine parsing and formal analysis

Unless otherwise noted, **casual conversation, literature, poetry, and cultural legacy**
are considered **out of scope**.

---

## 2. Design-Intent Alignment

Languages and systems are compared **only where their design intents overlap**.

For example:
- A natural language is not penalized for lacking formal ontology
- A formal notation system is not penalized for poor conversational flow

When intents differ, the comparison will explicitly state:
- where overlap exists
- where goals diverge
- whether divergence is intentional or incidental

---

## 3. Constraint-Based Evaluation

Comparisons prioritize **hard constraints** over subjective qualities.

Examples of hard constraints:
- mandatory evidentiality
- deterministic parsing
- finite lexicon limits
- explicit semantic classification
- formal grammar completeness

Soft or subjective traits (e.g., "beauty", "feel", "naturalness") may be mentioned,
but are clearly labeled as such and never treated as decisive.

---

## 4. Metrics Commonly Used

Not all metrics apply to all systems. When used, they are defined locally.

Common metrics include:
- ambiguity tolerance
- compression efficiency (information per symbol)
- learnability curve (initial vs long-term)
- tooling dependence
- formal expressiveness
- error detectability
- provenance clarity

Metrics are qualitative unless explicitly stated otherwise.

---

## 5. Strengths and Weaknesses

Every comparison **must** include:
- areas where Lingua Sona underperforms
- areas where the compared system underperforms
- areas of non-overlap

Omitting weaknesses is considered a methodological failure.

---

## 6. Time Sensitivity

Comparisons are **snapshots in time**, not permanent judgments.

Lingua Sona is under active development.
Other systems may also evolve.

Each comparison implicitly reflects:
- the state of Lingua Sona at time of writing
- the commonly accepted state of the compared system

Where relevant, versioning or dates should be noted.

---

## 7. Non-Goals

These comparisons do **not** aim to:
- rank languages universally
- predict adoption outcomes
- argue for replacement of existing languages
- establish cultural or literary superiority

Adoption, community size, and historical momentum are treated as **external factors**,
not design metrics.

---

## 8. Reproducibility and Extension

This methodology is intentionally reusable.

Contributors are encouraged to:
- apply the same framework to new comparisons
- critique Lingua Sona using this methodology
- extend metrics where justified

Disagreement is expected and considered productive.

---

## 9. Interpretation Guidance

Readers are encouraged to interpret results as:
- design tradeoffs
- suitability for specific tasks
- reflections of underlying priorities

Not as:
- prescriptions
- value judgments
- claims of inevitability

---

## 10. Summary

These comparisons exist to answer one question:

> “For a given task, under stated constraints, what does each system make easier or harder?”

No more.
No less.

