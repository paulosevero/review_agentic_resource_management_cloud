---
id: "paper-2926"
title: "AutoML-Pipeline: A RAG-Enhanced Code Generation Framework With Pre-Validation for Cloud-Native Machine Learning Workflows"
authors: ["Zhao, Wenyu", "Chen, Tingjie", "Yang, Jie Si", "Qiu, Lei"]
year: 2026
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2026.3673923"
url: "https://www.scopus.com/pages/publications/105032798285?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "41932--41945"
keywords: ["automated optimization", "cloud computing", "Code generation", "large language models", "retrieval-augmented generation"]
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
    human_justification: "RAG provavelmente indica LLM/SLM"

---

# paper-2926 — AutoML-Pipeline: A RAG-Enhanced Code Generation Framework With Pre-Validation for Cloud-Native Machine Learning Workflows

## Metadata

- **Authors:** Zhao, Wenyu and Chen, Tingjie and Yang, Jie Si and Qiu, Lei
- **Year:** 2026
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2026.3673923
- **URL:** https://www.scopus.com/pages/publications/105032798285?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 41932--41945
- **Language:** English
- **Keywords:** automated optimization; cloud computing; Code generation; large language models; retrieval-augmented generation

### Abstract

The proliferation of cloud-native machine learning platforms has significantly accelerated model development and deployment cycles. However, constructing and maintaining heterogeneous pipeline code spanning multiple languages (Python, YAML, Spark SQL) and cloud-specific configurations remains labor-intensive and error-prone. Existing LLM-based code generation tools lack awareness of runtime constraints and historical execution patterns, frequently producing code with resource misconfigurations or dependency conflicts that fail upon deployment. To address these challenges, we propose AutoML-Pipeline, a closed-loop code generation framework that integrates Retrieval-Augmented Generation (RAG) with reinforcement learning feedback mechanisms. Our approach leverages a knowledge base constructed from successful pipeline execution logs to guide GPT-4 in generating deployment-ready code that adheres to platform-specific constraints. The key innovation lies in a novel Pre-validation Agent that employs simulated execution environments to predict resource consumption and detect dependency conflicts before actual deployment. This agent iteratively refines generated code through a feedback loop informed by predicted execution profiles and dependency graphs. We evaluate our framework on the CodeSearchNet dataset augmented with Azure ML pipeline specifications, demonstrating a 43.7% improvement in first-submission success rate and 31.2% reduction in resource over-provisioning compared to vanilla GPT-4 baselines. Ablation studies confirm that both the RAG retrieval mechanism and pre-validation agent contribute substantially to performance gains. Our work establishes a practical paradigm for integrating large language models with domain-specific runtime intelligence, with potential applications extending to other infrastructure-as-code generation tasks.  © 2026 The Authors.

## 04 — Title Screening

**Title:** AutoML-Pipeline: A RAG-Enhanced Code Generation Framework With Pre-Validation for Cloud-Native Machine Learning Workflows

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AutoML-Pipeline: A RAG-Enhanced Code Generation Framework With Pre-Validation for Cloud-Native Machine Learning Workflows
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AutoML-Pipeline: A RAG-Enhanced Code Generation Framework With Pre-Validation for Cloud-Native Machine Learning Workflows
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
