---
id: "paper-466"
title: "Learning to make auto-scaling decisions with heterogeneous spot and on-demand instances via reinforcement learning"
authors: ["Lin, Liduo", "Pan, Li", "Liu, Shijun"]
year: 2022
venue: "Information Sciences"
venue_type: "journal"
doi: "10.1016/j.ins.2022.10.071"
url: "https://www.scopus.com/pages/publications/85141235781?origin=resultslist"
publisher: "Elsevier Inc."
pages: "480--496"
keywords: ["Auto-scaling", "Heterogeneous instances", "On-demand instance", "Reinforcement learning", "Spot instance"]
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
    human_justification: "RL"

---

# paper-466 — Learning to make auto-scaling decisions with heterogeneous spot and on-demand instances via reinforcement learning

## Metadata

- **Authors:** Lin, Liduo and Pan, Li and Liu, Shijun
- **Year:** 2022
- **Venue:** Information Sciences
- **DOI:** 10.1016/j.ins.2022.10.071
- **URL:** https://www.scopus.com/pages/publications/85141235781?origin=resultslist
- **Publisher:** Elsevier Inc.
- **Pages:** 480--496
- **Language:** English
- **Keywords:** Auto-scaling; Heterogeneous instances; On-demand instance; Reinforcement learning; Spot instance

### Abstract

Designing auto-scaling frameworks using spot and on-demand instances while considering their heterogeneity, can help Software-as-a-Service (SaaS) providers provide services with high availability to meet dynamic workloads and achieve significant cost savings. However, designing such an auto-scaling framework is difficult due to the lack of prior knowledge of the cloud. In this work, we propose an algorithm called SpotRL to solve the auto-scaling problem using heterogeneous spot and on-demand instances. Reinforcement learning (RL) approaches have been shown to be able to make effective decisions in highly dynamic environments, as they can learn step-by-step and find solutions without prior knowledge. SpotRL uses an RL-based approach for the scaling of heterogeneous spot instances. In the complex cloud environment, the training speed of RL agents is generally slow. Considering this issue, we use a multi-agent approach to decompose tasks to help agents learn faster. To reduce the negative impact of low service availability due to agents’ random explorations as they interact with the cloud environment, SpotRL uses a passive approach for the scaling of heterogeneous on-demand instances. Our experimental results show that the SpotRL approach can significantly reduce the deployment cost of SaaS providers while complying with high service availability. © 2022 Elsevier Inc.

## 04 — Title Screening

**Title:** Learning to make auto-scaling decisions with heterogeneous spot and on-demand instances via reinforcement learning

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Learning to make auto-scaling decisions with heterogeneous spot and on-demand instances via reinforcement learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Learning to make auto-scaling decisions with heterogeneous spot and on-demand instances via reinforcement learning
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
