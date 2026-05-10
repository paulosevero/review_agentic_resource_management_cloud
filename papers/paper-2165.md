---
id: paper-2165
title: Intelligent Load Balancing for AI-Enhanced Edge-Cloud Architectures
authors:
- Sowmya, H.D.
- George Fernandez, I.
- Mondal, Soumadip
venue: Proceedings - 2025 International Conference on Recent Innovation in Science Engineering and Technology, ICRISET 2025
venue_type: conference
year: 2025
doi: 10.1109/ICRISET64803.2025.11252490
url: https://www.scopus.com/pages/publications/105031409484?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Artificial Intelligence (AI)
- Context-Aware Decision Making
- Distributed Computing
- Edge-Cloud Collaboration
- Federated Learning
- Internet of Things (IoT)
- Latency Reduction
- Load Balancing
- Multi-Agent Reinforcement Learning (MARL)
- Network Optimization
- Quality of Service (QoS)
- Real-Time Analytics
- Reinforcement Learning (RL)
- Resource Allocation
- Traffic Forecasting
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

# paper-2165 — Intelligent Load Balancing for AI-Enhanced Edge-Cloud Architectures

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As Internet of Things (IoT) devices expand exponentially and surge in latency-sensitive and bandwidth-intensive applications like autonomous driving, augmented reality (AR), and real-time video analytics affect them, traditional centralized cloud computing models are running across major scalability and performance bottlenecks more and more. These limitations arise from natural network latencies, back haul congestion, and decreased responsiveness when servicing distributed end- customers over geographically dispersed sites. To address these challenges, edge-cloud collaborative architectures - which seamlessly mix scattered edge computing resources with centralized cloud data centers - have become a viable solution. This hybrid architecture permits localized data processing at the network edge while employing the computational scalability and storage capacity of the cloud for non-time-sensitive operations. Mostly due to highly dynamic network conditions, inconsistent workload variations, changing user demand patterns, and the different computational and storage capabilities of edge nodes against cloud servers, achieving an optimal load distribution across heterogeneous edge and cloud environments is still a non-trivial challenge. The current study offers AI-driven adaptive load balancing solutions by using reinforcement learning (RL) and machine learning (ML) methods to dynamically coordinate the distribution of work in real time. The suggested system combines predictive analysis models for predicting traffic, resource use, and service demand using both historical and real-time telemetry data. This makes it easier to make decisions ahead of time. The system also has context-aware decision engines that change load balancing policies on the fly by keeping an eye on key performance indicators (KPIs) like latency, throughput, energy use, and Quality of Service (QoS) levels. In this paper, we show a load balancer based on multi-agent reinforcement learning (MARL). It uses distributed agents that learn the best ways to allocate load by interacting with the environment and getting feedback on performance measures. To control the heterogeneity of the edge-cloud architecture, our approach integrates federated learning models that enable privacy-preserving training across geographically distributed edge nodes while lowering inter-node communication costs. Experimental results obtained through extensive simulations on a heterogeneous edge-cloud testbed show that the proposed AI-enabled adaptive load balancing framework considerably improves resource usage, reduces end-to-end latency, increases service availability, and maintains QoS under varying network load scenarios when compared to conventional heuristic-based load balancing algorithms.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2165.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
