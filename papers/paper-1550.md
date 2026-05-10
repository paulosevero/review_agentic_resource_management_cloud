---
id: paper-1550
title: Decentralized LSTM-Enhanced MADDPG Framework for Vehicular Edge Computing
authors:
- Dulout, Romain
- Mendiboure, Leo
- Pousset, Yannis
- Deniau, Virginie
- Sylla, Tidiane
venue: IEEE International Symposium on Personal, Indoor and Mobile Radio Communications, PIMRC
venue_type: conference
year: 2025
doi: 10.1109/PIMRC62392.2025.11274952
url: https://www.scopus.com/pages/publications/105030541537?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AI
- Energy Efficiency
- MADRL
- MEC
- NOMA
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1550 — Decentralized LSTM-Enhanced MADDPG Framework for Vehicular Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In today's intelligent transportation systems, emerging vehicular applications, such as multi-vehicle data fusion, platoon management, and high-definition video processing, demand a new generation of communication architectures to meet stringent processing and latency requirements. NOMA-based Vehicular Edge Computing (VEC) architectures have gained prominence as a solution, offering efficient spectrum reuse and reduced processing delays by leveraging distributed edge resources. While decentralized management of these architectures promises real-time, adaptive task offloading, existing approaches are limited by their reliance on local observations and insufficient integration of comprehensive global network state information. To address these challenges, we propose ROLAM, a novel framework that fuses LSTM-based state estimation with Multi-Agent Deep Deterministic Policy Gradient (MADDPG) to optimize resource allocation under dynamic conditions. Our evaluation demonstrates that ROLAM significantly improves energy efficiency and overall system performance, underscoring its potential to robustly meet the evolving needs of next-generation vehicular applications.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1550.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
