---
id: paper-2023
title: Smart 5G Network Slicing for Collaborative UAV Swarms via Federated Reinforcement Learning
authors:
- Patra, Pradyumna Ku
- Sahin, Onur
- Sathya, Vanlin
- Dutta, Ashutosh
venue: '2025 IEEE Future Networks World Forum: Beyond Connectivity: 6g for a Sustainable and Intelligent Future, FNWF 2025'
venue_type: conference
year: 2025
doi: 10.1109/FNWF66845.2025.11317543
url: https://www.scopus.com/pages/publications/105032421974?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 5G Network Slicing
- Dynamic Bandwidth Allocation
- Edge Computing
- Federated Reinforcement Learning
- Mission-Critical Communications
- Quality of Service
- Resource Allocation
- UAV Swarms
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2023 — Smart 5G Network Slicing for Collaborative UAV Swarms via Federated Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We present in this paper an AI empowered framework for smart 5G network slicing in the context of Unmanned Aerial Vehicle (UAV) swarm secured-interconnected environments, using Federated Reinforcement Learning (FRL) to optimize the dynamic bandwidth reservation according to mission-critical requisition. The architecture of the proposed model allows for on-the-fly adaptation in a heterogeneous mixed swarm that are carrying out surveillance, mapping, and relaying communication. The architecture preserves both privacy and incurs low communication latency as well as high scalability, since decentralized agents are jointly trained without the exchange of raw data. Simulation results demonstrate that our FRL-based slicing approach achieves significant performance improvement in throughput, task success ratio and resource utilization compared to traditional methods under different mission loads.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2023.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
