---
id: paper-2442
title: Joint optimization of computation offloading and power control in user-centric networks based on dual layer mobile edge computing
authors:
- Zhang, Peiying
- Sun, Yuekai
- Tan, Lizhuang
- Guizani, Maher
- Hasan, Mohammad Kamrul
- Wang, Jian
venue: Ad Hoc Networks
venue_type: journal
year: 2025
doi: 10.1016/j.adhoc.2025.103998
url: https://www.scopus.com/pages/publications/105014946090?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computation offloading
- Mobile edge computing
- Power control
- Reinforcement learning
- Resource allocation
- User-centric network
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2442 — Joint optimization of computation offloading and power control in user-centric networks based on dual layer mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In mobile edge computing (MEC) over traditional cellular networks (TCN), users located at the cell edges are prone to severe edge interference and signal attenuation, leading to low throughput and even transmission interruptions. These edge effects significantly hinder the offloading of computational tasks from end devices to MEC servers, adversely affecting the user equipment (UE) experience. To address these issues and improve UE experience within the network, we design a user-centric network (UCN) structure comprising a three-tier network interconnected through communication links to ensure low latency and reliable transmission during computation offloading. For the computation offloading problem within UCN, we design a network model with dual-layer MEC servers that considers the competitive nature of UEs in real-world scenarios. This model is solved using a multi-agent reinforcement learning algorithm to optimize network strategies, achieving minimal long-term average total delay and power consumption. Experimental results demonstrate that the proposed scheme significantly reduces system power consumption, with a maximum reduction of 36.19% compared to other baseline algorithms. The scheme also achieves substantial reduction in the long-term average total delay by 39.5%. These algorithms indicate that the proposed approach offers considerable advantages in enhancing UE experience and reducing the energy consumption. © 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2442.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
