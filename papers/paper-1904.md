---
id: paper-1904
title: 'Weak-to-Strong Attacking via Model Collaboration: A survey'
authors:
- Liu, Yameng
venue: 2025 7th International Conference on Next Generation Data-Driven Networks, NGDN 2025
venue_type: conference
year: 2025
doi: 10.1109/NGDN66208.2025.11182097
url: https://www.scopus.com/pages/publications/105019303690?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 345--348
keywords:
- AI Security
- Asymmetric Adversarial Attacks
- Black-Box Optimization
- Low-Resource High-Impact Attacks (LRHIA)
- Model Collaboration
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1904 — Weak-to-Strong Attacking via Model Collaboration: A survey

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the widespread application of deep learning models, security in asymmetric adversarial scenarios faces severe challenges. Existing defenses primarily target "strong-to-strong"attacks, lacking effective countermeasures against Low-Resource High-Impact Attacks (LRHIA) launched through system vulnerabilities when attackers are disadvantaged in resources, model capabilities, or knowledge. This paper proposes a Weak-to-Strong Attacking via Model Collaboration (WSC) framework. Focusing on scenarios where attackers are disadvantaged in at least one dimension (resources, models, knowledge), it explores asymmetric attack paths. Through core technologies like lightweight perturbation generation, adversarial transfer of heterogeneous models, and dynamic optimization of black-box decision boundaries, the WSC framework can breach the defenses of strong models despite significant disadvantages in a single dimension. Based on a systematic analysis of cutting-edge research (2023-2025), this paper reveals the potential risks of Large Language Models (LLMs) in asymmetric confrontations and verifies that attackers can achieve efficient attacks with a disadvantage in any one dimension. The results provide a theoretical basis for designing dynamic defense mechanisms in asymmetric scenarios and lay the foundation for innovating active defense paradigms in high-security domains like edge computing.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1904.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
