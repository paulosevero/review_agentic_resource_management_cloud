---
id: paper-2841
title: Multi-Agent Reinforcement Learning with Serverless Computing
authors:
- Wei, Rui
- Yu, Hanfei
- Song, Xikang
- Li, Jian
- Tiwari, Devesh
- Mao, Ying
- Wang, Hao
venue: SoCC 2025 - Proceedings of the 2025 ACM Symposium on Cloud Computing
venue_type: conference
year: 2026
doi: 10.1145/3772052.3772227
url: https://www.scopus.com/pages/publications/105028609214?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 225--239
keywords:
- Cloud Computing
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

# paper-2841 — Multi-Agent Reinforcement Learning with Serverless Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-agent reinforcement learning (MARL) has emerged as a promising approach for tasks requiring multiple agents for cooperation or competition, such as scientific simulation, multi-robot collaboration, and traffic control. Serverless computing, with its dynamic and flexible resource allocation, has demonstrated potential for improving training efficiency and cost-efficiency in RL workloads. However, existing serverless RL training systems focus primarily on single-agent scenarios, overlooking the unique characteristics and inherent complexities of MARL - such as dynamic inter-agent relationships and heterogeneous policy requirements across agents - leaving inefficient and even infeasible support to diverse and complex MARL algorithms.This paper introduces MARLess, the first serverless MARL framework designed to support general MARL algorithms. MARLess decomposes MARL algorithms into serverless functions. It further integrates a dynamic learner sharing mechanism that exploits agent similarities to reduce model update costs and employs actor scaling tailored to MARL tasks, minimizing unnecessary sampling costs based on the data requirements of agents' models. This design optimizes both training efficiency and costs without harming the training quality. Experiments on AWS EC2 testbeds show that MARLess outperforms SOTA MARL baselines with up to 1.27×faster training and 68% cost reduction. Large-scale evaluations on a 15-node cluster with a total of 1,920 vCPUs demonstrate MARLess's scalability and consistent performance under increasing workloads. For a real-world scientific application - turbulent flow simulation, MARLess achieves a 34% cost reduction and 1.1× speedup.  © 2025 Copyright held by the owner/author(s).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2841.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
