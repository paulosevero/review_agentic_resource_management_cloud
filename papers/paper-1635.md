---
id: paper-1635
title: Air-Ground Edge Task Offloading Based on Multi-UAV Path Optimization and Resource Allocation
authors:
- He, Chenguang
- Li, Jing
- Wei, Shouming
- Guo, Mengrui
venue: Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
venue_type: conference
year: 2025
doi: 10.1007/978-3-031-86203-8_16
url: https://www.scopus.com/pages/publications/105002140779?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 189--201
keywords:
- Deep Reinforcement Learning
- Edge Computing
- Task Offloading
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

# paper-1635 — Air-Ground Edge Task Offloading Based on Multi-UAV Path Optimization and Resource Allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, space-air-ground integrated network(SAGIN) has been recognized as a promising area in 6G research. In the air-ground component of SAGIN, airborne device such as unmanned aerial vehicles (UAVs) can provide task offloading and computing services to ground devices. Edge servers are installed on UAVs to provide data offloading services for ground devices. The high mobility of UAVs, compared to base stations and edge computing devices on the ground, makes it better able to provide timely and effective services to the devices. Considering the needs of delay-sensitive devices, this paper jointly allocates computational resources and designs UAV trajectories to achieve the goal of minimizing delay. In this paper, we use non-orthogonal multiple access (NOMA) technique in the uplink channel, which allows a UAV to serve multiple ground devices simultaneously. Both the UAV and the ground devices are moving, and the ground devices need to re-establish their connection to the UAV every once in a while. Based on the traditional Deep Reinforcement Learning (DRL) algorithm, this study proposes the Multi-Agent DRL (MADRL) algorithm to jointly determine the optimal 3D trajectory and computational resource allocation of UAVs.The MADRL algorithm achieves complete ground cooperation among multiple UAVs as agents in optimizing the latency by co-training the neural network, simplifying the network structure, and improving the training efficiency. Numerical results show that the proposed MADRL algorithm can converge under the system quality of service (QoS) constraints, and the convergence speed is faster than that of the traditional deep Q network (DQN) algorithm. The average total delay of the system can also be effectively reduced and converged in a multi-UAV scenario. © ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1635.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
