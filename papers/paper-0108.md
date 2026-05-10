---
id: paper-0108
title: A novel energy-aware scheduling and load-balancing technique based on fog computing
authors:
- Alzeyadi, Ahmad
- Farzaneh, Nazbanoo
venue: 2019 9th International Conference on Computer and Knowledge Engineering, ICCKE 2019
venue_type: conference
year: 2019
doi: 10.1109/ICCKE48569.2019.8964946
url: https://www.scopus.com/pages/publications/85079249753?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 104--109
keywords:
- Energy
- Fog computing
- Internet of things
- Load balancing
- Scheduling
- Smart factory
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0108 — A novel energy-aware scheduling and load-balancing technique based on fog computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Considering the development of modern information technology, the emergence of fog computing has gained equipment computing power and supplied new solutions for modern traditional industrial applications. Generally, providing communication among devices in smart factories structure is one of the most controversial issues. Since reciprocating lots of messages among existent various tools and intelligent agents is required in the smart factories, and the connections are naturally wireless, they will not have much to offer. If the intelligent agents tend to use broadcasting in sending their messages, the process will be costly with little outcome. Hence, in this paper, an effective solution is presented to gain optimum connections among these elements, while considering the complex issues on energy consumption, network efficiency, traffic, and latency in the exchange of messages. The proposed method is a scheduling awareness of the communicative fog while focusing on complicated energy consumption problems of manufacturing clusters. In the proposed algorithm, four criteria are considered: energy, dynamic threshold, waiting time of tasks, and communication delay among smart factors. These criteria are divided into two categories. The criteria according to which two scheduling and load adjusting procedures are performed depend on the user's opinion. The results of the experiments show that the workload in the proposed method is more balanced than the base method in the robot. This load balancing has reduced the amount of workload in each robot, which reduces the waiting time for each product to be packaged. Also, the amount of communication in the network in the proposed method has decreased about 63% compared to ELBS. © 2019 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0108.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
