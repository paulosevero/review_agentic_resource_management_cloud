---
id: paper-0454
title: Network Traffic Obfuscation System for IIoT-Cloud Control Systems
authors:
- Lee, Yangjae
- Baek, Sung Hoon
- Seo, Jung Taek
- Park, Ki-Woong
venue: Computers, Materials and Continua
venue_type: journal
year: 2022
doi: 10.32604/cmc.2022.026657
url: https://www.scopus.com/pages/publications/85128603703?origin=resultslist
publisher: Tech Science Press
pages: 4911--4929
keywords:
- Cloud computing system
- container orchestration
- moving-target defense
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

# paper-0454 — Network Traffic Obfuscation System for IIoT-Cloud Control Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> One of the latest technologies enabling remote control, operational efficiency upgrades, and real-time big-data monitoring in an industrial control system (ICS) is the IIoT-Cloud ICS, which integrates the Industrial Internet of Things (IIoT) and the cloud into the ICS. Although an ICS benefits from the application of IIoT and the cloud in terms of cost reduction, efficiency improvement, and real-time monitoring, the application of this technology to an ICS poses an unprecedented security risk by exposing its terminal devices to the outside world. An adversary can collect information regarding senders, recipients, and prime-time slots through traffic analysis and use it as a linchpin for the next attack, posing a potential threat to the ICS. To address this problem, we designed a network traffic obfuscation system (NTOS) for the IIoT-Cloud ICS, based on the requirements derived from the ICS characteristics and limitations of existing NTOS models. As a strategy to solve this problem wherein a decrease in the traffic volume facilitates traffic analysis or reduces the packet transmission speed, we proposed an NTOS based on packet scrambling, wherein a packet is split into multiple pieces before transmission, thus obfuscating network analysis. To minimize the ICS modification and downtime, the proposed NTOS was designed using an agentbased model. In addition, for the ICS network traffic analyzer to operate normally in an environment wherein theNTOS is applied, a rule-based NTOS was adopted such that the actual traffic flow is known only to the device that is aware of the rule and is blocked for attackers. The experimental results verified that the same time requested for response and level of difficulty of analysis were maintained by the application of an NTOS based on packet scrambling, even when the number of requests received by the server per second was reduced. The network traffic analyzer of the ICS can capture the packet flow by using the pre-communicated NTOS rule. In addition, by designing an NTOS using an agent-based model, the impact on the ICS was minimized such that the system could be applied with short downtime. © 2022 Tech Science Press. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0454.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
