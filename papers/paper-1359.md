---
id: paper-1359
title: 'Satellite Federated Fine-Tuning for Foundation Models: Architecture Design and System Optimization'
authors:
- Zhu, Yan
- Yang, Peng
- Zhu, Jingyang
- Wen, Dingzhu
- Wang, Ting
- Zhou, Yong
- Shi, Yuanming
- Jiang, Chunxiao
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2024
doi: 10.1109/GLOBECOM52923.2024.10901682
url: https://www.scopus.com/pages/publications/105000825669?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5030--5035
keywords:
- Edge computing
- Integrated circuit design
- Network security
- Privacy by design
- Satellite communication systems
- Tropics
- Architecture designs
- Design optimization
- Fine tuning
- Foundation models
- Intelligence models
- Low earth orbit satellites
- Modeling architecture
- Proposed architectures
- Satellite data
- System optimizations
- Satellite ground stations
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLMs é o workload não o tomador de decisões
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

# paper-1359 — Satellite Federated Fine-Tuning for Foundation Models: Architecture Design and System Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the surge in the number of low earth orbit (LEO) satellites, continuous research has emerged on using satellite data to train artificial intelligence models. On one hand, traditional centralized training on the ground is not feasible due to privacy concerns and limited bandwidth for downloading raw satellite data. On the other hand, due to the limited energy and computational capability of satellites, training directly on satellites suffers from prolonged latency, especially for large models. To alleviate these issues, we propose a novel satellite-ground collaborative federated fine-tuning architecture, where ground stations (GSs) and satellites collaboratively train a global model without the need for data downloads. In this proposed architecture, satellites serve as edge devices and the ground server serves as a coordinator. However, the short satellite-ground communication windows caused by the high mobility of satellites and the substantial intra-orbit data transmission bring special challenges to the transmission process of federated edge learning. To tackle these challenges, we carefully design the satellite-ground collaborative fine-tuning architecture and utilize an optimized ring all-reduce algorithm and network flow algorithm to enhance the intra-orbit and ground-satellite transmissions, respectively. Experimental results demonstrate that our proposed architecture significantly reduces the training time by 40% compared to training solely on satellite. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "LLMs é o workload não o tomador de decisões"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1359.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
