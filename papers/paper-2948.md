---
id: paper-2948
title: Multi-Agent Deep Reinforcement Learning-Based Distributed Task Assignment in Multi-UAV Cooperative Edge Computing
authors:
- Zuo, Wendong
- Liao, Siteng
- Cui, Yangguang
- Liu, Tong
- Cai, Hui
- Wan, Shaohua
venue: IEEE Transactions on Cloud Computing
venue_type: journal
year: 2026
doi: 10.1109/TCC.2026.3668236
url: https://www.scopus.com/pages/publications/105031650676?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- deep reinforcement learning
- Edge computing
- multi-unmanned aerial vehicle cooperation
- task assignment
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2948 — Multi-Agent Deep Reinforcement Learning-Based Distributed Task Assignment in Multi-UAV Cooperative Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Leveraging flexible deployment and wide-area coverage, Unmanned Aerial Vehicles (UAVs) assisted edge computing (EC) extends computation capability to the network edge and has become a key paradigm for improving the quality of service in the Internet of Things. However, constrained by onboard resources, UAVs struggle to independently process massive heterogeneous tasks in real time. Existing studies mainly focus on cooperation between UAVs and ground devices or the cloud, while the coupled cooperative relationships among UAVs and the performance scalability in large-scale UAV networks remain insufficiently characterized. To this end, we propose a distributed task assignment framework for a multi-UAV cooperative EC system, where each UAV explicitly accounts for cooperation with other UAVs and, leveraging controllable mobility, assigns a portion of local tasks to other UAVs or base stations to minimize the long-term system-wide total latency. To address the resulting joint trajectory control and task assignment optimization problem, we first formulate it as a Markov decision process. We then propose a Multi-head self-Attention critic-assisted MADDPG (MA<sup>2</sup> DDPG) algorithm to train local online decision models for UAVs. Under the fully cooperative setting, we employ a centralized Critic to exploit global information and reduce parameter redundancy; concurrently, a multi-head self-attention mechanism is incorporated into the Critic to aggregate multi-UAV interaction information, delineate implicit cooperative dependencies, and alleviate the network input dimensionality curse arising from increasing UAV scale. Finally, extensive simulation experiments validate the effectiveness of the proposed method. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2948.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
