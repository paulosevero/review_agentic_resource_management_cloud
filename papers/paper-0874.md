---
id: paper-0874
title: Energy-Efficient Computation Offloading Based on Multiagent Deep Reinforcement Learning for Industrial Internet of Things Systems
authors:
- Chouikhi, Samira
- Esseghir, Moez
- Merghem-Boulahia, Leila
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3333044
url: https://www.scopus.com/pages/publications/85177094060?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12228--12239
keywords:
- Computation offloading
- deep reinforcement learning (DRL)
- edge computing
- Industrial Internet of Things (IIoT)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0874 — Energy-Efficient Computation Offloading Based on Multiagent Deep Reinforcement Learning for Industrial Internet of Things Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The term Industrial Internet of Things (IIoT) was created to describe a specific area of the Internet of Things (IoT) that integrates information and communication technologies (ICTs) like cloud/edge computing, wireless sensor/actuator networks, and connected objects to enable and accelerate the development of Industry 4.0. IIoT applications (e.g., smart manufacturing, remote control of industrial machinery, and critical system monitoring) have various levels of criticality and Quality-of-Service (QoS) requirements. However, the characteristics of data collected by interconnected devices complicate the task of guaranteeing the QoS requirements in terms of latency and reliability in addition to the huge amount of energy consumption. As a potential solution, edge computing offers additional powerful resources in the proximity of the IIoT devices. Hence, the required QoS can be achieved by offloading computation-intensive tasks to edge servers. Moreover, the offloading process needs to be optimized to take full advantage. Unlikely, conventional optimization methods are very complex to be applied in the IIoT context. To overcome this issue, we propose a computation offloading approach based on deep reinforcement learning (DRL) to minimize long-term energy consumption and maximize the number of tasks completed before their tolerant deadlines. We introduce a system with multiple agents to deal with the increasing dimension of the action space, where each IIoT device is represented by its own DRL model. The goal of the model is to maximize a flexible and long-term reward. In addition, the DRL models are trained in the cloud and make decisions online in the edge servers, allowing quick decision making by avoiding iterative online optimization procedures. The performance of the proposed approach is evaluated through simulation. The proposal shows promising results compared to other approaches.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0874.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
