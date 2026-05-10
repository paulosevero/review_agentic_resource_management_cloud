---
id: paper-2732
title: Topology-Aware Multi-Hop Task Offloading via GNN-A Routing in Vehicular Networks
authors:
- Nie, Xuefang
- Sun, Guoquan
- Li, Sheng
- Zhang, Chen
- Zhu, Xuesheng
- Zhang, Jiliang
venue: 2026 International Conference on Electronics, Information, and Communication, ICEIC 2026
venue_type: conference
year: 2026
doi: 10.1109/ICEIC69189.2026.11386024
url: https://www.scopus.com/pages/publications/105034847225?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Graph Neural Networks
- Multi-hop Offloading
- Reinforcement Learning
- Task Scheduling
- Topology-Aware Routing
- Vehicular Edge Computing
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

# paper-2732 — Topology-Aware Multi-Hop Task Offloading via GNN-A Routing in Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) enables low-latency task execution by deploying computation at vehicles and roadside units (RSUs). However, high mobility and frequent topology variations cause multi-hop offloading paths to break easily, leading to task interruptions and performance degradation. Existing path selection methods, typically relying on static link metrics or exhaustive search, fail to adapt efficiently in large-scale dynamic networks. To address these challenges, we propose a joint optimization framework that integrates task scheduling with topology-aware routing. A multi-agent A3C module determines the offloading ratio and destination node, while a graph neural network-enhanced A<sup>∗</sup> (GNN-A*) planner constructs reliable, low-latency multi-hop paths by learning dynamic topological representations. The two modules operate collaboratively in an adaptive feedback loop, enabling online policy refinement under varying vehicular conditions. Simulation results show that the proposed framework significantly outperforms state-of-the-art baselines, achieving lower delay, higher task completion ratios, and better scalability as vehicle density increases. © 2026 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2732.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
