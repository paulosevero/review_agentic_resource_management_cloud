---
id: paper-2947
title: 'Satellite-Enabled Edge Intelligence for Climate-Resilient Emergency Mobility: A Survey of On-Orbit Edge Computing'
authors:
- Zong, Ping
- Ou, Zhonghong
- An, Ran
- Zhao, Qingnan
- Zhang, Guoxin
- Xue, Kaiwen
- Tian, Zijing
- Lyu, Shuai
- Shen, Yiran
- He, Sihao
- Zhu, Yifan
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2026
doi: 10.1109/TITS.2026.3677347
url: https://www.scopus.com/pages/publications/105034638563?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Climate-resilient transportation
- distributed inference
- earth observation
- emergency mobility
- low-carbon operations
- on-orbit edge computing
- satellite–ground collaboration
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-2947 — Satellite-Enabled Edge Intelligence for Climate-Resilient Emergency Mobility: A Survey of On-Orbit Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Climate change is increasing the frequency and intensity of extreme weather events, which can rapidly disrupt road capacity, public transit operations, and logistics corridors. Reliable emergency mobility and low-carbon recovery therefore require timely, trustworthy, and spatially comprehensive situational awareness as well as resilient decision-making under intermittent connectivity. Earth-observation satellites and emerging LEO constellations provide global coverage for hazard monitoring (e.g., floods, wildfires, landslides) and infrastructure assessment, yet the resulting data volumes and limited contact windows make purely ground-centric processing increasingly insufficient for real-time transportation response. This paper surveys on-orbit edge computing (OEC) as a spaceborne edge layer that can close the sensing–analysis–action loop for climate-resilient transportation systems. We organize the literature into three evolutionary stages: 1) single-satellite on-orbit processing for event triggering and data triage, 2) satellite–ground collaboration for split inference, task offloading, and end-to-end orchestration, and 3) inter-satellite distributed computing for constellation-scale learning and inference under dynamic topology. Beyond summarizing methods, datasets, and platforms, we discuss how these OEC capabilities can be integrated with transportation digital twins and emergency operations to enable faster disruption detection, evacuation planning support, and bandwidth- and carbon-aware information delivery. Finally, we outline open challenges and future directions, including robust benchmarking under climate stressors, trustworthy autonomy, and LLM-assisted decision support across satellite–ground workflows. © 2000-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2947.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
