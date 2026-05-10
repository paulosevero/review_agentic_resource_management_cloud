---
id: paper-0485
title: Learning-based Multi-Drone Network Edge Orchestration for Video Analytics
authors:
- Qu, Chengyi
- Singh, Rounak
- Esquivel-Morel, Alicia
- Calyam, Prasad
venue: Proceedings - IEEE INFOCOM
venue_type: conference
year: 2022
doi: 10.1109/INFOCOM48880.2022.9796706
url: https://www.scopus.com/pages/publications/85133283256?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1219--1228
keywords:
- Multi-access edge computing
- Multi-drone networks
- Network protocols
- Reinforcement learning
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

# paper-0485 — Learning-based Multi-Drone Network Edge Orchestration for Video Analytics

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (a.k.a. drones) with high-resolution video cameras are useful for applications in e.g., public safety and smart farming. Inefficient configurations in drone video analytics applications due to edge network miscon-figurations can result in degraded video quality and inefficient resource utilization. In this paper, we present a novel scheme for offline/online learning-based network edge orchestration to achieve pertinent selection of both network protocols and video properties in multi-drone based video analytics. Our approach features both supervised and unsupervised machine learning algorithms to enable decision making for selection of both network protocols and video properties in the drones' pre-takeoff stage i.e., offline stage. In addition, our approach facilitates drone trajectory optimization during drone flights through an online reinforcement learning-based multi-agent deep Q-network algorithm. Evaluation results show how our offline orchestration can suitably choose network protocols (i.e., amongst TCP/HTTP, UDP/RTP, QUIC). We also demonstrate how our unsupervised learning approach outperforms existing learning approaches, and achieves efficient offloading while also improving the network performance (i.e., throughput and round-trip time) by least 25% with satisfactory video quality. Lastly, we show via trace-based simulations, how our online orchestration achieves 91% of oracle baseline network throughput performance with comparable video quality. © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0485.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
