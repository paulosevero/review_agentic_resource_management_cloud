---
id: paper-1370
title: 'Cerebrum: A Proactive Federated Learning Framework for Multi-Objective Edge Workflow Scheduling'
authors:
- Ahmadpanah, Seyed Hossein
- Mirabi, Meghdad
venue: Journal of Grid Computing
venue_type: journal
year: 2025
doi: 10.1007/s10723-025-09816-3
url: https://www.scopus.com/pages/publications/105022514440?origin=resultslist
publisher: Springer Science and Business Media B.V.
pages: ''
keywords:
- Edge computing
- Federated architecture
- Proactive scheduling
- Reinforcement learning
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

# paper-1370 — Cerebrum: A Proactive Federated Learning Framework for Multi-Objective Edge Workflow Scheduling

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rise of 5G networks and the Internet of Things (IoT) is driving a shift towards edge computing, where applications increasingly consist of complex, containerized workflows. Existing orchestration platforms, designed for centralized data centers, are reactive, workflow-agnostic, and poorly scalable, leading to high makespan, energy consumption, and cost. This paper presents Cerebrum, a proactive, learning-based framework for multi-objective scheduling of containerized workflows at the edge. Cerebrum combines several key innovations: (1) hierarchical workflow decomposition for scalable DAG partitioning, (2) a proactive multi-objective reinforcement learning agent with predictive resource forecasting, (3) a two-tiered architecture separating global inter-cluster orchestration from local intra-cluster scheduling, and (4) a unified policy framework balancing performance, energy, and cost. Extensive simulations show that Cerebrum achieves the lowest average makespan (90 s, 5.3% improvement over FL-Proactive), reduces energy consumption to 1,950 kJ (6.0% lower), and cuts monetary cost to $2.4 (36.8% lower), while maintaining scheduling decision latency below 15 ms across 20 clusters. These results demonstrate that proactive, adaptive scheduling intelligence can simultaneously optimize multiple objectives, providing a robust and scalable solution for next-generation edge-cloud applications. © The Author(s), under exclusive licence to Springer Nature B.V. 2025.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1370.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
