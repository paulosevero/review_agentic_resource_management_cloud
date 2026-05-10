---
id: paper-2816
title: A digital twin-assisted framework for secure task offloading in adaptive vehicular edge computing system
authors:
- Wang, Chen
- Qian, Zhen
- Li, Guanghui
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2026.112117
url: https://www.scopus.com/pages/publications/105030549555?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Age of information
- Byzantine attack
- Digital twin
- Task offloading
- Vehicular edge computing
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2816 — A digital twin-assisted framework for secure task offloading in adaptive vehicular edge computing system

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Digital Twin (DT)-assisted vehicular edge computing (VEC) presents significant potential for Intelligent Transportation Systems (ITS), yet faces three interconnected challenges in practical implementation. Existing architectures exhibit insufficient adaptability to dynamically optimize physical-layer models in rapidly evolving vehicular environments. At the same time, conventional latency-driven optimization strategies inadequately exploit distributed edge resources and neglect information freshness requirements. Furthermore, global information sharing enabled by DTs introduces critical security vulnerabilities, as malicious agents can exploit this characteristic to launch Byzantine attacks, destabilizing the system. We propose an adaptive vehicular edge computing system (AVECS) in which the DT layer is synchronized with real-world vehicles, and the physical layer models are continuously optimised as the system evolves. A Byzantine resilience mechanism is integrated into the DT layer to improve reliability. We incorporate Age of Information (AoI) into the optimization process to improve the efficiency of task execution. The secure task offloading problem is formulated as a Decentralized Partially Observable Markov Decision Process (DEC-POMDP), and we develop a DT-assisted multi-agent proxy policy optimization (MAPPO) algorithm to learn optimal offloading actions that minimize task completion delay and the average AoI of the entire system. Extensive experiments demonstrate that AVECS reduces task completion delay and improves overall system throughput. The source code of AVECS is available at https://github.com/Gavan-Github/AVECS.git. © 2026 Elsevier B.V.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2816.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
