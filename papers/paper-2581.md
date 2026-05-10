---
id: paper-2581
title: A Pattern-Driven and LLM-Assisted Approach for Decomposing Monolithic ML-Based Systems into Microservices
authors:
- Ghlissi, Hakim
- Boukhatem, Mohamed El Hadi
- Abdellatif, Manel
- Moha, Naouel
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-981-95-5012-8_16
url: https://www.scopus.com/pages/publications/105028277821?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 221--229
keywords:
- Architecture
- Computer software
- Decomposition
- Embedded systems
- Learning systems
- Applications domains
- Architectural solutions
- Diverse applications
- Language model
- Machine-learning
- Monolithic architecture
- Monolithics
- Scalings
- Software-systems
- Traditional systems
- Semantics
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2581 — A Pattern-Driven and LLM-Assisted Approach for Decomposing Monolithic ML-Based Systems into Microservices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The evolution of software systems has witnessed a marked shift from monolithic architectures to microservices. This migration is driven by the need to improve the scalability and maintainability of monolithic software systems. However, this shift is most noticeable in Machine Learning (ML)-based systems, where adding learning components brings extra layers of complexity. As ML becomes increasingly embedded in diverse application domains, the challenges of evolving, scaling, and maintaining these systems demand novel architectural solutions. While microservices have proven effective in addressing such challenges in traditional systems, a principled and systematic decomposition strategy tailored specifically to ML-based monoliths remains underexplored. In this paper, we introduce an automated approach for decomposing ML-based monolithic systems into microservices. Leveraging ML-specific architectural patterns, our method employs Large Language Models (LLMs) to detect ML layers, transformer embeddings to capture semantic similarities, and clustering to form coherent microservice candidates. We validate our approach on three monolithic ML-based systems and compare our decomposition results with two baseline approaches from the literature. The results demonstrate the effectiveness of our method in producing modular and ML-aware decompositions, with a precision of 84% and a recall of 65%, outperforming the baseline approaches. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2581.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
