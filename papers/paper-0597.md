---
id: paper-0597
title: Decentralized Edge Intelligence-Driven Network Resource Orchestration Mechanism
authors:
- Gong, Yongkang
- Yao, Haipeng
- Wang, Jingjing
- Wu, Di
- Zhang, Ni
- Richard Yu, F.
venue: IEEE Network
venue_type: journal
year: 2023
doi: 10.1109/MNET.120.2200086
url: https://www.scopus.com/pages/publications/85135750456?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 270--276
keywords:
- computation offloading
- Heuristic algorithms
- Job analysis
- Multi agent systems
- Multitasking
- Optimization
- Simulation platform
- Collaborative Work
- Computational modelling
- Decentralised
- Edge computing
- Edge intelligence
- Energy-consumption
- Heuristics algorithm
- Multiaccess
- Optimisations
- Task analysis
- Energy utilization
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

# paper-0597 — Decentralized Edge Intelligence-Driven Network Resource Orchestration Mechanism

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of artificial intelligence of things (AIoT), multi-access edge computing (MEC) becomes a key enabler to migrate cloud services to edge clients. In comparison to traditional cloud computing techniques, MEC is characterized with low transmission latency, good flexibility, adaptability and robustness. Nevertheless, traditional resource allocation methods are difficult to meet the requirements of achieving a ubiquitous, pervasive, and intelligent computation offloading strategy in high-dynamic network environments. In this article, we construct an edge intelligence-enabled cloud-edge-client collaborative network structure, and conceive a model-aided multi-agent deep deterministic policy gradient (MA2DDPG) computation offloading framework relying on both centralized training and distributed execution. Simulation results corroborate that our proposed decentralized resource orchestration platform significantly reduces the energy consumption and the transmission latency against state-of-the-art methods. Finally, we highlight open challenges and potential solutions.  © 1986-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0597.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
