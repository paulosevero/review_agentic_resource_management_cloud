---
id: paper-2846
title: A QoE-Driven Personalized Incentive Mechanism Design for AIGC Services in Resource-Constrained Edge Networks
authors:
- Wu, Hongjia
- Xu, Minrui
- Xiong, Zehui
- Gao, Lin
- Pan, Haoyuan
- Niyato, Dusit
- Chan, Tse-Tin
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3625263
url: https://www.scopus.com/pages/publications/105019931476?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4121--4137
keywords:
- Generative AI (GAI)
- incentive mechanism
- mobile edge computing (MEC)
- multi-dimensional quality of experience (QoE)
- resource allocation
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
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
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2846 — A QoE-Driven Personalized Incentive Mechanism Design for AIGC Services in Resource-Constrained Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With rapid advancements in large language models (LLMs), AI-generated content (AIGC) has emerged as a key driver of technological innovation and economic transformation. Personalizing AIGC services to meet individual user demands is essential but challenging for AIGC service providers (ASPs) due to the subjective and complex demands of mobile users (MUs), as well as the computational and communication resource constraints faced by ASPs. To tackle these challenges, we first develop a novel multi-dimensional quality-of-experience (QoE) metric. This metric comprehensively evaluates AIGC services by integrating accuracy, token count, and timeliness. We focus on a mobile edge computing (MEC)-enabled AIGC network, consisting of multiple ASPs deploying differentiated AIGC models on edge servers and multiple MUs with heterogeneous QoE requirements requesting AIGC services from ASPs. To incentivize ASPs to provide personalized AIGC services under MEC resource constraints, we propose a QoE-driven incentive mechanism. We formulate the problem as an equilibrium problem with equilibrium constraints (EPEC), where MUs as leaders determine rewards, while ASPs as followers optimize resource allocation. To solve this, we develop a dual-perturbation reward optimization algorithm, reducing the implementation complexity of adaptive pricing. Experimental results demonstrate that our proposed mechanism achieves a reduction of approximately 64.9% in average computational and communication overhead, while the average service cost for MUs and the resource consumption of ASPs decrease by 66.5% and 76.8%, respectively, compared to state-of-the-art benchmarks. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2846.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
