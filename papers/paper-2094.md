---
id: paper-2094
title: Delay, Energy, and Outage Considerations in GenAI-Enhanced MEC-NOMA-Enabled Vehicular Networks
authors:
- Saleem, Muhammad Asim
- Zhou, Shijie
- Fengli, Zhang
- Ahmad, Tanveer
- Nigar, Nahida
- Hadi, Muhammad Usman
- Shabaz, Mohammad
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2025
doi: 10.1109/TITS.2025.3548268
url: https://www.scopus.com/pages/publications/105000514443?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- computation task offloading
- interference
- MEC
- NOMA
- outage probability
- vehicular networks
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
    my_justification: Out of scope
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

# paper-2094 — Delay, Energy, and Outage Considerations in GenAI-Enhanced MEC-NOMA-Enabled Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, vehicular networks have experienced substantial growth, transforming the landscape of the transportation industry. In particular, the issue of computing task offloading in vehicular networks is critically important. The two key considerations are offloading task delay and energy consumption. Thus, a multiple access (MA) scheme is necessary in vehicular networks to facilitate more efficient computation task offloading. Non-orthogonal multiple access (NOMA) is recognized as a promising candidate for multiple access in fifth-generation (5G) and beyond networks due to its potential to improve overall spectrum efficiency through superposition coding. Moreover, mobile edge computing (MEC) can minimize computation task delay and energy consumption by bringing computational resources closer to vehicles. Therefore, this paper examines the potential of employing mobile edge computing (MEC) with non-orthogonal multiple access (NOMA) in vehicular networks to reduce overall computation offloading task delay and energy consumption. Specifically, computation models for task delay and energy consumption are presented. Additionally, considering universal frequency reuse, we analyze interference-limited scenarios and allow interference from the transmissions of other vehicles and roadside units. The optimization problems for delay and energy are formulated based on the described models. Due to the non-convex nature of the optimization problem, they are solved numerically using the Python programming language. Furthermore, analytical expressions for outage probability are provided to evaluate the typical vehicle's outage performance. Simulation results demonstrate the delay and energy performance of the MEC-NOMA-enabled vehicular networks compared to their OMA-based counterparts. The results indicate that MEC-NOMA achieves lower delay, reduced energy consumption, and improved outage performance compared to OMA-based vehicular networks.  © 2000-2011 IEEE.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2094.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
