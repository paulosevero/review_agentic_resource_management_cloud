---
id: paper-0732
title: 'Intelligent Video Streaming at Network Edge: An Attention-Based Multiagent Reinforcement Learning Solution'
authors:
- Tang, Xiangdong
- Chen, Fei
- He, Yunlong
venue: Future Internet
venue_type: journal
year: 2023
doi: 10.3390/fi15070234
url: https://www.scopus.com/pages/publications/85166391170?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- edge computing
- multiagent
- QoE
- reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0732 — Intelligent Video Streaming at Network Edge: An Attention-Based Multiagent Reinforcement Learning Solution

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Video viewing is currently the primary form of entertainment for modern people due to the rapid development of mobile devices and 5G networks. The combination of pervasive edge devices and adaptive bitrate streaming technologies can lessen the effects of network changes, boosting user quality of experience (QoE). Even while edge servers can offer near-end services to local users, it is challenging to accommodate a high number of mobile users in a dynamic environment due to their restricted capacity to maximize user long-term QoE. We are motivated to integrate user allocation and bitrate adaptation into one optimization objective and propose a multiagent reinforcement learning method combined with an attention mechanism to solve the problem of multiedge servers cooperatively serving users. Through comparative experiments, we demonstrate the superiority of our proposed solution in various network configurations. To tackle the edge user allocation problem, we proposed a method called attention-based multiagent reinforcement learning (AMARL), which optimized the problem in two directions, i.e., maximizing the QoE of users and minimizing the number of leased edge servers. The performance of AMARL is proved by experiments. © 2023 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0732.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
