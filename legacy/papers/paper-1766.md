---
id: "paper-1766"
title: "KubeScribe: LLM-Driven Automation of Runtime Security Policies in Cloud-Native Environments"
authors: ["Lee, Jaeyoung", "Nam, Jaehyun"]
year: 2025
venue: "International Conference on ICT Convergence"
venue_type: "conference"
doi: "10.1109/ICTC66702.2025.11388772"
url: "https://www.scopus.com/pages/publications/105035064737?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "1793--1798"
keywords: ["LLM", "Policy Automation", "Runtime Security"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1766 — KubeScribe: LLM-Driven Automation of Runtime Security Policies in Cloud-Native Environments

## Metadata

- **Authors:** Lee, Jaeyoung and Nam, Jaehyun
- **Year:** 2025
- **Venue:** International Conference on ICT Convergence
- **DOI:** 10.1109/ICTC66702.2025.11388772
- **URL:** https://www.scopus.com/pages/publications/105035064737?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 1793--1798
- **Language:** English
- **Keywords:** LLM; Policy Automation; Runtime Security

### Abstract

Cloud-native infrastructures built on Kubernetes accelerate deployment and operations but broaden the runtime attack surface beyond traditional defenses. Runtime security solutions enforce fine-grained policies at the kernel and orchestration layers, yet policy authoring remains complex due to heterogeneous schemas and rapidly evolving workloads. Existing automation approaches focus mainly on network rules or syscall-level seccomp profiles, leaving system-level runtime policies unexplored. We present KubeScribe, the first framework to automate file-, process-, and syscall-aware runtime security policies using large language models. KubeScribe integrates runtime log analysis with LLM-based synthesis and applies dual validation (CRD schema and resource-level checks) to ensure safe deployment. Evaluations on KubeArmor, Tetragon, and Cilium show compile success rates improving from below 10% to above 66% and coverage exceeding 90%, with substantial gains in BLEU, ROUGE, and METEOR metrics. These results demonstrate that KubeScribe provides a practical and generalizable path toward automated runtime security in Kubernetes environments. © 2025 IEEE.

## 04 — Title Screening

**Title:** KubeScribe: LLM-Driven Automation of Runtime Security Policies in Cloud-Native Environments

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** KubeScribe: LLM-Driven Automation of Runtime Security Policies in Cloud-Native Environments
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** KubeScribe: LLM-Driven Automation of Runtime Security Policies in Cloud-Native Environments
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
