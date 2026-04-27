---
id: "paper-2563"
title: "RobGenX: Uncertainty-Aware Inference in eXtreme Computing Power Networks"
authors: ["El-Khatib, Rawan F.", "Zorba, Nizar", "Hassanein, Hossam S."]
year: 2026
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2025.3621342"
url: "https://www.scopus.com/pages/publications/105019580227?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "3828--3845"
keywords: ["alternating direction method of multipliers (ADMM)", "computing power networks (CPNs)", "eXtreme edge computing (XEC)", "generative artificial intelligence (GenAI)", "task allocation", "uncertainty-aware systems"]
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
    final_score: 0.0
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2563 — RobGenX: Uncertainty-Aware Inference in eXtreme Computing Power Networks

## Metadata

- **Authors:** El-Khatib, Rawan F. and Zorba, Nizar and Hassanein, Hossam S.
- **Year:** 2026
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2025.3621342
- **URL:** https://www.scopus.com/pages/publications/105019580227?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 3828--3845
- **Language:** English
- **Keywords:** alternating direction method of multipliers (ADMM); computing power networks (CPNs); eXtreme edge computing (XEC); generative artificial intelligence (GenAI); task allocation; uncertainty-aware systems

### Abstract

Computing Power Networks (CPNs) emerged as a promising architectural paradigm that unifies the edge and user-owned eXtreme Edge Devices (XEDs) into an orchestrated compute fabric. By leveraging opportunistic idle resources at the eXtreme Edge (XE), CPNs offer a pathway to democratize generative AI and reduce reliance on cloud monopolies. However, inference delegation within CPNs is hindered by the volatile and user-dependent nature of compute availability of XEDs. In this work, we propose RobGenX, a robust task allocation framework tailored for inference in XE-enabled CPNs under stochastic compute capacity constraints. To the best of our knowledge, RobGenX is the first work to explicitly model the uncertainty of XEDs' compute capacity. RobGenX integrates Recourse Programming (RP) to penalize overassignment and Chance-Constrained Programming (CCP) to enforce probabilistic workload guarantees, respectively. We model the task allocation problem as a two-stage chance-constrained program and obtain an equivalent deterministic reformulation using a scenario-based approach. To overcome the computational burden of the resulting Integer Linear Program (ILP), we develop a decomposition-based solution using the Alternating Direction Method of Multipliers (ADMM), which decouples the relaxed problem into parallelizable subproblems across uncertainty scenarios. Simulation results demonstrate that RobGenX and its lower complexity ADMM-based solution consistently outperform the state-of-the-art task allocation baselines, achieving up to 58% improvement in inference completion rates and 55% in assignment stability. © 2013 IEEE.

## 04 — Title Screening

**Title:** RobGenX: Uncertainty-Aware Inference in eXtreme Computing Power Networks

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** RobGenX: Uncertainty-Aware Inference in eXtreme Computing Power Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** RobGenX: Uncertainty-Aware Inference in eXtreme Computing Power Networks
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
