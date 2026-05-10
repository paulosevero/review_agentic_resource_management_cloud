---
id: paper-1580
title: LE-MHAPPO-Enhanced DNN Task Partitioning in Energy-Harvesting Heterogeneous UAV Swarms
authors:
- Gao, Ke
- Du, Jun
- Jiang, Chunxiao
- Mishra, Debashisha
- Zhang, Chao
- Debbah, Merouane
venue: IEEE International Conference on Communications
venue_type: conference
year: 2025
doi: 10.1109/ICC52391.2025.11162059
url: https://www.scopus.com/pages/publications/105018457763?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1280--1285
keywords:
- Antennas
- Behavioral research
- Data acquisition
- Data handling
- Decision theory
- Deep neural networks
- Distributed computer systems
- Energy harvesting
- Internet of things
- Markov processes
- Swarm intelligence
- Unmanned aerial vehicles (UAV)
- Aerial vehicle
- Computing system
- Delay-sensitive applications
- Edge computing
- Emergency response
- Energy
- Multi agent
- Neural-networks
- Policy optimization
- Task partitioning
- Long short-term memory
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

# paper-1580 — LE-MHAPPO-Enhanced DNN Task Partitioning in Energy-Harvesting Heterogeneous UAV Swarms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, multi-Unmanned Aerial Vehicle (UAV) swarms have been extensively deployed as mobile edge computing (MEC) systems to support delay-sensitive applications in emergency response, often integrated within Internet of Things (IoT) networks to enhance data collection and processing capabilities. Deep neural network (DNN) partition-assisted collaborative inference has garnered significant attention due to its ability to mitigate the computing and energy limitations of individual UAVs. However, most studies on UAV collaborative inference overlook the challenges posed by high-speed and unpredictable topology changes within UAV swarms. These dynamics require UAVs to make effective action decisions for future time periods based on current conditions. To tackle this issue, we formulate the multi-dimensional action decision problem of DNN partitioning in highly dynamic and energy-harvesting heterogeneous UAV swarms as a predictive Markov decision process (P-MDP) framework. By leveraging the long short-term memory (LSTM)-enhanced multi-agent hybrid action proximal policy optimization (LE-MHAPPO) algorithm, each UAV predicts hybrid action decisions using centralized training and distributed execution (CTDE). The simulation results demonstrate that the proposed algorithm lowers the weighted sum of task delay and energy consumption by 13.8% compared to the state-of-the-art MHAPPO. Furthermore, its performance degradation over time is only 27.7% of that observed in the baseline.  © 2025 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1580.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
