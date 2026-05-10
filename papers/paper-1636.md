---
id: paper-1636
title: Dual-Circulation Generative AI for Optimizing Resource Allocation in Multi-Granularity Heterogeneous Federated Learning
authors:
- He, Wenji
- Yao, Haipeng
- Ren, Xiaoxu
- Ouyang, Tianhao
- Xiong, Zehui
- He, Yuan
- Liu, Yunhao
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TCCN.2025.3542862
url: https://www.scopus.com/pages/publications/105002487379?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 817--831
keywords:
- Clustered federated learning
- generative artificial intelligence
- generative diffusion models
- heterogeneous data
- resource optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: LLM as workload
    winning_category: llm_as_workload
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
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

# paper-1636 — Dual-Circulation Generative AI for Optimizing Resource Allocation in Multi-Granularity Heterogeneous Federated Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid proliferation of Internet of Things (IoT) devices and the deployment of edge computing infrastructures have significantly advanced data processing and network communications. Federated Learning (FL), leveraging these developments, offers a decentralized approach to learning across edge devices while preserving local privacy. However, traditional FL paradigms encounter challenges related to non-IID data distributions, diverse computational capabilities of edge devices, and multimodal tasks. This paper proposes a novel Dual-Circulation Generative Artificial Intelligence (GAI) framework for Clustered Federated Learning (GAI-CFL), designed to address multi-granularity heterogeneity including data, resources, and task heterogeneity. The GAI-CFL framework integrates Generative Diffusion Models (GDMs) and Reinforcement Learning (RL) strategies to optimize data generation and resource allocation processes. GAI techniques are employed to reduce intra-cluster data heterogeneity by generating data, thereby enriching local datasets and enhancing model convergence. To address inter-cluster data and task heterogeneity, a dual-circulation optimization strategy is implemented, utilizing RL with GDMs to generate optimal strategies based on input data characteristics dynamically. Additionally, a Mixture of Experts (MoE) approach is incorporated within GDMs to select the best expert models for denoising steps, ensuring efficient data generation strategies. Comprehensive simulations clarify that the proposed GAI-CFL framework significantly presents benchmark schemes, achieving lower energy consumption and enhanced system performance under the same delay and performance constraints. © 2015 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative Artificial Intellig" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Generative AI for Optimizing R" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative Artificial Intellig" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1636.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
