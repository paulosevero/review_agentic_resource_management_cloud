---
id: paper-2724
title: Adaptive Request Scheduling and Load Balancing for Edge Deployed Large Language Models
authors:
- Mou, Fangyi
- Tang, Zhiqing
- Jia, Weijia
- Zhao, Wei
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2026.3665250
url: https://www.scopus.com/pages/publications/105030692754?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- deep reinforcement learning
- Edge computing
- LLM inference
- load balancing
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2724 — Adaptive Request Scheduling and Load Balancing for Edge Deployed Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The inference services of Large Language Models (LLMs) play a crucial role in many fields. Deploying LLMs at the network edge can effectively reduce response latency and enhance domain-specific knowledge. However, due to the dynamic and unpredictable nature of edge user requests and the limited resources of edge servers, improper request scheduling can lead to server load imbalance and increased inference latency. To address this challenge, we model edge LLM inference under dynamic workloads and constrained edge resources by fully considering mutual influences and trade-offs between inference performance, inference latency, and edge resource utilization. We propose a Workload Prediction and Dynamic Request Scheduling (WPDS) algorithm for edge computing environments. The WPDS algorithm first evaluates and prioritizes heterogeneous requests by extracting features and importance scores from user requests. A Transformer-based encoder is used to extract load characteristics of edge servers over different time periods to predict future GPU resource demands. Then, a soft actor-critic reinforcement learning model dynamically schedules requests to appropriate LLM instances, capturing the dynamic relationship between request processing and edge resource utilization from complex state spaces. We evaluate our algorithm in a real Kubernetes-based edge inference prototype system. Experimental results indicate that our approach reduces average inference time by approximately 16.6% compared to the best-performing heuristic baseline algorithm, while also achieving more balanced GPU utilization across edge servers. © 2008-2012 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2724.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
