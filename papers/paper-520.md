---
id: "paper-520"
title: "A Reinforcement Learning Based Data Storage and Traffic Management in Information-Centric Data Center Networks"
authors: ["Yang, Weihong", "Qin, Yang", "Yang, ZhaoZheng"]
year: 2022
venue: "Mobile Networks and Applications"
venue_type: "journal"
doi: "10.1007/s11036-020-01629-w"
url: "https://www.scopus.com/pages/publications/85089009517?origin=resultslist"
publisher: "Springer"
pages: "266--275"
keywords: ["Data storage", "Distributed Q-learning", "Information-centric data center networks", "Traffic management"]
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
    human_decision: ""
    human_justification: ""

---

# paper-520 — A Reinforcement Learning Based Data Storage and Traffic Management in Information-Centric Data Center Networks

## Metadata

- **Authors:** Yang, Weihong and Qin, Yang and Yang, ZhaoZheng
- **Year:** 2022
- **Venue:** Mobile Networks and Applications
- **DOI:** 10.1007/s11036-020-01629-w
- **URL:** https://www.scopus.com/pages/publications/85089009517?origin=resultslist
- **Publisher:** Springer
- **Pages:** 266--275
- **Language:** English
- **Keywords:** Data storage; Distributed Q-learning; Information-centric data center networks; Traffic management

### Abstract

Data Center Networks (DCN), a core infrastructure of cloud computing, place heavy demands on efficient storage and management of massive data. The data storage scheme, which decides how to assign data to nodes for storage, has a significant impact on the performance of the data center. However, most of the existing solutions focus on where to store the data (i.e., the selection of storage node) but have not considered how to store them (i.e., the traffic management such as routing and transmission rate adjustment). By leveraging the Information-Centric Networks (ICN) architecture, this paper tackles the data storage and traffic management issue in Information-Centric Data Center Networks (ICDCN) based on Reinforcement Learning (RL) method, since RL has been developed as a promising solution to address dynamic network issues. We present a global optimization of joint traffic management and data storage and then solve it by the distributed multi-agent Q-learning. In ICDCN, the data is routed based on the data’s name, which achieves better routing scalability by decoupling the data and its physical location. Compared with IP’s stateless forwarding plane, the stateful forwarding information maintained at every node supports adaptively routing and hop-by-hop traffic control by using the Q-learning method. We evaluate our proposal on an NS-3-based simulator, and the results show that the proposed scheme can effectively reduce transmission time and increase throughput while achieving load-balanced among servers. © 2020, Springer Science+Business Media, LLC, part of Springer Nature.

## 04 — Title Screening

**Title:** A Reinforcement Learning Based Data Storage and Traffic Management in Information-Centric Data Center Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** A Reinforcement Learning Based Data Storage and Traffic Management in Information-Centric Data Center Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Reinforcement Learning Based Data Storage and Traffic Management in Information-Centric Data Center Networks
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
