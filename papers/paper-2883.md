---
id: paper-2883
title: Fairness-Aware Deterministic Joint Offloading and Scheduling for Industrial Edge Computing
authors:
- Yao, Yingfei
- Zhou, Nan
- Yao, Shunchun
- Liang, Xiaojun
- Deng, Wenfeng
- Yang, Chunhua
- Gui, Weihua
venue: IEEE Transactions on Industrial Informatics
venue_type: journal
year: 2026
doi: 10.1109/TII.2026.3654608
url: https://www.scopus.com/pages/publications/105030185427?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- Industrial edge computing (IEC)
- multiagent deep deterministic policy gradient (MADDPG)
- task offloading
- time-sensitive networking (TSN)
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

# paper-2883 — Fairness-Aware Deterministic Joint Offloading and Scheduling for Industrial Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Industrial edge computing in time-sensitive, heterogeneous environments faces significant challenges in delivering deterministic, low-latency, and fair task offloading under mixed-criticality traffic. Existing solutions struggle with unpredictable delays, resource contention, and the joint optimization of offloading and scheduling. In this work, we propose a task queue mapping mechanism-based architecture that incorporates formal mixed-deterministic traffic modeling under time-sensitive networking, enabling unified computation and network resource management. The joint task offloading and traffic scheduling problem is rigorously formulated as a two-stage Markov decision process with embedded fairness constraints. To address the strong coupling and computational complexity, we develop a fairness-aware deterministic offloading and resource scheduling (FA-DORS) framework, a hierarchical multiagent deep deterministic policy gradient algorithm, enhanced by a contribution-based local reward mechanism to ensure adaptive resource allocation and fairness. Extensive experimental results demonstrate that in the proposed architecture, FA-DORS achieves lower task latency, higher completion rates, improved resource utilization, and enhanced transmission determinism while ensuring fairness in multitask offloading compared to baseline methods. In particular, FA-DORS achieves an 8.89%–39.15% reduction in average end-to-end delay and up to 39.73% reduction in average jitter under high load, compared with the baseline method. © 2005-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2883.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
