---
id: paper-1034
title: Neighborhood-aware distributed intelligent computing offloading and resource allocation for edge computing; [邻域感知的分布式智能边缘计算卸载和资源分配算法]
authors:
- Li, Yun
- Zhang, Jianxin
- Yao, Zhixiu
- Xia, Shichao
venue: Scientia Sinica Informationis
venue_type: journal
year: 2024
doi: 10.1360/SSI-2023-0177
url: https://www.scopus.com/pages/publications/85196969902?origin=resultslist
publisher: Science China Press
pages: 413--429
keywords:
- computing offloading
- graph attention network
- mobile edge computing
- multi-agent reinforcement learning
- resource allocation
language: Chinese
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1034 — Neighborhood-aware distributed intelligent computing offloading and resource allocation for edge computing; [邻域感知的分布式智能边缘计算卸载和资源分配算法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the emergence of massive compute-intensive and delay-sensitive tasks, mobile edge computing (MEC) has become an active research field to improve user experience and reduce system energy consumption. However, in densely deployed MEC networks, the complex spatial relations and dynamics of the wireless network state present serious challenges for designing offloading schemes. In this paper, an intelligent collaborative computing offload and resource allocation algorithm is proposed for a multibase station and multiuser MEC network. First, we formulate a joint optimization problem of offloading decision, channel allocation, transmit power allocation, and computation resource allocation to minimize the system energy consumption under delay constraints. Then, because this problem is a mixed integer nonlinear programming problem, we propose a graph attention network -based hybrid-action multiagent reinforcement learning algorithm (Gat-HMARL), where each base station refers to an agent and configures the Gat-HMARL algorithm. Gat-HMARL adopts a graph attention network to capture the potential spatial relations of wireless network states, allowing the base stations to selectively attend to the wireless network state of other base stations to learn better computing offloading and resource allocation strategies. Finally, the simulation results demonstrate that the proposed Gat-HMARL algorithm exhibits a remarkable performance improvement than the benchmark algorithms. © 2024 Science China Press. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1034.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
