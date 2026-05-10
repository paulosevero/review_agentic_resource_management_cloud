---
id: paper-2783
title: Multi agent federated reinforcement learning for Distributed MPTCP Agents
authors:
- Suarez, Jorge Abraham Rios
- Jia, Min
- Shibwabo, Anyembe
venue: Telecommunication Systems
venue_type: journal
year: 2026
doi: 10.1007/s11235-026-01408-0
url: https://www.scopus.com/pages/publications/105029055789?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Fairness Aware Scheduling
- Federated Learning
- Multi Access Edge Computing (MEC)
- Multi Agent Reinforcement Learning (MARL)
- Multipath TCP (MPTCP)
- Permutation Invariance
- Proximal Policy Optimization (PPO)
- Satellite Networks
- Set Transformer
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2783 — Multi agent federated reinforcement learning for Distributed MPTCP Agents

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of Multi access Edge Computing (MEC) with low Earth orbit (LEO) satellite constellations is a promising paradigm for global, low latency connectivity. However, the dynamic topology and heterogeneous link qualities of satellite networks pose significant challenges for efficient multipath transport protocol (MPTCP) scheduling. Traditional schedulers, often based on heuristics or designed for fixed size inputs, struggle to adapt to the variable number of available paths. We propose a novel Multi Agent Federated Reinforcement Learning (MAFRL) framework that leverages Set Transformers for permutation invariant encoding of variable path sets. Each agent learns a local policy using Proximal Policy Optimization (PPO), augmented with a soft fairness constraint to ensure equitable performance. A federated learning scheme, using FedProx aggregation, enables collaborative training across distributed agents without sharing raw data, preserving privacy and improving robustness to non IID data. Extensive emulation experiments show our approach outperforms heuristic and learning-based baselines in aggregate throughput, latency, and fairness, particularly under path variability. This work demonstrates the viability of set-based learning and federated optimization for intelligent resource management in next-generation satellite terrestrial networks. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2783.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
