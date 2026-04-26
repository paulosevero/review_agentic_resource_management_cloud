---
id: "paper-1057"
title: "Hybrid Elastic Scaling Strategy for Container Cloud based on Load Prediction and Reinforcement Learning"
authors: ["Liu, Peng", "Zhao, Weisen", "Zhang, Baoliang", "Wang, Jing"]
year: 2024
venue: "Journal of Physics: Conference Series"
venue_type: "conference"
doi: "10.1088/1742-6596/2732/1/012014"
url: "https://www.scopus.com/pages/publications/85190422007?origin=resultslist"
publisher: "Institute of Physics"
pages: ""
keywords: ["Container cloud", "Elastic scaling", "Kubernetes", "Load prediction", "Reinforcement learning"]
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
    final_score: 0.5
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1057 — Hybrid Elastic Scaling Strategy for Container Cloud based on Load Prediction and Reinforcement Learning

## Metadata

- **Authors:** Liu, Peng and Zhao, Weisen and Zhang, Baoliang and Wang, Jing
- **Year:** 2024
- **Venue:** Journal of Physics: Conference Series
- **DOI:** 10.1088/1742-6596/2732/1/012014
- **URL:** https://www.scopus.com/pages/publications/85190422007?origin=resultslist
- **Publisher:** Institute of Physics
- **Pages:** 
- **Language:** English
- **Keywords:** Container cloud; Elastic scaling; Kubernetes; Load prediction; Reinforcement learning

### Abstract

To harness the advantages of both proactive and responsive scaling, adapting to various workload scenarios, this paper introduces a container hybrid scaling strategy called HyPredRL, rooted in load prediction and reinforcement learning. Within the proactive scaling module RL-PM, a load prediction model, MSC-LSTM, predict workloads and, in conjunction with current workload states, leverages reinforcement learning agents for intelligent scaling decisions. The responsive scaling strategy, SLA-HPA, enhances Kubernetes' native scaling strategy, which primarily considers resource utilization, by incorporating response time metrics. Ultimately, a hybrid scaling controller is designed, applying the principles of "rapid scaling out"and "balanced conflicts"to coordinate proactive and responsive scaling. Experimental results demonstrate that HyPredRL outperforms existing methods in SLA violation rate, resource utilization, and request response time, effectively improving application performance and scalability.  © Published under licence by IOP Publishing Ltd.

## 04 — Title Screening

**Title:** Hybrid Elastic Scaling Strategy for Container Cloud based on Load Prediction and Reinforcement Learning

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Hybrid Elastic Scaling Strategy for Container Cloud based on Load Prediction and Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Hybrid Elastic Scaling Strategy for Container Cloud based on Load Prediction and Reinforcement Learning
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
