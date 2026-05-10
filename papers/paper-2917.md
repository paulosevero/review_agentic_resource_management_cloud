---
id: paper-2917
title: Physical System-Constrained Transactive Bidding Strategy for Data Centers with Workload Flexibility in Electricity Markets
authors:
- Zhang, Ke
- Wang, Xu
- Jiang, Chuanwen
- Dong, Yahan
- Shahidehpour, Mohammad
- Wang, Chongyu
venue: IEEE Transactions on Industry Applications
venue_type: journal
year: 2026
doi: 10.1109/TIA.2026.3654487
url: https://www.scopus.com/pages/publications/105028041541?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- bidding strategy
- cluster algorithm
- data center
- power flexibility
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2917 — Physical System-Constrained Transactive Bidding Strategy for Data Centers with Workload Flexibility in Electricity Markets

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The workload flexibility in data centers remains underutilized in electricity markets, limiting their market-driven adaptability and overlooking dynamic market conditions. To address this challenge, we propose a physical system-constrained transactive bidding method for data centers to leverage market-driven flexibility of workload. First, we construct the energy model of data centers considering virtual machine multiplexing and support infrastructure constraints. Second, the market-driven flexibility of computational jobs is analyzed based on market requirements for classification and clustering. To reduce the computational burden of spectral clustering, we replace the intensive eigen-decomposition step with a lightweight orthogonal iteration method, enhancing scalability for large-scale datasets in data centers. Finally, the physical system models are integrated into the modified multi-agent deep deterministic policy gradient (MADDPG) method to ensure the inclusion of operation constraints and the optimal transactive bidding strategy. Numerical tests validate that the proposed method enables data centers to achieve higher profits across various ancillary markets while significantly improving computational speed. © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2917.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
