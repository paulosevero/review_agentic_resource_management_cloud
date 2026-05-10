---
id: paper-2741
title: 'Telescopic STAR-RIS-Aided Full-Duplex Task Offloading Towards Smart City: A Quantum Federated DRL Approach'
authors:
- Paul, Anal
- Singh, Keshav
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2026
doi: 10.1109/TCE.2026.3675560
url: https://www.scopus.com/pages/publications/105033622889?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 6G networks
- deep reinforcement learning
- federated learning
- full‑duplex
- multi‑access edge computing
- quantum computing
- smart city
- STAR‑RIS
- task offloading
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2741 — Telescopic STAR-RIS-Aided Full-Duplex Task Offloading Towards Smart City: A Quantum Federated DRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper targets low-latency edge intelligence for smart city services by proposing a telescopic simultaneously transmitting and reflecting RIS (T-STAR-RIS) and a privacy-preserving multi-agent quantum federated DRL (MA-QFDRL) framework. Each RIS element supports controllable vertical displacement in addition to amplitude/phase tuning, adding a spatial degree of freedom for joint BS–edge–RIS optimization.We consider a full-duplex distributed multi-access edge computing (DMEC) architecture for city-scale workloads (e.g., public-safety video analytics, AR guidance, and e-health telemetry), where tasks are partitioned across edge servers and the cloud under power, caching, computing, and QoS constraints. The resulting latency minimization is modeled as a high-dimensional Markov decision process problem and solved by MA-QFDRL, which integrates parameterized quantum circuits into a federated learning loop to enhance function approximation while preserving data locality. Simulations show stable training in the tested settings and convergence within the reported episode budget. Under blocked BS–UE links, the proposed T-STAR-RIS achieves up to 54.55% and on average 29.58% higher downlink sum rate than a conventional STAR-RIS, yielding marked reductions in end-to-end task latency. These results suggest T-STAR-RIS with MA-QFDRL as a scalable and privacy-preserving enabler for smart city edge services. © 1975-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2741.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
