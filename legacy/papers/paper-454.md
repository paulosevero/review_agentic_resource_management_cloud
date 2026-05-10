---
id: "paper-454"
title: "Network Traffic Obfuscation System for IIoT-Cloud Control Systems"
authors: ["Lee, Yangjae", "Baek, Sung Hoon", "Seo, Jung Taek", "Park, Ki-Woong"]
year: 2022
venue: "Computers, Materials and Continua"
venue_type: "journal"
doi: "10.32604/cmc.2022.026657"
url: "https://www.scopus.com/pages/publications/85128603703?origin=resultslist"
publisher: "Tech Science Press"
pages: "4911--4929"
keywords: ["Cloud computing system", "container orchestration", "moving-target defense"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-454 — Network Traffic Obfuscation System for IIoT-Cloud Control Systems

## Metadata

- **Authors:** Lee, Yangjae and Baek, Sung Hoon and Seo, Jung Taek and Park, Ki-Woong
- **Year:** 2022
- **Venue:** Computers, Materials and Continua
- **DOI:** 10.32604/cmc.2022.026657
- **URL:** https://www.scopus.com/pages/publications/85128603703?origin=resultslist
- **Publisher:** Tech Science Press
- **Pages:** 4911--4929
- **Language:** English
- **Keywords:** Cloud computing system; container orchestration; moving-target defense

### Abstract

One of the latest technologies enabling remote control, operational efficiency upgrades, and real-time big-data monitoring in an industrial control system (ICS) is the IIoT-Cloud ICS, which integrates the Industrial Internet of Things (IIoT) and the cloud into the ICS. Although an ICS benefits from the application of IIoT and the cloud in terms of cost reduction, efficiency improvement, and real-time monitoring, the application of this technology to an ICS poses an unprecedented security risk by exposing its terminal devices to the outside world. An adversary can collect information regarding senders, recipients, and prime-time slots through traffic analysis and use it as a linchpin for the next attack, posing a potential threat to the ICS. To address this problem, we designed a network traffic obfuscation system (NTOS) for the IIoT-Cloud ICS, based on the requirements derived from the ICS characteristics and limitations of existing NTOS models. As a strategy to solve this problem wherein a decrease in the traffic volume facilitates traffic analysis or reduces the packet transmission speed, we proposed an NTOS based on packet scrambling, wherein a packet is split into multiple pieces before transmission, thus obfuscating network analysis. To minimize the ICS modification and downtime, the proposed NTOS was designed using an agentbased model. In addition, for the ICS network traffic analyzer to operate normally in an environment wherein theNTOS is applied, a rule-based NTOS was adopted such that the actual traffic flow is known only to the device that is aware of the rule and is blocked for attackers. The experimental results verified that the same time requested for response and level of difficulty of analysis were maintained by the application of an NTOS based on packet scrambling, even when the number of requests received by the server per second was reduced. The network traffic analyzer of the ICS can capture the packet flow by using the pre-communicated NTOS rule. In addition, by designing an NTOS using an agent-based model, the impact on the ICS was minimized such that the system could be applied with short downtime. © 2022 Tech Science Press. All rights reserved.

## 04 — Title Screening

**Title:** Network Traffic Obfuscation System for IIoT-Cloud Control Systems

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Network Traffic Obfuscation System for IIoT-Cloud Control Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Network Traffic Obfuscation System for IIoT-Cloud Control Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
