---
id: paper-2843
title: Energy-efficient real-time workflow scheduling in edge–cloud environments based on multi-agent reinforcement learning
authors:
- Wen, Mengyao
- Ning, Xin
- Pu, Mengyang
- Liu, Cong
- Wang, Qingle
- Chen, Xiaomin
- Cheng, Long
venue: Applied Energy
venue_type: journal
year: 2026
doi: 10.1016/j.apenergy.2026.127866
url: https://www.scopus.com/pages/publications/105035672332?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Distributed computing
- Edge-cloud computing
- Energy consumption
- Multi-agent deep reinforcement learning
- Real-time scheduling
- Workflow scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2843 — Energy-efficient real-time workflow scheduling in edge–cloud environments based on multi-agent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the widespread deployment of Internet of Things devices, the complexity of resource-intensive workloads and the associated pressures on energy consumption are steadily increasing. This trend necessitates an efficient workflow scheduling mechanism between edge nodes and the central cloud to strike a dynamic balance between low latency and low energy consumption. Traditional heuristic or meta-heuristic-based scheduling methods struggle to address the challenges posed by dynamic environments and high computational complexity. To tackle these challenges, we propose MAES, a novel real-time workflow scheduling method based on Multi-Agent Deep Reinforcement Learning for edge-cloud collaborative computing environments. MAES adopts a multi-agent system architecture, where each virtual machine acts as an agent, optimizing workflow allocation through a collaborative approach of centralized training and decentralized execution. Experimental evaluations using real scientific workflows were conducted across different scenarios, including varying task numbers and types, workflow arrival intervals, edge-cloud VM ratios, and network jitter. Specifically, MAES reduces average latency and cost, while significantly lowering total system energy consumption, providing a highly energy-efficient solution for workflow scheduling in edge-cloud collaborative environments. © 2026 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2843.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
