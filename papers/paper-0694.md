---
id: paper-0694
title: Joint Optimization and Scheduling of Computing and Caching Resource for Blockchain-Empowered IoT via CDRL Approach
authors:
- Pei, Pan
- Li, Meng
- Huang, Yudian
- Yang, Ruizhe
- Sun, Yanhua
- Wang, Zhuwei
venue: ICICN 2023 - 2023 IEEE 11th International Conference on Information, Communication and Networks
venue_type: conference
year: 2023
doi: 10.1109/ICICN59530.2023.10393482
url: https://www.scopus.com/pages/publications/85184996788?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 43--49
keywords:
- blockchain
- collective deep reinforcement learning
- edge computing and caching
- Internet of Things
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0694 — Joint Optimization and Scheduling of Computing and Caching Resource for Blockchain-Empowered IoT via CDRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, the rise of the virtual reality (VR) and augmented reality (AR) application has led the significant evolution of smart Internet of Things (IoT). To improve the transmission efficiency and system overheads for IoT system, edge computing and caching have been treated as a prospective technology. However, there are some inevitable issues need to be emphasized such as limited computing and caching resources, as well as centralized learning and training by agents for resource allocation. In order to tackle above issues, in this article, based on deep reinforcement learning (DRL), we propose and introduce a novel collective and intelligent optimization algorithm - collective deep reinforcement learning (CDRL). Through collective learning and training by multi-agents, it can avoid excessive consumption of energy resources, and realize intelligent resource allocation. Moreover, blockchain technology is viewed to guarantee the security of shared data for the cloud-edge-end collaborative IoT network. optimized design for the offloading decision of computation tasks of VR device and the consensus task of blockchain, as well as caching decision, the computing overheads and energy consumption aim to be minimized. Then, we design the formulated problem as a Markov decision process, the optimal scheduling and policies can be achieved based on the CDRL. Simulation results reveal that the proposed scheme outperforms other existing schemes. © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0694.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
