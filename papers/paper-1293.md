---
id: paper-1293
title: Task Offloading and Resource Allocation in an RIS-Assisted NOMA-Based Vehicular Edge Computing
authors:
- Yakubu, Abdul-Baaki
- Abd El-Malek, Ahmed H.
- Abo-Zahhad, Mohammed
- Muta, Osamu
- Elsabrouty, Maha M.
venue: IEEE Access
venue_type: journal
year: 2024
doi: 10.1109/ACCESS.2024.3454810
url: https://www.scopus.com/pages/publications/85203413903?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 124330--124348
keywords:
- multi-agent deep reinforcement learning
- non-orthogonal multiple access
- real-time task offloading
- Reconfigurable intelligent surface
- vehicular edge computing
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

# paper-1293 — Task Offloading and Resource Allocation in an RIS-Assisted NOMA-Based Vehicular Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rise of intelligent transportation (ITS), autonomous cars, and on-the-road entertainment and computation, vehicular edge computing (VEC) has become a primary research topic in 6G and beyond communications. On the other hand, reconfigurable intelligent surfaces (RIS) are a major enabling technology that can help in the task offloading domain. This study introduces a novel VEC architecture that incorporates non-orthogonal multiple access (NOMA) and reconfigurable intelligent surfaces (RIS), where vehicles perform binary or partial computation offloading to edge nodes (eNs) for task execution. We construct a vehicle-to-infrastructure (V2I) transmission model by considering vehicular interference and formulating a joint task offloading and resource allocation (JTORA) problem with the goal of reducing total service latency and energy usage. Next, we decompose this problem into task offloading (TO) problem on the vehicle side and resource allocation (RA) problem on the eN side. Specifically, we describe offloading decisions and offloading ratios as a decentralized partially observable Markov decision process (Dec-POMDP). Subsequently, a multi-agent distributed distributional deep deterministic policy gradient (MAD4PG) is proposed to solve the TO problem, where every vehicular agent learns the global optimal policy and obtains individual decisions. Furthermore, a whale optimization algorithm (WOA) is used to optimize the phase shift coefficient of the RIS. Upon receiving offloading ratios and offloading decisions from vehicles, edge nodes utilize the Lagrange multiplier method (LMM) and Karush-Kuhn-Tucker (KKT) conditions to address the RA problem. Finally, we design a simulation model based on real-world vehicular movements. The numerical results demonstrate that, compared to previous algorithms, our proposed approach reduces the overall delay and energy consumption more effectively. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1293.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
