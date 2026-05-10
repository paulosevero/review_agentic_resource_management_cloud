---
id: paper-0327
title: Sim-to-Real Transfer in Multi-agent Reinforcement Networking for Federated Edge Computing
authors:
- Pinyoanuntapong, Pinyarash
- Pothuneedi, Tagore
- Balakrishnan, Ravikumar
- Lee, Minwoo
- Chen, Chen
- Wang, Pu
venue: 6th ACM/IEEE Symposium on Edge Computing, SEC 2021
venue_type: conference
year: 2021
doi: 10.1145/3453142.3491419
url: https://www.scopus.com/pages/publications/85126179723?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 355--360
keywords:
- Edge Computing
- Federated learning
- Network Simulation
- Reinforcement Learning
- Transfer Learning
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
    my_justification: Out of scope
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

# paper-0327 — Sim-to-Real Transfer in Multi-agent Reinforcement Networking for Federated Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Federated Learning (FL) over wireless multi-hop edge computing networks, i.e., multi-hop FL, is a cost-effective distributed on-device deep learning paradigm. This paper presents FedEdge simulator, a high-fidelity Linux-based simulator, which enables fast prototyping, sim-to-real code, and knowledge transfer for multi-hop FL systems. FedEdge simulator is built on top of the hardware-oriented FedEdge experimental framework with a new extension of the realistic physical layer emulator. This emulator exploits trace-based channel modeling and dynamic link scheduling to minimize the reality gap between the simulator and the physical testbed. Our initial experiments demonstrate the high fidelity of the FedEdge simulator and its superior performance on sim-to-real knowledge transfer in reinforcement learning -optimized multi-hop FL.  © 2021 ACM.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0327.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
