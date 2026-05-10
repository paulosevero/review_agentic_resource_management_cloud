---
id: paper-1748
title: Small Language Model-Guided Quantile Temporal Difference Learning for Improved IoT Application Placement in Fog Computing
authors:
- Krishnamurthy, Bhargavi
- Shiva, Sajjan G.
venue: Mathematics
venue_type: journal
year: 2025
doi: 10.3390/math13172768
url: https://www.scopus.com/pages/publications/105015400811?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- application placement
- fog computing
- quantile temporal difference learning
- small language model
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
  05-abstract-screening: include
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
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

# paper-1748 — Small Language Model-Guided Quantile Temporal Difference Learning for Improved IoT Application Placement in Fog Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The global market for fog computing is expected to reach USD 6385 million by 2032. Modern enterprises rely on fog computing since it offers computational resources at edge devices through decentralized computation mechanisms. One of the crucial components of fog computing is the proper placement of applications on fog nodes (edge devices, Internet of Things (IoT)) for servicing. Large-scale, geographically distributed fog networks and heterogeneity of fog nodes make application placement a challenging task. Quantile Temporal Difference Learning (QTDL) is a promising distributed form of a reinforcement learning algorithm. It is superior compared to traditional reinforcement learning as it learns the act of prediction based on the full distribution of returns. QTDL is enriched by a small language model (SLM), which results in low inference latency, reduced costs of operation, and also enhanced rates of learning. The SLM, being a lightweight model, has policy-shaping capability, which makes it an ideal choice for the resource-constrained environment of edge devices. The data-driven quantiles of temporal difference learning are blended with the informed heuristics of the SLM to prevent quantile loss and over- or underestimation of the policies. In this paper, a novel SLM-guided QTDL framework is proposed to perform task scheduling among fog nodes. The proposed framework is implemented using the iFogSim simulator by considering both certain and uncertain fog computing environments. Further, the results obtained are validated using expected value analysis. The performance of the proposed framework is found to be satisfactory with respect of the following performance metrics: energy consumption, makespan time violations, budget violations, and load imbalance ratio. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Small Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "small language model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "SLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "SLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "SLM" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1748.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
