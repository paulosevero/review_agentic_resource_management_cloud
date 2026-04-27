---
id: "paper-628"
title: "A Deep Reinforcement Learning Framework for Optimizing Congestion Control in Data Centers"
authors: ["Ketabi, Shiva", "Chen, Hongkai", "Dong, Haiwei", "Ganjali, Yashar"]
year: 2023
venue: "Proceedings of IEEE/IFIP Network Operations and Management Symposium 2023, NOMS 2023"
venue_type: "conference"
doi: "10.1109/NOMS56928.2023.10154411"
url: "https://www.scopus.com/pages/publications/85164725546?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Deep learning", "Learning algorithms", "Learning systems", "Multi agent systems", "Congestion control protocols", "Control actions", "Control parameters", "Datacenter", "Learning frameworks", "Network environments", "Online learning", "Performance", "Reinforcement learnings", "Stringents", "Reinforcement learning"]
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
    final_score: 0.1666
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-628 — A Deep Reinforcement Learning Framework for Optimizing Congestion Control in Data Centers

## Metadata

- **Authors:** Ketabi, Shiva and Chen, Hongkai and Dong, Haiwei and Ganjali, Yashar
- **Year:** 2023
- **Venue:** Proceedings of IEEE/IFIP Network Operations and Management Symposium 2023, NOMS 2023
- **DOI:** 10.1109/NOMS56928.2023.10154411
- **URL:** https://www.scopus.com/pages/publications/85164725546?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Deep learning; Learning algorithms; Learning systems; Multi agent systems; Congestion control protocols; Control actions; Control parameters; Datacenter; Learning frameworks; Network environments; Online learning; Performance; Reinforcement learnings; Stringents; Reinforcement learning

### Abstract

Various congestion control protocols have been designed to achieve high performance in different network environments. Modern online learning solutions that delegate the congestion control actions to a machine cannot properly converge in the stringent time scales of data centers. We leverage multi-agent reinforcement learning to design a system for dynamic tuning of congestion control parameters at end-hosts in a data center. The system includes agents at the end-hosts to monitor and report the network and traffic states, and agents to run the reinforcement learning algorithm given the states. Based on the state of the environment, the system generates congestion control parameters that optimize network performance metrics such as throughput and latency. As a case study, we examine BBR, an example of a prominent recently-developed congestion control protocol. Our experiments demonstrate that the proposed system has the potential to mitigate the problems of static parameters. © 2023 IEEE.

## 04 — Title Screening

**Title:** A Deep Reinforcement Learning Framework for Optimizing Congestion Control in Data Centers

### Machine Screening

- **Final Score:** 0.1666 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Deep Reinforcement Learning Framework for Optimizing Congestion Control in Data Centers
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** A Deep Reinforcement Learning Framework for Optimizing Congestion Control in Data Centers
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
