---
id: paper-2545
title: 'AirMUA: Dynamically Allocating Users on the Fly in Collaborative Large-Small Model Systems'
authors:
- Cui, Guangming
- Xu, Xiaolong
- Zhang, Yiwen
- Qi, Lianyong
- Cai, Zhipeng
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3632801
url: https://www.scopus.com/pages/publications/105021878341?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5590--5603
keywords:
- collaborative large-small language model system
- Dynamic mobile user allocation
- mobile edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2545 — AirMUA: Dynamically Allocating Users on the Fly in Collaborative Large-Small Model Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In a collaborative large-small language model (CLSLM) system, application providers can deploy their small-scale intelligent services at the edge to serve the mobile users. Due to the personalized characteristics of edge small models, an application provider must properly accommodate its users for service and/or data provision. In general, a cost-effective mobile user allocation (MUA) solution must serve the maximum number of users with minimum edge resources by considering mobile users' preferences. However, existing studies of MUA assume that users' and edge servers' available resources are static and neglect the matching between mobile users' preferences and the edge small models' personalization. This is unrealistic in real-world CLSLM systems where the mobility of users changes dynamically and the edge servers' available resources differ periodically. Therefore, users must be allocated on the fly to edge servers whose available resources also vary over time. Most existing MUA approaches are impractical in real-world CLSLM systems because they are usually designed to address the MUA problem offline, and their performance is usually poor. In this paper, AirMUA, a novel online scheme, is designed, aiming to solve the dynamic MUA (DMUA) problem. AirMUA allocates users to edge servers as they join the system and utilizes system resources dynamically released by user departures. Comprehensive experiments and analyses are conducted to evaluate its performance systematically. Extensive experimental results show the high performance of AirMUA, which ensures its practicality in real-world CLSLM systems.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2545.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
