---
id: paper-1339
title: A Socialized Learning-Based Scheduling Framework in Intricate Edge Clouds
authors:
- Zhao, Yunfeng
- Wang, Ziwei
- Qiu, Chao
- He, Qiang
- Niyato, Dusit
- Wang, Xin
- Wang, Xiaofei
- Hu, Qinghua
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2024
doi: 10.1109/TSC.2024.3403048
url: https://www.scopus.com/pages/publications/85194043095?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3092--3109
keywords:
- Deep reinforcement learning
- edge computing
- edge-cloud collaboration
- request dispatch
- service orchestration
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

# paper-1339 — A Socialized Learning-Based Scheduling Framework in Intricate Edge Clouds

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing has emerged as a powerful paradigm for efficient scheduling at the network edge to fulfill users' requirements for low latency. Edge servers' and clouds' ability to interact allows them to leverage edge servers' limited computing and storage resources collectively to handle all requests collaboratively. This has unlocked the potential of the edge-cloud system. However, its sophistication (e.g., heterogeneous resources, intertwined dependencies, etc.) also raised unforeseen challenges in request dispatch and service orchestration phases within the scheduling process, including complex hierarchy, limited cooperation and unfocused information. Traditional resource optimization methods for edge-cloud systems cannot address these intricate situations properly, raising concerns over system efficiency, stability, and costs. This article proposes learning-based methods to accommodate time-varying requests and dynamic service prevalence. Specifically, we employ the multi-agent advantage actor-critic (MAA2C) and the graph convolutional networks-based MAA2C (GCN-MAA2C) in two phases, respectively, to enhance individual intelligence and facilitate optimal dispatch and orchestration decisions. Inspired by the regulations in human society, we propose SocialEdge, a socialized learning-based scheduling framework for the edge-cloud system. To leverage the hierarchical correlation, we develop an inter-layer socialized refining mechanism. The inference results from one layer guide the training process of the next layer, enabling the abstraction of optimization-critical knowledge. Moreover, we apply intra-layer socialized cooperating, where federated averaging with MAA2C is implemented to ensure the cooperation of individuals over private data for achieving optimal global solutions. Furthermore, we propose a socialized resonance mechanism across the layers to extract high-value information and induce resonance toward the system objective, aiming to improve the efficiency of scheduling. Experimental evaluations on a proof-of-concept testbed and two real traces demonstrate that SocialEdge reduces scheduling cost by 11.2% while enhancing time efficiency by 77.4%, and system throughput by 17.9%, compared to baseline methods.  © 2008-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1339.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
