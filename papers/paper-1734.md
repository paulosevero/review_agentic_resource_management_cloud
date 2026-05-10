---
id: paper-1734
title: Blockchain-Enabled Self-Autonomous Intelligent Transport System for Drone Task Workflow in Edge Cloud Networks
authors:
- Khuwuthyakorn, Pattaraporn
- Lakhan, Abdullah
- Majumdar, Arnab
- Thinnukool, Orawit
venue: Algorithms
venue_type: journal
year: 2025
doi: 10.3390/a18080530
url: https://www.scopus.com/pages/publications/105014354933?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- autonomous agent drone
- blockchain
- cost
- deep Q-learning network
- scheduling
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1734 — Blockchain-Enabled Self-Autonomous Intelligent Transport System for Drone Task Workflow in Edge Cloud Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, self-autonomous intelligent transportation applications such as drones and autonomous vehicles have seen rapid development and deployment across various countries. Within the domain of artificial intelligence, self-autonomous agents are defined as software entities capable of independently operating drones in an intelligent transport system (ITS) without human intervention. The integration of these agents into autonomous vehicles and their deployment across distributed cloud networks have increased significantly. These systems, which include drones, ground vehicles, and aircraft, are used to perform a wide range of tasks such as delivering passengers and packages within defined operational boundaries. Despite their growing utility, practical implementations face significant challenges stemming from the heterogeneity of network resources, as well as persistent issues related to security, privacy, and processing costs. To overcome these challenges, this study proposes a novel blockchain-enabled self-autonomous intelligent transport system designed for drone workflow applications. The proposed system architecture is based on a remote method invocation (RMI) client–server model and incorporates a serverless computing framework to manage processing costs. Termed the self-autonomous blockchain-enabled cost-efficient system (SBECES), the framework integrates a client and system agent mechanism governed by Q-learning and deep-learning-based policies. Furthermore, it incorporates a blockchain-based hash validation and fault-tolerant (HVFT) mechanism to ensure data integrity and operational reliability. A deep reinforcement learning (DRL)-enabled adaptive scheduler is utilized to manage drone workflow execution while meeting quality of service (QoS) constraints, including deadlines, cost-efficiency, and security. The overarching objective of this research is to minimize the total processing costs that comprise execution, communication, and security overheads, while maximizing operational rewards and ensuring the timely execution of drone-based tasks. Experimental results demonstrate that the proposed system achieves a 30% reduction in processing costs and a 29% improvement in security and privacy compared to existing state-of-the-art solutions. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1734.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
