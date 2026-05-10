---
id: paper-0246
title: A Combinatorial Bandit Approach to UAV-aided Edge Computing
authors:
- Wu, Bochun
- Chen, Tianyi
- Wang, Xin
venue: Conference Record - Asilomar Conference on Signals, Systems and Computers
venue_type: conference
year: 2020
doi: 10.1109/IEEECONF51394.2020.9443306
url: https://www.scopus.com/pages/publications/85107742361?origin=resultslist
publisher: IEEE Computer Society
pages: 304--308
keywords:
- combinatorial multi-armed bandit
- edge-cloud coordination
- mobile edge computing
- task offloading
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

# paper-0246 — A Combinatorial Bandit Approach to UAV-aided Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The development of Internet of Things (IoT) leads to an exponential growth of computing demands. To meet the increasing demand of computation under limited resource, tasks at terminals are often offloaded to nearby mobile edge computing (MEC) nodes or remote cloud servers in order to reduce latency. It has been established that when serving as a small base station, an unmanned aerial vehicle (UAV) outperforms its terrestrial counterparts in many ways. We present in this paper a scenario, where a cluster of UAVs floating in the sky can serve multiple UEs as edge computing servers or edge relaying nodes. We aim to minimize the total delay of the offloaded tasks over time, subject to the unknown network states and the multi-agent matching conflicts. To this end, we formulate the multi-agent offloading allocation as a combinatorial multi-armed bandit (C-MAB) problem and propose an efficient algorithm. The algorithm achieves (i) an exploration/exploitation trade- off, (ii) an edge-cloud coordination, and (iii) an asymptotically optimal set of agent-action matching pairs. We prove that the proposed algorithm has a sublinear regret bound against the optimal benchmark with full a-priori knowledge. Numerical results demonstrate the merits of the proposed schemes. © 2020 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0246.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
