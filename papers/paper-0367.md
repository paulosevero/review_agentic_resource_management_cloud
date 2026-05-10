---
id: paper-0367
title: Distributed Multi-Cloud Multi-Access Edge Computing by Multi-Agent Reinforcement Learning
authors:
- Zhang, Yutong
- Di, Boya
- Zheng, Zijie
- Lin, Jinlong
- Song, Lingyang
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2021
doi: 10.1109/TWC.2020.3043038
url: https://www.scopus.com/pages/publications/85098776958?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2565--2578
keywords:
- Distributed
- multi-access edge computing
- multi-agent reinforcement learning
- multi-cloud
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

# paper-0367 — Distributed Multi-Cloud Multi-Access Edge Computing by Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we consider a three-layer distributed multi-access edge computing (MEC) network where multiple clouds, MEC servers, and edge devices (EDs) are deployed at the top layer, middle layer, and bottom layer, respectively. Each cloud center (CC) is associated with an independent service provider and publishes an application-driven computing task. To deliver the tasks, CCs rely on EDs to generate the raw data and offload part of the computing tasks to both EDs and MEC servers such that their computing and transmission resources can be fully utilized to reduce the system latency. However, in such a three-layer network, the distributed deployment of tasks leads to inevitable resource competition among CCs. To address this issue, we propose a distributed scheme based on multi-agent reinforcement learning, where each CC jointly determines the task offloading and resource allocation strategy based on its inference of other CCs' decisions. Simulation results indicate that a lower system latency is achieved via our proposed scheme compared with the existing schemes. In addition, the influence of the number of CCs, MEC servers, and EDs on latency performance is also discussed.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0367.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
