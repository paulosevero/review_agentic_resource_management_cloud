---
id: "paper-2364"
title: "Dangers Behind Access Control: Understanding and Exploiting Implicit Permissions in Kubernetes"
authors: ["Yang, Nanzi", "Liu, Xingyu", "Shen, Wenbo", "Li, Jinku", "Lu, Kangjie"]
year: 2025
venue: "CCS 2025 - Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security"
venue_type: "conference"
doi: "10.1145/3719027.3765106"
url: "https://www.scopus.com/pages/publications/105023835960?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "3401--3415"
keywords: ["Access Control", "Implicit Permission", "Kubernetes"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2364 — Dangers Behind Access Control: Understanding and Exploiting Implicit Permissions in Kubernetes

## Metadata

- **Authors:** Yang, Nanzi and Liu, Xingyu and Shen, Wenbo and Li, Jinku and Lu, Kangjie
- **Year:** 2025
- **Venue:** CCS 2025 - Proceedings of the 2025 ACM SIGSAC Conference on Computer and Communications Security
- **DOI:** 10.1145/3719027.3765106
- **URL:** https://www.scopus.com/pages/publications/105023835960?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 3401--3415
- **Language:** English
- **Keywords:** Access Control; Implicit Permission; Kubernetes

### Abstract

As the de-facto standard for container orchestration, Kubernetes is extensively adopted by numerous companies and cloud vendors, making its security critical. In this paper, we define a new attack surface called implicit permission: The execution of explicitly granted permissions in Kubernetes dynamically leads to implicit operations on other resources, enabling new permissions beyond the explicitly granted ones. Such implicit permissions create security vulnerabilities that attackers can exploit to compromise an entire cluster. Automatically identifying implicit permissions is challenging due to implicit relation reasoning and dynamic behaviors across diverse components of Kubernetes. To address that, we devise a systematic approach that combines static analysis techniques with the advanced capabilities of the large language model (LLM, e.g., GPT-4.5). Initially, we develop a static analysis to identify all Kubernetes resources. Building on this, we use static analysis to identify all explicit permissions for each resource. Finally, by combining the semantic reasoning capabilities of LLMs with the pattern-based precision of static analysis, we reason about what explicit permissions may dynamically lead to implicit permissions through complex interactions and uncover 593 implicit permissions derived from explicit permissions. We use the implicit permission references as insights to identify potential risks of CNCF projects and applications provided by the top four cloud vendors. With responsible disclosure, we obtain five new CVEs, six acknowledgments of cloud vendors, and a bounty awarded by Google. These acknowledgments underlie the practical impact of our attack. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Dangers Behind Access Control: Understanding and Exploiting Implicit Permissions in Kubernetes

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Dangers Behind Access Control: Understanding and Exploiting Implicit Permissions in Kubernetes
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Dangers Behind Access Control: Understanding and Exploiting Implicit Permissions in Kubernetes
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
