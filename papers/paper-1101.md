---
id: paper-1101
title: Age of Information Minimization in Hierarchical Aerial Networks via MADDPG Approach
authors:
- Nguyen, Tri-Hai
- Nguyen, Truong Khang
- Bui, Minh-Phung
- Nguyen, Tuan-Duc
- Bao, Vo Nguyen Quoc
- Lakew, Demeke Shumeye
venue: Lecture Notes on Data Engineering and Communications Technologies
venue_type: book-chapter
year: 2024
doi: 10.1007/978-3-031-75593-4_34
url: https://www.scopus.com/pages/publications/85214015246?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 375--384
keywords:
- Aerial Computing
- Age of Information
- DRL
- MADDPG
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1101 — Age of Information Minimization in Hierarchical Aerial Networks via MADDPG Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This work introduces a hierarchical aerial computing system designed to minimize the Age of Information (AoI) for ground devices. The system utilizes a high-altitude platform in conjunction with multiple unmanned aerial vehicles to provide edge computing capabilities. Non-orthogonal multiple access is employed for uplink communication to improve efficiency. To achieve minimal average AoI, a multi-agent deep deterministic policy gradient (MADDPG)-based approach is proposed. This approach optimizes the trajectories of the aerial vehicles, their transmit power, and the allocation of computing resources. Simulation results validate the feasibility of the proposed system. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2024.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1101.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
