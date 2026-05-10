---
id: paper-2913
title: Multi-Agent Deep Reinforcement Learning for Safe Autonomous Driving With RICS-Assisted MEC
authors:
- Zhang, Xueyao
- Yang, Bo
- Cao, Xuelin
- Yu, Zhiwen
- Alexandropoulos, George C.
- Zhang, Yan
- Debbah, Merouane
- Yuen, Chau
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2026
doi: 10.1109/TITS.2025.3632408
url: https://www.scopus.com/pages/publications/105022694338?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 800--815
keywords:
- Autonomous driving
- multi-access edge computing
- multi-agent deep reinforcement learning
- reconfigurable intelligent computational surface
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2913 — Multi-Agent Deep Reinforcement Learning for Safe Autonomous Driving With RICS-Assisted MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Environment sensing and fusion via onboard sensors are envisioned to be widely applied in future autonomous driving networks. This paper considers a vehicular system with multiple self-driving vehicles that is assisted by multi-access edge computing (MEC), where image data collected by the sensors is offloaded from cellular vehicles to the MEC server using vehicle-to-infrastructure (V2I) links. Sensory data can also be shared among surrounding vehicles via vehicle-to-vehicle (V2V) communication links. To improve spectrum utilization, the V2V links may reuse the same frequency spectrum as the V2I links, which may cause severe interference. To tackle this issue, we leverage reconfigurable intelligent computational surfaces (RICSs) to jointly enable V2I reflective links and mitigate interference appearing at the V2V links. Considering the limitations of traditional algorithms in addressing this problem, such as the assumption of quasi-static channel state information, which restricts their ability to adapt to dynamic environmental changes and leads to poor performance under frequently varying channel conditions, in this paper, we formulate the problem at hand as a Markov game. Our novel formulation is applied to time-varying channels subject to multi-user interference and introduces a collaborative learning mechanism among users. The considered optimization problem is solved via a driving safety-enabled multi-agent deep reinforcement learning (DS-MADRL) approach that capitalizes on the RICS presence. Our extensive numerical investigations showcase that the proposed reinforcement learning approach achieves faster convergence and significant enhancements in both data rate and driving safety, as compared to various state-of-the-art benchmarks. © 2000-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2913.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
