---
id: "paper-914"
title: "Case Study: Applying Automated Optimization Tooling to Microservice Environments that Scale Safely at Ancestry.com and the Learnings"
authors: ["Gajewski, Darek", "Arju, Muhammad Ashfakur Rahman", "Abdelfattah, Amr S.", "Cerny, Tomas"]
year: 2024
venue: "Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)"
venue_type: "conference"
doi: "10.1007/978-3-031-70797-1_2"
url: "https://www.scopus.com/pages/publications/85203601811?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "20--36"
keywords: ["Canary Testing", "Case Study", "Cloud Systems", "Container Right-sizing Optimization", "Enterprise Architecture"]
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
    human_decision: ""
    human_justification: ""

---

# paper-914 — Case Study: Applying Automated Optimization Tooling to Microservice Environments that Scale Safely at Ancestry.com and the Learnings

## Metadata

- **Authors:** Gajewski, Darek and Arju, Muhammad Ashfakur Rahman and Abdelfattah, Amr S. and Cerny, Tomas
- **Year:** 2024
- **Venue:** Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
- **DOI:** 10.1007/978-3-031-70797-1_2
- **URL:** https://www.scopus.com/pages/publications/85203601811?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 20--36
- **Language:** English
- **Keywords:** Canary Testing; Case Study; Cloud Systems; Container Right-sizing Optimization; Enterprise Architecture

### Abstract

In 2018, Ancestry migrated into Amazon’s public cloud. Hundreds of applications that were hosted on physical hardware were migrated to the cloud onto internally supported Kubernetes environments. This established a microservice architecture for many applications at Ancestry. In 2020, Ancestry’s cloud expenses goals were set at $12M in Operating expenses savings over 2 years. To overcome the problem of scale, an automated right-sizing effort needed to take place. Ancestry purchased a tool called Opsani. Opsani allowed the team to use dynamic canary testing in combination with a CanaryAdvisor to act as the AI agent. Opsani was integrated into Ancestry’s continuous integration and continuous delivery platform to automate right-sizing and help reach cost optimization targets with limited resources. After a successful proof of concept was developed by the DNA Matches agile team, there was a company-wide integration of Opsani into Ancestry’s CI/CD platform. The tool would need to scale out continuous optimization efforts across many of the teams utilizing Kubernetes and virtual machine infrastructure. This case study details the experience and knowledge gained from scaling automation optimizations using an AI agent with more than 200 individual applications across 30 agile teams. The challenges introduced by the rate of changes in the system and monitoring feedback delays began to affect the customer experience with the product. As teams adopted optimization changes at higher rates, new guard rails were introduced to control the release cycles and ensure stability for paying customers. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2024.

## 04 — Title Screening

**Title:** Case Study: Applying Automated Optimization Tooling to Microservice Environments that Scale Safely at Ancestry.com and the Learnings

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Case Study: Applying Automated Optimization Tooling to Microservice Environments that Scale Safely at Ancestry.com and the Learnings
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Case Study: Applying Automated Optimization Tooling to Microservice Environments that Scale Safely at Ancestry.com and the Learnings
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
