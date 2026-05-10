---
id: paper-0710
title: Multiagent Federated Reinforcement Learning for Resource Allocation in UAV-Enabled Internet of Medical Things Networks
authors:
- Seid, Abegaz Mohammed
- Erbad, Aiman
- Abishu, Hayla Nahom
- Albaseer, Abdullatif
- Abdallah, Mohamed
- Guizani, Mohsen
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3283353
url: https://www.scopus.com/pages/publications/85161497981?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 19695--19711
keywords:
- Emergency
- federated learning (FL)
- healthcare
- Internet of Medical Things (IoMT)
- multiagent RL (MARL)
- unmanned aerial vehicle (UAV)
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-0710 — Multiagent Federated Reinforcement Learning for Resource Allocation in UAV-Enabled Internet of Medical Things Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the 5G/B5G network paradigms, intelligent medical devices known as the Internet of Medical Things (IoMT) have been used in the healthcare industry to monitor remote users' health status, such as elderly monitoring, injuries, stress, and patients with chronic diseases. Since IoMT devices have limited resources, mobile edge computing (MEC) has been deployed in 5G networks to enable them to offload their tasks to the nearest computational servers for processing. However, when IoMTs are far from network coverage or the computational servers at the terrestrial MEC are overloaded/emergencies occur, these devices cannot access computing services, potentially risking the lives of patients. In this context, unmanned aerial vehicles (UAVs) are considered a prominent aerial connectivity solution for healthcare systems. In this article, we propose a multiagent federated reinforcement learning (MAFRL)-based resource allocation framework for a multi-UAV-enabled healthcare system. We formulate the computation offloading and resource allocation problems as a Markov decision process game in federated learning with multiple participants. Then, we propose an MAFRL algorithm to solve the formulated problem, minimize latency and energy consumption, and ensure the quality of service. Finally, extensive simulation results on a real-world heartbeat data set prove that the proposed MAFRL algorithm significantly minimizes the cost, preserves privacy, and improves accuracy compared to the baseline learning algorithms.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0710.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
