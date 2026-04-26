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
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
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

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
