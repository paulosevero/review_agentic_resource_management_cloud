---
id: paper-0889
title: Optimizing Mobility-Aware Task Offloading in Smart Healthcare for Internet of Medical Things Through Multiagent Reinforcement Learning
authors:
- Dong, Chongwu
- Sun, Yanbin
- Shafiq, Muhammad
- Hu, Ning
- Liu, Yuan
- Tian, Zhihong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3338718
url: https://www.scopus.com/pages/publications/85179800207?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13677--13691
keywords:
- Edge computing
- Internet of Medical Things (IoMT)
- mobility aware
- multiagent reinforcement learning
- task offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0889 — Optimizing Mobility-Aware Task Offloading in Smart Healthcare for Internet of Medical Things Through Multiagent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the scenario of smart healthcare applications, the Internet of Medical Things (IoMT) devices, equipped with limited resources, would offload numerous computation-heavy tasks to an edge server through 5G networks. However, IoMT devices should usually move around different diagnostic areas in smart healthcare systems, leading to the dynamics of the uplink channel quality. Moreover, the burst generation of a substantial number of tasks from IoMT devices can result in congestion within the computing queue of the edge server, and heterogeneous services in IoMT devices make it hard to collect global information for a central controller to get the optimal optimization for all IoMT devices. So, how to determine task offloading among IoMT devices in a distributed scenario of smart healthcare applications should be considered appropriately and comprehensively. In this article, we investigate task offloading in mobile edge computing (MEC) through wireless networks. To improve the utilization of wireless resources, nonorthogonal multiple access (NOMA) is adopted in 5G networks. We first formulate the mobility of IoMT devices as a hidden Markov model (HMM) and the problem of task offloading policy as a Distributed partial Markov decision process (Dec-POMDP). Then, we propose a mobility-aware method based on Multiagent reinforcement learning for task offloading in 5G NOMA-enabled networks. In our approach, task offloading scheduling for each IoMT device in NOMA-enabled 5G networks is considered to improve energy efficiency and guarantee service quality. Besides, the time complexity and the existence of a Nash equilibrium for our proposed Dec-POMDP method are theoretically derived. Simulations are conducted to show that our algorithm outperforms other alternative methods in energy consumption under the delay constraint.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0889.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
