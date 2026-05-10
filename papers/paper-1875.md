---
id: paper-1875
title: Deep reinforcement learning-aided multi-step job scheduling in optical data center networks
authors:
- Liu, Che-Yu
- Chen, Xiaoliang
- Proietti, Roberto
- Zhu, Zuqing
- Yoo, S.J. Ben
venue: Journal of Optical Communications and Networking
venue_type: journal
year: 2025
doi: 10.1364/JOCN.562531
url: https://www.scopus.com/pages/publications/105011950181?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: D96 - D105
keywords:
- Data centers
- Deep learning
- Deep reinforcement learning
- Job shop scheduling
- Learning algorithms
- Multi agent systems
- Optical communication
- Scheduling algorithms
- Data center networks
- Distributed machine learning
- Jobs scheduling
- Joint optimization
- Multi dimensional
- Multisteps
- Novel applications
- Optical data
- Reinforcement learnings
- Simple++
- Bandwidth
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

# paper-1875 — Deep reinforcement learning-aided multi-step job scheduling in optical data center networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Orchestrating job scheduling and topology reconfiguration in optical data center networks (ODCNs) is essential for meeting the intensive communication demand of novel applications, such as distributed machine learning (ML) workloads. However, this task involves joint optimization of multi-dimensional resources that can barely be effectively addressed by simple rule-based policies. In this paper, we leverage the powerful state representation and self-learning capabilities from deep reinforcement learning (DRL) and propose a multi-step job schedule algorithm for ODCNs. Our design decomposes a job request into an ordered sequence of virtual machines (VMs) and the related bandwidth demand in between, and then makes a DRL agent learn how to place the VMs sequentially. To do so, we feed the agent with the global bandwidth and IT resource utilization state embedded with the previousVMallocation decisions in each step and reward the agent with both team and individual incentives. The team reward encourages the agent to jointly optimize the VM placement in multiple steps to pursue successful provisioning of the job request, while the individual reward favors advantageous local placement decisions, i.e., to prevent effective policies being overwhelmed by a few subpar decisions.We also introduce a penalty on reconfiguration to balance between performance gains and reconfiguration overheads. Simulation results under various ODCN configurations and job loads show our proposal outperforms the existing heuristic solutions and reduces the job-blocking probability and reconfiguration frequency by at least 7.35× and 4.59×, respectively.  © 2025 Optica Publishing Group.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1875.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
