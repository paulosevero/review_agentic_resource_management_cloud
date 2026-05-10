---
id: "paper-362"
title: "ACC: Automatic ECN tuning for high-speed datacenter networks"
authors: ["Yan, Siyu", "Wang, Xiaoliang", "Zheng, Xiaolong", "Xia, Yinben", "Liu, Derui", "Deng, Weishan"]
year: 2021
venue: "SIGCOMM 2021 - Proceedings of the ACM SIGCOMM 2021 Conference"
venue_type: "conference"
doi: "10.1145/3452296.3472927"
url: "https://www.scopus.com/pages/publications/85113246703?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "384--397"
keywords: ["AQM", "congestion control", "datacenter network", "ECN"]
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

# paper-362 — ACC: Automatic ECN tuning for high-speed datacenter networks

## Metadata

- **Authors:** Yan, Siyu and Wang, Xiaoliang and Zheng, Xiaolong and Xia, Yinben and Liu, Derui and Deng, Weishan
- **Year:** 2021
- **Venue:** SIGCOMM 2021 - Proceedings of the ACM SIGCOMM 2021 Conference
- **DOI:** 10.1145/3452296.3472927
- **URL:** https://www.scopus.com/pages/publications/85113246703?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 384--397
- **Language:** English
- **Keywords:** AQM; congestion control; datacenter network; ECN

### Abstract

For the widely deployed ECN-based congestion control schemes, the marking threshold is the key to deliver high bandwidth and low latency. However, due to traffic dynamics in the high-speed production networks, it is difficult to maintain persistent performance by using the static ECN setting. To meet the operational challenge, in this paper we report the design and implementation of an automatic run-time optimization scheme, ACC, which leverages the multi-agent reinforcement learning technique to dynamically adjust the marking threshold at each switch. The proposed approach works in a distributed fashion and combines offline and online training to adapt to dynamic traffic patterns. It can be easily deployed based on the common features supported by major commodity switching chips. Both testbed experiments and large-scale simulations have shown that ACC achieves low flow completion time (FCT) for both mice flows and elephant flows at line-rate. Under heterogeneous production environments with 300 machines, compared with the well-tuned static ECN settings, ACC achieves up to 20\% improvement on IOPS and 30\% lower FCT for storage service. ACC has been applied in high-speed datacenter networks and significantly simplifies the network operations.  © 2021 ACM.

## 04 — Title Screening

**Title:** ACC: Automatic ECN tuning for high-speed datacenter networks

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ACC: Automatic ECN tuning for high-speed datacenter networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ACC: Automatic ECN tuning for high-speed datacenter networks
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
