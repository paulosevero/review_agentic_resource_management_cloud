---
id: paper-0781
title: Learning-Based Privacy-Preserving Computation Offloading in Multi-Access Edge Computing
authors:
- You, Feiran
- Yuan, Xin
- Ni, Wei
- Jamalipour, Abbas
venue: Proceedings - IEEE Global Communications Conference, GLOBECOM
venue_type: conference
year: 2023
doi: 10.1109/GLOBECOM54140.2023.10437967
url: https://www.scopus.com/pages/publications/85187366298?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 922--927
keywords:
- game theory
- local differential privacy (LDP)
- Multi-access edge computing (MEC)
- multi-agent deep deterministic policy gradient (MADDPG)
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0781 — Learning-Based Privacy-Preserving Computation Offloading in Multi-Access Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As a technology intended to reduce cellular network congestion and enhance user service quality, computation offloading in Multi-access Edge Computing (MEC) networks highlights the crucial issue of privacy protection. This paper proposes a novel solution to the computation offloading and privacy protection problem in the MEC network using a Multi-agent Deep Deterministic Policy Gradient (MADDPG) framework. Our approach utilizes game theory to encourage computation offloading by modeling the interaction between cloudlets, Data Center Operator (DCO), and users as an auction game. We formulate the resource allocation and privacy protection as an auction game with multiple bidders and incomplete information and then use MADDPG to find an optimal solution. To ensure privacy protection, we design a Local Differential Privacy (LDP) method in the MADDPG algorithm. Theoretical analysis and simulation results demonstrate the effectiveness of our approach in satisfying differential privacy and converging to an equilibrium. The proposed solution holds significant promise in addressing the computation offloading and privacy protection challenges in MEC networks. © 2023 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0781.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
