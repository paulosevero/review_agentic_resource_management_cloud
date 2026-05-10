---
id: paper-2676
title: Multi-agent deep reinforcement learning based on cloud-edge computing for urban vehicle route guidance
authors:
- Liao, Zhuhua
- Gao, Junjian
- Yi, Aiping
- Zhao, Yijiang
- Tang, Yue
venue: Cluster Computing
venue_type: journal
year: 2026
doi: 10.1007/s10586-025-05842-8
url: https://www.scopus.com/pages/publications/105021482511?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Cloud-edge computing
- Dueling Q-routing
- Graph neural network
- Multi-agent deep reinforcement learning
- Urban route guidance
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

# paper-2676 — Multi-agent deep reinforcement learning based on cloud-edge computing for urban vehicle route guidance

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Urban traffic congestion has emerged as a significant challenge impairing travel efficiency and transportation resource utilization. Although vehicle route guidance plays a crucial role in mitigating urban traffic congestion, traditional methods fail to accurately assess the spatiotemporal traffic patterns and adapt swiftly to dynamic traffic conditions and vehicular interactions. To address the issues, this paper proposes a Multi-agent Deep Reinforcement Learning framework based on cloud-edge computing for urban vehicle route guidance. The framework deploys intersection-based agents to collect realtime traffic data, facilitate global deep reinforcement learning, and offer intelligent and interactive route guidance. Moreover, an accurately spatiotemporal traffic state information mining method is proposed by integrating Graph Convolutional Network (GCN) and Gated Recurrent Unit network (GRU) with an attention mechanism. Subsequently, a modeling approach for inter-agent spatial relationship based on Graph Attention Network (GAT) is presented to facilitate the transmission and fusion of traffic characteristics on cloud. Finally, the Spatio-Temporal Mean-Field multi-agent Dueling Q-Routing (ST-MF-DQR) algorithm is proposed to optimize vehicular spatiotemporal coordination. The experimental evaluations on both synthetic and real traffic networks demonstrate that our method minimizes average vehicle waiting and travel times, significantly improving urban traffic mobility. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2676.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
