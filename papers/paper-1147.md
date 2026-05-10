---
id: paper-1147
title: Asynchronous Federated Learning for Resource Allocation in Software-Defined Internet of UAVs
authors:
- Qureshi, Khalid Ibrahim
- Wang, Lei
- Xiong, Xuanrui
- Lodhi, Muhammad Ali
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3345864
url: https://www.scopus.com/pages/publications/85181797749?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 20899--20911
keywords:
- Communication optimization
- Internet of Things (IoT)
- transmission power optimization
- unmanned aerial vehicles (UAVs)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1147 — Asynchronous Federated Learning for Resource Allocation in Software-Defined Internet of UAVs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The use of unmanned aerial vehicles (UAVs) as flying base stations to support various tasks, such as data collection, machine learning (ML) model training, and wireless communication in Internet of Things (IoT) networks, has garnered significant attention in recent years. Nonetheless, several challenges have arisen in this context, including data privacy concerns and limited onboard computational and communication resources. These challenges make the direct transmission of raw data to a central server for training impractical. Moreover, UAV-based networks are susceptible to fluctuating channel conditions and the heterogeneous computing capabilities of IoT devices. Therefore, enhancing the reliability and efficiency of such networks is imperative. In this article, we introduce a novel framework known as the asynchronous federated framework for IoT-enabled UAV (AF3N) networks. AF3N enables local model training with subsequent parameter transmission to the mobile-edge computing (MEC) server. To further enhance learning efficiency, we incorporate a device selection strategy into the AF3N framework. Additionally, we employ a multiagent asynchronous advantage actor-critic (A3C)-based joint resource allocation algorithm aimed at reducing latency and energy utilization within the Internet of UAVs (IoUAVs) network. Through extensive simulations we comprehensively examine the efficacy and performance of our proposed framework.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1147.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
