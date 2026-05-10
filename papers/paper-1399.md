---
id: paper-1399
title: Multi-Agent Deep Reinforcement Learning for Efficient Vehicular Mobility via Federated Fog Computing
authors:
- Arora, Ashok
- Kumar, Neetesh
- Singh, Pramod Kumar
venue: ACM Transactions on Cyber-Physical Systems
venue_type: journal
year: 2025
doi: 10.1145/3744349
url: https://www.scopus.com/pages/publications/105021962680?origin=resultslist
publisher: Association for Computing Machinery
pages: ''
keywords:
- deep reinforcement learning
- emergency vehicles
- federated fog computing
- Intelligent Transportation System (ITS)
- Intersection management
- traffic flow
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

# paper-1399 — Multi-Agent Deep Reinforcement Learning for Efficient Vehicular Mobility via Federated Fog Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Optimizing vehicle waiting time is essential for an intelligent intersection management system as it directly influences traffic flow, public safety, and overall network performance. Conventional emergency vehicle management methods rely on static rules that are unable to adapt to dynamic traffic conditions. This article presents MADQL-FFC, a multi-agent deep Q-learning framework combined with federated fog computing for real-time traffic signal control at the intersection that prioritizes emergency vehicles. In this framework, deep Q-network agents are deployed at individual intersections to make localized decisions, while a federated fog computing architecture is used in information sharing among neighboring agents for coordinated decision making. This helps in decentralized, low-latency coordination across the traffic network without the need for centralized control. The proposed approach is evaluated using realistic traffic simulations based on OpenStreetMap data of Gwalior City, India, implemented in the Simulation of Urban Mobility (SUMO) simulator. Comparative results against state-of-the-art methods demonstrate that MADQL-FFC achieves reductions in waiting time for all vehicle categories. Overall, the proposed model achieves a performance improvement of 5–32%, 12–44%, 4–46%, and 13–38% in average waiting time, average vehicle speed, average queue length, and average throughput, respectively, when compared to state of the art methods. © 2025 Copyright held by the owner/author(s).

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1399.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
