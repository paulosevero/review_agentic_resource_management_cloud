---
id: "paper-1351"
title: "Scheduling Generative-AI Job DAGs with Model Serving in Data Centers"
authors: ["Zheng, Ying", "Jiao, Lei", "Xu, Yuedong", "An, Bo", "Wang, Xin", "Li, Zongpeng"]
year: 2024
venue: "IEEE International Workshop on Quality of Service, IWQoS"
venue_type: "conference"
doi: "10.1109/IWQoS61813.2024.10682885"
url: "https://www.scopus.com/pages/publications/85206383798?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Edge computing", "Generative adversarial networks", "Integer programming", "Job shop scheduling", "Mixed-integer linear programming", "Profitability", "Acyclic graphs", "Computing environments", "Datacenter", "Edge computing", "Model Selection", "Non linear", "Non-trivial", "Scheduling selection", "Task modelling", "Tasks scheduling", "Integer linear programming"]
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

# paper-1351 — Scheduling Generative-AI Job DAGs with Model Serving in Data Centers

## Metadata

- **Authors:** Zheng, Ying and Jiao, Lei and Xu, Yuedong and An, Bo and Wang, Xin and Li, Zongpeng
- **Year:** 2024
- **Venue:** IEEE International Workshop on Quality of Service, IWQoS
- **DOI:** 10.1109/IWQoS61813.2024.10682885
- **URL:** https://www.scopus.com/pages/publications/85206383798?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge computing; Generative adversarial networks; Integer programming; Job shop scheduling; Mixed-integer linear programming; Profitability; Acyclic graphs; Computing environments; Datacenter; Edge computing; Model Selection; Non linear; Non-trivial; Scheduling selection; Task modelling; Tasks scheduling; Integer linear programming

### Abstract

Scheduling generative-AI jobs in the edge computing environment faces multiple non-trivial challenges, including the Directed Acyclic Graph (DAG) dependency among tasks, the intrinsic intertwinement between task scheduling and model selection, and the dynamic unpredictable arrival of job DAGs. In this work, we capture all such challenges and formulate a non-linear integer program to optimize the long-term profit of the generative-AI service provider, i.e., service revenue of the admitted jobs minus system costs of executing the tasks contained in such job DAGs. This problem is NP-hard even in the offline setting. To solve it, we first reformulate it into an equivalent schedule selection problem using generated schedules to tackle complex constraints. Then, we design a new online scheduling method through the online primal-dual technique. Experimental results confirm that our approach can increase the total service profit by up to 41.2% compared to existing algorithms. © 2024 IEEE.

## 04 — Title Screening

**Title:** Scheduling Generative-AI Job DAGs with Model Serving in Data Centers

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Scheduling Generative-AI Job DAGs with Model Serving in Data Centers
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Scheduling Generative-AI Job DAGs with Model Serving in Data Centers
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
