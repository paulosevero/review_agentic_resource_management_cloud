---
id: paper-1268
title: Large-Scale Parallel Embedded Computing With Improved-MPI in Off-Chip Distributed Clusters
authors:
- Wei, Xile
- Wei, Hengyi
- Lu, Meili
- Zhang, Zhen
- Chang, Siyuan
- Zeng, Shunqi
- Wang, Fei
- Chen, Minghui
venue: IEEE Transactions on Industrial Informatics
venue_type: journal
year: 2024
doi: 10.1109/TII.2024.3423330
url: https://www.scopus.com/pages/publications/85208709928?origin=resultslist
publisher: IEEE Computer Society
pages: 12575--12585
keywords:
- Distributed computing
- embedded system
- large language model (LLM)
- message passing interface (MPI)
- neural networks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1268 — Large-Scale Parallel Embedded Computing With Improved-MPI in Off-Chip Distributed Clusters

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Distributed architecture is expected to be an effective solution for large-scale edge computing tasks in terminal devices. However, it remains a great challenge to resolve the conflict between parallel efficiency and constrained physical resources in a specific embedded structure. This article proposes a universal scalable off-chip parallel computing architecture to maximize the computing efficiency for distributed embedded computing clusters. This architecture is based on an improved Message Passing Interface (Improved-MPI). To address the limited communication speed in embedded environments, a multilevel communication mechanism is employed to alleviate the communication pressure on nodes. By flexibly allocating computing tasks, efficient utilization of every embedded cluster node is ensured, while also solving the problem of single point of failure. In addition, to overcome the challenge of limited RAM in embedded devices, the architecture utilizes the interleaved memory initialization mechanism to run larger computing tasks. Based on this architecture, a specific embedded cluster platform is constructed using the RK3399 board. Various large-scale tasks are deployed on this platform to validate the performance of the architecture. First, a large-scale randomly connected neural network is executed, which serves to verify the architecture's outstanding computational performance and communication capability. Secondly, a functional model of Small-World Spiking Neural Network is constructed, achieving real-time and efficient digital speech recognition. Finally, the implementation of Large Language Models demonstrates that the embedded clusters can achieve performance comparable to modern computers.  © 2005-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1268.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
