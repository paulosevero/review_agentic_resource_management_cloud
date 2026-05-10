---
id: paper-1054
title: A Multi-Agent Reinforcement Learning-Based Task-Offloading Strategy in a Blockchain-Enabled Edge Computing Network
authors:
- Liu, Chenlei
- Sun, Zhixin
venue: Mathematics
venue_type: journal
year: 2024
doi: 10.3390/math12142264
url: https://www.scopus.com/pages/publications/85199914521?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- blockchain
- mobile edge computing
- multi-agent reinforcement learning
- task offloading
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

# paper-1054 — A Multi-Agent Reinforcement Learning-Based Task-Offloading Strategy in a Blockchain-Enabled Edge Computing Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, many mobile edge computing network solutions have enhanced data privacy and security and built a trusted network mechanism by introducing blockchain technology. However, this also complicates the task-offloading problem of blockchain-enabled mobile edge computing, and traditional evolutionary learning and single-agent reinforcement learning algorithms are difficult to solve effectively. In this paper, we propose a blockchain-enabled mobile edge computing task-offloading strategy based on multi-agent reinforcement learning. First, we innovatively propose a blockchain-enabled mobile edge computing task-offloading model by comprehensively considering optimization objectives such as task execution energy consumption, processing delay, user privacy metrics, and blockchain incentive rewards. Then, we propose a deep reinforcement learning algorithm based on multiple agents sharing a global memory pool using the actor–critic architecture, which enables each agent to acquire the experience of another agent during the training process to enhance the collaborative capability among agents and overall performance. In addition, we adopt attenuatable Gaussian noise into the action space selection process in the actor network to avoid falling into the local optimum. Finally, experiments show that this scheme’s comprehensive cost calculation performance is enhanced by more than 10% compared with other multi-agent reinforcement learning algorithms. In addition, Gaussian random noise-based action space selection and a global memory pool improve the performance by 38.36% and 43.59%, respectively. © 2024 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1054.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
