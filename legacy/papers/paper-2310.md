---
id: "paper-2310"
title: "Automated Bug Discovery in Cloud Infrastructure-as-Code Updates with LLM Agents"
authors: ["Xiang, Yiming", "Yang, Zhenning", "Peng, Jingjia", "Bauer, Hermann", "Kon, Patrick Tser Jern", "Qiu, Yiming", "Chen, Ang"]
year: 2025
venue: "Proceedings - 2025 IEEE/ACM International Workshop on Cloud Intelligence and AIOps, AIOps 2025"
venue_type: "conference"
doi: "10.1109/AIOps66738.2025.00011"
url: "https://www.scopus.com/pages/publications/105009458915?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "20--25"
keywords: ["Infrastructure-as-Code", "Program update", "Reliability", "Software testing and debugging", "Using LLMs for Cloud Ops"]
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

# paper-2310 — Automated Bug Discovery in Cloud Infrastructure-as-Code Updates with LLM Agents

## Metadata

- **Authors:** Xiang, Yiming and Yang, Zhenning and Peng, Jingjia and Bauer, Hermann and Kon, Patrick Tser Jern and Qiu, Yiming and Chen, Ang
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE/ACM International Workshop on Cloud Intelligence and AIOps, AIOps 2025
- **DOI:** 10.1109/AIOps66738.2025.00011
- **URL:** https://www.scopus.com/pages/publications/105009458915?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 20--25
- **Language:** English
- **Keywords:** Infrastructure-as-Code; Program update; Reliability; Software testing and debugging; Using LLMs for Cloud Ops

### Abstract

Cloud environments are increasingly managed by Infrastructure-as-Code (IaC) platforms (e.g., Terraform), which allow developers to define their desired infrastructure as a configuration program that describes cloud resources and their dependencies. This shields developers from low-level operations for creating and maintaining resources, since they are automatically performed by IaC platforms when compiling and deploying the configuration. However, while IaC platforms are rigorously tested for initial deployments, they exhibit myriad errors for runtime updates, e.g., adding/removing resources and dependencies. IaC updates are common because cloud infrastructures are long-lived but user requirements fluctuate over time. Unfortunately, our experience shows that updates often introduce subtle yet impactful bugs. The update logic in IaC frameworks is hard to test due to the vast and evolving search space, which includes diverse infrastructure setups and a wide range of provided resources with new ones frequently added. We introduce TerraFault, an automated, efficient, LLM-guided system for discovering update bugs, and report our findings with an initial prototype. TerraFault incorporates various optimizations to navigate the large search space efficiently and employs techniques to accelerate the testing process. Our prototype has successfully identified bugs even in simple IaC updates, showing early promise in systematically identifying update bugs in today's IaC frameworks to increase their reliability.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Automated Bug Discovery in Cloud Infrastructure-as-Code Updates with LLM Agents

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Automated Bug Discovery in Cloud Infrastructure-as-Code Updates with LLM Agents
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Automated Bug Discovery in Cloud Infrastructure-as-Code Updates with LLM Agents
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
