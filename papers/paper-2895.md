---
id: paper-2895
title: 'CORE: Toward Ubiquitous 6G Intelligence Through Collaborative Orchestration of Large Language Model Agents Over Hierarchical Edge'
authors:
- Yu, Zitong
- Sun, Boquan
- Li, Yang
- Qu, Zheyan
- Zhang, Xing
venue: IEEE Communications Magazine
venue_type: journal
year: 2026
doi: 10.1109/MCOM.001.2500469
url: https://www.scopus.com/pages/publications/105033393626?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Artificial intelligence
- Intelligent agents
- Mobile edge computing
- Optimization
- Collaborative learning systems
- Computing resource
- Distributed Artificial Intelligence
- Heterogeneous computing
- Hierarchical network
- Language model
- Model agents
- Reasoning tasks
- Seamless connectivity
- Ubiquitous intelligence
- Collaborative learning
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
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

# paper-2895 — CORE: Toward Ubiquitous 6G Intelligence Through Collaborative Orchestration of Large Language Model Agents Over Hierarchical Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Rapid advancements in sixth-generation (6G) networks and large language models (LLMs) have paved the way for ubiquitous intelligence, wherein seamless connectivity and distributed artificial intelligence (AI) have revolutionized various aspects of our lives. However, realizing this vision faces significant challenges owing to the fragmented and heterogeneous computing resources across hierarchical networks, which are insufficient for individual LLM agents to perform complex reasoning tasks. To address this issue, we propose Collaborative Orchestration Role at Edge (CORE), an innovative framework that employs a collaborative learning system in which multiple LLMs, each assigned a distinct functional role, are distributed across mobile devices and tiered edge servers. The system integrates three optimization modules, encompassing real-time perception, dynamic role orchestration, and pipeline-parallel execution, to facilitate efficient and rapid collaboration among distributed agents. Furthermore, we introduce a novel role affinity scheduling algorithm for dynamically orchestrating LLM role assignments across the hierarchical edge infrastructure, intelligently matching computational demands with available dispersed resources. Finally, comprehensive case studies and performance evaluations across various 6G application scenarios demonstrated the efficacy of CORE, revealing significant enhancements in the system efficiency and task completion rates. Building on these promising outcomes, we further validated the practical applicability of CORE by deploying it on a real-world edge-computing platform, that exhibits robust performance in operational environments. © 1979-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2895.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
