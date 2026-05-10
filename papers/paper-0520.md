---
id: paper-0520
title: A Reinforcement Learning Based Data Storage and Traffic Management in Information-Centric Data Center Networks
authors:
- Yang, Weihong
- Qin, Yang
- Yang, ZhaoZheng
venue: Mobile Networks and Applications
venue_type: journal
year: 2022
doi: 10.1007/s11036-020-01629-w
url: https://www.scopus.com/pages/publications/85089009517?origin=resultslist
publisher: Springer
pages: 266--275
keywords:
- Data storage
- Distributed Q-learning
- Information-centric data center networks
- Traffic management
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0520 — A Reinforcement Learning Based Data Storage and Traffic Management in Information-Centric Data Center Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Data Center Networks (DCN), a core infrastructure of cloud computing, place heavy demands on efficient storage and management of massive data. The data storage scheme, which decides how to assign data to nodes for storage, has a significant impact on the performance of the data center. However, most of the existing solutions focus on where to store the data (i.e., the selection of storage node) but have not considered how to store them (i.e., the traffic management such as routing and transmission rate adjustment). By leveraging the Information-Centric Networks (ICN) architecture, this paper tackles the data storage and traffic management issue in Information-Centric Data Center Networks (ICDCN) based on Reinforcement Learning (RL) method, since RL has been developed as a promising solution to address dynamic network issues. We present a global optimization of joint traffic management and data storage and then solve it by the distributed multi-agent Q-learning. In ICDCN, the data is routed based on the data’s name, which achieves better routing scalability by decoupling the data and its physical location. Compared with IP’s stateless forwarding plane, the stateful forwarding information maintained at every node supports adaptively routing and hop-by-hop traffic control by using the Q-learning method. We evaluate our proposal on an NS-3-based simulator, and the results show that the proposed scheme can effectively reduce transmission time and increase throughput while achieving load-balanced among servers. © 2020, Springer Science+Business Media, LLC, part of Springer Nature.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0520.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
