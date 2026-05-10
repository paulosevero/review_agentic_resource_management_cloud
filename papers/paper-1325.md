---
id: paper-1325
title: A Method for Joint Edge Server Deployment and Service Placement
authors:
- Zhang, Junna
- Han, Chaochen
- Chen, Jiawei
- Zhao, Xiaoyan
- Yuan, Peiyan
venue: Jisuanji Gongcheng/Computer Engineering
venue_type: journal
year: 2024
doi: 10.19678/j.issn.1000-3428.0068576
url: https://www.scopus.com/pages/publications/85210251812?origin=resultslist
publisher: Editorial Office of Computer Engineering
pages: 266--280
keywords:
- Edge Computing(EC)
- Edge Server(ES) deployment
- k-means clustering algorithm
- multi-agent reinforcement learning algorithm
- service placement
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

# paper-1325 — A Method for Joint Edge Server Deployment and Service Placement

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge Computing (EC) deploys Edge Servers (ES) at the edge of the network close to the user. Services are placed on the ES to meet users' service needs. Several independent studies have been conducted on ES deployment and service placement. However, a highly coupled relationship exists between the two and they should be studied simultaneously. In addition, the economic benefit of the EC system is a consideration because paid services must be provided for the EC system to earn revenue in processing user service requests; however, the EC system incurs delays and energy costs when processing the user service requests. To maximize the benefits of the EC system under the constraint that user service requests and service prices are different, appropriate service placement solutions are required to increase the overall profit. To that end, this study considers the constraints of the location relationship between ES and base stations, coupling relationship between ES deployment and service placement, number of service replicas, and price of the service and proposes a two-step approach that includes an improved k-means algorithm and a multi-agent reinforcement learning algorithm. The goal is to maximize the benefits of EC systems. First, a joint ES deployment and service placement model is constructed. One of the ES deployments explicitly considers the location relationship between base stations, whereas service placement considers the location of ES deployments as well as different service requests and pricing. Subsequently, based on the location relationship of base stations and service request load of base stations, the k-means algorithm is used under constraints to determine the optimal deployment location and collaborative domain of ES under different constraint conditions. Finally, to maximize the benefits of the EC system, a multi-agent reinforcement learning algorithm is used to place services on the ES. The experimental results show that the proposed algorithm increases the benefits by 7% to 23% relative to the comparison algorithms. © 2024, Editorial Office of Computer Engineering. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1325.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
