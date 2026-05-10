---
id: paper-2030
title: A Hybrid Forecasting and Reinforcement Learning Approach for Latency-Constrained Scaling of Generative AI Systems
authors:
- Peng, Yue
- Sinnott, Richard
venue: Proceedings of the 18th IEEE/ACM International Conference on Utility and Cloud Computing, UCC 2025
venue_type: conference
year: 2025
doi: 10.1145/3773274.3774258
url: https://www.scopus.com/pages/publications/105027154636?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: ''
keywords:
- Generative AI
- GPU Sharing
- Kubernetes
- Reinforcement Learning
- Time Series Forecasting
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2030 — A Hybrid Forecasting and Reinforcement Learning Approach for Latency-Constrained Scaling of Generative AI Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing popularity of generative AI applications has introduced new challenges in how to effectively utilize hardware (GPUs). As generative AI models become more widely adopted, optimising the deployment of models emerges as a critical concern due to the substantial computational overheads, variable workloads, and the need for low-latency inference of many AI applications needing GPUs with often limited availability. In this paper, we investigate strategies for the efficient deployment of a text-to-image application, treating the underlying generative model as a black box. Leveraging Kubernetes and the Ray distributed computing framework, we explore the integration of NVIDIA GPU sharing techniques to improve resource utilization and train an auto-scaling agent using Proximal Policy Optimization (PPO) reinforcement learning with time-series forecasting enhancements to tackle real-world workloads. We identify that our forecasting-enhanced PPO agent outperforms traditional threshold-based strategies by reducing the number of required replicas and better adapting to fluctuating user demand, whilst exhibiting reduced latency and requiring fewer provisioning operations in scenarios with long replica startup times. © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2030.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
