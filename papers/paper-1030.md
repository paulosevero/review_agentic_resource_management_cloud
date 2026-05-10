---
id: paper-1030
title: Multi-agent Reinforcement Learning Based Collaborative Multi-task Scheduling for Vehicular Edge Computing
authors:
- Li, Peisong
- Xiao, Ziren
- Wang, Xinheng
- Huang, Kaizhu
- Huang, Yi
- Tchernykh, Andrei
venue: Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
venue_type: conference
year: 2024
doi: 10.1007/978-3-031-54531-3_1
url: https://www.scopus.com/pages/publications/85187774882?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 3--22
keywords:
- Cloud-edge-end collaboration
- Multi-agent reinforcement learning
- Multi-task scheduling
- Vehicular edge computing
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

# paper-1030 — Multi-agent Reinforcement Learning Based Collaborative Multi-task Scheduling for Vehicular Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Nowadays, connected vehicles equipped with advanced computing and communication capabilities are increasingly viewed as mobile computing platforms capable of offering various in-vehicle services, including but not limited to autonomous driving, collision avoidance, and parking assistance. However, providing these time-sensitive services requires the fusion of multi-task processing results from multiple sensors in connected vehicles, which poses a significant challenge to designing an effective task scheduling strategy that can minimize service requests’ completion time and reduce vehicles’ energy consumption. In this paper, a multi-agent reinforcement learning-based collaborative multi-task scheduling method is proposed to achieve a joint optimization on completion time and energy consumption. Firstly, the reinforcement learning-based scheduling method can allocate multiple tasks dynamically according to the dynamic-changing environment. Then, a cloud-edge-end collaboration scheme is designed to complete the tasks efficiently. Furthermore, the transmission power can be adjusted based on the position and mobility of vehicles to reduce energy consumption. The experimental results demonstrate that the designed task scheduling method outperforms benchmark methods in terms of comprehensive performance. © ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1030.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
