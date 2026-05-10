---
id: "paper-882"
title: "Research on Dynamic Fuzzy Testing in Securing Cloud Infrastructure based on Deep Learning"
authors: ["Dan, Ningyun", "Zhao, Lun", "Pan, Wenjin", "Cai, Yan"]
year: 2024
venue: "2024 3rd International Conference on Cloud Computing, Big Data Application and Software Engineering, CBASE 2024"
venue_type: "conference"
doi: "10.1109/CBASE64041.2024.10824501"
url: "https://www.scopus.com/pages/publications/85217187711?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "859--863"
keywords: ["cloud infrastructure security", "Deep learning", "dynamic fuzzing", "reinforcement learning"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-882 — Research on Dynamic Fuzzy Testing in Securing Cloud Infrastructure based on Deep Learning

## Metadata

- **Authors:** Dan, Ningyun and Zhao, Lun and Pan, Wenjin and Cai, Yan
- **Year:** 2024
- **Venue:** 2024 3rd International Conference on Cloud Computing, Big Data Application and Software Engineering, CBASE 2024
- **DOI:** 10.1109/CBASE64041.2024.10824501
- **URL:** https://www.scopus.com/pages/publications/85217187711?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 859--863
- **Language:** English
- **Keywords:** cloud infrastructure security; Deep learning; dynamic fuzzing; reinforcement learning

### Abstract

As cloud infrastructure assumes an increasingly pivotal role in contemporary computing environments, ensuring its security becomes a matter of paramount importance. As a prevalent vulnerability detection technology, traditional fuzz testing encounters the challenge of scalability in the context of the intricate and evolving nature of cloud computing systems. Our approach employs deep neural networks (DNNs) to analyze the behavior of diverse software components within cloud systems. It incorporates multi-dimensional data, including system logs, network traffic, and resource utilization in virtualized environments. The neural network is capable of identifying potential vulnerability points through an automated process. To generate effective test cases, we introduce a reinforcement learning framework based on a policy gradient algorithm. This framework enables an intelligent agent to interact with the system in order to obtain feedback and subsequently update the policy in order to progressively generate more aggressive test cases. The framework is designed with an adaptive reward mechanism that not only encourages triggering crashes but also focuses on edge use cases that reveal system bottlenecks, thereby improving vulnerability coverage. Furthermore, in consideration of the dynamic nature of the cloud environment, we have developed a distributed test architecture that enables the parallel deployment of tasks in virtual machines or containers, simulates multi-tenancy and dynamic load change scenarios, and introduces a vulnerability detection mechanism at the virtualization layer. The proposed model is capable of adaptively generating highly targeted test cases and optimizing the test strategy through continuous learning, thereby markedly enhancing the detection capability of complex vulnerabilities in cloud infrastructure.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Research on Dynamic Fuzzy Testing in Securing Cloud Infrastructure based on Deep Learning

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Research on Dynamic Fuzzy Testing in Securing Cloud Infrastructure based on Deep Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Research on Dynamic Fuzzy Testing in Securing Cloud Infrastructure based on Deep Learning
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
