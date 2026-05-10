---
id: paper-0432
title: 'Decentralized Computation Offloading with Cooperative UAVs: Multi-Agent Deep Reinforcement Learning Perspective'
authors:
- Hwang, Sangwon
- Lee, Hoon
- Park, Juseong
- Lee, Inkyu
venue: IEEE Wireless Communications
venue_type: journal
year: 2022
doi: 10.1109/MWC.003.2100690
url: https://www.scopus.com/pages/publications/85140894041?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 24--31
keywords:
- Antennas
- computation offloading
- Data handling
- Deep learning
- Mobile edge computing
- Multi agent systems
- Reinforcement learning
- Unmanned aerial vehicles (UAV)
- Aerial vehicle
- Computation offloading
- Computing resource
- Decentralised
- Edge server
- Input datas
- Multi agent
- Reinforcement learnings
- Research opportunities
- Task offloading
- Internet of things
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0432 — Decentralized Computation Offloading with Cooperative UAVs: Multi-Agent Deep Reinforcement Learning Perspective

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Limited computing resources of internet-of-things (IoT) nodes incur prohibitive latency in processing input data. This triggers new research opportunities toward task offloading systems where edge servers handle intensive computations of IoT devices. Deploying the computing servers at existing base stations may not be sufficient to support IoT nodes operating in a harsh environment. This requests mobile edge servers to be mounted on unmanned aerial vehicles (UAVs) that provide on-demand mobile edge computing (MEC) services. Time-varying offloading demands and mobility of UAVs need a joint design of the optimization variables for all time instances. Therefore, an online decision mechanism is essential for UAV-aided MEC networks. This article presents an overview of recent deep reinforcement learning (DRL) approaches where decisions about UAVs and IoT nodes are taken in an online manner. Specifically, joint optimization over task offloading, resource allocation, and UAV mobility is addressed from the DRL perspective. For the decentralized implementation, a multi-agent DRL method is proposed where multiple intelligent UAVs cooperatively determine their computations and communication policies without central coordination. Numerical results demonstrate that the proposed decentralized learning strategy is superior to existing DRL solutions. The proposed framework sheds light on the viability of the decentralized DRL techniques in designing self-organizing IoT networks.  © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0432.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
