---
id: paper-1544
title: Joint Task Scheduling and Resource Allocation in Cloud-Edge Collaborative Computing Systems
authors:
- Du, Boyu
- Zhou, Jingya
- Wang, Jin
- Wang, Jiangwei
- Li, Zhijun
venue: 54th International Conference on Parallel Processing, ICPP 2025 - Main Conference Proceedings
venue_type: conference
year: 2025
doi: 10.1145/3754598.3754646
url: https://www.scopus.com/pages/publications/105026444400?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 586--596
keywords:
- cloud-edge collaborative computing
- multi-agent reinforcement learning.
- resource allocation
- task scheduling
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

# paper-1544 — Joint Task Scheduling and Resource Allocation in Cloud-Edge Collaborative Computing Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud-edge collaborative computing (CECC) facilitates the sharing of computing resources by collaboratively scheduling tasks among servers, thereby maximizing task execution efficiency. Task scheduling and resource allocation (TS-RA) are two interrelated issues that significantly affect the efficient utilization of computing resources. In this paper, we decouple the joint optimization problem of TS-RA and propose a novel model based on multi-agent reinforcement learning (TRMARL), which is applicable to distributed task scheduling and resource allocation in a heterogeneous CECC system. TRMARL consists of two modules: 1) the task scheduling module, where we introduce a value factorization algorithm to maximize joint rewards of distributed scheduling actions; 2) the resource allocation module, where we present a proximal policy optimization (PPO) algorithm based mechanism to optimize resource allocation. TRMARL efficiently captures the state difference among heterogeneous servers through a graph attention network-based recurrent deep Q-network (GAT-based recurrent-DQN) architecture and learns different strategies for heterogeneous services through a multi-expert schema. The experimental results demonstrate that TRMARL effectively improves the task completion rate, reduces average system latency, and enhances convergence stability in a heterogeneous CECC system. © 2025 Copyright held by the owner/author(s).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1544.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
