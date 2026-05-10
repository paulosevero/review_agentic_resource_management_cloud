---
id: paper-1294
title: 'DeepAir: A Multi-Agent Deep Reinforcement Learning-Based Scheme for an Unknown User Location Problem'
authors:
- Yamansavascilar, Baris
- Ozgovde, Atay
- Ersoy, Cem
venue: IEEE Access
venue_type: journal
year: 2024
doi: 10.1109/ACCESS.2024.3518562
url: https://www.scopus.com/pages/publications/85212643391?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 192195--192208
keywords:
- Deep reinforcement learning
- task offloading
- UAVs
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1294 — DeepAir: A Multi-Agent Deep Reinforcement Learning-Based Scheme for an Unknown User Location Problem

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicles (UAVs) are a major component in next-generation network architecture proposals, playing a critical role in problems like dynamic capacity enhancement, user coverage, and task offloading. When smart utilization of the UAVs is missing, these proposals may require sophisticated approaches, including the deployment of additional edge servers and orchestration efforts. A typical challenge arises from the dynamic nature of real-world problems in which the required capacity should be provided at particular times when fixed infrastructure proves insufficient. One of those existing dynamic problems is the unknown user locations in an infrastructure-less environment in which users cannot connect to any communication device or computation-providing server, which is essential to task offloading in order to achieve the required quality of service (QoS). Therefore, in this study, we investigate this problem thoroughly and propose a novel deep reinforcement learning (DRL) based scheme, DeepAir. DeepAir uses four main phases including sensing, localization, resource allocation, and multi-access edge computing (MEC) to provide the corresponding QoS requirements for the offloaded tasks without violating the maximum tolerable delay. To this end, we use two types of UAVs including detector UAVs, and serving UAVs. We utilize detector UAVs as DRL agents which ensure the sensing, localization, and resource allocation phases. On the other hand, we utilize serving UAVs to provide MEC features. Our experiments show that DeepAir provides higher task success rates by deploying fewer detector UAVs in different scenarios with different numbers of users and user attraction points compared to benchmark methods. Thus, DeepAir achieves 59.65%, 86.06%, and 86.72% task success rates for 2, 4, and 6 detector UAVs, respectively, by using 12 serving UAVs, while the most successful benchmark method provides 28.62%, 41.39%, and 61.09% task success rates for the same configuration, respectively.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1294.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
