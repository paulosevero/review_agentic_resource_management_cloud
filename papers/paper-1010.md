---
id: paper-1010
title: Cloud-edge-device System architecture and key technologies of industrial digital twin System based on multi-agent; [基于多智能体的工业数字孪生系统云边端架构与关键技术]
authors:
- Li, Hao
- Xing, Zhiyuan
- Li, Linli
- Lu, Xiaoping
- Yang, Wenchao
- Wang, Haoqi
- Liu, Gen
- Wang, Xiaocong
- Liu, Xiaojun
- Wen, Xiaoyu
- Wu, Chunlong
- Xing, Hongwen
- Dong, Liyang
- Wang, Zhiqiang
venue: Jisuanji Jicheng Zhizao Xitong/Computer Integrated Manufacturing Systems, CIMS
venue_type: journal
year: 2024
doi: 10.13196/j.cims.2024.0462
url: https://www.scopus.com/pages/publications/85211006665?origin=resultslist
publisher: CIMS
pages: 3755--3770
keywords:
- artificial intelligence
- cloud-edge-end collaboration
- distributed Computing
- industrial digital twin
- multi-agent
language: Chinese
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_modifier_by_llm
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-1010 — Cloud-edge-device System architecture and key technologies of industrial digital twin System based on multi-agent; [基于多智能体的工业数字孪生系统云边端架构与关键技术]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The multi-agent-based industrial Digital Twin System (iDTS) is composed of multiple agents, including humans, machines, environments, digital twin Simulation Systems and Computing Systems. It is a new generation of iDTS System driven by the Integration of multiple agents, Artificial Intelligence (AI) algorithms and digital twin Systems. In view of the real-time, intelligence and load balancing needs of the iDTS System, the typical characteris-tics, cloud-edge-device System architecture and key technologies of the iDTS System were presented based on multiple agents, which mainly included the methods of agents' self-learning and optimization driven by Large Language Models (LLMs), the methods of clock synchronization and data sharing for the interaction of iDTS System based on multiple agents, the distributed control methods for the collaboration of multiple agents in the iDTS System, the col-laborative scheduling methods for multiple manufacturing resources in the iDTS System and the load balancing methods for the iDTS System with a cloud-edge-device architecture. Finally, the application effect of multi-agent-based iDTS System was demonstrated through a typical case. The proposed System architecture and key technologies pro-vide important reference for the in-depth application of AI and digital twin technology in intelligent manufacturing processes. © 2024 CIMS. All rights reserved.

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
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_modifier_by_llm']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: llm_as_workload, pattern_id: ovr_modifier_by_llm, matched_substring: "driven by Large Language" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1010.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
