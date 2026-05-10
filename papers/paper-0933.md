---
id: paper-0933
title: 'PDPPnet: Prioritized Delay-aware and Peer-to-Peer Task Offloading in Cloud-Edge Continuum with Double Dueling Deep Q-Networks'
authors:
- Giannopoulos, Anastasios
- Paralikas, Ilias
- Spantideas, Sotirios
- Nomikos, Nikolaos
- Trakadas, Panagiotis
venue: IEEE International Workshop on Computer Aided Modeling and Design of Communication Links and Networks, CAMAD
venue_type: conference
year: 2024
doi: 10.1109/CAMAD62243.2024.10943043
url: https://www.scopus.com/pages/publications/105002854266?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Cloud-edge continuum
- deep Q-network (DQN)
- deep reinforcement learning
- multi-agent systems
- prioritized task management
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

# paper-0933 — PDPPnet: Prioritized Delay-aware and Peer-to-Peer Task Offloading in Cloud-Edge Continuum with Double Dueling Deep Q-Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient management of computational tasks in the cloud-edge continuum (CEC) is crucial for modern computing environments. This paper introduces the Prioritized Delay-aware and Peer-to-Peer Task Offloading (PDPPnet) scheme, employing multi-agent Double Dueling Deep Q-Networks (DDDQNs) to optimize task offloading in a distributed framework. PDPPnet uniquely addresses the challenges of uncertain load dynamics and task prioritization at edge nodes, enabling autonomous decision-making for non-divisible, delay-sensitive tasks without reliance on prior task models from other nodes. By formulating a multi-agent computation offloading problem, PDPPnet minimizes the expected long-term latency and task drop ratio while respecting task priorities. The architecture supports both peer-to-peer (P2P) and peer-to-Cloud (P2C) offloading, ensuring seamless task flow across the CEC. We integrated LSTM-predicted load dynamics with DDDQNs to enhance the long-term cost estimation, significantly improving decision-making efficacy. Simulation results demonstrate that PDPPnet markedly outperforms conventional offloading algorithms, reducing task drop ratios, average delay, and improving prioritized task throughput, thus optimizing the use of edge computational resources.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0933.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
