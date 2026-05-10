---
id: paper-0685
title: Centralized and Collaborative RL-Based Resource Allocation in Virtualized Dynamic Fog Computing
authors:
- Mseddi, Amina
- Jaafar, Wael
- Elbiaze, Halima
- Ajib, Wessam
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3283143
url: https://www.scopus.com/pages/publications/85161495539?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 14239--14253
keywords:
- Collaborative learning
- deep reinforcement learning (RL)
- fog computing (FC)
- multiagent RL
- QMIX
- resource allocation
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

# paper-0685 — Centralized and Collaborative RL-Based Resource Allocation in Virtualized Dynamic Fog Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog computing (FC) emerged as a new paradigm enabling the deployment of new Internet of Things (IoT) applications. Fog infrastructure is composed of heterogeneous nodes characterized by a complex distribution, mobility, and sporadic resource availability. Hence, resource coordination for continuous Quality-of-Service (QoS) satisfaction becomes challenging, and accurate resource tracking is needed for flawless servicing. In this context, we investigate and propose online resource allocation solutions. The main objective is to maximize the number of satisfied users within a predefined latency requirement. Hence, we model the FC environment as a Markov Decision Process, and then, we formulate the optimization problem. Due to the problem's NP-hardness, we leverage the reinforcement learning (RL) tool to develop resource allocation schemes. First, a centralized method where a smart fog controller possesses a global awareness of the FC environment is proposed. Next, a more practical and collaborative solution is presented, where each RL-enabled agent manages a group of fog nodes and their resources in order to satisfy computing requests. Based on real-world mobility data sets, simulation results illustrate the high efficiency of the proposed solutions with a preference for the collaborative approach. The superiority of our proposed solutions over state-of-the-art methods is also illustrated.  © 2014 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0685.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
