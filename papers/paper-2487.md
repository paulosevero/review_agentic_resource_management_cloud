---
id: paper-2487
title: Task Offloading with LLM-Enhanced Multi-Agent Reinforcement Learning in UAV-Assisted Edge Computing
authors:
- Zhu, Feifan
- Huang, Fei
- Yu, Yantao
- Liu, Guojin
- Huang, Tiancong
venue: Sensors
venue_type: journal
year: 2025
doi: 10.3390/s25010175
url: https://www.scopus.com/pages/publications/85214466090?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- LLM
- multi-agent deep learning
- trajectory planning
- UAV
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2487 — Task Offloading with LLM-Enhanced Multi-Agent Reinforcement Learning in UAV-Assisted Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) furnished with computational servers enable user equipment (UE) to offload complex computational tasks, thereby addressing the limitations of edge computing in remote or resource-constrained environments. The application of value decomposition algorithms for UAV trajectory planning has drawn considerable research attention. However, existing value decomposition algorithms commonly encounter obstacles in effectively associating local observations with the global state of UAV clusters, which hinders their task-solving capabilities and gives rise to reduced task completion rates and prolonged convergence times. To address these challenges, this paper introduces an innovative multi-agent deep learning framework that conceptualizes multi-UAV trajectory optimization as a decentralized partially observable Markov decision process (Dec-POMDP). This framework integrates the QTRAN algorithm with a large language model (LLM) for efficient region decomposition and employs graph convolutional networks (GCNs) combined with self-attention mechanisms to adeptly manage inter-subregion relationships. The simulation results demonstrate that the proposed method significantly outperforms existing deep reinforcement learning methods, with improvements in convergence speed and task completion rate exceeding 10%. Overall, this framework significantly advances UAV trajectory optimization and enhances the performance of multi-agent systems within UAV-assisted edge computing environments. © 2024 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2487.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
