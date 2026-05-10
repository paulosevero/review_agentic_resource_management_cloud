---
id: paper-1443
title: Interruption-Aware Computation Offloading in the Industrial Internet of Things
authors:
- Bui, Khoi Anh
- Yoo, Myungsik
venue: Sensors
venue_type: journal
year: 2025
doi: 10.3390/s25092904
url: https://www.scopus.com/pages/publications/105004895922?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- edge computing
- IIoT
- multi-agent deep reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1443 — Interruption-Aware Computation Offloading in the Industrial Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Designing an efficient task offloading system is essential in the Industrial Internet of Things (IIoT). Owing to the limited computational capability of IIoT devices, offloading tasks to edge servers enhances computational efficiency. When an edge server is overloaded, it may experience interruptions, preventing it from serving local devices. Existing studies mainly address interruptions by rerouting, rescheduling, or implementing reactive strategies to mitigate their impact. In this study, we introduce an interruption-aware proactive task offloading framework for IIoT. We develop a load-based interruption model in which the probability of server interruption is formulated as an exponential function of the total computational load, which provides a more realistic estimation of service availability. This framework employs Multi-Agent Advantage Actor–Critic (MAA2C)—a simple yet efficient approach that enables decentralized decision-making while handling large action spaces and maintaining coordination through the centralized critic to make adaptive offloading decisions, taking into account edge availability, resource limitations, device cooperation, and interruptions. Experimental results show that our approach effectively reduces the average total service delay by optimizing the tradeoff between system delay and availability in IIoT networks. Additionally, we investigate the impact of various system parameters on performance under an interruptible edge task offloading scenario, providing valuable insights into how these parameters influence the overall system behavior and efficiency. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1443.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
