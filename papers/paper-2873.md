---
id: paper-2873
title: Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits
authors:
- Yahya, Mariam
- Sezgin, Aydin
- Maghsudi, Setareh
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3670034
url: https://www.scopus.com/pages/publications/105032419744?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Best arm identification (BAI)
- collaborative learning
- linear bandits
- multi -access edge computing (MEC)
- service placement
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2873 — Service Placement in Small Cell Networks Using Distributed Best Arm Identification in Linear Bandits

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As users in small cell networks increasingly rely on computation-intensive services, cloud-based access often results in high latency. Multi-access edge computing (MEC) mitigates this by bringing computational resources closer to end users, with small base stations (SBSs) serving as edge servers to enable low-latency service delivery. However, limited edge capacity makes it challenging to decide which services to deploy locally versus in the cloud, especially under unknown service demand and dynamic network conditions. To tackle this problem, we model service demand as a linear function of service attributes and formulate the service placement task as a linear bandit problem, where SBSs act as agents and services as arms. The goal is to identify the service that, when placed at the edge, offers the greatest reduction in total user delay compared to cloud deployment. We propose a distributed and adaptive multi-agent best-arm identification (BAI) algorithm under a fixed-confidence setting, where SBSs collaborate to accelerate learning. Simulations show that our algorithm identifies the optimal service with the desired confidence and achieves near-optimal speedup, as the number of learning rounds decreases proportionally with the number of SBSs. We also provide theoretical analysis of the algorithm's sample complexity and communication overhead. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2873.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
