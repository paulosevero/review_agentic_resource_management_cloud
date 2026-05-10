---
id: paper-1190
title: Relay-Assisted Edge Computing Framework for Dynamic Resource Allocation and Multiple-Access Task Processing in Digital Divide Regions
authors:
- Shu, Zhenyang
- Deng, Xiaoheng
- Wang, Leilei
- Gui, Jinsong
- Wan, Shaohua
- Zhang, Honggang
- Min, Geyong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3439332
url: https://www.scopus.com/pages/publications/85200816114?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 35724--35741
keywords:
- Deep reinforcement learning (DRL)
- digital divide regions
- multiaccess edge computing (MEC)
- nonorthogonal multiple access (NOMA)
- relay
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

# paper-1190 — Relay-Assisted Edge Computing Framework for Dynamic Resource Allocation and Multiple-Access Task Processing in Digital Divide Regions

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the digital divide regions, the edge computing can improve the performance of application services for the Internet of Things (IoT) devices. However, the lagging of information and communication technology (ICT) results in congested access spectrum and imbalanced computational load. Moreover, the mobility of IoT devices further exacerbates the fluctuating quality of communication links and the frequent changing of access positions. So, how to realize the reliable service requirements of devices in a heterogeneous environment with multiscale constraints should be considered appropriately and comprehensively. In this article, we model a relay-assisted multiaccess edge computing (MEC) framework, employing multihop transmission to enable the cross-domain service coverage. Under this framework, we formulate a quantitative model to characterize communication and computation processes within task migration, and derive analytical results for service latency. To improve the access resource efficiency, we adopt a joint nonorthogonal multiple access (NOMA) scheme to extend the transmission dimension, and employ proportional fairness to dynamically allocate resources. Besides, we propose a multiagent deep reinforcement learning (DRL) for optimizing the long-term task offloading scheduling, address the optimization problem of maximizing the system throughput efficiency. And we improve the action exploration and output dimensions of DRL to achieve convergence and performance enhancement. Simulation and analytical results show that our proposed algorithm outperforms the comparison algorithms in the key performance indicators. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1190.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
