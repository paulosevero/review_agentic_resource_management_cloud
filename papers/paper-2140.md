---
id: paper-2140
title: A low-complexity task offloading algorithm for 5G base station energy conservation based on multi-agent reinforcement learning
authors:
- Si, Peishuo
- Li, Yufeng
venue: 2025 International Conference on Aerospace Information Perception and Intelligent Processing, AIPIP 2025
venue_type: conference
year: 2025
doi: 10.1109/AIPIP66876.2025.11299202
url: https://www.scopus.com/pages/publications/105032063306?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 202--208
keywords:
- 5G base station clusters,task offloading,Multi-Agent Reinforcement Learning (MARL),edge computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2140 — A low-complexity task offloading algorithm for 5G base station energy conservation based on multi-agent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the challenges of high energy consumption, high latency, and the inconsistency between algorithmic complexity and the limited computing resources at the edge in task offloading for 5G base station clusters operating under dynamic traffic conditions, this paper presents a low-complexity task offloading framework based on Multi-Agent Reinforcement Learning (MARL). This framework models each base station as an independent agent and uses an Actor-Critic dual-network architecture to generate task offloading and operation mode adjustment actions. By integrating a multi-dimensional state model that combines real-time traffic load, remaining computing resources, the framework enhances resource matching accuracy. Additionally, it utilizes an optimized experience replay mechanism to improve sample sampling and training stability, achieving a coordinated optimization of energy consumption and latency. Simulation experiments show that compared with the full-power operation mode, this method reduces energy consumption by an average of 18.7%, with a slight increase in latency but still significantly better than the low-power operation mode. Compared with the genetic algorithm, energy consumption is reduced by an average of 3.7%, and latency is basically the same under various task loads. Compared with the all-low-power operation mode, latency is reduced by an average of 12.6%, effectively balancing energy efficiency and service quality, and meeting the task processing requirements of 5G dynamic traffic scenarios.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2140.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
