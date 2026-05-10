---
id: paper-1324
title: 'Towards Network Infrastructure Research for the Era of Large Language Models: Challenges, Practices, and Prospects; [面向大模型时代的网络基础设施研究：挑战、阶段成果与展望]'
authors:
- Zhai, Ennan
- Cao, Jiamin
- Qian, Kun
- Guan, Yu
venue: Jisuanji Yanjiu yu Fazhan/Computer Research and Development
venue_type: journal
year: 2024
doi: 10.7544/issn1000-1239.202440576
url: https://www.scopus.com/pages/publications/85210285646?origin=resultslist
publisher: Science Press
pages: 2664--2677
keywords:
- AI infrastructure
- collective communication
- communication scheduling
- data center networks
- large language model (LLMs)
- large models
- model training
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-1324 — Towards Network Infrastructure Research for the Era of Large Language Models: Challenges, Practices, and Prospects; [面向大模型时代的网络基础设施研究：挑战、阶段成果与展望]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) with hundreds of billions of parameters have brought significant technological and business transformations to today’s AI and cloud services. However, there exists a fundamental difference in network pattern between LLM training and general cloud computing (e.g., Amazon EC2 Elastic compute service), leading to a variety of new challenges. These challenges mainly include load balancing difficulties due to the traffic pattern difference (Challenge 1), the impact of multi-job communication contention on GPU utilization (Challenge 2), and high sensitivity to network failures (Challenge 3). Therefore, data center network technologies designed for general cloud computing (e.g., network architecture, routing, communication scheduling, and reliability) are no longer suitable for LLM training today. This necessitates the development of new data center networks and accompanying technical solutions specifically for LLM training. We introduce Alibaba Cloud’s high-performance network (HPN) and the multi-job communication scheduling approach Crux, designed to address the aforementioned challenges. HPN introduces a two-layer, dual-plane network architecture, which not only achieves high-speed interconnectivity for 15 000 GPUs within a Pod but also ensures precise routing suitable for LLM training (addressing Challenge 1). Furthermore, HPN proposes a novel dual-top-of-rack (ToR) design, replacing the traditional single ToR switch connection in data center networks and fundamentally avoiding single-point failure reliability risks (partially addressing Challenge 3). To tackle Challenge 2, Crux reduces the NP-complete problem of optimizing GPU utilization by modeling it as a communication scheduling issue related to GPU computational intensity. Crux then proposes an algorithm that prioritizes the flows of job with higher GPU computational intensity, significantly reducing multi-job communication contention and improving GPU utilization. Compared with the state-of-the-art efforts, Crux increases GPU utilization by up to 23%. Both HPN and Crux have been deployed and used in Alibaba Cloud production for over eight months and will continue to evolve and iterate. Building on this, we further envision possible research directions in the field of LLM training and inference, providing guidance for subsequent work. © 2024 Science Press. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1324.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
