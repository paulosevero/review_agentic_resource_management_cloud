---
id: paper-1914
title: A 5G Computing-Network-Storage Collaborative Scheduling Method for Edge Intelligence in Power Systems
authors:
- Luo, Shijun
- Liao, Hui
- Xiao, Renjie
- Xiao, Zhaokai
venue: 2025 6th International Conference on Artificial Intelligence and Computer Engineering, ICAICE 2025
venue_type: conference
year: 2025
doi: 10.1109/ICAICE68195.2025.11382401
url: https://www.scopus.com/pages/publications/105034832273?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 747--751
keywords:
- Computing-Network-Storage
- Edge Computing
- Federated Learning
- Multi-Agent Reinforcement Learning
- Resource Scheduling
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1914 — A 5G Computing-Network-Storage Collaborative Scheduling Method for Edge Intelligence in Power Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The widespread adoption of high-real-time intelligent services in new power systems faces a critical challenge: the bottleneck of "siloed"resource scheduling. This occurs when computational, network, and storage resources lack cross-domain coordination, resulting in low resource utilization and increased end-to-end latency. This paper proposes a 5G computation-network-storage (CNS) collaborative scheduling method for power edge systems to maximize service quality (QoS) and resource efficiency. The core of this solution is a "perception-prediction-decision"intelligent closed-loop framework: First, integrated federated learning (FL) aggregates edge node data to achieve distributed, privacy-preserving high-precision load prediction. Next, prediction results feed into a multi-agent deep reinforcement learning (MADRL) model - specifically the MADPG algorithm - which abstracts edge servers and 5G controllers as collaborative agents. Through joint learning, it generates globally optimal integrated CNS allocation strategies. Simulation results for typical video analysis scenarios demonstrate that compared to the computation-network separation baseline strategy, the proposed method reduces average service processing latency by 41.2% and increases edge server resource utilization by 25%. Furthermore, relative to the pure storage baseline strategy, the FL-MADRL framework significantly enhances system sustainability by reducing total energy consumption by 20.0%. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1914.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
