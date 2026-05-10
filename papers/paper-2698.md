---
id: paper-2698
title: Deep reinforcement learning-based computation offloading and resource allocation in user-centered UAV-MEC
authors:
- Luo, Zhongqiang
- Wu, Wenjie
- Dai, Xiang
- Han, Qiang
venue: Physical Communication
venue_type: journal
year: 2026
doi: 10.1016/j.phycom.2026.102992
url: https://www.scopus.com/pages/publications/105027628841?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computation offloading
- Dual connectivity technology
- Multi-access edge computing
- Resource allocation
- UAV-assisted MEC
- User-centric network
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2698 — Deep reinforcement learning-based computation offloading and resource allocation in user-centered UAV-MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Using unmanned aerial vehicles (UAVs) equipped with servers to assist multi-access edge computing (MEC) can provide computing support in areas with insufficient network coverage or hotspots. However, UAV-MEC systems under traditional cellular network support are susceptible to inter-cell interference and shadow fading, resulting in increased task processing delays and higher energy consumption. To address these challenges, this paper proposes a user-centric UAV-MEC architecture (UCUAV-MEC). This architecture integrates a user-centered transmission method, dynamically adjusting the UAV and access point (AP) to provide flexible computing and communication support for user equipment (UE). Additionally, dual connectivity (DC) technology is employed to enable parallel processing, alleviating resource competition and transmission interference. The delay and energy minimization problem is then formulated by jointly optimizing the UAV position, offloading decision, power allocation, and computing resource allocation within the UCUAV-MEC framework. To solve this problem, this paper proposes a multi-agent collaborative optimization scheme based on deep reinforcement learning (DRL) and convex optimization. Simulation results demonstrate that, compared to traditional UAV-MEC, the proposed optimization scheme based on UCUAV-MEC can reduce delay by up to 72.26% and energy consumption by 73.29%. © 2026 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2698.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
