---
id: "paper-446"
title: "Madelyn: Multi-Domain Multi-Agent Reinforcement Learning for Data-center Networks"
authors: ["Kattepur, Ajay", "David, Sushanth"]
year: 2022
venue: "Proceedings - 2022 IEEE 46th Annual Computers, Software, and Applications Conference, COMPSAC 2022"
venue_type: "conference"
doi: "10.1109/COMPSAC54236.2022.00109"
url: "https://www.scopus.com/pages/publications/85137006932?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "624--629"
keywords: ["5G Service", "Data-center Networks", "Kubernetes", "Multi-Agent Reinforcement Learning"]
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
    human_justification: "RL"

---

# paper-446 — Madelyn: Multi-Domain Multi-Agent Reinforcement Learning for Data-center Networks

## Metadata

- **Authors:** Kattepur, Ajay and David, Sushanth
- **Year:** 2022
- **Venue:** Proceedings - 2022 IEEE 46th Annual Computers, Software, and Applications Conference, COMPSAC 2022
- **DOI:** 10.1109/COMPSAC54236.2022.00109
- **URL:** https://www.scopus.com/pages/publications/85137006932?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 624--629
- **Language:** English
- **Keywords:** 5G Service; Data-center Networks; Kubernetes; Multi-Agent Reinforcement Learning

### Abstract

Data-center network configurations are crucial in ensuring end-to-end differentiated service performance within 5G. Data-center networks encom-pass two domains: (i) the fat-tree networking fabric with leaf, spine and super-spine layers (ii) data-center server nodes with container and workload placement policies. These have traditionally been managed within silos with context and configurations driven within each domain. In this work, we examine the effect of configuration changes in one domain and its effect on the other. We develop Madelyn, a multi-domain multi-agent rein-forcement learning framework for data-center networks that can propose network-aware, virtual network function placement. This framework takes into account the data-center fabric wights, drop rates, capacities, load balancing and traffic shaping. It also considers the network function pod placements based on affinity / anti-affinity rules, node capacities and taints/tolerations. Using this multi-agent framework, we provide network aware scheduling policies for differentiated network function virtualization services running on Kubernetes pods within data-center networks. The results are demonstrated over a real traffic dataset collected over Ericsson's testbed networks. © 2022 IEEE.

## 04 — Title Screening

**Title:** Madelyn: Multi-Domain Multi-Agent Reinforcement Learning for Data-center Networks

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Madelyn: Multi-Domain Multi-Agent Reinforcement Learning for Data-center Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Madelyn: Multi-Domain Multi-Agent Reinforcement Learning for Data-center Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
