---
id: paper-1702
title: Deep Reinforcement Learning and Edge Computing for Multisatellite On-Orbit Task Scheduling
authors:
- Jiang, Qiangqiang
- Han, Peng
- Xin, Xu
- Chen, Kang
venue: IEEE Transactions on Aerospace and Electronic Systems
venue_type: journal
year: 2025
doi: 10.1109/TAES.2025.3583276
url: https://www.scopus.com/pages/publications/105009275986?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 14143--14159
keywords:
- Multiagent deep reinforcement learning (MADRL)
- multisatellite on-orbit computation
- satellite edge computing (SEC)
- task scheduling
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

# paper-1702 — Deep Reinforcement Learning and Edge Computing for Multisatellite On-Orbit Task Scheduling

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Today’s satellite applications often require the immediate processing of exploding data, which has driven a shift to on-orbit computing needs. Due to the limited onboard resources and energy supply, satellite edge computing is developed for intersatellite and satellite–ground collaborations. However, it is a challenge to achieve efficient multisatellite on-orbit computation considering the harsh satellite-to-ground transmission. Therefore, this article proposes an edge-computing-enabled multisatellite on-orbit computation scheduling (MSOCS) through multiagent deep reinforcement learning (MADRL). First, we formulate the MSOCS problem, where on-orbit computation tasks are described as a directed acyclic graph, and the intermittent satellite-to-ground link is established as connectable and disconnectable constraints. Second, a multiagent proximal policy optimization-based algorithm is developed by modeling the MSOCS problem via a partially observable Markov decision process. To cope with the dynamic change of observational input, we design a problem-specific embedding constructor, which is also utilized as the structural basis of the policy and value networks. Finally, practical remote sensing data processing missions are employed as the case study to conduct evaluation experiments. Simulation results validate the scheduling effectiveness of the proposed MSOCS algorithm in the test instances with different data scales, which surpasses other MADRL approaches. Moreover, our MSOCS improves the efficiency of on-orbit computation by 70.48% in time and 68.33% in energy, compared with the baseline without scheduling optimization. © 1965-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1702.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
