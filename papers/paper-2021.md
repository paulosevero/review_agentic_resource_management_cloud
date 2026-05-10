---
id: paper-2021
title: Decentralized Multi-Agent Reinforcement Learning for the Green Serverless Cloud-Edge Continuum
authors:
- Patel, Yashwant Singh
- Choubey, Anurag
- Singh, Anil
- Townend, Paul
venue: Proceedings - 19th IEEE International Conference on Service-Oriented System Engineering, SOSE 2025
venue_type: conference
year: 2025
doi: 10.1109/SOSE67019.2025.00017
url: https://www.scopus.com/pages/publications/105016114830?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 108--117
keywords:
- Cloud-Edge Continuum
- Function-as-a-Service
- Green Computing
- Multi-Agent Reinforcement Learning
- Serverless Computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2021 — Decentralized Multi-Agent Reinforcement Learning for the Green Serverless Cloud-Edge Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Cloud-Edge Continuum systems are inherently complex and massive, often featuring federated multi-provider stakeholders (e.g. cloud/edge service providers, energy providers), heterogeneous platforms, and dynamic infrastructures; this significantly increases the complexity of developing, deploying, and managing applications. The Serverless computing offers a powerful tool to simplify and speed up the Continuum application development. However, existing scheduling mechanisms for Serverless platforms focus primarily on performance metrics such as latency, model accuracy, and throughput, often neglecting critical factors such as energy efficiency and sustainability. This gap is further exacerbated in Continuum environments, where computational nodes may rely on unpredictable and intermittent green energy sources, leading to availability bottlenecks and energy constraints. This work investigates the design of a decentralized green energy-aware approach for scheduling Serverless functions across the Cloud-Edge Continuum. To achieve this, we introduce a formal model of the green energy-aware workload scheduling problem. We then develop a consensus-based upper confidence bound (UCB) approach for cooperative multi-agent reinforcement learning (MARL) that leverages distributed agents to consider energy awareness and quality-of-service (QoS) requirements of different functions into their scheduling decisions. To demonstrate the practicality of our approach, we implement a real-world prototype using a cluster of Raspberry Pis, Cloud servers, Kubernetes, and OpenFaaS. Experimental results show that our approach maximizes the green energy utilization by (44%) and reduces total latency by (25%) compared to the centralized technique, highlighting its energy efficiency, scalability, and overall sustainability in Continuum settings.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2021.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
