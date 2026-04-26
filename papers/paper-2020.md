---
id: "paper-2020"
title: "KIMERA: From Evaluation-as-a-Service to Evaluation-in-the-Cloud"
authors: ["Pasin, Andrea", "Ferro, Nicola"]
year: 2025
venue: "SIGIR 2025 - Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval"
venue_type: "conference"
doi: "10.1145/3726302.3730298"
url: "https://www.scopus.com/pages/publications/105011823475?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "3584--3594"
keywords: ["Docker", "Evaluation", "Information Retrieval", "Infrastructure", "Kubernetes", "Large Language Models", "Quantum Computing", "Reproducibility"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2020 — KIMERA: From Evaluation-as-a-Service to Evaluation-in-the-Cloud

## Metadata

- **Authors:** Pasin, Andrea and Ferro, Nicola
- **Year:** 2025
- **Venue:** SIGIR 2025 - Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval
- **DOI:** 10.1145/3726302.3730298
- **URL:** https://www.scopus.com/pages/publications/105011823475?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 3584--3594
- **Language:** English
- **Keywords:** Docker; Evaluation; Information Retrieval; Infrastructure; Kubernetes; Large Language Models; Quantum Computing; Reproducibility

### Abstract

Experimental evaluation steers the development of Information Retrieval (IR) systems, and large-scale evaluation campaigns provide the field with a common infrastructure to conduct comparable evaluation exercises. Over the years, tools and platforms have been developed to manage and automate these activities, enhance the reproducibility of conducted experiments and facilitate data sharing. In this context, Evaluation-as-a-Service (EaaS) emerged as an approach to avoid distributing experimental collections, which may contain copyrighted or sensitive data, and instead execute containerised code on that data on remote servers. We propose Kubernetes Infrastructure for Managed Evaluation and Resource Access (KIMERA) as the next step from EaaS into Evaluation-in-the-Cloud (EitC), allowing researchers to directly code and execute their systems through their browsers, requiring only an internet connection. Moreover, recent advancements, such as Large Language Models, or new computing paradigms, such as quantum computers, require external third-party services and computational resources. In this respect, KIMERA streamlines and simplifies access to such services on-demand via their APIs. More in detail, KIMERA relies on state-of-the-art containerization and orchestration tools, such as Docker and Kubernetes, to provide a robust, scalable, secure, and fault-tolerant IR evaluation platform. KIMERA monitors and stores all the participants’ submissions, accurately keeping track of the resource usage, allowing for evaluating both the efficiency and the effectiveness of the deployed methods. Moreover, all participants can be assigned workspaces sharing the same resources (i.e., CPU and RAM), thus enhancing reproducibility and comparability among systems. Finally, KIMERA has been designed with modularity and extensibility in mind, allowing it to be easily adapted to new use cases and usage scenarios. KIMERA has been developed and adopted in the context of the QuantumCLEF lab, to allow for mixed experiments, comparing approaches running on traditional hardware and on real quantum annealers provided by external companies. KIMERA has also been used as a learning resource to provide Quantum Computing tutorials for IR at major conferences, such as ECIR and SIGIR. The source code of KIMERA is openly available at https://github.com/MjPaxter/KIMERA. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** KIMERA: From Evaluation-as-a-Service to Evaluation-in-the-Cloud

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** KIMERA: From Evaluation-as-a-Service to Evaluation-in-the-Cloud
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** KIMERA: From Evaluation-as-a-Service to Evaluation-in-the-Cloud
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
