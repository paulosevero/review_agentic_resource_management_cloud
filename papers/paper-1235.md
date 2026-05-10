---
id: paper-1235
title: Deep Reinforcement Learning Based Secure Transmission for UAV-Assisted Mobile Edge Computing
authors:
- Vijayalakshmi, N.
- Gulati, Sagar
- Sujin, B. Ben
- Rao, B. Madhav
- Kumar, K. Kiran
venue: International Journal of Interactive Mobile Technologies
venue_type: journal
year: 2024
doi: 10.3991/ijim.v18i17.50729
url: https://www.scopus.com/pages/publications/85204727139?origin=resultslist
publisher: International Federation of Engineering Education Societies (IFEES)
pages: 154--169
keywords:
- deep reinforcement learning (DRL)
- mobile edge computing (MEC)
- secure transmission
- unmanned aerial vehicle (UAV) communication
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1235 — Deep Reinforcement Learning Based Secure Transmission for UAV-Assisted Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing computational demand for real-time mobile applications has led to the development of mobile edge computing (MEC), with support from unmanned aerial vehicles (UAVs), as a promising paradigm for constructing high-throughput line-of-sight links for ground users and pushing computational resources to network edges. Users can reduce processing latency and the load on their local computers by delegating tasks to the UAV in its role as an edge server. The coverage capacity of a single UAV is, however, very limited. Moreover, it will be easy to intercept the data that is transferred to the unmanned aerial vehicle. Thus, for UAV-assisted mobile edge computing, we proposed a transmission technique based on multi-agent deep reinforcement learning in this study. The recommended approach to maximize UAV deployment first applies the particle swarm optimization algorithm. Then, deep reinforcement learning is utilized to optimize the secure offloading to maximize the system utility and minimize the quantity of information eavesdropping, taking into consideration different user task types with diverse preferences for processing time and residual energy of computing equipment. The results of the simulation demonstrate that, in comparison to the single-agent strategy and the benchmark, the multi-agent approach can optimize offloading more successfully and produce higher system utility. © 2024 by the authors of this article.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1235.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
