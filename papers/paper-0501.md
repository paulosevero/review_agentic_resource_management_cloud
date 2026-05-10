---
id: paper-0501
title: Delay Minimization for NOMA-Enabled Mobile Edge Computing in Industrial Internet of Things
authors:
- Tuong, Van Dat
- Noh, Wonjong
- Cho, Sungrae
venue: IEEE Transactions on Industrial Informatics
venue_type: journal
year: 2022
doi: 10.1109/TII.2021.3117968
url: https://www.scopus.com/pages/publications/85119579780?origin=resultslist
publisher: IEEE Computer Society
pages: 7321--7331
keywords:
- Delay minimization
- industrial Internet of Things (IoT)
- mobile edge computing (MEC)
- nonorthogonal multiple access (NOMA)
- reinforcement learning
- resource allocation
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

# paper-0501 — Delay Minimization for NOMA-Enabled Mobile Edge Computing in Industrial Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing and nonorthogonal multiple access (NOMA) have been considered as promising technologies that can satisfy rigorous requirements of industrial Internet of Things systems. However, system dynamics, including channel states and computation task requests, may continuously change NOMA decoding order and computation uploading time, making it difficult to reduce latency using conventional highly complex optimization methods. In this article, we investigate a novel scheme that effectively reduces the average task delay to improve the quality of service for all users by jointly optimizing subchannel assignment (SA), offloading decision (OD), and computation resource allocation (CRA). To deal with the high complexity, the original multiserver problem is first decomposed into multiple single-server problems. Subsequently, each single-server problem is decoupled into CRA and SA/OD subproblems. Using convex optimization, a closed-form solution is derived for the optimal CRA action. Concurrently, the optimal SA/OD action is obtained using a distributed multiagent deep reinforcement learning algorithm. Simulation results reveal that the proposed scheme significantly outperforms the state-of-the-art schemes. In particular, it reduces the action decision duration by 30 times while achieving a near-optimal performance of up to 97% of the optimum under the exhaustive search scheme. © 2005-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0501.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
