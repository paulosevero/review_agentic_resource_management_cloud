---
id: paper-2272
title: 'Mercury: A Dynamic Multi-path Packet Spraying Scheme for RDMA Networks'
authors:
- Wang, Yuxiang
- Zhang, Jiao
- Wan, Zirui
- Cai, Leixin
- Wang, Shuo
- Huang, Tao
venue: Proceedings - International Conference on Computer Communications and Networks, ICCCN
venue_type: conference
year: 2025
doi: 10.1109/ICCCN65249.2025.11133854
url: https://www.scopus.com/pages/publications/105016222647?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Congestion Control
- Data-center networks
- Packet Spraying
- RDMA
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2272 — Mercury: A Dynamic Multi-path Packet Spraying Scheme for RDMA Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to the low entropy traffic characteristics of LLM (Large Language Model) training, existing load balancing mechanisms such as Equal-Cost Multi-Path (ECMP) fail to fully utilize the redundant bandwidth between computing nodes in RDMA over Converged Ethernet (RoCE). Packet spraying mechanism has become a typical solution to the load balancing problem in RoCEs. However, it has a negative effect on congestion control mechanisms and suffers severe out-of-order problems.In this paper, we propose Mercury, an host-driven spraying scheme that synergizes congestion feedback and reordering control. Mercury selects paths by leveraging ECN, RTT, and reordering metrics, adjusts rates via multi-metric window. It also employs receiver-side buffers with priority-based dropping to mitigate out-of-order penalties. Evaluations in ns-3 under AllReduce/All-to-All traffic show Mercury reduces maximum flow completion time (Max FCT) by 40%-63% compared to ECMP-based DCQCN/TIMELY/HPCC. It also achieves at least 10%-20% improvement against switch-based spraying. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2272.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
