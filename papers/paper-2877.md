---
id: paper-2877
title: Vehicle-Mounted Multi-UAV Cooperative Collection and Scheduling Mechanism for Multisource Heterogeneous Tasks
authors:
- Yan, Junjie
- Guo, Mengyao
- Liu, Jingxian
- Deng, Junyi
- Yuan, Haohao
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2025.3627329
url: https://www.scopus.com/pages/publications/105020718436?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1070--1084
keywords:
- Cooperative collection
- mobile edge computing (MEC)
- multiagent reinforcement learning (MARL)
- vehicle-mounted multi-UAV
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2877 — Vehicle-Mounted Multi-UAV Cooperative Collection and Scheduling Mechanism for Multisource Heterogeneous Tasks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the advancement of artificial intelligence (AI) technology, edge networks are progressively evolving toward intelligence, and mobile intelligent agents such as uncrewed aerial vehicles (UAVs) and unmanned ground vehicles (UGVs) are playing an increasingly vital role in this process. However, existing studies have addressed cooperation among homogeneous agents, such as multiple UAVs, without exploring collaboration between heterogeneous mobile intelligent agents. For this purpose, we propose a vehicle-mounted multi-UAV cooperative service system to collaboratively collect and process multisource heterogeneous Internet of Things (IoTs) tasks under strict latency and resource constraints. To address the complexities of heterogeneous task structures and dynamic collaboration, the article first introduces a multisource heterogeneous task scheduling mechanism, which optimizes task prioritization and resource allocation for efficient processing. In addition, a decentralized reinforcement learning approach based on partial reward decoupling (PRD) heterogeneous agent proximal policy optimization (PRD-HAPPO) is employed to enhance collaboration and trajectory planning between UAVs and vehicles. Simulation results demonstrate that the proposed framework significantly improves task completion efficiency, reduces system latency, and outperforms existing deep reinforcement learning (DRL) algorithms in terms of convergence and scalability. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2877.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
