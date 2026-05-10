---
id: paper-2922
title: Task-Aware Collaborative Inference and Fine-Grained DNN Partitioning in MEC Networks
authors:
- Zhang, Guanlei
- Zhang, Qiyang
- Feng, Lei
- Zhou, Fanqin
- Donta, Praveen Kumar
- Dustdar, Schahram
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3650680
url: https://www.scopus.com/pages/publications/105027279751?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Deep Reinforcement Learning
- Distributed Inference
- Mobile Edge Computing
- Model Partitioning
- Resource Allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2922 — Task-Aware Collaborative Inference and Fine-Grained DNN Partitioning in MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile devices (MDs) are increasingly incorporating deep neural network (DNN) inference into their systems due to the rapid growth of intelligent applications. Mobile edge computing-based distributed DNN collaborative inference has gained popularity due to limited on-device computation and energy budgets. However, the resource competition among MDs, along with the coupling of collaborative inference tasks across MDs and servers, creates significant challenges for efficient resource management. This issue is further exacerbated by the complexity of directed acyclic graph (DAG)-structured DNNs. Most prior studies do not jointly address the dual challenges of partitioning complex-structured DNNs and leveraging advanced optimization for collaborative inference, and their resilience to channel condition fluctuations remains underexplored. To address these challenges, we propose a novel task-aware collaborative inference framework. First, we devise a fine-grained partitioning point search algorithm based on a bidirectional graph linked list, which enables one-dimensional and flexible partitioning of DAG-structured DNNs. We then reformulate the problem of minimizing collaborative inference energy consumption and latency as a task-aware Markov decision process (MDP), which partitions each user's inference task queue into consecutive task windows for resource allocation. Building on this, we propose an Embedded Multi-Agent Hybrid Proximal Policy Optimization (EMH-PPO) algorithm to learn effective policies. Extensive experiments conducted across diverse network scenarios reveal that, compared to local DNN inference on MDs, our proposed method reduces inference latency by up to 64% and energy consumption by up to 46%. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2922.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
