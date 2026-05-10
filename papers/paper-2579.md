---
id: paper-2579
title: Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network
authors:
- Gao, Yunfei
- Wu, Peng
- Yuan, Xiaopeng
- Hu, Yulin
- Cao, Xiaoxiang
- Schmeink, Anke
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3656412
url: https://www.scopus.com/pages/publications/105028518205?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 3D deployment and association
- federated MADRL
- MEC
- Multi-UAV
- no-fly zones
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

# paper-2579 — Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We investigate a multi-unmanned aerial vehicle (UAV)-aided mobile edge computing (MEC) system where UAVs provide to ground devices (GDs) comprehensive services, including communication, computation, and joint decision-making (CCJD). Specifically, the system is dynamic and heterogeneous, with time-varying task requests and UAVs of diverse capabilities, data processing requirements, and priorities. To enhance the task execution efficiency, we provide a joint optimization design that minimizes the average system operation time by optimizing UAVs' three-dimensional (3D) deployment and GDs association, while adhering to no-fly zones (NFZs) and obstacle constraints. Nevertheless, the formulated problem exhibits high non-convexity with a rapidly scaling complexity w.r.t. the number of both UAVs and GDs. To address the challenges, we propose an efficient and low-complexity learning-based approach accelerated by analytical characterizations on GD's association to enhance algorithm convergence. First, we derive a closed-form solution for GD's association based on the Lagrangian dual method and optimal transmission theory (OTT). We also analytically derive the performance gap between the closed-form association and the optimal exhaustive search-based solution. Theoretical analysis demonstrates that our proposed approach achieves substantial complexity reduction compared to exhaustive search, while almost achieving the same performance. Based on the characterized optimal association, we reformulate the original joint design problem equivalently into a UAV 3D deployment optimization problem without loss of optimality, which is further established as a Markov decision process (MDP). Afterwards, an efficient algorithm based on the proposed federated multi-agent deep reinforcement learning algorithm is proposed to solve the reformulated problem, where the reward function is designed based on the closed-form GD's association and its corresponding average delay, leveraging the dueling network architecture to enhance training stability and accelerate convergence. Finally, simulation results demonstrate the superior performance of the proposed method compared to the benchmarks. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2579.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
