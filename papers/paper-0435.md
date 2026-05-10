---
id: paper-0435
title: Lyapunov Optimization Based Mobile Edge Computing for Internet of Vehicles Systems
authors:
- Jia, Yi
- Zhang, Cheng
- Huang, Yongming
- Zhang, Wei
venue: IEEE Transactions on Communications
venue_type: journal
year: 2022
doi: 10.1109/TCOMM.2022.3206885
url: https://www.scopus.com/pages/publications/85139394215?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 7418--7433
keywords:
- computation offloading
- graph convolutional neural network (GCN)
- Lyapunov optimization
- MEC
- multi-agent proximal policy optimization (MAPPO)
- task dependency graph
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0435 — Lyapunov Optimization Based Mobile Edge Computing for Internet of Vehicles Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile-Edge Computing (MEC) is an emerging paradigm in the Internet of Vehicles (IoV) to meet the ever-increasing computation demands of smart applications. To provide satisfactory computation performance, it is of significant importance to conduct computation offloading in IoV. In this paper, we investigate a multi-vehicle IoV system assisted by MECs with limited computation resources, where vehicles with complex applications can offload their subtasks to MEC servers. Applications are modeled as interdependent subtasks with general random task graphs, different from existing works with independent ones. To maximize the average logarithmic data processing rate (LDPR), the computation offloading problem is formulated as a time-average optimization with long-term constraints, which results from variable vehicle number, various applications and time-varying communication channels. To reduce the cooperation overhead, we propose a multi-agent Proximal Policy Optimization algorithm (Ly-MAPPO) which requires local observation only to solve the subproblems achieved by Lyapunov optimization technique in real time. In addition, to improve the performance of the Ly-MAPPO algorithm, Graph Convolutional Neural Network (GCN) is introduced to extract inter-dependencies between subtasks. Extensive simulations show that the GCN embedded Ly-MAPPO outperforms other baseline algorithms, e.g., greedy algorithm and gene algorithm, etc., for different traffic loads and computation resources in MEC servers.  © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0435.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
