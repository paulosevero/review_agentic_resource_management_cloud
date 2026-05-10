---
id: paper-0357
title: Multi-Agent Multi-Armed Bandit Learning for Online Management of Edge-Assisted Computing
authors:
- Wu, Bochun
- Chen, Tianyi
- Ni, Wei
- Wang, Xin
venue: IEEE Transactions on Communications
venue_type: journal
year: 2021
doi: 10.1109/TCOMM.2021.3113386
url: https://www.scopus.com/pages/publications/85115130315?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 8188--8199
keywords:
- Edge computing
- multi-agent multi-armed bandit (MA-MAB)
- upper confidence bound (UCB)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0357 — Multi-Agent Multi-Armed Bandit Learning for Online Management of Edge-Assisted Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> By orchestrating resources of edge and core network, the delays of edge-assisted computing can decrease. Offloading scheduling is challenging though, especially in the presence of many edge devices with randomly varying link and computing conditions. This paper presents a new online learning-based approach to the offloading scheduling, where multi-agent multi-armed bandit (MA-MAB) learning is designed to exploit the randomly varying conditions and asymptotically minimize the computing delay. We first propose a combinatorial bandit upper confidence bound (CB-UCB) algorithm, where users collectively feed back the observed delays of all edge devices and links. The optimistic bound of the delay is derived to facilitate centralized offloading scheduling for all users. In addition, we put forth a distributed bandit upper confidence bound (DB-UCB) algorithm, where users take random turns to make conflict-free, distributed selections of edge devices. The optimistic confidence bound of each user is developed to allow the user's selection only based on its own observations and decisions. Furthermore, we establish the asymptotic optimality of the proposed algorithms by proving the sublinearity of their regrets, and that the random turns the users take to make decisions do not compromise the asymptotic optimality of the DB-UCB algorithm, as corroborated by numerical simulations.  © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0357.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
