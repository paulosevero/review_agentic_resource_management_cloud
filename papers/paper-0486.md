---
id: paper-0486
title: 'UAV Swarms in Smart Agriculture: Experiences and Opportunities'
authors:
- Qu, Chengyi
- Boubin, Jayson
- Gafurov, Durbek
- Zhou, Jianfeng
- Aloysius, Noel
- Nguyen, Henry
- Calyam, Prasad
venue: Proceedings - 2022 IEEE 18th International Conference on e-Science, eScience 2022
venue_type: conference
year: 2022
doi: 10.1109/eScience55777.2022.00029
url: https://www.scopus.com/pages/publications/85145438688?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 148--158
keywords:
- computation offloading
- intelligent orchestration
- multi-sensor network
- smart agriculture
- UAV swarms
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0486 — UAV Swarms in Smart Agriculture: Experiences and Opportunities

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Smart agriculture benefits from unmanned aerial vehicles (UAV), and in-field sensors to collect data used to make responsible crop management decisions which sustainably increase yields. In addition, smart agriculture relies on machine learning algorithms, creative networking solutions, and edge and cloud computing resources to collect, transfer, and process agricultural data. UAV can carry a wide array of sensors, maneuver rapidly throughout the field, apply treatments for some crop health problems, and can be flown by software. UAV, however, have small batteries and limited carrying capacities which keep missions short. In this paper, we provide an overview of state-of-the-art UAV swarm technology for smart agriculture, and present experiences from real-world agricultural UAV swarm case studies. We describe how quick mapping of large areas such as crop fields necessitates multiple UAV missions, potentially using multiple UAV simultaneously as a swarm. We detail how swarms of UAV have added advantages over a single UAV deployment. They can coordinate to map areas in parallel, leverage multiple sensor types, target areas for close inspection, and diagnose and treat problems rapidly. UAV swarms come with additional implementation difficulties beyond single UAV. We list challenges to implementers in terms of Resource allocation, compute orchestration, multi-agent mission planning and swarm goal definition. We also describe recent advances in edge computing, machine learning, and autonomy in orchestration and resource management techniques for swarm deployments. Finally, we conclude with research opportunities that future work can address to improve swarm performance, scale, and adoption for smart agriculture.  © 2022 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0486.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
