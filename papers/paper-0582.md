---
id: paper-0582
title: Quantum Particle Swarm Optimization for Task Offloading in Mobile Edge Computing
authors:
- Dong, Shi
- Xia, Yuanjun
- Kamruzzaman, Joarder
venue: IEEE Transactions on Industrial Informatics
venue_type: journal
year: 2023
doi: 10.1109/TII.2022.3225313
url: https://www.scopus.com/pages/publications/85144080257?origin=resultslist
publisher: IEEE Computer Society
pages: 9113--9122
keywords:
- Mobile edge computing (MEC)
- particle swarm optimization (PSO)
- quantum PSO (QPSO)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: PSO
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

# paper-0582 — Quantum Particle Swarm Optimization for Task Offloading in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) deploys servers on the edge of the mobile network to reduce the data transmission delay between servers and mobile devices, and can meet the computing demand of mobile computing tasks. It alleviates the problem of computing power and delay requirements of mobile computing tasks and reduces the energy consumption of mobile devices. However, the MEC server has limited computing and storage resources and mobile network bandwidth, making it impossible to offload all mobile computing tasks to MEC servers for processing. Therefore, MEC needs to reasonably offload and schedule mobile computing tasks, to achieve efficient utilization of server resources. To solve the above-mentioned problems, in this article, the task offloading problem is formulated as an optimization problem, and particle swarm optimization (PSO) and quantum PSO based task offloading strategies are proposed. Extensive simulation results show that the proposed algorithm can significantly reduce the system energy consumption, task completion time, and running time compared with recent advanced strategies, namely ant colony optimization, multiagent deep deterministic policy gradients, deep meta reinforcement learning-based offloading, iterative proximal algorithm, and parallel random forest. © 2005-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "PSO"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0582.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
