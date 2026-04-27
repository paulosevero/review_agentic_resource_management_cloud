---
id: "paper-2699"
title: "SALB: Security-Aware Load Balancing for Large Language Model Training in Datacenter Networks"
authors: ["Luo, Wangqing", "Hu, Jinbin", "Sun, Hua", "Sharma, Pradip Kumar", "Wang, Jin"]
year: 2026
venue: "IEEE Transactions on Network and Service Management"
venue_type: "journal"
doi: "10.1109/TNSM.2026.3678979"
url: "https://www.scopus.com/pages/publications/105035331212?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Data Security", "Datacenter Networks", "Deep Reinforcement Learning", "Load Balancing"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-2699 — SALB: Security-Aware Load Balancing for Large Language Model Training in Datacenter Networks

## Metadata

- **Authors:** Luo, Wangqing and Hu, Jinbin and Sun, Hua and Sharma, Pradip Kumar and Wang, Jin
- **Year:** 2026
- **Venue:** IEEE Transactions on Network and Service Management
- **DOI:** 10.1109/TNSM.2026.3678979
- **URL:** https://www.scopus.com/pages/publications/105035331212?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Data Security; Datacenter Networks; Deep Reinforcement Learning; Load Balancing

### Abstract

To meet the massive compute and high-speed communication demands of Large Language Model (LLM) training, modern datacenters typically adopt multipath topologies such as Fat-Tree and Clos to host parallel jobs across hundreds to thousands of GPUs. However, LLM training exhibits periodic, high-bandwidth communication patterns. Existing load-balancing schemes become misaligned under dynamic congestion and anomalous surges: they struggle to promptly mitigate iteration-peak congestion and lack effective isolation of anomalous traffic. To address this, we propose Security-Aware Load Balancing (SALB) for LLM training. SALB leverages a Deep Reinforcement Learning (DRL) controller with queue and delay signals for packet-level multipath load balancing and employs path binding to confine suspicious flows. By integrating data security into load balancing, SALB simultaneously achieves high throughput and robust traffic isolation. NS-3 simulation results show that, compared with CONGA, Hermes, and ConWeave, SALB reduces the 99<sup>th</sup>-percentile flow completion time (FCT) of short flows by an average of 65% and increases the throughput of long flows by an average of 54%. It further outperforms the baselines in aggregate throughput, path utilization, and packet loss rate, thereby significantly enhancing system stability, robustness, and data security. © 2004-2012 IEEE.

## 04 — Title Screening

**Title:** SALB: Security-Aware Load Balancing for Large Language Model Training in Datacenter Networks

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** SALB: Security-Aware Load Balancing for Large Language Model Training in Datacenter Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** SALB: Security-Aware Load Balancing for Large Language Model Training in Datacenter Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
