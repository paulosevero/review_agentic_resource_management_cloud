---
id: "paper-2187"
title: "SmartIntent: A Serverless LLM -Oriented Architecture for Intent-Driven Building Automation"
authors: ["Sun, Shuyi", "Chen, Zhiyuan", "Shi, Dina", "Li, Chaofan", "Wu, Zhenghao", "Malazi, Hadi Tabatabaee"]
year: 2025
venue: "Proceedings - 2025 IEEE International Conference on Cloud Computing Technology and Science, CloudCom 2025"
venue_type: "conference"
doi: "10.1109/CloudCom67567.2025.11331438"
url: "https://www.scopus.com/pages/publications/105034656576?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Building automation", "Edge intelligence", "Event-driven architecture", "Intent-based systems", "Internet of things", "Large language models", "Real-time command interpretation", "Serverless computing", "Sustainable computing"]
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

# paper-2187 — SmartIntent: A Serverless LLM -Oriented Architecture for Intent-Driven Building Automation

## Metadata

- **Authors:** Sun, Shuyi and Chen, Zhiyuan and Shi, Dina and Li, Chaofan and Wu, Zhenghao and Malazi, Hadi Tabatabaee
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE International Conference on Cloud Computing Technology and Science, CloudCom 2025
- **DOI:** 10.1109/CloudCom67567.2025.11331438
- **URL:** https://www.scopus.com/pages/publications/105034656576?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Building automation; Edge intelligence; Event-driven architecture; Intent-based systems; Internet of things; Large language models; Real-time command interpretation; Serverless computing; Sustainable computing

### Abstract

Building automation is a representative AIoT-driven cyber-physical scenario, where intelligent systems interact with physical devices to manage lighting, climate, and appliances in real time. Traditional machine learning struggles with ambiguous, multilingual, and colloquial user inputs, limiting effectiveness in dynamic building environments. Recent advances in large language models (LLMs) enable more natural command interpretation, but high resource demands challenge their sustainable deployment on edge nodes. This paper proposes a serverless architecture based on event-driven microservices and container orchestration that dynamically manages the deployment, execution, and scaling of compact, fine-tuned LLMs across distributed edge nodes for building automation. We fine-tune compact LLMs with ambiguous and colloquial command examples to enhance robustness and enable context-aware deployment at the edge. Platform elasticity, enabled by Knative, allows rapid model adaptation without persistent resource allocation. We evaluate the system on a multilingual building automation dataset (Chinese, English, French) with ambiguous and colloquial commands, using an automated framework to assess interpretation and execution. Results show that the fine-tuned model outperforms the baseline Qwen-2.5-14B on five of six metrics and performs comparably on output format compliance. It also generalizes well across languages, although fuzzy instructions remain challenging. © 2025 IEEE.

## 04 — Title Screening

**Title:** SmartIntent: A Serverless LLM -Oriented Architecture for Intent-Driven Building Automation

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** SmartIntent: A Serverless LLM -Oriented Architecture for Intent-Driven Building Automation
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** SmartIntent: A Serverless LLM -Oriented Architecture for Intent-Driven Building Automation
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
