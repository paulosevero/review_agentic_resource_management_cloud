---
id: paper-0384
title: Combined use of coral reefs optimization and multi-agent deep Q-network for energy-aware resource provisioning in cloud data centers using DVFS technique
authors:
- Asghari, Ali
- Sohrabi, Mohammad Karim
venue: Cluster Computing
venue_type: journal
year: 2022
doi: 10.1007/s10586-021-03368-3
url: https://www.scopus.com/pages/publications/85112178134?origin=resultslist
publisher: Springer
pages: 119--140
keywords:
- Cloud computing
- Coral reefs optimization
- Deep Q-network
- Energy-aware
- Resource management
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
    my_justification: RL
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

# paper-0384 — Combined use of coral reefs optimization and multi-agent deep Q-network for energy-aware resource provisioning in cloud data centers using DVFS technique

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Big data processing, scientific calculations, and multimedia operations are some applications that require very complex time-consuming computations which cannot be performed on personal computers. Utilizing powerful cloud resources is a common method to address this problem. The amount of energy consumption of cloud data centers is an important challenge in these complex calculations, and reducing the energy consumption of cloud data centers is one of the most important goals of the researches in this area. The proposed method of this paper, called multi-agent deep Q-network with coral reefs optimization (MDQ-CR), combines the coral reefs optimization algorithm and multi-agent deep Q-network to reduce the energy consumption of data centers and cloud resources using the dynamic voltage and frequency scaling (DVFS) technique. The MDQ-CR has two main phases. The first phase exploits coral reefs optimization algorithm with a short-term view, and the second phase uses deep Q-network with a long-term view. The Markov game model is used to lead the learning agents to converge to the global optimal solution. Since processors consume the highest amount of energy of cloud compared to the other resources, the proposed method focuses on reducing the processors’ energy consumption. Reducing the voltage and frequency of processors, considering expiration times of their tasks, can reduce their energy consumption significantly. The empirical experiments show that the proposed method can save energy about 89% compared to completely randomized methods, and about 20% compared to the two recent methods of the literature. © 2021, The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0384.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
