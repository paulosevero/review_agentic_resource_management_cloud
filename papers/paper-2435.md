---
id: paper-2435
title: Fault-Tolerant Resource Allocation and Task Offloading Scheme for UAV NOMA-MEC Networks
authors:
- Zhang, Quanjing
- Zhang, Huixiang
- Zhang, Shangwei
- Liao, Kaihua
- Habib, Ayesha
venue: Proceedings - 2025 IEEE International Symposium on Parallel and Distributed Processing with Applications, ISPA 2025
venue_type: conference
year: 2025
doi: 10.1109/ISPA67752.2025.00038
url: https://www.scopus.com/pages/publications/105030208574?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 219--227
keywords:
- Mobile edge computing (MEC)
- multiagent proximal policy optimization (MAPPO)
- non-orthogonal multiple access (NOMA)
- task offloading
- unmanned aerial vehicle (UAV)
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

# paper-2435 — Fault-Tolerant Resource Allocation and Task Offloading Scheme for UAV NOMA-MEC Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) is essential for UAV-assisted applications such as emergency response and disaster rescue. However, limited computing capacity, scarce spectrum resources, and stringent transmit power constraints pose significant challenges to task offloading and resource allocation, which in turn degrades system performance in terms of latency, energy consumption, and task execution reliability. To address these issues, we formulate an optimization problem for a cooperative multi-UAV system with non-orthogonal multiple access (NOMA), explicitly accounting for device failures and task reliability requirements. Given the complexity of the problem and the slow convergence of conventional approaches, we develop a fault-tolerant resource allocation and task offloading (FTRATO) scheme based on multi-agent proximal policy optimization (MAPPO). The proposed scheme further incorporates a logarithmic ratio reward function and an action mask to accelerate convergence and stabilize training. Simulation results demonstrate that FTRATO reduces energy consumption and latency while improving task execution reliability.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2435.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
