---
id: paper-0759
title: Reinforcement Learning Based Energy-Efficient Collaborative Inference for Mobile Edge Computing
authors:
- Xiao, Yilin
- Xiao, Liang
- Wan, Kunpeng
- Yang, Helin
- Zhang, Yi
- Wu, Yi
- Zhang, Yanyong
venue: IEEE Transactions on Communications
venue_type: journal
year: 2023
doi: 10.1109/TCOMM.2022.3229033
url: https://www.scopus.com/pages/publications/85144745628?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 864--876
keywords:
- Collaborative inference
- computation partition
- mobile edge computing
- multi-agent reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0759 — Reinforcement Learning Based Energy-Efficient Collaborative Inference for Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Collaborative inference in mobile edge computing (MEC) enables mobile devices to offload the computation tasks for the computation-intensive perception services, and the inference policy determines the inference latency and energy consumption. The optimal inference policy depends on the inference performance model of deep learning, the data generation model and the network model that are rarely known by mobile devices in time. In this paper, we propose a multi-agent reinforcement learning (RL) based energy-efficient MEC collaborative inference scheme, which enables each mobile device to choose both the partition point of deep learning and the collaborative edge of each mobile device based on the image quantity, the channel conditions and the previous inference performance. A learning experience exchange mechanism exploits the Q-values of the neighboring mobile devices to accelerate the inference policy optimization with less energy consumption. We also provide a deep multi-agent RL based inference scheme to accelerate learning for large-scale MEC networks, in which an actor network yields the collaborative inference policy probability distribution and a critic network guides the weight update of the actor network to enhance sample efficiency. We provide the inference performance bound and analyze the computational complexity. Both simulation and experimental results show that our proposed schemes reduce the inference latency and save the MEC energy consumption.  © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0759.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
