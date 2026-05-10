---
id: "paper-2133"
title: "FlowXpert: Expertizing Troubleshooting Workflow Orchestration with Knowledge Base and Multi-Agent Coevolution"
authors: ["Shi, Binpeng", "Luo, Yu", "Wang, Jingya", "Zhao, Yongxin", "Zhang, Shenglin", "Hao, Bowen", "Zhao, Chenyu", "Sun, Yongqian", "Zhang, Zhi", "Sun, Ronghua", "Li, Haihua", "Song, Wei", "Chen, Xiaolong", "Miao, Jingbo", "Pei, Dan"]
year: 2025
venue: "Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining"
venue_type: "conference"
doi: "10.1145/3711896.3737221"
url: "https://www.scopus.com/pages/publications/105014319291?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "4839--4850"
keywords: ["incident management", "large language model", "troubleshooting", "workflow orchestration"]
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
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."

---

# paper-2133 — FlowXpert: Expertizing Troubleshooting Workflow Orchestration with Knowledge Base and Multi-Agent Coevolution

## Metadata

- **Authors:** Shi, Binpeng and Luo, Yu and Wang, Jingya and Zhao, Yongxin and Zhang, Shenglin and Hao, Bowen and Zhao, Chenyu and Sun, Yongqian and Zhang, Zhi and Sun, Ronghua and Li, Haihua and Song, Wei and Chen, Xiaolong and Miao, Jingbo and Pei, Dan
- **Year:** 2025
- **Venue:** Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining
- **DOI:** 10.1145/3711896.3737221
- **URL:** https://www.scopus.com/pages/publications/105014319291?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 4839--4850
- **Language:** English
- **Keywords:** incident management; large language model; troubleshooting; workflow orchestration

### Abstract

Incident management remains a critical yet challenging task for large-scale cloud services. Most cloud service providers abstract troubleshooting into predefined workflows for different incidents, offering step-by-step guidance. However, manually crafting workflows is resource-consuming and knowledge-intensive, hindering large-scale deployment. Most automated techniques for workflow orchestration rely on large language models (LLMs) to handle complex tasks but overlook key aspects of troubleshooting, including complex expertise, domain requirements, and the reliability of AI feedback. These limitations undermine workflow quality. Therefore, we propose FlowXpert, a novel framework for troubleshooting workflow orchestration. Leveraging LLMs, it first builds a knowledge base centered on incident-aware nodes to precisely depict expertise. Then, fed into AI feedback and synthetic preference data, reinforcement learning is applied to refine the workflow generator and evaluator. To assess troubleshooting workflows, we introduce OpsFlowBench based on Huawei Cloud's datacenter switch operation documents. Benchmark tests under the tailored STEPScore metric validate its effectiveness. Furthermore, during a 10-week deployment in Huawei Cloud's datacenter network, FlowXpert provided valuable support to both on-call engineers and AI executors, as evidenced by empirical data and case study. © 2025 ACM.

## 04 — Title Screening

**Title:** FlowXpert: Expertizing Troubleshooting Workflow Orchestration with Knowledge Base and Multi-Agent Coevolution

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** FlowXpert: Expertizing Troubleshooting Workflow Orchestration with Knowledge Base and Multi-Agent Coevolution
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** FlowXpert: Expertizing Troubleshooting Workflow Orchestration with Knowledge Base and Multi-Agent Coevolution
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
