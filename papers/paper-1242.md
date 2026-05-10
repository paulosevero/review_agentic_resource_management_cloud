---
id: paper-1242
title: Distributed Trusted Demand Response Bidding Mechanism Empowered by Blockchain
authors:
- Wang, Lei
- Li, Tong
- Yang, Chao
- Chen, Jiang
- Liu, Yang
- Ren, Shuai
venue: Intelligent and Converged Networks
venue_type: journal
year: 2024
doi: 10.23919/ICN.2024.0013
url: https://www.scopus.com/pages/publications/85207078399?origin=resultslist
publisher: Tsinghua University Press
pages: 181--191
keywords:
- blockchain
- demand bidding
- demand response
- edge and cloud computing
- virtual resource management
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

# paper-1242 — Distributed Trusted Demand Response Bidding Mechanism Empowered by Blockchain

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the demand response process involving multi-agent participation, multiple parties' interests are involved and response execution status supervision is required. Traditional centralized demand response systems lack trust attributes. At the same time, traditional centralized cloud management can no longer support massive terminal services, resulting in delays in demand response services. We build a distributed trusted demand response architecture based on blockchain, illustrating the information interaction process in the demand bidding process and container-based edge-side heterogeneous resource management. We also propose a demand bidding algorithm that takes into account both the day-ahead market and the intraday market, aiming to maximize the aggregator's benefits. In addition, a virtual resource management algorithm to support demand response tasks is also proposed to optimize computing resource allocation and meet business latency requirements. Simulation results demonstrate that compared with only cloud computing or edge computing, the solution we proposed can reduce response delay by more than 39% for the sample system. Energy cost is saved by about 10.25% during container scheduling.  © 2020 Tsinghua University Press.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1242.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
