---
id: paper-0707
title: Multi-agent QoS-aware autonomic resource provisioning framework for elastic BPM in containerized multi-cloud environment
authors:
- Saif, Mufeed Ahmed Naji
- Niranjan, S.K.
- Murshed, Belal Abdullah Hezam
- Al-ariki, Hasib Daowd Esmail
- Abdulwahab, Hudhaifa Mohammed
venue: Journal of Ambient Intelligence and Humanized Computing
venue_type: journal
year: 2023
doi: 10.1007/s12652-022-04120-4
url: https://www.scopus.com/pages/publications/85141465666?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 12895--12920
keywords:
- Autonomic resource provisioning
- Business process management
- Cloud computing
- Container
- Elasticity
- Multi-cloud
- Multi-objective termite colony optimization
- QoS
- Workload prediction
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
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-0707 — Multi-agent QoS-aware autonomic resource provisioning framework for elastic BPM in containerized multi-cloud environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing enables businesses to improve their market competitiveness, enabling instant and easy access to a pool of virtualized and distributed resources such as virtual machines (VM) and containers for executing their business operations efficiently. Though the cloud enables the deployment and management of business processes (BPs), it is challenging to deal with the enormous fluctuating resource demands and ensure smooth execution of business operations in containerized multi-cloud. Therefore, there is a need to ensure elastic provisioning of resources to tackle the over and under-provisioning problems and satisfy the objectives of cloud providers and end-users considering the quality of service (QoS) and service level agreement (SLA) constraints. In this article, an efficient multi-agent autonomic resource provisioning framework is proposed to ensure the effective execution of BPs in a containerized multi-cloud environment with guaranteed QoS. To improve the performance and ensure elastic resource provisioning, autonomic computing is utilized to monitor the resource usage and predict the future resource demands, then resources are scaled based on demand. Initially, the required resources for executing the incoming workloads are identified by clustering the workloads into CPU and I/O intensive, and the local agent achieves this with the help of an initialization algorithm and K-means clustering. Then, the analysis phase predicts the workload demand using the proposed enhanced deep stacked auto-encoder (EDSAE), further, the containers are scaled based on the prediction outcomes, finally, the multi-objective termite colony optimization (MOTCO) algorithm is used by the global agent to find suitable containers for executing the clustered workloads. The proposed framework has been implemented in the Container Cloudsim platform and evaluated using the business workload traces. The overall simulation results proved the effectiveness of the proposed approach compared to other approaches in terms of SLA violation rate, CPU utilization, response time, execution cost, energy consumption, make-span, and throughput. © 2022, The Author(s), under exclusive licence to Springer-Verlag GmbH Germany, part of Springer Nature.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "autonomic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "autonomic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "autonomic" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0707.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
