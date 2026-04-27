---
id: "paper-1953"
title: "Analyzing and mitigating (with LLMs) the security misconfigurations of Helm charts from Artifact Hub"
authors: ["Minna, Francesco", "Massacci, Fabio", "Tuma, Katja"]
year: 2025
venue: "Empirical Software Engineering"
venue_type: "journal"
doi: "10.1007/s10664-025-10688-0"
url: "https://www.scopus.com/pages/publications/105010112880?origin=resultslist"
publisher: "Springer"
pages: ""
keywords: ["Helm charts", "Kubernetes", "LLM", "Misconfigurations", "Mitigations"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1953 — Analyzing and mitigating (with LLMs) the security misconfigurations of Helm charts from Artifact Hub

## Metadata

- **Authors:** Minna, Francesco and Massacci, Fabio and Tuma, Katja
- **Year:** 2025
- **Venue:** Empirical Software Engineering
- **DOI:** 10.1007/s10664-025-10688-0
- **URL:** https://www.scopus.com/pages/publications/105010112880?origin=resultslist
- **Publisher:** Springer
- **Pages:** 
- **Language:** English
- **Keywords:** Helm charts; Kubernetes; LLM; Misconfigurations; Mitigations

### Abstract

Helm is a package manager that allows defining, installing, and upgrading applications with Kubernetes (K8s), a popular container orchestration platform. A Helm chart is a collection of files describing all dependencies, resources, and parameters required for deploying an application within a K8s cluster. This study aimed to mine and empirically evaluate the security of Helm charts, comparing the performance of existing tools in terms of misconfigurations reported by policies available by default, and measuring to what extent LLMs could be used for removing misconfigurations. For these reasons, we proposed a pipeline to mine Helm charts from Artifact Hub, a popular centralized repository, and analyze them using state-of-the-art open-source tools like Checkov and KICS. First, the pipeline runs several chart analyzers and identifies the common and unique misconfigurations reported by each tool. Secondly, it uses LLMs to suggest a mitigation for each misconfiguration. Finally, the LLM refactored chart previously generated is analyzed again by the same tools to see whether it satisfies the tool’s policies. We also performed a manual analysis on a subset of charts to evaluate whether there are false positive misconfigurations from the tool’s reporting and in the LLM refactoring. We found that (i) there is a significant difference between LLMs, (ii) providing a snippet of the YAML template as input might be insufficient compared to all resources, and (iii) even though LLMs can generate correct fixes, they may also delete other irrelevant configurations that break the application. © The Author(s) 2025.

## 04 — Title Screening

**Title:** Analyzing and mitigating (with LLMs) the security misconfigurations of Helm charts from Artifact Hub

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Analyzing and mitigating (with LLMs) the security misconfigurations of Helm charts from Artifact Hub
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Analyzing and mitigating (with LLMs) the security misconfigurations of Helm charts from Artifact Hub
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
