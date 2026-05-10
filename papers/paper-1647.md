---
id: paper-1647
title: Reinforcement Learning-Driven Hybrid Precopy/Postcopy VM Migration for Energy-Efficient Data Centers
authors:
- Hidayat, Taufik
- Ramli, Kalamullah
- Harwahyu, Ruki
- Salman, Muhammad
- Surya Gunawan, Teddy
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3613235
url: https://www.scopus.com/pages/publications/105017307127?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 169521--169533
keywords:
- energy efficiency
- hybrid migration
- Reinforcement learning
- VM migration
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
    my_justification: RL
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

# paper-1647 — Reinforcement Learning-Driven Hybrid Precopy/Postcopy VM Migration for Energy-Efficient Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This study proposes the use of a hybrid precopy/postcopy virtual machine (VM) migration framework to aid an autonomous agent when making migration decisions to continuously optimize the balance among migration time, downtime, and energy consumption. The data center state and the resource load, including the CPU, memory, and network, are represented in the agent’s state space using a two-layer graph neural network (GNN), and the asynchronous advantage actor–critic (A3C) algorithm is employed to dynamically determine whether to continue the precopy phase or switch to postcopy and optimize the trade-off among the total migration time, downtime, and energy consumption while adhering to the service-level agreement (SLA) constraints. An adaptive host selection policy ensures that VMs are migrated only to underloaded machines, preventing overload and ensuring system stability. A simulation evaluation that employed the VM workload from the GWA-Bitbrains dataset revealed that this framework achieved a total migration time of 45.5 s, with 30.1 s spent on the precopy phase and 15.4 s spent on the postcopy phase, resulting in a downtime of 15.4 s. Compared with previous approaches, this result represents an decrease in total migration time of 12.5% from 52 s to 45.5 s; a 23% decrease in downtime from 20 s to 15.4 s; and a 4.4% increase in energy efficiency from 87% to 91.4%. The SLA compliance remained stable at 92.8%, affirming that the service quality was preserved. This study demonstrates the effectiveness of integrating GNN-based embeddings and A3C scheduling in terms of reducing downtime and energy usage while maintaining reliable service delivery in data centers. © 2013 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1647.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
