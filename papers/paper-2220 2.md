---
id: "paper-2220"
title: "Towards Orchestrating Agentic Applications as FaaS Workflows"
authors: ["Tokal, Shiva Sai Krishna Anand", "Jha, Vaibhav", "Eswaran, Anand", "Jayachandran, Praveen", "Simmhan, Yogesh"]
year: 2025
venue: "Proceedings - 2025 IEEE International Parallel and Distributed Processing Symposium Workshops, IPDPSW 2025"
venue_type: "conference"
doi: "10.1109/IPDPSW66978.2025.00156"
url: "https://www.scopus.com/pages/publications/105015528025?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1003--1010"
keywords: ["agent", "faas", "llm", "workflow"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2220 — Towards Orchestrating Agentic Applications as FaaS Workflows

## Metadata

- **Authors:** Tokal, Shiva Sai Krishna Anand and Jha, Vaibhav and Eswaran, Anand and Jayachandran, Praveen and Simmhan, Yogesh
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE International Parallel and Distributed Processing Symposium Workshops, IPDPSW 2025
- **DOI:** 10.1109/IPDPSW66978.2025.00156
- **URL:** https://www.scopus.com/pages/publications/105015528025?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1003--1010
- **Language:** English
- **Keywords:** agent; faas; llm; workflow

### Abstract

Agentic applications consist of multiple agents that encapsulate tools that can be selected by an Large Language Model (LLM) to execute real-world tasks while also collaborating with other agents to solve complex applications, including scientific tasks. However, creating these agentic applications require substantial user effort, involving model selection, prompt engineering and guardrails. There are also limitation in deploying these applications on cloud platforms. In this early work, we take a step towards addressing these limitations by proposing an intuitive pattern comprising of a planner, executor, evaluator and judge agents to compose these as agentic workflows with simple prompt specifications. We also propose to model these as Function as a Service (FaaS) workflows on public/private clouds to simplify their deployment and outsourcing their orchestration. A preliminary implementation of our AgentX platform provides Python modules for these roles, which are used to compose AWS Step Functions. Our initial results on local machine and AWS using Open AI and Claude show promise in simpler compositions, but also expose challenges due to diverse behavior of LLMs. As future work, we will explore the use of our XFaaS hybrid cloud orchestration platform to deploy these on hybrid public/private clouds to leverage cost arbitrage, and offer flexible and automated selection of model to trade-off latency, accuracy and reliability.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Towards Orchestrating Agentic Applications as FaaS Workflows

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Towards Orchestrating Agentic Applications as FaaS Workflows
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Towards Orchestrating Agentic Applications as FaaS Workflows
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
