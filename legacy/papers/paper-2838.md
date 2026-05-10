---
id: "paper-2838"
title: "Towards a scalable reinforcement learning approach for fair service function chain partitioning in mobile edge computing"
authors: ["Wang, Qiyu", "Zhang, Zilin", "Zhu, Qiang"]
year: 2026
venue: "Computer Networks"
venue_type: "journal"
doi: "10.1016/j.comnet.2026.112131"
url: "https://www.scopus.com/pages/publications/105031601143?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Fairness", "Network function parallelization", "Network function virtualization", "Reinforcement learning", "Scalability", "Service function chain", "SFC partitioning"]
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

# paper-2838 — Towards a scalable reinforcement learning approach for fair service function chain partitioning in mobile edge computing

## Metadata

- **Authors:** Wang, Qiyu and Zhang, Zilin and Zhu, Qiang
- **Year:** 2026
- **Venue:** Computer Networks
- **DOI:** 10.1016/j.comnet.2026.112131
- **URL:** https://www.scopus.com/pages/publications/105031601143?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Fairness; Network function parallelization; Network function virtualization; Reinforcement learning; Scalability; Service function chain; SFC partitioning

### Abstract

Network Function Virtualization (NFV) enables flexible and dynamic network processing by decoupling network functions from dedicated hardware devices. However, the rapid expansion of NFV introduces new challenges in efficiently managing and deploying Service Function Chains (SFCs) within distributed Mobile Edge Computing (MEC) infrastructures. The inherent length of SFCs—comprising multiple interconnected Virtual Network Functions (VNFs)—often results in undesirable end-to-end latency. To address this issue, Network Function Parallelization (NFP) allows concurrent execution of multiple VNFs, thereby reducing service latency. A key challenge in NFP lies in partitioning SFCs into multiple sub-SFCs, where resource constraints make optimal partitioning difficult. Traditional SFC partitioning methods often suffer from high computational overhead and poor scalability, while existing reinforcement learning-based approaches struggle to capture interdependencies among VNFs. To bridge this gap, this paper introduces a Scalable Reinforcement Learning-based Fair SFC Partitioning framework (SRLFP) for NFP-oriented orchestration that jointly balances resource utilization and service latency. The SRLFP employs a multi-agent cooperative actor–critic architecture that enables efficient inter-agent communication and coordination. Furthermore, a self-attention mechanism is integrated to identify and model intricate dependencies among VNFs, enhancing decision accuracy. SRLFP incorporates a partial parallelization strategy to decompose SFC requests into multiple parallel partitions while mitigating excessive parallelization overhead. Extensive simulation results demonstrate that SRLFP significantly improves resource utilization efficiency and scalability, achieving lower service latency compared to state-of-the-art baseline methods. © 2026 Elsevier B.V.

## 04 — Title Screening

**Title:** Towards a scalable reinforcement learning approach for fair service function chain partitioning in mobile edge computing

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Towards a scalable reinforcement learning approach for fair service function chain partitioning in mobile edge computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Towards a scalable reinforcement learning approach for fair service function chain partitioning in mobile edge computing
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
