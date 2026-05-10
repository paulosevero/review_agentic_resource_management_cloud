---
id: paper-2731
title: 'Transfer Reinforcement Learning for Resource Allocation in Mobile Edge Computing Systems: A Survey'
authors:
- Ni, Chenhao
- Kong, Xiangjie
- Du, Jiaxin
- Shen, Guojiang
- Al-Asad, Wail
- Min, Geyong
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2026.3658306
url: https://www.scopus.com/pages/publications/105028915059?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1708--1727
keywords:
- deep reinforcement learning
- resource allocation
- satellite-assisted mobile edge computing
- Transfer learning
- unmanned aerial vehicle
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
    my_justification: Review
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

# paper-2731 — Transfer Reinforcement Learning for Resource Allocation in Mobile Edge Computing Systems: A Survey

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge intelligence capitalizes on heterogeneous edge resources to empower artificial intelligence-driven applications while mitigating dependence on centralized cloud infrastructures. In mobile edge computing (MEC) systems, resource scheduling constitutes a latency-critical task within inherently dynamic environments. Deep reinforcement learning (DRL) has been widely employed to address this challenge, as it enables agents to derive task-specific policies through continual interactions with the environment. Nevertheless, MEC environments exhibit substantial heterogeneity, and the relative importance of various resource types may fluctuate as the system evolves, thereby altering task objectives. Consequently, agents often necessitate retraining across new domains, the process that is computationally intensive and time inefficient. To surmount these challenges, transfer reinforcement learning (TRL) has emerged as a promising paradigm that facilitates the transfer of agents' acquired knowledge from the source domain to the target domain. To the best of our knowledge, this is the first comprehensive survey dedicated to TRL applications in MEC systems. Specifically, we first elucidates the foundational principles of TRL, encompassing problem formulation and DRL methodologies. Subsequently, we systematically reviews and critically analyzes existing research on TRL and its applications in MEC systems. Finally, we discuss persistent technical limitations and delineates promising avenues for future exploration. © 2008-2012 IEEE.

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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2731.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
