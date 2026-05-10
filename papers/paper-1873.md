---
id: paper-1873
title: Cost-Efficient Deployment Optimization for Multi-UAV-Assisted Vehicular Edge Computing Networks
authors:
- Liu, Yinan
- Yang, Chao
- Tang, Yanqun
- Zhao, Haitao
- Liu, Yi
- Xie, Shengli
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3515107
url: https://www.scopus.com/pages/publications/86000435093?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6158--6170
keywords:
- Deployment
- hierarchical reinforcement learning (HRL)
- multiagent reinforcement learning
- uncrewed aerial vehicle (UAV)
- vehicular edge computing networks (VECNs)
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

# paper-1873 — Cost-Efficient Deployment Optimization for Multi-UAV-Assisted Vehicular Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Taking into account the flexible deployment and Line-of-Sight (LoS) communication links of uncrewed aerial vehicles (UAVs), this article proposes a multi-UAV-assisted vehicular edge computing networks (VECNs) architecture to provide instantaneous computation support at multiple congestion road segments. Given that the computation resources of a single UAV are insufficient, and offloading tasks directly to the cloud computing center (CCC) in intelligent transportation systems (ITSs) introduces significant latency, multiple UAVs with precached service or content caching data are deployed optimally for the vehicle users. In order to address the tradeoff between system costs and service efficiency, we propose a novel cost-efficient layered optimization scheme, in which the number and deployment positions of UAVs are jointly optimized. According to the varying vehicular network environments and the dynamic requirements of vehicle users, we design a hierarchical reinforcement learning algorithm, combining double deep Q network (DDQN) and multiagent deep deterministic policy gradient (MADDPG), the former is used to optimize the number of UAVs, and the deployment of UAVs are optimized via the MADDPG. Simulation results demonstrate the effectiveness of the proposed scheme in lowering total task completed latency and increasing the system profits. The service efficiency in dealing with the vehicle users' requirements also be improved.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1873.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
