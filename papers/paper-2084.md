---
id: paper-2084
title: A hybrid swarm intelligence approach for optimizing Multimodal Large Language Models deployment in edge-cloud-based Federated Learning environments
authors:
- Rjoub, Gaith
- Elmekki, Hanae
- Islam, Saidul
- Bentahar, Jamal
- Dssouli, Rachida
venue: Computer Communications
venue_type: journal
year: 2025
doi: 10.1016/j.comcom.2025.108152
url: https://www.scopus.com/pages/publications/105001939471?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Ant Colony Optimization
- Edge-cloud computing
- Federated Learning
- Large Multimodal Models
- Particle Swarm Optimization
- Resource optimization
- Swarm intelligence
- Unmanned Vehicle System
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

# paper-2084 — A hybrid swarm intelligence approach for optimizing Multimodal Large Language Models deployment in edge-cloud-based Federated Learning environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The combination of Federated Learning (FL), Multimodal Large Language Models (MLLMs), and edge-cloud computing enables distributed and real-time data processing while preserving privacy across edge devices and cloud infrastructure. However, the deployment of MLLMs in FL environments with resource-constrained edge devices presents significant challenges, including resource management, communication overhead, and non-IID data. To address these challenges, we propose a novel hybrid framework wherein MLLMs are deployed on edge devices equipped with sufficient resources and battery life, while the majority of training occurs in the cloud. To identify suitable edge devices for deployment, we employ Particle Swarm Optimization (PSO), and Ant Colony Optimization (ACO) is utilized to optimize the transmission of model updates between edge and cloud nodes. This proposed swarm intelligence-based framework aims to enhance the efficiency of MLLM training by conducting extensive training in the cloud and fine-tuning at the edge, thereby reducing energy consumption and communication costs. The framework is particularly applicable in Unmanned Vehicle System (UVS)-based edge-cloud computing environments, where efficient resource management and real-time decision-making are critical for autonomous operations. The autonomous nature of UVS requires efficient resource management and a reliable communication system. The proposed swarm intelligence-based framework aims to satisfy these requirements through optimized edge device selection, while minimizing communication overhead. Our experimental results show that the proposed method significantly improves system performance, achieving an accuracy of 92%, reducing communication cost by 30%, and enhancing client participation compared to traditional FL methods. These results make the proposed approach highly suitable for large-scale edge-cloud computing systems. © 2025 The Authors

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2084.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
