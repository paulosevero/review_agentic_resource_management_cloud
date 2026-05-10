---
id: paper-1482
title: QoS-Aware multi-agent DDPG for adaptive edge service distribution in intelligent wireless communication networks
authors:
- Chen, Shuang
- Li, Dong
- Mohajer, Amin
venue: Ain Shams Engineering Journal
venue_type: journal
year: 2025
doi: 10.1016/j.asej.2025.103543
url: https://www.scopus.com/pages/publications/105007969909?origin=resultslist
publisher: Ain Shams University
pages: ''
keywords:
- Dynamic multi-channel access
- Intelligent wireless control networks
- Mobile edge computing
- Multi-agent deep reinforcement learning
- Traffic prediction
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

# paper-1482 — QoS-Aware multi-agent DDPG for adaptive edge service distribution in intelligent wireless communication networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Effective service distribution management is essential in Intelligent Wireless Communication Networks to meet the increasing Quality of Service (QoS) demands across various applications. Traditional transmission strategies often prioritize high-QoS data, which can lead to access starvation for lower-priority data in resource-constrained environments. To address this, we propose a QoS-aware adaptive service distribution strategy that balances the needs of high- and low-priority data without compromising the performance of either. Leveraging enhanced Multi-Agent Deep Deterministic Policy Gradient (e-MADDPG), our solution dynamically optimizes service distribution in mobile edge networks. By employing a gated recurrent unit-enhanced reinforcement learning framework, we enable intelligent agents to collaboratively decide channel access based on real-time traffic conditions. The proposed multi-criteria Decision-based Multi-channel Access algorithm allows high-priority data to defer access if necessary, improving the completion rates of lower-priority data. Furthermore, our method integrates network slicing and computation offloading to enhance service adaptability, ensuring efficient use of edge resources. Simulation results confirm that our framework significantly outperforms existing approaches in terms of channel utilization, QoS adherence, and overall network efficiency. © 2025 The Authors

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1482.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
