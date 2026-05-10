---
id: paper-2202
title: Research on Integrated Sensing, Communication Resource Allocation, and Digital Twin Placement Based on Digital Twin in IoV
authors:
- Tang, Lun
- Wang, Asha
- Xia, Bingsen
- Tang, Yuanchun
- Chen, Qianbin
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3535767
url: https://www.scopus.com/pages/publications/85219679616?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17300--17315
keywords:
- Communication and computing
- deep reinforcement learning (DRL)
- digital twin (DT)
- integrated sensing
- Internet of Vehicle
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2202 — Research on Integrated Sensing, Communication Resource Allocation, and Digital Twin Placement Based on Digital Twin in IoV

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the challenges faced by vehicles using integrated sensing and communication (ISAC) devices in maintaining sensing quality while maximizing the timeliness of sensing information, as well as the allocation of limited edge computing resources when large amounts of sensing data are uploaded to edge servers (ESs), we propose an integrated sensing, communication resource allocation, and digital twin (DT) placement scheme based on DT in IoV. First, a frame structure with an adjustable ISAC slot ratio was designed. Under the constraints of sensing mutual information and uplink communication rate, the timeliness of sensed data is enhanced by minimizing the Age of Information (AoI) during data transmission. Second, a vehicle DT (VDT) placement cost model, incorporating both latency and energy consumption, was constructed. The optimal VDT placement strategy was derived by minimizing placement costs, leading to efficient allocation of edge computing resources. Furthermore, considering the impact of vehicle mobility on real-time interaction between vehicles and VDTs, a migration utility based on vehicle migration latency and migration energy consumption between edge nodes was designed. On this basis, a joint system utility maximization optimization model was established, integrating sensing data AoI utility, VDT placement cost, and migration utility. Due to the continuous and discrete variables in the optimization problem, we develop an algorithm based on multiagent deep reinforcement learning (MADRL) to solve the problem, called SCDTP-MPDQN. Simulation results demonstrate the superiority of the proposed scheme in enhancing sensing information utility and system utility. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2202.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
