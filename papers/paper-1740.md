---
id: paper-1740
title: IoT Integration With CMPA-PINN for Islanding Detection Through Microgrid Hierarchical Control
authors:
- Komala, C.R.
- Jeyakumar, S.
- Deepika, G.
- Swaroopa, K.
- Rangaree, Pankaj
- Arif, Mohammad
- Saikia, Bhargabjyoti
- BalaSubramanyam, P.N.V.
venue: International Journal of Communication Systems
venue_type: journal
year: 2025
doi: 10.1002/dac.6087
url: https://www.scopus.com/pages/publications/85216241847?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: ''
keywords:
- distributed generator
- energy management
- Internet of Things
- islanding detection
- microgrid
- system operator
- total harmonic distortion
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1740 — IoT Integration With CMPA-PINN for Islanding Detection Through Microgrid Hierarchical Control

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Internet of Things (IoT) and cloud computing are becoming increasingly important in the solution of many industrial problems. Effective management of microgrid (MG) requires a strong and scalable information and communication technology (ICT) infrastructure. IoT devices with effective measurement and control capabilities have the potential to be very important in the MG environment. MG was run in both grid-connected and island mode. This paper proposes to improve the MG hierarchical control with IoT using CMPA-PINN techniques for islanding detection. The proposed hybrid method is the joint execution of both the Coronavirus Mask Protection Algorithm (CMPA) and physics-informed neural networks (PINNs). Hence, it is named as CMPA-PINN approach. The major goal of this proposed method is to reduce the deviation of voltage, frequency, and total harmonic distortion (THD). The proposed CMPA is used to optimize the traffic flow over a communication network, and the PINNs are used to predict the optimized traffic flow. By then, the MATLAB platform has adopted the proposed method, and the current process is used to compute its execution. The proposed technique outperforms all current systems, including maximum power point tracking (MPPT), multi-agent reinforcement learning (MARL), and deep reinforcement learning (DRL). The proposed approach shows the THD is 2%, which is lower than other existing systems. © 2025 John Wiley & Sons Ltd.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1740.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
