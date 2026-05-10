---
id: paper-0932
title: 'COOLER: Cooperative Computation Offloading in Edge-Cloud Continuum Under Latency Constraints via Multi-Agent Deep Reinforcement Learning'
authors:
- Giannopoulos, Anastasios
- Paralikas, Ilias
- Spantideas, Sotirios
- Trakadas, Panagiotis
venue: 2024 International Conference on Intelligent Computing, Communication, Networking and Services, ICCNS 2024
venue_type: conference
year: 2024
doi: 10.1109/ICCNS62192.2024.10776151
url: https://www.scopus.com/pages/publications/85215271305?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9--16
keywords:
- 6G network
- deep reinforcement learning
- edge computing
- edge-cloud continuum
- resource management
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0932 — COOLER: Cooperative Computation Offloading in Edge-Cloud Continuum Under Latency Constraints via Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the burgeoning domain of the edge-cloud con-tinuum (ECC), the efficient management of computational tasks offloaded from mobile devices to edge nodes is paramount. This paper introduces a Cooperative cOmputation Offloading scheme for ECC via Latency-aware multi-agent Reinforcement learning (COOLER), a distributed framework designed to address the challenges posed by the uncertain load dynamics at edge nodes. COOLER enables each edge node to autonomously make offloading decisions, optimizing for non-divisible, delay-sensitive tasks without prior knowledge of other nodes' task models and decisions. By formulating a multi-agent computation offloading problem, COOLER aims to minimize the expected long-term latency and task drop ratio. Following the ECC requirements for seamless task flow both within Edge layer and between Edge-Cloud layers, COOLER considers that task computation decisions are three-fold: (i) local computation, (ii) horizontal offloading to another edge node, or (iii) vertical offloading to the Cloud. The integration of advanced techniques such as long short-term memory (LSTM), double deep Q-network (DQN) and dueling DQN enhances the estimation of long-term costs, thereby improving decision-making efficacy. Simulation results demonstrate that COOLER significantly outperforms baseline offloading algorithms, reducing both the ratio of dropped tasks and average delay, and better harnessing the processing capacities of edge nodes. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0932.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
