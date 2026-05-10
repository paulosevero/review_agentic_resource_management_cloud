---
id: paper-1625
title: Learning Adaptive Multi-Timescale Scheduling for Mobile Edge Computing
authors:
- Hao, Yijun
- Yang, Shusen
- Li, Fang
- Zhang, Yifan
- Wang, Shibo
- Ren, Xuebin
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3548533
url: https://www.scopus.com/pages/publications/105000106325?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7297--7311
keywords:
- adaptive timescales
- Mobile edge computing
- reinforcement learning
- resource scheduling
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1625 — Learning Adaptive Multi-Timescale Scheduling for Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In mobile edge computing (MEC), resource scheduling is crucial to task requests’ performance and service providers’ cost, involving multi-layer heterogeneous scheduling decisions. Existing MEC schedulers typically adopt static-timescale scheduling, where scheduling decisions are updated regularly at fixed intervals for all layers. The inflexible updating timescales lead to poor performance in the production networks. In this paper, we propose EdgeTimer, an unprecedented approach that automatically and adaptively determines respective updating timescales of multiple scheduling layers to achieve a better trade-off between the operation cost and service performance. Specifically, we design (i) a three-layer hierarchical deep reinforcement learning (DRL) framework for efficient learning of tightly coupled policies, (ii) a tailored multi-agent DRL algorithm for decentralized scheduling, with the convergence strictly proved, and (iii) a lightweight system defender for deterministic reliability assurance. Furthermore, we apply EdgeTimer to a wide range of Kubernetes scheduling rules, and evaluate it using production traces with different workload patterns. Through extensive trace-driven experiments, we demonstrate that EdgeTimer can significantly decrease the operation cost for service providers without sacrificing the delay performance, thereby improving overall profits, compared with the state-of-the-art approaches. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1625.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
