---
id: "paper-259"
title: "Consistency Guaranteed Multi Container Migration for Smart Community Network Services"
authors: ["Abeysiriwardhana, W.A.P. Shanaka", "Morishima, Ryo", "Miura, Tatsuki", "Nishi, Hiroaki"]
year: 2021
venue: "IEEJ Transactions on Electronics, Information and Systems"
venue_type: "journal"
doi: "10.1541/ieejeiss.141.1453"
url: "https://www.scopus.com/pages/publications/85138185184?origin=resultslist"
publisher: "Institute of Electrical Engineers of Japan"
pages: "1453--1461"
keywords: ["container migration", "data plane development", "network services", "smart community"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-259 — Consistency Guaranteed Multi Container Migration for Smart Community Network Services

## Metadata

- **Authors:** Abeysiriwardhana, W.A.P. Shanaka and Morishima, Ryo and Miura, Tatsuki and Nishi, Hiroaki
- **Year:** 2021
- **Venue:** IEEJ Transactions on Electronics, Information and Systems
- **DOI:** 10.1541/ieejeiss.141.1453
- **URL:** https://www.scopus.com/pages/publications/85138185184?origin=resultslist
- **Publisher:** Institute of Electrical Engineers of Japan
- **Pages:** 1453--1461
- **Language:** English
- **Keywords:** container migration; data plane development; network services; smart community

### Abstract

Smart Community (SC) uses IoT sensors to provide smart grid control, traffic management, and similar IoT services. These services expect to run at the network edge or fog layer to provide low latency network services, encapsulate citizens' private information, support low-cost IoT terminals from cyber-attacks, and support other cutting-edge fog and edge services. SC edge is a service platform that supports edge/fog services for IoT terminals by using Docker containers. Initially, SC edge/fog computing nodes did not support the function of service migration. However, service migration is necessary to support remote deployment and service distribution in SC networks. The existing container migration techniques focus mainly on resource utilization. However, SC services should handle loss-free data stream processing and order-preservation of network packets to gather IoT sensor data after migration. In addition, SC services require one-to-many migration to support high throughput loads when required. Therefore, this paper focuses on enhancing SC service flexibility by introducing migration for relocatable and network consistency guaranteed containerized services. SC edge proposes multiple container migration techniques that are suitable for network services. The proposed techniques can improve resource consumption, guarantee network traffic consistency, and apply one-to-many migration patterns. Layer leveraging migration (LLM) reduces the overall migration time by 10.8% for an elastic search Docker container than available Docker migration methods. Additionally, consistency guaranteed migration (CGM) is proposed to guarantee network consistency. However, CGM consumes additional resources compared to LLM for IoT data management. Finally, One to N Consistency Guaranteed Migration (O2NCGM) is proposed to support one-to-many migration with data consistency that shows similar performance to CGM. © 2021 The Institute of Electrical Engineers of Japan.

## 04 — Title Screening

**Title:** Consistency Guaranteed Multi Container Migration for Smart Community Network Services

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Consistency Guaranteed Multi Container Migration for Smart Community Network Services
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Consistency Guaranteed Multi Container Migration for Smart Community Network Services
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
