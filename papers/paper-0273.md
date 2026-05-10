---
id: paper-0273
title: 'Computation Offloading in beyond 5G Networks: A Distributed Learning Framework and Applications'
authors:
- Chen, Xianfu
- Wu, Celimuge
- Liu, Zhi
- Zhang, Ning
- Ji, Yusheng
venue: IEEE Wireless Communications
venue_type: journal
year: 2021
doi: 10.1109/MWC.001.2000296
url: https://www.scopus.com/pages/publications/85106170246?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 56--62
keywords:
- 5G mobile communication systems
- computation offloading
- Markov processes
- Multi agent systems
- Queueing networks
- Reinforcement learning
- Communication access
- Computation offloading
- Computing system
- Distributed learning
- Edge computing
- Learning frameworks
- Multiaccess
- Technical challenges
- Uncertainty
- Wireless communications
- Learning algorithms
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0273 — Computation Offloading in beyond 5G Networks: A Distributed Learning Framework and Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Facing the trend of merging wireless communications and multi-access edge computing (MEC), this article studies computation offloading in beyond fifth generation networks. To address the technical challenges originating from the uncertainties and the sharing of limited resource in an MEC system, we formulate the computation offloading problem as a multi-agent Markov decision process, for which a distributed learning framework is proposed. We present a case study on resource orchestration in computation offloading to showcase the potential of an online distributed reinforcement learning algorithm developed under the proposed framework. Experimental results demonstrate that our learning algorithm outperforms the benchmark resource orchestration algorithms. Furthermore, we outline the research directions worth in-depth investigation to minimize the time cost, which is one of the main practical issues that prevent the implementation of the proposed distributed learning framework.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0273.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
