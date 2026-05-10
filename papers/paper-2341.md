---
id: paper-2341
title: Survey on Fine-Grained Flow Control for Artificial Intelligence Data Centers; [面向智算中心的细粒度流量控制技术综述]
authors:
- Xu, Jing
- Wang, Zhan
- Yuan, Guojun
- Ma, Zhenlong
- Yang, Fan
- Sun, Ninghui
venue: Jisuanji Yanjiu yu Fazhan/Computer Research and Development
venue_type: journal
year: 2025
doi: 10.7544/issn1000-1239.202440796
url: https://www.scopus.com/pages/publications/105023492445?origin=resultslist
publisher: Science Press
pages: 2806--2825
keywords:
- artificial intelligence data centers
- congestion control
- load balancing
- out-of-order reordering
- packet spray
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2341 — Survey on Fine-Grained Flow Control for Artificial Intelligence Data Centers; [面向智算中心的细粒度流量控制技术综述]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of artificial intelligence generated content (AIGC) technologies and the widespread deployment of large language models (LLMs), networks in artificial intelligence data centers are encountering significant challenges. Flow control is a crucial approach for optimizing network performance, providing extremely high bandwidth and ultra-low latency. This paper reviews key issues and solutions in the field of fine-grained flow control, focusing on advances in three key areas: adaptive load balancing mechanisms that dynamically distribute traffic making full use of network resources to avoid congestion, proactive congestion control strategies designed to predict and alleviate potential congestion, and out-of-order packet reordering techniques that ensure data integrity despite non-sequential arrivals. We summarize the mainstream implementation solutions and provide a detailed comparison. Building on this, we discuss the key technical solutions currently adopted by leading artificial intelligence data centers, along with the network devices that support fine-grained flow control. We also identify unresolved challenges in this field, propose potential solutions, and explore future development trends, especially as AI technologies continue to evolve and demand more sophisticated network infrastructures. This review offers valuable insights for researchers and practitioners to optimize network performance in AI-driven applications and highlights important directions for future research in fine-grained flow control. © 2025 Science Press. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2341.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
