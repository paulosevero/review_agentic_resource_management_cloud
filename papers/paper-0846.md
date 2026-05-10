---
id: paper-0846
title: Scaling Up Edge-Assisted Real-Time Collaborative Visual SLAM Applications
authors:
- Cao, Hao
- Xu, Jingao
- Yang, Zheng
- Shangguan, Longfei
- Zhang, Jialin
- He, Xiaowu
- Liu, Yunhao
venue: IEEE/ACM Transactions on Networking
venue_type: journal
year: 2024
doi: 10.1109/TNET.2023.3330763
url: https://www.scopus.com/pages/publications/85178016314?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1823--1838
keywords:
- collaborative mapping
- edge computing
- multi-agent SLAM
- Visual SLAM
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0846 — Scaling Up Edge-Assisted Real-Time Collaborative Visual SLAM Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The edge-based multi-agent visual SLAM is crucial for emerging mobile applications like search-and-rescue, inventory automation, and industrial inspection. It uses a central node to manage the global map and schedule tasks for agents. However, as the number of agents increases, the system faces scalability challenges due to operational overhead, such as data redundancy, bandwidth consumption, and localization errors. In this paper, we introduce SwarmMap, a framework designed to enhance the scalability of collaborative visual SLAM service in edge offloading settings. SwarmMap consists of three system modules: a change log-based server-client synchronization mechanism, a priority-aware task scheduler, and a lean global map representation. These modules work together to address the challenges of data explosion problems. SwarmMap is open-source and compatible with the robotic operating system (ROS). Existing visual SLAM applications could incorporate SwarmMap through SwarmAPI, a set of well-packaged APIs, to compose SwarmMap's function modules to enhance their performance and capacity in multi-agent scenarios. Comprehensive evaluations and a three-month case study at one of the world's largest oilfields demonstrate that SwarmMap can serve 2× more agents (> 20 agents) than the state-of-the-arts with the same resource overhead, meanwhile maintaining an average trajectory error of 38cm , outperforming existing works by > 55%.  © 1993-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0846.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
