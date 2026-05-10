---
id: paper-2424
title: Decentralized User Association and Resource Allocation for Mobile Edge Computing Network
authors:
- Zhang, Jie
- Sun, Kai
- Huang, Wei
- Wu, Jingmiao
- Zhang, Haijun
- Leung, Victor C.M.
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3637866
url: https://www.scopus.com/pages/publications/105023164837?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- game theory
- mobile edge computing (MEC)
- multi-agent multi-armed bandit (MAMAB)
- User association resource allocation (UARA)
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

# paper-2424 — Decentralized User Association and Resource Allocation for Mobile Edge Computing Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) has become a novel paradigm for addressing the resource management issues of densely coupled base stations (BSs) and edge servers (ESs), however, the randomness of communication links and the variability of resource demands from edge user equipments (EUEs) make the user association and resource allocation (UARA) problem in MEC networks more challenging. In this paper, we model the edge UARA problem as a potential game and introduce a weighted fairness Jain factor, which considers the pursuit of higher data rates by EUEs with different resource demands. The Nash Fairness-Upper Confidence Bound (NF-UCB) algorithm is proposed to guide EUEs in exploring and exploiting association strategies and achieving Nash equilibrium. The regret upper bound of NF-UCB is proven to be sublinear and simulation results show that NF-UCB outperforms other state-of-the-art multi-agent multi-armed bandit (MAMAB) and UARA algorithms in terms of throughput, fairness, and Nash equilibrium in both constant resource demand scenario and dynamic resource demand scenario. © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2424.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
