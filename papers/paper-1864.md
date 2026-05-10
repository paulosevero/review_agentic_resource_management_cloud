---
id: paper-1864
title: A Parallel Service Function Chain Deployment Method Combining Federated Learning and Deep Reinforcement Learning
authors:
- Liu, Guangyuan
- Du, Jie
- Pang, Ziyuan
venue: Hsi-An Chiao Tung Ta Hsueh/Journal of Xi'an Jiaotong University
venue_type: journal
year: 2025
doi: 10.7652/xjtuxb202509011
url: https://www.scopus.com/pages/publications/105021317568?origin=resultslist
publisher: Xi'an Jiaotong University
pages: 110--121
keywords:
- deep reinforcement learning
- dynamic deployment
- federated averaging
- multi-domain edge cloud networks
- parallel service function chain
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
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1864 — A Parallel Service Function Chain Deployment Method Combining Federated Learning and Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the dynamic deployment of parallel service function chains (SFCs) in multi-domain edge cloud networks, this paper constructs an optimized parallel SFC architecture and proposes a novel approach combining federated learning (FedAvg) and deep reinforcement learning (DRL), termed FA-D3QN-PER. This method resolves the issues of imbalanced resource allocation and privacy leakage inherent in existing single-agent DRL and centralized decision-making frameworks when handling SFC partitioning and deployment. By enabling independent training of agents within each domain and leveraging FedAvg for model parameter sharing, it optimizes global strategies while preserving data privacy. The deployment phase involves the analysis and optimization of the hybrid SFC parallel structure; intelligent partitioning of the optimized hybrid SFC into sub-chains and their allocation to suitable edge domains; mapping of virtual network functions (VNFs) within each sub-chain to physical nodes in target domains. Simulation results demonstrate that the FA-D3QN-PER method exhibits strong stability and fast convergence, significantly improving SFC deployment acceptance rates while effectively reducing average latency and total costs. Compared to FA-DQN, DFSC, and MuL, the FA-D3QN-PER method increases acceptance rates by 11.6%, while reducing average latency and total costs by 17% and 18.56%, respectively. © 2025, Xi'an Jiaotong University. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1864.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
