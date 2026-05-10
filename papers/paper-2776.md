---
id: paper-2776
title: Optimized load balancing with task priority for reliable data management in IoT-Fog-enabled healthcare systems
authors:
- Shrawankar, Urmila
- Kokate, Shatakshi
- Jadhav, Amolkumar
venue: Information Security Journal
venue_type: journal
year: 2026
doi: 10.1080/19393555.2026.2620424
url: https://www.scopus.com/pages/publications/105028411741?origin=resultslist
publisher: Taylor and Francis Ltd.
pages: ''
keywords:
- Fog computing
- IoT
- load balancing
- PBDRA
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2776 — Optimized load balancing with task priority for reliable data management in IoT-Fog-enabled healthcare systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid proliferation of IoT devices has led to massive data generation, often resulting in delays and network congestion when relying solely on cloud-based processing. Fog computing offers a promising alternative by enabling computation closer to data sources, yet overloaded fog nodes remain a significant challenge. To address this, we propose a Priority-Based Dynamic Load Balancing (PBDLB) algorithm that leverages task criticality for efficient distribution across fog nodes. Tasks are classified into high-priority (urgent/critical) and low-priority (non-critical) categories, ensuring that time-sensitive operations receive immediate processing. Unlike traditional equal-weight models, the proposed approach incorporates dynamic resource weighting (CPU, memory, and bandwidth) to better reflect real-world workloads. Experimental results demonstrate that PBDLB achieves up to 95% resource utilization and reduces latency by 17–32% compared to state-of-the-art baselines such as Deep Reinforcement Learning-based Scheduler (DRLIS) and Multi-Agent Reinforcement Learning (MARL). These improvements highlight the scalability and reliability of PBDLB, making it particularly effective for critical IoT domains such as healthcare, agriculture, education, and smart cities. © 2026 Taylor & Francis Group, LLC.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2776.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
