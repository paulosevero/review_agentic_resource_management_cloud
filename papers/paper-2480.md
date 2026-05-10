---
id: paper-2480
title: 'Birds in Cages: Edge Inference Allocation for Distributed LLM Deployment'
authors:
- Zhu, Jiahao
- Zhao, Lu
- Xiao, Fu
- Duan, Lingjie
venue: IEEE International Workshop on Quality of Service, IWQoS
venue_type: conference
year: 2025
doi: 10.1109/IWQoS65803.2025.11143464
url: https://www.scopus.com/pages/publications/105016993620?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Approximate Algorithm
- Distributed LLM Inference
- Edge Computing
- Inference Allocation
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

# paper-2480 — Birds in Cages: Edge Inference Allocation for Distributed LLM Deployment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The distributed deployment of Large Language Models (LLM) on edge servers close to users has unlocked the service provider's potential to deliver low-latency inference. To obtain more benefit by serving more resource-demanding inference tasks based on resource-limited edge servers, it is critical for the service provider to allocate inference to suitable edge servers. Three new challenges hinder existing approaches from being implemented: the distributed LLM inference requires edge servers to collaborate following a novel workflow different from other tasks; the generative nature of LLM incurs uncertainty in task resource occupations; considering the heterogeneity in users' latency requirements and service benefit, merely minimizing the total user-perceived latency can not maximize the benefit. In this paper, we make the first attempt to study the edge inference allocation problem for distributed LLM deployment while conquering these challenges. Specifically, we propose a collaborative workflow for edge servers to conduct distributed LLM inferences. Then, we estimate the resource occupations by employing Exact Conic Reformulation (ECR). Based on this, with the objective of maximizing the total service benefit, we formulate the inference allocation problem as a binary integer programming problem which is NP-hard. An approximate algorithm is proposed to find approximate solutions efficiently. Extensive experiments based on a real-world dataset demonstrate the performance of our approach. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2480.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
