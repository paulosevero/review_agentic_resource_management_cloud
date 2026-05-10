---
id: paper-2615
title: Manufacturing service recommendation method based on bidirectional sequence feature and topic semantic model; [基于双向序列特征和主题语义模型的制造服务推荐方法]
authors:
- Huang, Shenquan
- Zhu, Xiaohui
- Chen, Zirui
- Li, Panfeng
- Yu, Luchuan
venue: Jisuanji Jicheng Zhizao Xitong/Computer Integrated Manufacturing Systems, CIMS
venue_type: journal
year: 2026
doi: 10.13196/j.cims.2023.0732
url: https://www.scopus.com/pages/publications/105033081557?origin=resultslist
publisher: CIMS
pages: 772--785
keywords:
- attention mechanism
- bidirectional sequence feature
- manufacturing cloud services
- service recommendation
- topic semantic model
language: Chinese
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

# paper-2615 — Manufacturing service recommendation method based on bidirectional sequence feature and topic semantic model; [基于双向序列特征和主题语义模型的制造服务推荐方法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The manufacturing cloud service recommendation model is a key technology for users to quickly discover and obtain the personalized services they need from the increasingly expanding manufacturing cloud. Aiming at the problem that the manufacturing cloud service recommendation model lacks in-depth mining of topic features and does not fully consider service sequence context information, a manufacturing service recommendation method framework based on bidirectional sequence features and topic semantic model was proposed. By introducing Huffman tree to improve the Latent Dirichlet Allocation(LDA) topic model to build the topic vector of the service, the Service2vector service semantic model incorporating the topic features was proposed, and the deep features were mined from the perspectives of words, topics and service content. Considering the bidirectional sequence features, a service recommendation method based on mask language model was proposed. Time interval was used to represent the time-location features in the sequence, and the bidirectional sequence features were learned by multi-layer attention mechanism. Finally, the service data on Programmable Web platform were crawled to conduct experiments. The results showed that the recommendation method had good effect. © 2026 CIMS. All rights reserved.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2615.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
