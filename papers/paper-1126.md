---
id: paper-1126
title: Minimizing URLLC Task Offloading Latency with Full-Duplex STAR-RIS-Aided DRL-ISAC Systems
authors:
- Paul, Anal
- Singh, Keshav
- Li, Chih-Peng
- Mumtaz, Shahid
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2024
doi: 10.1109/GLOBECOM52923.2024.10901282
url: https://www.scopus.com/pages/publications/105000824374?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 73--78
keywords:
- full-duplex
- Integrated sensing and communications
- multi-agent deep reinforcement learning
- simultaneous transmitting and reflecting intelligent surface
- task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1126 — Minimizing URLLC Task Offloading Latency with Full-Duplex STAR-RIS-Aided DRL-ISAC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates the deployment of a full-duplex integrated sensing and communication (ISAC) system for task offloading service to serve ultra-reliable low-latency communications (URLLC), significantly enhanced by a simultaneously transmitting and reflecting reconfigurable intelligent surface (STAR-RIS). Utilizing a non-orthogonal multiple access frame-work, this study extensively addresses the challenges associated with latency-sensitive task offloading from information receivers (IRs) to a mobile edge computing platform. We introduce a novel and sophisticated multi-agent deep reinforcement learning (MA-DRL) approach aimed at minimizing latency in task offloading under a variety of stringent ISAC-URLLC network constraints, including imperfect channel state information. The proposed MA-DRL operates on decentralized execution while maintaining centralized training, using multi-actor-critic networks to enhance learning and performance. The innovative reward decentralization framework in the present MA-DRL optimizes downlink and uplink communications through dynamic power allocation, precise beamforming, and intelligent phase shift management facilitated by the STAR-RIS. The proposed MA-DRL framework significantly outperforms existing multi-agent DRL algorithms, demonstrating substantial gain in reward maximization (i.e., linked to offloading latency minimization) by 27.46% and 52.73%. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1126.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
