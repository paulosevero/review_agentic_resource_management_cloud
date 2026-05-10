---
id: paper-1388
title: Advanced DDOS Attack Detection in Vanet Cloud Systems Using Secretary Bird Optimization and Machine Learning
authors:
- Alsamman, Salsabil
- Panthakkan, Alavikunhu
- Gawanmeh, Amjad
venue: 2025 International Conference on Computational Intelligence and Knowledge Economy, ICCIKE 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCIKE67021.2025.11318177
url: https://www.scopus.com/pages/publications/105032712849?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 651--656
keywords:
- bio-inspired optimization
- cloud computing
- DDoS attack detection
- intrusion detection
- machine learning
- network security
- Secretary Bird Optimization Algorithm
- VANET
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1388 — Advanced DDOS Attack Detection in Vanet Cloud Systems Using Secretary Bird Optimization and Machine Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This study proposes machine learning-based intrusion detection system optimized using Secretary Bird Optimization Algorithm (SBOA) to detect DDoS attacks in real-time. The method uses Random Forest classifier with hyperparameters tuned through bio-inspired optimization across 100 iterations with 30 search agents. Network Simulator 2 (NS2) simulations were conducted with 20-50 vehicles traveling at 60-100 ~km / h over 2000 ~m × 500 ~m area, testing scenarios with 10-25 % malicious nodes. SBOA-optimized Random Forest achieved 99.78 % detection accuracy, 99.79 % precision, and 99.78% F1-score on 200,000 samples, outperforming baseline Random Forest (99.47 %), Decision Tree (99.12 %), and existing methods including PSO-based (99.65 %) and GA-based (99.58 %) approaches. Confusion matrix revealed only 88 misclassifications from 40,000 test samples, with balanced false positive and false negative rates of 0.22 % each. The obtained results in this work showed that SBOA-RF is effective and practical as solution for protecting VANETs against DDoS attacks while at the same time maintaining real-time detection ability, which is needed for some critical applications. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1388.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
