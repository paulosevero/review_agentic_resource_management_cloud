---
id: paper-1827
title: Task offloading and computing resource allocation of the joint UAV with computing power network
authors:
- Li, JunFei
- Zeng, QingTao
- Lu, LiKun
- Zhang, ErQing
- Xu, AnPing
- Li, WenJing
venue: Journal of Supercomputing
venue_type: journal
year: 2025
doi: 10.1007/s11227-025-07351-2
url: https://www.scopus.com/pages/publications/105006449869?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Computing power network
- Deep reinforcement learning
- Resource allocation
- UAV
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1827 — Task offloading and computing resource allocation of the joint UAV with computing power network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the advent of the 6 G era, computing power is the new productivity in the era of the digital economy. In response to the growing global demand for computing power, the computing power network (CPN) came into being. The goal of the computing power network is to gather idle computing power, build a collaborative computing system of “cloud, edge, and end,” and improve the utilization rate of computing power resources in the whole network. In traditional cellular-based mobile edge computing, due to signal attenuation and interference between users, users at the edge of the cell have a great impact on the use of computing resources. UAV-assisted resource management is critical to developing sixth-generation networks, where aerial base stations have a higher chance of establishing line-of-sight connections with users on the ground due to their greater coverage. How to share computing resources more efficiently and how to optimize resource allocation are urgent problems to be solved. To address these issues, this paper proposes a new user-centric computing power network architecture that considers unmanned aerial vehicles (UAVs) as access points with offloading capabilities and models the joint resource management process in user-centered UAV-assisted computing power network architecture (UCUAV-CPN) as a partially observable Markov decision process. A decentralized joint optimization scheme based on multi-agent deep reinforcement learning and convex optimization is proposed. The experimental results show that the scheme proposed in UCUAV-CPN can significantly reduce the average total delay by up to 83.58%, and the scheme proposed in this paper can also significantly improve the uplink transmission rate by up to 131.69%. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1827.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
