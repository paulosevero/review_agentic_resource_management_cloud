---
id: paper-2510
title: 'Disaggregated Near-RT RIC for User-Centric RAN Management: A Multi-Agent Bandit Approach'
authors:
- Amrallah, Amr
- Murakami, Takahide
- Tsukamoto, Yu
- Konishi, Yohei
- Ikami, Akio
venue: Proceedings - IEEE Consumer Communications and Networking Conference, CCNC
venue_type: conference
year: 2026
doi: 10.1109/CCNC65079.2026.11366353
url: https://www.scopus.com/pages/publications/105034134811?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- mixed-integer nonlinear programming
- multi-armed bandit
- near-RT RIC
- user-centric RAN
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

# paper-2510 — Disaggregated Near-RT RIC for User-Centric RAN Management: A Multi-Agent Bandit Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> At-scale deployment of a disaggregated near-real-time radio access network (RAN) Intelligent Controller (near-RT RIC) remains challenging in user-centric RANs, given concurrent objectives of low control-latency and low deployment cost. The placement problem of disaggregated near-RT RIC is formulated as a mixed-integer nonlinear programming (MINLP) that jointly minimizes control-latency and deployment cost across cloud and edge computing nodes. To address the computational complexity and adapt to network dynamics, a multi-armed bandit (MAB) approach, specifically, cost-subsidy explore-then-commit (CSETC) policy, is leveraged to decouple the joint latency and cost objective into metric-specific policies for online placement under feasibility constraints. In simulations with 512 user equipment (UEs), the proposed CS-ETC-RIC algorithm achieves up to 67% and 55% lower total control-latency than the co-located near-RT RIC and the HG-RIC benchmarks, respectively, while activating fewer edge computing nodes and thereby lowering deployment cost. These findings indicate a scalable and effective mechanism for user-centric RAN management within the O-RAN ALLIANCE framework. © 2026 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2510.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
