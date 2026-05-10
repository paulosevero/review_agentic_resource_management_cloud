---
id: paper-2517
title: 'CarbonWise CX: An Agentic AI Framework for Carbon-Aware Customer Support Analytics Using RAG and LLM-Based Code Generation'
authors:
- Beena, B.M.
- Manideep, Thotapalli Sri Surya
- Saragadam, Sneha
- Rathi, Sailesh
- Ramesh, Ramaswamy
- Holimath, Vijay
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2026.3681110
url: https://www.scopus.com/pages/publications/105035303230?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 53442--53460
keywords:
- Agentic AI
- carbon-aware routing
- carbon-aware workload scheduling
- cloud-native systems
- customer experience analytics
- enterprise analytics
- green cloud computing
- large language models (LLMs)
- retrieval-augmented generation (RAG)
- sustainable AI
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2517 — CarbonWise CX: An Agentic AI Framework for Carbon-Aware Customer Support Analytics Using RAG and LLM-Based Code Generation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Organizations accumulate sufficient amounts of structured and unstructured customer support data, but current systems like SQL queries and fixed dashboards still generate actionable insights on a delay, increasing operational expenses, and inefficient use of cloud energies. This project aims at developing a cloud-native, agentic AI-driven analytics system that can be used to improve the decision-making processes of enterprises without violating the principles of green cloud computing. The proposed system is called CarbonWise CX, which incorporates Retrieval-Augmented Generation (RAG) to perform qualitative reasoning, the dynamic generation of Python code, which entails the use of LLM when making quantitative decisions, and cloud-deployed versions that are scalable. The queries in natural language are handled via, agentic decision layer that automatically identifies which analytics workflow to choose. One of such innovations is the carbon-conscious cloud routing, the dynamic choice of the execution areas according to the current carbon intensity, with maintained latency and SLA limitations. The system with a deployed infrastructure on AWS EC2 will exhibit a 34.6 percent reduction in the number of carbon emissions per query in the operation using a modular architecture and on multi-region workloads simulated in the BAR. Also, 8,469 actual customer support records were analyzed resulting in 62.3 percent less manual tasks and 41.8 percent faster query response time than traditional workflows. The results of CarbonWise CX yield to achieve a better SLA compliance (29.5% of the significant improvement), to optimize cloud resource usage (36.7% of the significant improvement), and to minimize the work of the analyst (they were decreased significantly). The architecture shows how agentic AI and green cloud computing can provide intelligent and scalable, as well as environmentally friendly customer experience analytics. The article corresponds to the United Nations Sustainable Development Goals SDG 12 (Responsible Consumption and Production), SDG 13 (Climate Action).  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2517.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
