---
id: paper-2354
title: 'From ATOP to ZCube: Automated Topology Optimization Pipeline and A Highly Cost-Effective Network Topology for Large Model Training'
authors:
- Yan, Zihan
- Li, Dan
- Chen, Li
- Xiong, Dian
- Gao, Kaihui
- Zhang, Yiwei
- Yan, Rui
- Zhang, Menglei
- Zhang, Bochun
- Jiang, Zhuo
- Ye, Jianxi
- Lin, Haibin
venue: SIGCOMM 2025 - ACM SIGCOMM 2025 Conference
venue_type: conference
year: 2025
doi: 10.1145/3718958.3750503
url: https://www.scopus.com/pages/publications/105016234831?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 861--881
keywords:
- AI infrastructure
- Data center networks
- Network topology
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2354 — From ATOP to ZCube: Automated Topology Optimization Pipeline and A Highly Cost-Effective Network Topology for Large Model Training

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The development of large language models (LLMs) poses new challenges in data center network topology design. To assist in exploring topology design, we propose ATOP, an Automated Topology Optimization Pipeline, which models network topology as a set of hyperparameters, enabling the discovery of potential topologies. With various optimization algorithms and customizable optimization objectives, ATOP achieves automated topology optimization on a scale of tens of thousands of GPUs. We apply ATOP on network topologies for 256, 1024, 4096, and 16384 GPUs, optimizing performance under LLMs training traffic patterns, collective communication performance, fault tolerance, and network cost. We also evaluate ATOP in different scenarios: building, optimizing, and expanding a data center. From ATOP’s results, we discover a new topology - ZCube, which reaches the highest cost-effectiveness across various GPU scales. Simulation results show that ZCube, compared to the previous state-of-the-art topologies, including Rail-optimized Fat-tree (ROFT), Rail-only, and HPN, improves end-to-end LLM training speed by 3% to 7% and reduces network hardware costs by 26% to 46%. We also construct ZCube on a real-world testbed. Results show that ZCube reduces hardware costs by 25% compared to Rail-Optimized Topology while maintaining the same all-reduce and all-to-all performance. © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2354.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
