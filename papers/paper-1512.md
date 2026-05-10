---
id: paper-1512
title: 'Energy-Efficient Strategic AAV-Enabled MEC Networks via STAR-RIS: Joint Optimization of Trajectory and User Association'
authors:
- Deng, Xiaoheng
- Yang, Pinwei
- Lin, Hairong
- Wang, Leilei
- Lin, Siyu
- Gui, Jinsong
- Chen, Xuechen
- Qian, Yurong
- Zhang, Jingjing
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3527002
url: https://www.scopus.com/pages/publications/85214502055?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 14921--14937
keywords:
- Autonomous aerial vehicle (AAV)
- Mobile edge computing (MEC)
- multiagent reinforcement learning (MARL). simultaneously transmitting and reflecting reconfigurable intelligent surfaces
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

# paper-1512 — Energy-Efficient Strategic AAV-Enabled MEC Networks via STAR-RIS: Joint Optimization of Trajectory and User Association

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The deployment of Simultaneously Transmitting and Reflecting Reconfigurable Intelligent Surfaces (STAR-RIS) has proven to be an effective means to extend coverage and improve wireless signal quality. STAR-RIS in wireless networks for aided autonomous aerial vehicle (AAV) communications enables a significant boost in network capacity and the provision of virtual line-of-sight (LoS) links to efficiently meet the quality-of-service (QoS) requirements of user equipment (UE). Accordingly, this article proposes a novel STAR-RIS-aided multi-AAV communication framework to exploit energy efficiency and total throughput maximally. We formulate the long-term optimization problem as a decentralized, partially observed Markov decision process (DEC-POMDP). Then, we formulate the discrete association scheduling problem as a noncooperative theoretical game and propose the UA-CFG algorithm to realize the UE association scheme that converges to a Nash equilibrium (NE). Then, a multiagent reinforcement learning (MARL) method with well-established robustness is devised to continuously optimize the trajectories and energetic consumption of AAVs through centralized training and distributed implementation. Experimental results reveal that the performance of the proposed algorithm is considerable compared to other traditional schemes. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1512.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
