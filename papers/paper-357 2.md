---
id: "paper-357"
title: "Multi-Agent Multi-Armed Bandit Learning for Online Management of Edge-Assisted Computing"
authors: ["Wu, Bochun", "Chen, Tianyi", "Ni, Wei", "Wang, Xin"]
year: 2021
venue: "IEEE Transactions on Communications"
venue_type: "journal"
doi: "10.1109/TCOMM.2021.3113386"
url: "https://www.scopus.com/pages/publications/85115130315?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "8188--8199"
keywords: ["Edge computing", "multi-agent multi-armed bandit (MA-MAB)", "upper confidence bound (UCB)"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-357 — Multi-Agent Multi-Armed Bandit Learning for Online Management of Edge-Assisted Computing

## Metadata

- **Authors:** Wu, Bochun and Chen, Tianyi and Ni, Wei and Wang, Xin
- **Year:** 2021
- **Venue:** IEEE Transactions on Communications
- **DOI:** 10.1109/TCOMM.2021.3113386
- **URL:** https://www.scopus.com/pages/publications/85115130315?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 8188--8199
- **Language:** English
- **Keywords:** Edge computing; multi-agent multi-armed bandit (MA-MAB); upper confidence bound (UCB)

### Abstract

By orchestrating resources of edge and core network, the delays of edge-assisted computing can decrease. Offloading scheduling is challenging though, especially in the presence of many edge devices with randomly varying link and computing conditions. This paper presents a new online learning-based approach to the offloading scheduling, where multi-agent multi-armed bandit (MA-MAB) learning is designed to exploit the randomly varying conditions and asymptotically minimize the computing delay. We first propose a combinatorial bandit upper confidence bound (CB-UCB) algorithm, where users collectively feed back the observed delays of all edge devices and links. The optimistic bound of the delay is derived to facilitate centralized offloading scheduling for all users. In addition, we put forth a distributed bandit upper confidence bound (DB-UCB) algorithm, where users take random turns to make conflict-free, distributed selections of edge devices. The optimistic confidence bound of each user is developed to allow the user's selection only based on its own observations and decisions. Furthermore, we establish the asymptotic optimality of the proposed algorithms by proving the sublinearity of their regrets, and that the random turns the users take to make decisions do not compromise the asymptotic optimality of the DB-UCB algorithm, as corroborated by numerical simulations.  © 1972-2012 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Multi-Armed Bandit Learning for Online Management of Edge-Assisted Computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Multi-Armed Bandit Learning for Online Management of Edge-Assisted Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Multi-Armed Bandit Learning for Online Management of Edge-Assisted Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
