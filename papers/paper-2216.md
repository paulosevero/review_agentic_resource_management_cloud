---
id: paper-2216
title: O-RAN-Enabled Collaborative Multi-Access Edge Computing Over Optical Metro and Access Networks for Enhanced Load Balancing
authors:
- Tian, Bo
- Pan, Xiaolong
- Wang, Fu
- Hu, Shanting
- Zhu, Lei
- Xin, Xiangjun
- Yu, Jianjun
venue: Journal of Lightwave Technology
venue_type: journal
year: 2025
doi: 10.1109/JLT.2025.3566334
url: https://www.scopus.com/pages/publications/105004030394?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6515--6532
keywords:
- Collaborative computing
- load balancing
- metro-access network
- multi-access edge computing
- open radio access network
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

# paper-2216 — O-RAN-Enabled Collaborative Multi-Access Edge Computing Over Optical Metro and Access Networks for Enhanced Load Balancing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The. open radio access network (O-RAN) and multi-access edge computing (MEC) are promising techniques for 6G cellular networks. O-RAN promotes the evolution of cellular ecosystem through function disaggregation and artificial intelligence (AI) controllers, while MEC enables latency-critical tasks offloading at the network edge. However, the finite number of edge servers (ESs) and limited computational resources may lead to resource shortages, particularly in hotspot areas with dense MEC activities. Our work considers an O-RAN-enabled collaborative MEC (C-MEC) network that employs passive optical network (PON)-based metro-access network to establish virtualized connections between ESs, while utilizing AI to enable intelligent RAN/C-MEC resource management. With the objective of optimizing hotspot throughput, we propose a function splitting (FS)-based load balancing (FS-LL) problem to jointly schedule RAN slicing and manage C-MEC traffic migration. We formulate FS-LL problem as an integer linear programming (ILP) model considering capacity constraints of computing and bandwidth resources, while satisfying latency requirements. Furthermore, we develop a greedy-search-assisted multi-agent deep reinforcement learning (GA-MADRL) algorithm, where each ES cluster is equipped with a dedicated agent to orchestrate traffic for the implementation of C-MEC. The results demonstrate that GA-MADRL algorithm can obtain close-to-optimal solutions compared to the ILP formulation, while also achieving higher hotspot throughput and better workload balancing performance than benchmark algorithms and traditional FS methods © 1983-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2216.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
