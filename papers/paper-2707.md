---
id: paper-2707
title: 'Task Offloading Based on Virtual Network Embedding in Software-Defined Edge Networks: A Deep Reinforcement Learning Approach'
authors:
- Ma, Lixin
- Zhang, Peiying
- Chen, Ning
venue: Information (Switzerland)
venue_type: journal
year: 2026
doi: 10.3390/info17030278
url: https://www.scopus.com/pages/publications/105034105068?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- deep reinforcement learning
- edge computing
- software-defined network
- task offloading
- virtual network embedding
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
    my_justification: RL
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

# paper-2707 — Task Offloading Based on Virtual Network Embedding in Software-Defined Edge Networks: A Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The advent of 5G/6G technologies and the pervasive deployment of IoT devices are driving the emergence of demanding applications that necessitate ultra-low latency, high bandwidth, and significant computational power. Traditional cloud computing models fall short in meeting these stringent requirements. To address this, Software-Defined Edge Networks (SDENs) have emerged as a promising architecture, yet efficiently managing their heterogeneous and geographically distributed resources poses substantial challenges for optimal application provisioning. In response, this paper proposes a novel framework for intelligent task offloading, which reframes the intricate multi-component application task offloading problem as a Virtual Network Embedding (VNE) challenge within a SDEN environment. We introduce a comprehensive model where complex applications are represented as Virtual Network Requests (VNRs). In this model, each VNR consists of virtual nodes that demand specific computing and storage resources, as well as virtual links that demand specific bandwidth and must adhere to maximum tolerable delay constraints. To dynamically solve this NP-hard VNE problem in the face of stochastic VNR arrivals and dynamic network conditions, we leverage Deep Reinforcement Learning (DRL). Specifically, a Soft Actor-Critic (SAC) agent is employed at the SDN controller. This agent learns a sequential decision-making policy for mapping virtual nodes to physical edge servers and virtual links to network paths. To guide the agent towards efficient resource utilization, we define the reward for each successful embedding as the long-term revenue-to-cost ratio. By learning to maximize this reward, the agent is naturally driven to find economically viable allocation strategies. Comprehensive simulation experiments demonstrate that our SAC-based VNE approach significantly outperforms other baselines across key metrics, affirming its efficacy in dynamic SDEN environments. © 2026 by the authors.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2707.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
