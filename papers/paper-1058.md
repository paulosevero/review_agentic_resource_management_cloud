---
id: paper-1058
title: Lyapunov-Based MADRL Policy in Wireless Powered MEC Assisted Monitoring Systems
authors:
- Liu, Xinying
- Yi, Yuhan
- Zhang, Wenqian
- Zhang, Guanglin
venue: IEEE INFOCOM 2024 - IEEE Conference on Computer Communications Workshops, INFOCOM WKSHPS 2024
venue_type: conference
year: 2024
doi: 10.1109/INFOCOMWKSHPS61880.2024.10620870
url: https://www.scopus.com/pages/publications/105003145643?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Age of information
- Lyapunov optimization
- mobile edge computing
- multi-agent deep reinforcement learning
- wireless power transfer
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1058 — Lyapunov-Based MADRL Policy in Wireless Powered MEC Assisted Monitoring Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In real-time monitoring systems, wireless de-vices(WDs) are employed for information gathering, with age of information(AoI) serving as a crucial measure to assess the timeliness of status information. The combination of wireless power transfer(WPT) and mobile edge computing(MEC) effectively address the challenges posed by the limited battery lifespan and computation capabilities of WDs. This paper focuses on a WP-MEC system where WDs adopt a zero-waiting strategy. A multi-stage stochastic optimization problem is formulated with the goal of age minimization. By utilizing Lyapunov optimization, we convert the problem into deterministic subproblems. However, solving the subproblems proves challenging as they remain mixed-integer nonlinear programming(MINLP) problems. We propose LyMAPPO and LyIPPO to tackle this problem, which leverage the benefits of Lyapunov optimization and multi-agent deep reinforcement learning(MADRL). MADRL enables WDs to make optimal decisions of task scheduling, resource allocation and computation offloading. Simulation results confirm the findings of our theoretical analyses, demonstrating the improved performance of LyMAPPO and LyIPPO in comparison to bench-mark algorithms. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1058.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
