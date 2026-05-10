---
id: paper-0220
title: A Driver-Centric Vehicle Reposition Framework via Multi-agent Reinforcement Learning
authors:
- Liu, Chenxi
- Deng, Mingyu
- Chen, Chao
- Xiang, Chaocan
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2020
doi: 10.1007/978-3-030-64243-3_17
url: https://www.scopus.com/pages/publications/85097834464?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 217--230
keywords:
- Deep reinforcement learning
- Multi-agent reinforcement learning
- Vehicle reposition
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

# paper-0220 — A Driver-Centric Vehicle Reposition Framework via Multi-agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The e-hailing platforms have transformed the way people travel, live, and socialize. The efficiency of the platform is substantially influenced by the distribution differences between demands and supplies in the city. Therefore, an appropriate reposition vehicle strategy can significantly balance this distribution difference, which will promote platform benefits, customer goodwill and greatly alleviate traffic congestions. Due to the complicated relationship between vehicles and the temporal correlation of reposition actions, it is a challenging task to reposition vehicles in the city. Existing studies mostly focus on individual drivers that can hardly capture the relationship between drivers and long-term variations of demands and supplies in the city. In this paper, we introduce the reinforcement learning with geographic information and propose a geographic-based multi-agent deep deterministic policy gradient algorithm (gbMADDPG). The algorithm is driver-centric which takes the passenger searching time as an optimization goal to reduce the idle time of vehicles. We will demonstrate the effectiveness of our proposed algorithm framework through simulation experiments based on real data. © 2020, Springer Nature Switzerland AG.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0220.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
