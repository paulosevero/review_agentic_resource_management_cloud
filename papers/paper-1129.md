---
id: paper-1129
title: Reliable Task Offloading in Sustainable Edge Computing with Imperfect Channel State Information
authors:
- Peng, Peng
- Wu, Wentai
- Lin, Weiwei
- Zhang, Fan
- Liu, Yongheng
- Li, Keqin
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2024
doi: 10.1109/TNSM.2024.3456568
url: https://www.scopus.com/pages/publications/85204138894?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6423--6436
keywords:
- deep reinforcement learning
- Edge computing
- reliability
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

# paper-1129 — Reliable Task Offloading in Sustainable Edge Computing with Imperfect Channel State Information

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As a promising paradigm, edge computing enhances service provisioning by offloading tasks to powerful servers at the network edge. Meanwhile, Non-Orthogonal Multiple Access (NOMA) and renewable energy sources are increasingly adopted for spectral efficiency and carbon footprint reduction. However, these new techniques inevitably introduce reliability risks to the edge system generally because of i) imperfect Channel State Information (CSI), which can misguide offloading decisions and cause transmission outages, and ii) unstable renewable energy supply, which complicates device availability. To tackle these issues, we first establish a system model that measures service reliability based on probabilistic principles for the NOMA-based edge system. As a solution, a Reliable Offloading method with Multi-Agent deep reinforcement learning (ROMA) is proposed. In ROMA, we first reformulate the reliability-critical constraint into an long-term optimization problem via Lyapunov optimization. We discretize the hybrid action space and convert the resource allocation on edge servers into a 0-1 knapsack problem. The optimization problem is then formulated as a Partially Observable Markov Decision Process (POMDP) and addressed by multi-agent proximal policy optimization (PPO). Experimental evaluations demonstrate the superiority of ROMA over existing methods in reducing grid energy costs and enhancing system reliability, achieving Pareto-optimal performance under various settings.  © 2004-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1129.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
