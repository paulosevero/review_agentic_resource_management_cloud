---
id: paper-1555
title: Toward Energy Efficiency and Fairness in UAV-Based Task Offloading
authors:
- El-Emary, Mohamed
- Ranjha, Ali
- Naboulsi, Diala
- Stanica, Razvan
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3584645
url: https://www.scopus.com/pages/publications/105010109527?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 115178--115195
keywords:
- Mobile edge computing
- task offloading
- trajectory design
- unmanned aerial vehicle
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

# paper-1555 — Toward Energy Efficiency and Fairness in UAV-Based Task Offloading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rising demand for compute-intensive mobile applications challenges the limited energy and processing power of user equipment (UE). While Mobile Edge Computing (MEC) enables task offloading to nearby servers, deploying fixed MEC infrastructure is often impractical in settings like disaster zones or temporary high-density events. Furthermore, challenges such as high task delays, limited UE battery life, and unfair load distribution persist. To address these issues, we propose a system where Unmanned Aerial Vehicles (UAVs) serve as mobile relays between UEs and MEC servers. This results in a joint optimization framework combining 1) a Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm for UAV trajectory control to enhance service coverage and energy efficiency, with 2) a low-complexity task offloading algorithm for UEs. The framework is explicitly designed to minimize UE energy consumption while promoting fairness in task allocation and data rates. Simulations demonstrate that our approach significantly outperforms state-of-the-art benchmarks, reducing UE energy consumption by 25–30% and improving fairness indices by up to 90%. The proposed system proves scalable and robust, making it suitable for real-time deployment in resource-constrained environments with dynamic workloads. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1555.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
