---
id: paper-0800
title: Cloud-Edge-Client Collaborative Learning in Digital Twin Empowered Mobile Networks
authors:
- Zhao, Lindong
- Ni, Shouxiang
- Wu, Dan
- Zhou, Liang
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2023
doi: 10.1109/JSAC.2023.3310060
url: https://www.scopus.com/pages/publications/85169677649?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3491--3503
keywords:
- data-driven resource allocation
- Digital twin
- human-robot collaboration
- privacy-enhanced federated learning
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

# paper-0800 — Cloud-Edge-Client Collaborative Learning in Digital Twin Empowered Mobile Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Digital twin (DT) has emerged as a key enabler for the intelligent-oriented evolution of mobile networks. With the rise of privacy concerns for enabling intelligent applications in DT-empowered mobile networks (DTMNs), federated learning has garnered wide attention due to its potential on breaking down data silos. However, the data privacy of federated learning is greatly threatened by emerging gradient leakage attacks, and the need for frequent knowledge exchange limits its training efficiency over resource-constrained DTMNs. To circumvent such dilemmas, this work first proposes a privacy-enhanced federated learning framework based on cloud-edge-client collaborations. Particularly, model splitting between clients and edge servers makes gradient leakage attacks computationally prohibitive, and cloud-side partial model aggregation provides hierarchical data utility. To improve the training efficiency of the proposed learning framework, we further establish its communication and computation cost models, and develop a DT-Assisted multi-Agent deep reinforcement learning-based resource scheduler for joint client association and channel assignment. Finally, as a case study of intelligent applications in DTMNs, a human-robot collaborative nursing task is designed to evaluate the practical performance of our proposed scheduler. Experimental results show its superiority in saving training costs and preserving learning accuracy.  © 1983-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0800.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
