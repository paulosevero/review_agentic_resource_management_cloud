---
id: paper-1538
title: 'Log-Scale Quantization in Distributed First-Order Methods: Gradient-Based Learning From Distributed Data'
authors:
- Doostmohammadian, Mohammadreza
- Qureshi, Muhammad I.
- Hossein Khalesi, Mohammad
- Rabiee, Hamid R.
- Khan, Usman A.
venue: IEEE Transactions on Automation Science and Engineering
venue_type: journal
year: 2025
doi: 10.1109/TASE.2025.3526967
url: https://www.scopus.com/pages/publications/105003042085?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10948--10959
keywords:
- data classification
- Distributed algorithm
- graph theory
- optimization
- quantization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1538 — Log-Scale Quantization in Distributed First-Order Methods: Gradient-Based Learning From Distributed Data

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Decentralized strategies are of interest for learning from large-scale data over networks. This paper studies learning over a network of geographically distributed nodes/agents subject to quantization. Each node possesses a private local cost function, collectively contributing to a global cost function, which the considered methodology aims to minimize. In contrast to many existing papers, the information exchange among nodes is log-quantized to address limited network-bandwidth in practical situations. We consider a first-order computationally efficient distributed optimization algorithm (with no extra inner consensus loop) that leverages node-level gradient correction based on local data and network-level gradient aggregation only over nearby nodes. This method only requires balanced networks with no need for stochastic weight design. It can handle log-scale quantized data exchange over possibly time-varying and switching network setups. We study convergence over both structured networks (for example, training over data-centers) and ad-hoc multi-agent networks (for example, training over dynamic robotic networks). Through experimental validation, we show that (i) structured networks generally result in a smaller optimality gap, and (ii) log-scale quantization leads to a smaller optimality gap compared to uniform quantization. © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1538.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
