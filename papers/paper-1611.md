---
id: paper-1611
title: Multi-Agent DRL for Distributed Task Offloading in Energy Harvesting Enhanced Hierarchical MEC
authors:
- Guo, Chunyu
- Di, Boya
- Song, Lingyang
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2025
doi: 10.1109/VTC2025-Fall65116.2025.11309886
url: https://www.scopus.com/pages/publications/105032412178?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- deep reinforcement learning
- energy harvesting
- mobile edge computing
- Stackelberg game
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

# paper-1611 — Multi-Agent DRL for Distributed Task Offloading in Energy Harvesting Enhanced Hierarchical MEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of the Internet of Things (IoT), mobile edge computing (MEC) and energy harvesting (EH) technologies are applied to handle numerous computing-intensive and latency-sensitive IoT applications by offloading data to MEC servers as well as achieving sustainable operation. In this paper, we investigate a distributed EH-enhanced MEC system consisting of multiple MEC servers and user mobile devices (MDs). The MEC servers, as service providers, inherently control the price and availability of resources. MDs reactively optimize their task offloading and battery energy management strategies. Considering the hierarchical structure and large optimization dimension of MEC, a Stackelberg game-based bi-level multi-agent deep deterministic policy gradient (BL-MADDPG) algorithm is proposed which treats the MD and joint MEC servers as follower and leader, respectively. Different from the parallel decision of conventional multi-agent deep reinforcement learning, the BL-MADDPG algorithm establishes a two-stage decision process and can achieve an energy efficient offloading strategy by taking MDs' limited EH power into account. Simulation results are carried out to validate the effectiveness of the proposed scheme.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1611.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
