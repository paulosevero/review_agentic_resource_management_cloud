---
id: paper-2714
title: On an Intelligent Collaborative Computation Strategy for Low Earth Orbit Satellite Edge Computing Networks
authors:
- Mao, Bomin
- Xia, Zhili
- Yin, Yingqi
- Zhang, Xuyan
- Cui, Mingshi
- Zhang, Rongqian
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3668721
url: https://www.scopus.com/pages/publications/105031728190?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- collaborative computation
- LEO satellite networks
- reinforcement learning
- resource optimization
- Software Defined Networking
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2714 — On an Intelligent Collaborative Computation Strategy for Low Earth Orbit Satellite Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the decreasing cost of satellite launch, Low Earth Orbit (LEO) satellite constellations have become an important part to complement the terrestrial communication systems for seamless coverage, limited latency, and high throughput. Meanwhile, the developing hardware computation capacity and Inter-Satellite Links (ISLs) have enabled LEO satellites to collaboratively conduct the onboard data processing, which is significantly important for the on-orbit Earth observation, environmental monitoring, and space exploration. However, the highly dynamic topology and heterogeneous resource distribution of LEO networks lead to traditional terrestrial scheduling mechanisms being ineffective. To address these challenges, this paper proposes a collaborative computation offloading framework based on the Software Defined Networking (SDN) technique for heterogeneous LEO satellite networks. The logically centralized controllers obtain global network states (e.g., satellite computing load and ISL conditions) to enable flexible-adaptive task scheduling. A Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm is proposed to decide the task splitting ratio, task processing satellites, and result aggregation satellite under dynamic network conditions. The simulation results demonstrate that the proposed MADDPG strategy significantly reduces the average task completion latency and improves the task success rate compared to benchmarks. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2714.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
