---
id: paper-0905
title: Decentralized Multi-layer Vehicular Edge Computing Framework for Time-Efficient Task Coordination
authors:
- Fardad, Mohammad
- Muntean, Gabriel-Miro
- Tal, Irina
venue: IEEE International Symposium on Broadband Multimedia Systems and Broadcasting, BMSB
venue_type: conference
year: 2024
doi: 10.1109/BMSB62888.2024.10608220
url: https://www.scopus.com/pages/publications/85201528990?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- latency
- Multi-agent deep-reinforcement learning
- Task coordination
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0905 — Decentralized Multi-layer Vehicular Edge Computing Framework for Time-Efficient Task Coordination

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicle edge computing (VEC) offers substantial potential to enhance real-time applications in the connected autonomous vehicle (CAV) sector by positioning edge servers near CAVs. The need to balance real-time application demands and the diversity of tasks underscores the criticality of carefully deciding whether to process these tasks locally or to offload them for remote processing. This decision is pivotal in achieving efficient resource management, particularly in dynamic vehicular environments, emphasizing the requirement of exquisite policies to optimize VEC systems' performance within the CAV ecosystem. While centralized policies face limitations in managing largescale deployments, decentralized approaches often fail to foster effective collaboration and coordination among CAVs. This paper proposes a novel multi-layered, decentralized framework designed for time-efficient task management and optimized network resource utilization in dynamic vehicular scenarios to address these limitations. This framework incorporates a novel multiagent deep reinforcement learning (MADRL) algorithm to enable intelligent decision-making for efficient task execution. The proposed algorithm considers the diverse computing capabilities of network entities, aiming to reduce latency without compromising task completion rates. Simulation results demonstrate that our proposed algorithm has superior performance in latency reduction while improving task completion rates compared to existing algorithms. © 2024 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0905.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
