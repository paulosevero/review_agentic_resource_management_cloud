---
id: paper-1612
title: Personalized Mobility-Aware Caching Strategies in Multi-access Edge Computing
authors:
- Guo, Kunyin
- Zhao, Han
- Xia, Yunni
- Wan, Yunye
- Yang, Long
- Feng, Jiafeng
- Yu, Yang
- Zhang, Ke
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2025
doi: 10.1007/978-3-031-77072-2_6
url: https://www.scopus.com/pages/publications/85210251879?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 78--92
keywords:
- Cooperative caching
- Mobility-aware
- Multi-access edge computing
- Multi-agent deep reinforcement learning
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

# paper-1612 — Personalized Mobility-Aware Caching Strategies in Multi-access Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Although Multi-Access Edge Computing (MEC) has evolved into a key technology for provisioning mobility-oriented and delay-sensitive applications, the storage and computing power limitations of user-end MEC devices still present a significant challenge in guaranteeing low latency in content delivery. When the requested content is out of the caching scope of local devices, effectively caching user-requested content with low cost and high hit rate has become a widely acknowledged research hotspot. Traditional caching strategies inadequately address the challenges posed by mobility and runtime variations in content popularity. In this work, we propose a personalized mobility-aware caching method (MAPHC) that synthesizes a content suitability prediction algorithm (CSPA) for identifying the caching needs of edge servers and a multi-agent deep reinforcement learning model for dynamically adjusting user mobility-aware caching strategies. Simulation results clearly demonstrate that MAPHC outperforms its peers across multiple performance metrics. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2025.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1612.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
