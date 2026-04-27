---
id: "paper-1751"
title: "Pedagogy Meets AI & Systems: Towards Orchestrating Tutor Agents in Moodle using FaaS"
authors: ["Kulkarni, Varad", "Reddy, Nikhil", "Simmhan, Yogesh"]
year: 2025
venue: "Proceedings of the IEEE International Conference on High Performance Computing, Data, and Analytics Workshops, HiPCW"
venue_type: "conference"
doi: "10.1109/HiPCW66559.2025.00052"
url: "https://www.scopus.com/pages/publications/105036053754?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "195--196"
keywords: ["ai agents on faas", "ai for education", "pedagogy workflows"]
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
    human_justification: "Não é gerenciamento de recursos em infraestruturas de cloud/edge/fog etc."

---

# paper-1751 — Pedagogy Meets AI & Systems: Towards Orchestrating Tutor Agents in Moodle using FaaS

## Metadata

- **Authors:** Kulkarni, Varad and Reddy, Nikhil and Simmhan, Yogesh
- **Year:** 2025
- **Venue:** Proceedings of the IEEE International Conference on High Performance Computing, Data, and Analytics Workshops, HiPCW
- **DOI:** 10.1109/HiPCW66559.2025.00052
- **URL:** https://www.scopus.com/pages/publications/105036053754?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 195--196
- **Language:** English
- **Keywords:** ai agents on faas; ai for education; pedagogy workflows

### Abstract

Large Language Models (LLMs) are enabling scalable, personalized AI-driven education. We study a real-world setting where teaching for a post-graduate course is handled by a configured AI Tutor Agent based on MS Teams Copilot, with students interacting with it through a chat interface. Tutor-Student conversation transcripts are submitted into the Moodle LMS for analysis. Our workflows assess these interactions via two pipelines: for personalized feedback and class-level insights. These analytics are deployed on public-cloud FaaS platforms, as AWS Step Functions and Azure Durable Functions, to exploit autoscaling and pay-per-use efficiency suited to bursty submission patterns. We benchmark latency, cost and I/O tokens, positioning pedagogy as a novel systems workload and revealing the limits of current FaaS platforms for educational AI.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Pedagogy Meets AI & Systems: Towards Orchestrating Tutor Agents in Moodle using FaaS

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Pedagogy Meets AI & Systems: Towards Orchestrating Tutor Agents in Moodle using FaaS
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Pedagogy Meets AI & Systems: Towards Orchestrating Tutor Agents in Moodle using FaaS
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
