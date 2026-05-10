---
id: paper-0876
title: 'DiCE-M: Distributed Code Generation and Execution for Marine Applications-An Edge-Cloud Approach'
authors:
- Coviello, Giuseppe
- Rao, Kunal
- Mellone, Gennaro
- De Vita, Ciro Giuseppe
- Chakradhar, Srimat
venue: Proceedings - 2024 IEEE/ACM Symposium on Edge Computing, SEC 2024
venue_type: conference
year: 2024
doi: 10.1109/SEC62691.2024.00054
url: https://www.scopus.com/pages/publications/85216767314?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 468--475
keywords:
- Cloud computing
- Code generation
- Distributed computing
- Edge computing
- Generative artificial intelligence
- Large language models
- Marine science
- Runtime
- Vision applications
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0876 — DiCE-M: Distributed Code Generation and Execution for Marine Applications-An Edge-Cloud Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing has emerged as a transformative technology that reduces application latency, improves cost efficiency, enhances security, and enables large-scale deployment of applications across various domains. In environmental monitoring, systems such as MegaSense[49], use low-cost sensors to gather and process real-Time air quality data through edge-cloud collaboration, highlighting the critical role of edge computing in enabling scalable, efficient solutions. Similarly, marine science increasingly requires real-Time processing and analysis of marine data from remote, resource-constrained environments. In this paper, we extend the power of edge computing by integrating it with Generative Artificial Intelligence(GenAI),specifically large language models (LLMs), to address challenges in marine science applications. We propose DiCE-M (Distributed Code generation and Execution for Marine applications), a robust system that uses LLM to generate distributed code for marine applications and then utilizes a runtime to efficiently execute it on an edge+cloud computing infrastructure. Specifically, DiCE-M leverages edge computing to execute lightweight AI models locally on unmanned surface vehicles(USVs)while offloading complex tasks to the cloud, thus balancing computational load and enabling realtime monitoring in marine environments. We use marine litter identification as an example application to demonstrate the utility of DiCE-M. Our results show that DiCE-M reduces latency by more than 2X when marine litter is not detected and cuts cloud computing costs by more than half compared to traditional cloud-based approaches. By selectively cropping and transmitting relevant image portions, DiCE-M further improves bandwidth efficiency, making it a reliable and cost-effective solution for deploying AI-drivenapplications on resource-constrained USVs in dynamic marine environments.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0876.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
