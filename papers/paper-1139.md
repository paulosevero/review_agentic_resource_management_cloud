---
id: paper-1139
title: Collaborative Edge Computing and Program Caching with Routing Plan in C-NOMA-Enabled Space-Air-Ground Network
authors:
- Qin, Peng
- Fu, Min
- Fu, Yang
- Ding, Rui
- Zhao, Xiongwen
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2024
doi: 10.1109/TWC.2024.3464610
url: https://www.scopus.com/pages/publications/85205316979?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 18302--18315
keywords:
- program caching
- routing plan
- Space-air-ground edge computing network (SAGECN)
- task offloading
- trajectory design
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

# paper-1139 — Collaborative Edge Computing and Program Caching with Routing Plan in C-NOMA-Enabled Space-Air-Ground Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Through deploying satellites and unmanned aerial vehicles (UAVs) with onboard processing capability, the space-air-ground edge computing network (SAGECN) is poised to support ubiquitous access and computation offloading for Internet of Things (IoT) terminals deployed in remote areas. However, the current SAGECN faces several challenges in realizing its full potential, such as scarce spectrum resources, diverse computational demands, and dynamic network circumstances. To meet these challenges, we propose a cluster-non-orthogonal multiple access (C-NOMA)-enabled SAGECN model, where a satellite and multiple UAVs act as collaborative edge servers to execute tasks from IoT terminals. Since each offloaded task should be processed via a specific program, the edge servers carry out program caching, whilst transfer the tasks that do not match the cached programs to another server in a multi-hop manner. Considering the delay-sensitive requirements of computation tasks, we formulate a joint task offloading, communication-computation-cache resource assignment, and routing plan problem, aimed at minimizing the average system latency. To cope with this challenging issue, we partition it into three subproblems. First, a multi-agent learning-based approach is developed to collaboratively train the task offloading, flight trajectory, and program caching. As a step further, two optimization subroutines are embedded to perform routing plan, subchannel allocation, and power control, thereby rendering the overall solution. Experimental results reveal that our approach achieves outstanding performance in terms of system delay and spectrum efficiency. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1139.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
