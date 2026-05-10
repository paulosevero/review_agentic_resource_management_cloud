---
id: paper-1330
title: Decentralized and Fault-Tolerant Task Offloading for Enabling Network Edge Intelligence
authors:
- Zhang, Huixiang
- Liao, Kaihua
- Tai, Yu
- Ma, Wenqiang
- Cao, Guoyan
- Sun, Wen
- Xu, Lexi
venue: IEEE Systems Journal
venue_type: journal
year: 2024
doi: 10.1109/JSYST.2024.3403696
url: https://www.scopus.com/pages/publications/85195400194?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1459--1470
keywords:
- deep reinforcement learning
- fault tolerance
- Mobile edge computing (MEC)
- multiagent proximal policy optimization (MAPPO)
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

# paper-1330 — Decentralized and Fault-Tolerant Task Offloading for Enabling Network Edge Intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge intelligence has recently attracted great interest from industry and academia, and it greatly improves the processing speed at the edge by moving data and artificial intelligence to the edge of the network. However, edge devices have bottlenecks in battery capacity and computing power, making it challenging to perform computing tasks in dynamic and harsh network environments. Especially in disaster scenarios, edge (rescue) devices are more likely to fail due to unreliable wireless communications and scattered rescue requests, which makes it urgent to explore how to provide low-latency, reliable services through edge collaboration. In this article, we investigate the task offloading mechanism in mobile edge computing networks, aiming to ensure fault tolerance and rapid response of computing services in dynamic and harsh scenarios. Specifically, we design a fault-tolerant distributed task offloading scheme, which minimizes task execution time and system energy consumption through the multi-agent proximal policy optimization algorithm. Furthermore, we introduce logarithmic ratio reward functions and action masking to reduce the impact of different task queue lengths while accelerating model convergence. Numerical results show that the proposed algorithm is suitable for service failure scenarios, effectively meeting the reliability requirements of tasks while simultaneously reducing system energy consumption and processing latency.  © 2007-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1330.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
