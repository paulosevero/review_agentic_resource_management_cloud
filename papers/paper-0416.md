---
id: paper-0416
title: Multi-Agent Deep Reinforcement Learning in Flying Ad-Hoc Networks for Delay-Constrained Applications
authors:
- Grasso, Christian
- Raftopoulos, Raoul
- Schembra, Giovanni
venue: Procedia Computer Science
venue_type: conference
year: 2022
doi: 10.1016/j.procs.2022.07.011
url: https://www.scopus.com/pages/publications/85144594607?origin=resultslist
publisher: Elsevier B.V.
pages: 69--78
keywords:
- 6G
- Deep Reinforcement Learning
- Low-latency
- Network Slicing
- UAVs
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

# paper-0416 — Multi-Agent Deep Reinforcement Learning in Flying Ad-Hoc Networks for Delay-Constrained Applications

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the near future, 6G networks will be able to provide its users with heterogeneous tailored end-to-end network services for edge AI-powered applications. However, in many 6G use case scenarios there may not be structured network infrastructures. One of the most appealing solutions to meet this problem is to bring computing, networking and storage facilities on site by means of UAVs. The target of this paper is the definition of a management framework for Flying Ad-Hoc Networks (FANET) aimed at bringing edge computing to remote areas, guaranteeing low latency to ground devices with heterogeneous requirements in terms of mean latency. The proposed framework allows zero-touch management of different network slices realized by partitioning the Computing Elements (CE) installed on each UAV of the FANET and wireless links connecting them to each other. An Inter-Slice Orchestrator is in charge of deciding this resource partition, while an Intra-Slice Orchestrator manages horizontal offload among UAVs for each slice via Reinforcement Learning, in order to reduce end-to-end latency and delay jitter. © 2022 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0) Peer-review under responsibility of the Conference Program Chairs.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0416.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
