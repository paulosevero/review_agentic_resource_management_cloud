---
id: paper-2326
title: 'Computation offloading and resource allocation in satellite edge computing networks: A multi-agent reinforcement learning approach'
authors:
- Xiu, Qingxiao
- Liu, Jun
- Liu, Xiangjun
- Wang, Jintao
venue: Computer Networks
venue_type: journal
year: 2025
doi: 10.1016/j.comnet.2025.111680
url: https://www.scopus.com/pages/publications/105015544422?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computation offloading
- Multi-agent reinforcement learning
- Resource allocation
- Satellite edge computing
- Twin delayed deterministic policy gradient
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2326 — Computation offloading and resource allocation in satellite edge computing networks: A multi-agent reinforcement learning approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The development of Low Earth Orbit (LEO) satellite networks and Mobile Edge Computing (MEC) technologies supports the placement of MEC servers on LEO satellites, facilitating computation offloading in remote areas where computing resources are limited. However, the on-board computing and communication resources of LEO satellite networks are similarly constrained, while the system environment remains highly dynamic and complex. Moreover, diverse task requirements often require offloading across multiple time slots, which increases the complexity of offloading decisions and resource allocation for terrestrial tasks. In this study, we model this problem within satellite edge computing networks as a partially observable Markov decision process (POMDP). To achieve effective joint optimization, we introduce a multi-agent recurrent attentional double delayed deep deterministic policy gradient (MARATD3) algorithm. First, we utilize the recurrent neural network (RNN) to summarize historical observations of users, which improves adaptability to dynamic system environments and enables accurate predictions of system states. Then, a multi-head attention mechanism is introduced to strengthen the ability of user agents to capture critical information within the joint state space, reduce interference from irrelevant information, and improve training efficiency. According to the experimental results, MARATD3 achieves a considerable reduction in energy consumption and delay relative to the baseline algorithms while maintaining task delay and resource constraints. © 2025 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2326.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
