---
id: paper-2680
title: 'Distributed Two-Tier Edge Computing in Integrated Satellite-Terrestrial Networks: A Multiagent Deep Deterministic Policy Gradient Approach'
authors:
- Liu, Shanyun
- Zhu, Xiangming
- Chang, Jingfei
- Xu, Tao
- Chen, Hongyang
- Han, Zhu
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2025.3611920
url: https://www.scopus.com/pages/publications/105016846086?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 308--324
keywords:
- Delay optimization
- integrated satellite-terrestrial networks
- mobile edge computing
- multiagent deep deterministic policy gradient (MADDPG)
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

# paper-2680 — Distributed Two-Tier Edge Computing in Integrated Satellite-Terrestrial Networks: A Multiagent Deep Deterministic Policy Gradient Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integrated satellite-terrestrial network architecture has emerged as a hotspot for the Internet of Everything (IoE), which is a promising approach to provide communication service anytime and anywhere. In this article, we aim to facilitate the system delay reduction through the two-tier cooperative edge computing of terrestrial base stations (BSs) and the satellite. To avoid the two-way propagation delay brought by the centralized decision process, we propose a distributed offloading scheme for the BSs and the satellite. First, we equivalently decompose the offloading problem into multiple subproblems, based on which the optimal user–BS time slot allocation strategy for each BS is derived. Then, by means of multiagent deep deterministic policy gradient (MADDPG) reinforcement learning (RL), the resource allocation strategy of each BS is obtained distributedly, which effectively avoids the two-way propagation delay. Based on the BS resource allocation strategy obtained, the optimal satellite computation capacity allocation strategy is proposed to minimize the total edge computing delay at the satellite. Finally, exhaustive simulations are implemented to demonstrate the performance of the proposed distributed offloading strategy. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2680.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
