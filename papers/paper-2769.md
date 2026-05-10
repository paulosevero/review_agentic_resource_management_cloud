---
id: paper-2769
title: 'MonoEmbed: Enhancing LLM representations for monolith to microservices decomposition through contrastive learning'
authors:
- Sellami, Khaled
- Saied, Mohamed Aymen
venue: Empirical Software Engineering
venue_type: journal
year: 2026
doi: 10.1007/s10664-025-10732-z
url: https://www.scopus.com/pages/publications/105021083713?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Contrastive learning
- Language model
- Microservice
- Monolith decompostion
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

# paper-2769 — MonoEmbed: Enhancing LLM representations for monolith to microservices decomposition through contrastive learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As Monolithic applications evolve, they become increasingly difficult to maintain and improve, leading to scaling and organizational issues. The Microservices architecture, known for its modularity, flexibility and scalability, offers a solution for large-scale applications allowing them to adapt and meet the demand on an ever increasing user base. Despite its advantages, migrating from a monolithic to a microservices architecture is often costly and complex, with the decomposition step being a significant challenge. This research addresses this issue by introducing MonoEmbed, a Language Model based approach for automating the decomposition process. MonoEmbed leverages state-of-the-art Large Language Models (LLMs) and representation learning techniques to generate representation vectors for monolithic components, which are then clustered to form microservices. By evaluating various pre-trained models and applying fine-tuning techniques such as Contrastive Learning and Low Rank Adaptation (LoRA), MonoEmbed aims to optimize these representations for microservice partitioning. The evaluation of the fine-tuned models showcases that they were able to significantly improve the quality of the representation vectors when compared with pre-trained models and traditional representations. The proposed approach was benchmarked against existing decomposition methods, demonstrating superior performance in generating cohesive and balanced microservices for monolithic applications with varying scales. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2769.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
