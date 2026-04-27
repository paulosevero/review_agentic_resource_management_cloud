---
id: "paper-2753"
title: "D3T: Dual-Timescale Optimization of Task Scheduling and Thermal Management for Energy Efficient Geo-Distributed Data Centers"
authors: ["Ran, Yongyi", "Yin, Hui", "Sun, Tongyao", "Zhou, Xin", "Luo, Jiangtao", "Chen, Shuangwu"]
year: 2026
venue: "IEEE Transactions on Parallel and Distributed Systems"
venue_type: "journal"
doi: "10.1109/TPDS.2025.3631654"
url: "https://www.scopus.com/pages/publications/105021539884?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "230--246"
keywords: ["Deep reinforcement learning", "geo-distributed data center", "task scheduling", "thermal management"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2753 — D3T: Dual-Timescale Optimization of Task Scheduling and Thermal Management for Energy Efficient Geo-Distributed Data Centers

## Metadata

- **Authors:** Ran, Yongyi and Yin, Hui and Sun, Tongyao and Zhou, Xin and Luo, Jiangtao and Chen, Shuangwu
- **Year:** 2026
- **Venue:** IEEE Transactions on Parallel and Distributed Systems
- **DOI:** 10.1109/TPDS.2025.3631654
- **URL:** https://www.scopus.com/pages/publications/105021539884?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 230--246
- **Language:** English
- **Keywords:** Deep reinforcement learning; geo-distributed data center; task scheduling; thermal management

### Abstract

The surge of artificial intelligence (AI) has intensified compute-intensive tasks, sharply increasing the need for energy-efficient management in geo-distributed data centers. Existing approaches struggle to coordinate task scheduling and cooling control due to mismatched time constants, stochastic Information Technology (IT) workloads, variable renewable energy, and fluctuating electricity prices. To address these challenges, we propose D3T, a dual-timescale deep reinforcement learning (DRL) framework that jointly optimizes task scheduling and thermal management for energy-efficient geo-distributed data centers. At the fast timescale, D3T employs Deep Q-Network (DQN) to schedule tasks, reducing operational expenditure (OPEX) and task sojourn time. At the slow timescale, a QMIX-based multi-agent DRL method regulates cooling across distributed data centers by dynamically adjusting airflow rates, thereby preventing hotspots and reducing energy waste. Extensive experiments were conducted using TRNSYS with real-world traces, and the results demonstrate that, compared to baseline algorithms, D3T reduces OPEX by 13% in IT subsystems and 29% in cooling subsystems, improves power usage effectiveness (PUE) by 7%, and maintains more stable thermal safety across geo-distributed data centers. © 1990-2012 IEEE.

## 04 — Title Screening

**Title:** D3T: Dual-Timescale Optimization of Task Scheduling and Thermal Management for Energy Efficient Geo-Distributed Data Centers

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** D3T: Dual-Timescale Optimization of Task Scheduling and Thermal Management for Energy Efficient Geo-Distributed Data Centers
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** D3T: Dual-Timescale Optimization of Task Scheduling and Thermal Management for Energy Efficient Geo-Distributed Data Centers
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
