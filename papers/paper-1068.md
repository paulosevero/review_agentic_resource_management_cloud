---
id: paper-1068
title: Stackelberg-Game Computation Offloading Scheme for Parked Vehicle-Assisted VEC and Experiment Analysis
authors:
- Liu, Chunhong
- Zhao, Mengdi
- Wang, Huaichen
- Cheng, Bo
- Liu, Jialei
- Yuan, Peiyan
venue: IEEE Transactions on Intelligent Vehicles
venue_type: journal
year: 2024
doi: 10.1109/TIV.2024.3357076
url: https://www.scopus.com/pages/publications/85184008882?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5694--5705
keywords:
- computation offloading
- computational experiment
- Stackelberg game
- vehicle collaboration
- Vehicle edge computing
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
    my_justification: Game theory
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

# paper-1068 — Stackelberg-Game Computation Offloading Scheme for Parked Vehicle-Assisted VEC and Experiment Analysis

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicle edge computing (VEC) offers users low-latency and high-reliability services by using computational resources at the network's edge. Nevertheless, because of inadequate infrastructure and limited resources, computation-intensive and delay-sensitive vehicle applications cannot be performed efficiently at the edge. Therefore, several studies have used the idle resources of parked vehicles to assist in computation offloading. In this article, we propose a parked vehicle-assisted vehicle edge computing architecture considering multi-agent collaboration, including intelligent vehicles and edge servers. Additionally, we propose a framework for a parallel Internet of Vehicles (IoV) utilizing computational experiment. The service provider is assigned the role of owning VEC resources and recruiting parking vehicle resources. The model was constructed by using the resource consumption-service relationship of both offloading parties to ensure service quality. First, a Stackelberg game model was constructed based on the interaction between requesting vehicles and a service provider. The latter was the leader, and the requesting vehicles were the followers. The Nash equilibrium for optimal pricing and offloading allocations was attained and verified, and a distributed gradient-based equilibrium algorithm was designed to solve the Stackelberg game model and obtain the final decision through mutual communication. The method also protects the privacy of participants and respects the willingness of requesting vehicles to offload. Finally, the simulation experiments confirmed that the proposed algorithm can achieve game equilibrium. Furthermore, it outperformed state-of-the-art algorithms in improving the service provider's utility. © 2016 IEEE.

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
- **my_justification:** "Game theory"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1068.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
