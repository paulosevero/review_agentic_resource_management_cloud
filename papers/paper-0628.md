---
id: paper-0628
title: A Deep Reinforcement Learning Framework for Optimizing Congestion Control in Data Centers
authors:
- Ketabi, Shiva
- Chen, Hongkai
- Dong, Haiwei
- Ganjali, Yashar
venue: Proceedings of IEEE/IFIP Network Operations and Management Symposium 2023, NOMS 2023
venue_type: conference
year: 2023
doi: 10.1109/NOMS56928.2023.10154411
url: https://www.scopus.com/pages/publications/85164725546?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Deep learning
- Learning algorithms
- Learning systems
- Multi agent systems
- Congestion control protocols
- Control actions
- Control parameters
- Datacenter
- Learning frameworks
- Network environments
- Online learning
- Performance
- Reinforcement learnings
- Stringents
- Reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0628 — A Deep Reinforcement Learning Framework for Optimizing Congestion Control in Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Various congestion control protocols have been designed to achieve high performance in different network environments. Modern online learning solutions that delegate the congestion control actions to a machine cannot properly converge in the stringent time scales of data centers. We leverage multi-agent reinforcement learning to design a system for dynamic tuning of congestion control parameters at end-hosts in a data center. The system includes agents at the end-hosts to monitor and report the network and traffic states, and agents to run the reinforcement learning algorithm given the states. Based on the state of the environment, the system generates congestion control parameters that optimize network performance metrics such as throughput and latency. As a case study, we examine BBR, an example of a prominent recently-developed congestion control protocol. Our experiments demonstrate that the proposed system has the potential to mitigate the problems of static parameters. © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0628.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
