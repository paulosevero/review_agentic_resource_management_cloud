---
id: paper-2909
title: Eco-efficient task scheduling for MLLMs in edge-cloud continuum
authors:
- Zhang, Manjun
- Wang, Ying
- Yu, Peng
- Qiu, Xuesong
- Guo, Shaoyong
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2026.112257
url: https://www.scopus.com/pages/publications/105034384222?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Eco-efficient computing
- Edge-cloud continuum
- GAT
- Green energy utilization
- MAPPO
- MLLM Task scheduling
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
    my_justification: LLM as workload
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

# paper-2909 — Eco-efficient task scheduling for MLLMs in edge-cloud continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Task scheduling for multimodal large language model (MLLM) applications in edge-cloud continuum faces critical challenges, as they simultaneously balance system delay, carbon emissions, and model accuracy requirements, while adapting to network conditions and varying energy availability. To address this, we formulate a joint optimization problem integrating MLLM task scheduling, resource allocation, and green energy utilization to minimize system delay and carbon emissions while meeting strict accuracy requirements. A Green-Aware MAPPO scheduling approach is proposed, which fuses graph attention networks (GAT) with multi-agent proxy policy optimization (MAPPO) to enable distributed decision-making in edge-cloud continuum. By modeling the problem as a partially observable Markov decision process (POMDP), the approach allows edge or cloud servers to capture complex resource dependencies through relation-specific attention mechanisms, even with limited local observations. Experiments across diverse network configurations show that compared with baseline algorithms such as MADDPG, MADQN, and DDPG, the proposed method reduces system delay by 28.3%-66.7%, energy consumption by 17.9%-47.4%, carbon emissions by 11.6%-63.5%, and overall SLA violation rate by 22.21%-73.7% and maintaining MLLM task accuracy above the required threshold. This work provides an effective solution for balancing performance and sustainability in MLLM-enabled edge-cloud continuum. © 2026

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2909.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
