---
id: paper-1218
title: Joint Optimization of Vehicular Sensing and Vehicle Digital Twins Deployment for DT-Assisted IoVs
authors:
- Tang, Lun
- Cheng, Zhangchao
- Dai, Jun
- Zhang, Hongpeng
- Chen, Qianbin
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2024.3373175
url: https://www.scopus.com/pages/publications/85187315873?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 11834--11847
keywords:
- age of information (AoI)
- deep reinforcement learning
- digital twin (DT)
- Internet of vehicles (IoVs)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1218 — Joint Optimization of Vehicular Sensing and Vehicle Digital Twins Deployment for DT-Assisted IoVs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Emerging Intelligent Transportation Systems (ITS) applications in the B5G/6G era have higher demands on real-time information in real traffic scenarios, and the current Internet of Vehicles (IoVs) can hardly support the operation of such applications. To realize the efficient operation of ITS applications, we integrate Digital Twin (DT) technology into IoVs and propose a framework of DT-assisted cloud-edge collaboration IoVs for intelligent transportation. DT synchronization requires vehicular sensing and data uploading, where the sensing capability and sensing policy of different vehicles affect the accuracy of DT, and the simultaneous sensing of neighboring vehicles creates data redundancy. The deployment strategy of Vehicle DTs (VDTs) at the network edge affects the real-time performance of DT. The mobility of vehicles, the low-latency requirements of DT, and the limited heterogeneous resources of edge servers pose great challenges to the deployment of VDTs. To address the above problems, we established the vehicular sensing model considering sensing quality, cost and redundancy. Then, A DT synchronization mechanism is designed and an improved Age of Information (AoI) metric is used to measure the freshness of the real vehicle state data received by the cloud during the DT synchronization process. We proposed a joint optimization problem of vehicular sensing and VDTs deployment to maximize the system Quality of Services (QoS), which is reflected through the vehicular sensing quality, AoI and system cost in DT synchronization process. We develop an algorithm based on Multi-Agent Deep Reinforcement Learning (MADRL) to solve this optimization problem, called DTSD-MAPPO. Numerical results show that the scheme reduces the system cost and improves the accuracy and real-time in DT synchronization. © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1218.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
