---
id: "paper-154"
title: "Regression training using model parallelism in a distributed cloud"
authors: ["Reijonen, Joel", "Opsenica, Miljenko", "Morabito, Roberto", "Komu, Miika", "Elmusrati, Mohammed"]
year: 2019
venue: "Proceedings - IEEE 17th International Conference on Dependable, Autonomic and Secure Computing, IEEE 17th International Conference on Pervasive Intelligence and Computing, IEEE 5th International Conference on Cloud and Big Data Computing, 4th Cyber Science and Technology Congress, DASC-PiCom-CBDCom-CyberSciTech 2019"
venue_type: "conference"
doi: "10.1109/DASC/PiCom/CBDCom/CyberSciTech.2019.00139"
url: "https://www.scopus.com/pages/publications/85075166650?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "741--747"
keywords: ["Intelligent agent", "Intelligent cloud", "Model parallelism", "Regression training"]
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

# paper-154 — Regression training using model parallelism in a distributed cloud

## Metadata

- **Authors:** Reijonen, Joel and Opsenica, Miljenko and Morabito, Roberto and Komu, Miika and Elmusrati, Mohammed
- **Year:** 2019
- **Venue:** Proceedings - IEEE 17th International Conference on Dependable, Autonomic and Secure Computing, IEEE 17th International Conference on Pervasive Intelligence and Computing, IEEE 5th International Conference on Cloud and Big Data Computing, 4th Cyber Science and Technology Congress, DASC-PiCom-CBDCom-CyberSciTech 2019
- **DOI:** 10.1109/DASC/PiCom/CBDCom/CyberSciTech.2019.00139
- **URL:** https://www.scopus.com/pages/publications/85075166650?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 741--747
- **Language:** English
- **Keywords:** Intelligent agent; Intelligent cloud; Model parallelism; Regression training

### Abstract

Machine learning requires a relevant amount of computational resources and it is usually executed in high-capacity centralized cloud infrastructures (e.g., data centers). In such infrastructures, resources are shared in a scalable manner through instantiation and orchestration of multiple virtualized services. Emerging trends in machine learning are distribution and parallelization of model training, which allows the execution of model training tasks in multiple distributed computational domains, with the aim of reducing the overall training time. A possible drawback in decentralization of machine learning is that performance latency issues may arise when the computation of training is geographically distributed to nodes with long distance from each other. One way to reduce latency is to utilize edge computing infrastructure, i.e., to distribute computation near the origin of the request. As edge resources can be scarce, it is important to orchestrate the model training in a parallelized manner. To this extent, in order to effectively ease the use of parallelization both in centralized and in distributed scenarios, we propose and implement a concept that we refer to Intelligent Agent (IA). An IA is responsible for instantiating and scheduling of the machine learning tasks (e.g., model training), and deriving inferences. In our solution, model training is distributed to multiple IAs in parallel. Each IA is packaged into a Linux container in order to take advantage of container portability across heterogenous deployments and to reuse existing container orchestration tools. We validate our proposal by deploying and instantiating multiple IAs across a distributed cloud environment, where each IA is accounting for a fixed amount of computational resources. Keywords - Intelligent agent, Model parallelism, Regression training, Intelligent cloud. © 2019 IEEE.

## 04 — Title Screening

**Title:** Regression training using model parallelism in a distributed cloud

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Regression training using model parallelism in a distributed cloud
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Regression training using model parallelism in a distributed cloud
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
