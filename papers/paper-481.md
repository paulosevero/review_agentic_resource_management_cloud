---
id: "paper-481"
title: "EdgeML: Towards network-accelerated federated learning over wireless edge"
authors: ["Pinyoanuntapong, Pinyarash", "Janakaraj, Prabhu", "Balakrishnan, Ravikumar", "Lee, Minwoo", "Chen, Chen", "Wang, Pu"]
year: 2022
venue: "Computer Networks"
venue_type: "journal"
doi: "10.1016/j.comnet.2022.109396"
url: "https://www.scopus.com/pages/publications/85140294752?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Federated learning", "Multi-agent reinforcement learning", "Multi-hop wireless edge", "Wireless networking"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-481 — EdgeML: Towards network-accelerated federated learning over wireless edge

## Metadata

- **Authors:** Pinyoanuntapong, Pinyarash and Janakaraj, Prabhu and Balakrishnan, Ravikumar and Lee, Minwoo and Chen, Chen and Wang, Pu
- **Year:** 2022
- **Venue:** Computer Networks
- **DOI:** 10.1016/j.comnet.2022.109396
- **URL:** https://www.scopus.com/pages/publications/85140294752?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Federated learning; Multi-agent reinforcement learning; Multi-hop wireless edge; Wireless networking

### Abstract

Federated learning (FL) is a distributed machine learning technology for next-generation AI systems that allows a number of workers, i.e., edge devices, collaboratively learn a shared global model while keeping their data locally to prevent privacy leakage. Enabling FL over wireless multi-hop networks can democratize AI and make it accessible in a cost-effective manner. However, the noisy bandwidth-limited multi-hop wireless connections can lead to delayed and nomadic model updates, which significantly slows down the FL convergence speed. To address such challenges, this paper aims to accelerate FL convergence over wireless edge by optimizing the multi-hop federated networking performance. In particular, the FL convergence optimization problem is formulated as a Markov decision process (MDP). To solve such MDP, multi-agent reinforcement learning (MA-RL) algorithms along with domain-specific action space refining schemes are developed, which online learn the delay-minimum forwarding paths to minimize the model exchange latency between the edge devices (i.e., workers) and the remote server. To validate the proposed solutions, EdgeML is developed and implemented, which is the first experimental framework in the literature for FL over multi-hop wireless edge computing networks. EdgeML allows us to fast prototype, deploy, and evaluate novel FL algorithms along with RL-based system optimization methods in real wireless devices. Moreover, a physical experimental testbed is implemented by customizing the widely adopted Linux wireless routers and ML computing nodes. Such testbed can provide valuable insights into the practical performance of FL in the field. Finally, our experimentation results on the testbed show that the proposed network-accelerated FL system can practically and significantly improve FL convergence speed, compared to the FL system empowered by the production-grade commercially-available wireless networking protocol, BATMAN-Adv. © 2022 Elsevier B.V.

## 04 — Title Screening

**Title:** EdgeML: Towards network-accelerated federated learning over wireless edge

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeML: Towards network-accelerated federated learning over wireless edge
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeML: Towards network-accelerated federated learning over wireless edge
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
