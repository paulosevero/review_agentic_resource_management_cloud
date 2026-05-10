---
id: "paper-1419"
title: "SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems"
authors: ["Becattini, Marco", "Verdecchia, Roberto", "Vicario, Enrico"]
year: 2025
venue: "Proceedings - 2025 IEEE/ACM International Workshop on New Trends in Software Architecture, SATrends 2025"
venue_type: "conference"
doi: "10.1109/SATrends66715.2025.00006"
url: "https://www.scopus.com/pages/publications/105009458305?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "5--8"
keywords: ["llm", "se4ai", "software architecture"]
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

# paper-1419 — SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems

## Metadata

- **Authors:** Becattini, Marco and Verdecchia, Roberto and Vicario, Enrico
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE/ACM International Workshop on New Trends in Software Architecture, SATrends 2025
- **DOI:** 10.1109/SATrends66715.2025.00006
- **URL:** https://www.scopus.com/pages/publications/105009458305?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 5--8
- **Language:** English
- **Keywords:** llm; se4ai; software architecture

### Abstract

As a new and disruptive technology, the introduction of large language models (LLMs) may be the first step into a paradigm shift of how we develop and deploy software-intensive systems. While the capabilities of LLM agents for software engineering and architecture tasks are currently explored, how to architect LLM-based systems appears to be to date an uncharted territory. Software architectures based on a single LLM agent face inherent challenges, such as lack of task customization, lack of memory, and limited access to ground truth. These challenges become especially pressing in real-world contexts that demand persistent context, validated information, and task-specific flexibility. As a potential solution to overcome these challenges, multiple LLM-agents can be adopted for specialized tasks within a single software-intensive system. In this contribution, we open the discourse on architecting LLM-intensive software products by presenting SALLMA, a Software Architecture for LLMbased Multi-Agent systems. SALLMA leverages two core layers, namely (i) the Operational Layer, responsible for request intent management, handling real-time task execution and dynamic orchestration of agents, and (ii) the Knowledge Layer, used to to store and manage metamodels and configurations for workflows and agents. To primarily assess the viability of SALLMA, we develop a proof of concept leveraging as key technologies Docker, Kubernetes, Python, LangChain, Hugging Face, Mistral, LLaMA, and SQL and NoSQL databases. Currently, SALLMA is deployed to provide information on behalf of public administration offices, and is currently utilized in a business simulation scenario. © 2025 IEEE.

## 04 — Title Screening

**Title:** SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** SALLMA: A Software Architecture for LLM-Based Multi-Agent Systems
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
