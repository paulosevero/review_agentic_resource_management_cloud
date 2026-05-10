---
id: paper-2162
title: Multi-Objective Resource Optimization in UAV-Enabled Heterogeneous Cellular Networks Using Serverless Federated Learning and Power-Domain NOMA
authors:
- Song, Qinghua
- Yang, Junru
- Mohajer, Amin
venue: Transactions on Emerging Telecommunications Technologies
venue_type: journal
year: 2025
doi: 10.1002/ett.70210
url: https://www.scopus.com/pages/publications/105011280738?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- backhaul traffic optimization
- cell-free communication
- intelligent reflecting surfaces
- multi-agent deep learning
- resource management
- UAV-enabled networks
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2162 — Multi-Objective Resource Optimization in UAV-Enabled Heterogeneous Cellular Networks Using Serverless Federated Learning and Power-Domain NOMA

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of unmanned aerial vehicles (UAVs) into cellular networks has emerged as a promising solution to enhance connectivity and service quality in both urban and remote areas. In this paper, we propose a comprehensive framework that combines multi-agent deep learning with backhaul traffic optimization to effectively manage resources in UAV-enabled communication networks. By leveraging the capabilities of intelligent reflecting surfaces (IRS) and cell-free communication strategies, our approach aims to optimize backhaul traffic, ensuring seamless data transmission and improved network throughput. Our methodology involves a dynamic resource allocation mechanism that utilizes multi-agent deep learning to accurately predict network demands and adaptively allocate resources. The process begins with the collection of real-time network data, including user demand, traffic patterns, and UAV positions. This data is then fed into a deep learning model, where multiple agents collaboratively analyze and predict future network requirements. Based on the predictions, the resource allocation mechanism dynamically adjusts the distribution of resources, such as bandwidth and power, to meet the anticipated demand. This adaptive strategy enables the network to efficiently handle varying traffic loads, reducing congestion and latency. Furthermore, our backhaul traffic optimization technique focuses on minimizing the energy consumption of UAVs while maximizing their coverage and connectivity. By optimizing the flight paths and altitudes of UAVs, we ensure that they provide optimal coverage with minimal energy expenditure. Additionally, the IRS-assisted communication further enhances signal quality, reducing the need for high-power transmissions and thus conserving energy. Our simulations show that our framework improves network throughput, energy efficiency, and reliability. It offers a promising way to manage resources in future UAV-enabled communication networks. © 2025 John Wiley & Sons Ltd.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2162.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
