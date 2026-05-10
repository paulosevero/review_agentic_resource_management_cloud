---
id: paper-0235
title: A Lightweight Reinforcement-Learning-Based Mechanism for Bandwidth Provisioning on Multitenant Data Center
authors:
- Santos Filho, Reiner H.
- Ferreira, Tadeu N.
- Mattos, Diogo M. F.
- Medeiros, Dianne S. V.
venue: International Conference on Systems, Signals, and Image Processing
venue_type: conference
year: 2020
doi: 10.1109/IWSSIP48289.2020.9145174
url: https://www.scopus.com/pages/publications/85089141959?origin=resultslist
publisher: IEEE Computer Society
pages: 331--336
keywords:
- bandwidth provisioning
- data center
- markov decision process
- reinforcement learning
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-0235 — A Lightweight Reinforcement-Learning-Based Mechanism for Bandwidth Provisioning on Multitenant Data Center

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient management of cloud traffic leads to resource sharing among clients. To meet clients' performance restrictions, however, cloud providers adopt strict resource allocation that implies idle resources as clients' bandwidth thresholds are over-provisioned. We propose a dynamic mechanism to provide resources on-demand in a multitenant data center. The mechanism relies on Q-learning multi-agent for managing each client access to the cloud resources. The proposed mechanism either measure the throughput continuously or map the CPU usage into bandwidth usage. We assess our mechanism in an emulated environment, in which a network controller provisions bandwidth. Results show that the mechanism reduces cloud idleness, allowing low-priority clients to use bandwidth while there is idle capacity. Our mechanism incurs low processing overhead, even when the number of states and action space grow, while the memory cost per agent increases, peaking at 300 kB for 200 states and actions. When mapping CPU usage into bandwidth usage, the mechanism achieves fair bandwidth sharing at the cost of small increase on the convergence time to an optimal policy. © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0235.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
