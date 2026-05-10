---
id: paper-0896
title: UAV-aided distribution line inspection using double-layer offloading mechanism
authors:
- Duo, Chunhong
- Li, Yongqian
- Gong, Wenwen
- Li, Baogang
- Qi, Guoliang
- Zhang, Ji
venue: IET Generation, Transmission and Distribution
venue_type: journal
year: 2024
doi: 10.1049/gtd2.13207
url: https://www.scopus.com/pages/publications/85196674279?origin=resultslist
publisher: John Wiley and Sons Inc
pages: 2353--2372
keywords:
- artificial intelligence
- computational intelligence
- decision making
- Markov processes
- power distribution lines
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

# paper-0896 — UAV-aided distribution line inspection using double-layer offloading mechanism

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the continuous growth of electricity demand, the safe and stable operation of distribution lines is crucial for power transportation. Unmanned aerial vehicle (UAV) inspection has been widely used for the maintenance and repair of distribution lines. Due to the limitations of computational power and endurance, it is difficult for UAVs to independently complete data processing. Combined with mobile edge computing (MEC), this paper proposes a computing offloading strategy based on multi-agent reinforcement learning and double-layer offloading mechanism, which can further utilize the computing power of non-task devices and edge servers. Firstly, three-layer system architecture, named MEC-U-NTDC (MEC-UAV-Non-task Device Cloud), is built. Secondly, double-layer offloading mechanism is designed to comprehensively utilize the computing power of edge servers and neighbouring non-task devices. Finally, a multi-agent algorithm DLMQMIX is proposed to minimize the total cost for UAV inspection. Simulation experiments show that the proposed algorithm can effectively solve the task offloading problem of UAV-aided distribution line inspection, and compared with algorithms such as PSO, GA, and QMIX, it performs better in terms of average delay, system cost, and load balancing, achieving a smaller total system cost. © 2024 The Author(s). IET Generation, Transmission & Distribution published by John Wiley & Sons Ltd on behalf of The Institution of Engineering and Technology.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0896.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
