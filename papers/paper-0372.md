---
id: paper-0372
title: Deep reinforcement learning based task scheduling scheme in mobile edge computing network
authors:
- Zhao, Qi
- Feng, Mingjie
- Li, Li
- Li, Yi
- Liu, Hang
- Chen, Genshe
venue: Proceedings of SPIE - The International Society for Optical Engineering
venue_type: conference
year: 2021
doi: 10.1117/12.2589070
url: https://www.scopus.com/pages/publications/85108994177?origin=resultslist
publisher: SPIE
pages: ''
keywords:
- Deep Q-learning
- Distributed computing
- Markov decision process
- Mobile edge computing
- Multi-armed bandit
- Task scheduling and offloading
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

# paper-0372 — Deep reinforcement learning based task scheduling scheme in mobile edge computing network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing is a new distributed computing paradigm which brings computation and data storage closer to the location where it is needed, to improve response times and save bandwidth in the dynamic mobile networking environment. Despite the improvements in network technology, data centers cannot always guarantee acceptable transfer rates and response times, which could be a critical requirement for many applications. The aim of mobile edge computing is to move the computation away from data centers towards the edge of the network, exploiting smart objects, mobile phones or network gateways to perform tasks and provide services on behalf of the cloud. In this paper, we design a task offloading scheme in the mobile edge network to handle the task distribution, offloading and management by applying deep reinforcement learning. Specifically, we formulate the task offloading problem as a multi-agent reinforcement learning problem. The decision-making process of each agent is modeled as a Markov decision process and deep Q-learning approach is applied to deal with the large scale of states and actions. To evaluate the performance of our proposed scheme, we develop a simulation environment for the mobile edge computing scenario. Our preliminary evaluation results with a simplified multi-armed bandit model indicate that our proposed solution can provide lower latency for the computational intensive tasks in mobile edge network, and outperforms than naïve task offloading method. © COPYRIGHT SPIE. Downloading of the abstract is permitted for personal use only.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0372.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
