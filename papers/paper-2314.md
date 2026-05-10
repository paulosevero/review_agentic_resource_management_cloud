---
id: paper-2314
title: Multi-Agent Collaboration for Workflow Task Offloading in End-Edge-Cloud Environments Using Deep Reinforcement Learning
authors:
- Xiao, Bohuai
- Yu, Chujia
- Chen, Xing
- Chen, Zheyi
- Min, Geyong
venue: IEEE Transactions on Parallel and Distributed Systems
venue_type: journal
year: 2025
doi: 10.1109/TPDS.2025.3606001
url: https://www.scopus.com/pages/publications/105015335353?origin=resultslist
publisher: IEEE Computer Society
pages: 2281--2296
keywords:
- computation offloading
- deep reinforcement learning
- End-edge-cloud computing
- workflow tasks
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

# paper-2314 — Multi-Agent Collaboration for Workflow Task Offloading in End-Edge-Cloud Environments Using Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Computation offloading utilizes powerful cloud and edge resources to process workflow applications offloaded from Mobile Devices (MDs), effectively alleviating the resource constraints of MDs. In end-edge-cloud environments, workflow applications typically exhibit complex task dependencies. Meanwhile, parallel tasks from multi-MDs result in an expansive solution space for offloading decisions. Therefore, determining optimal offloading plans for highly dynamic and complex end-edge-cloud environments presents significant challenges. The existing studies on offloading tasks for multi-MD workflows often adopt centralized decision-making methods, which suffer from prolonged decision time, high computational overhead, and inability to identify suitable offloading plans in large-scale scenarios. To address these challenges, we propose a Multi-agent Collaborative method for Workflow Task offloading in end-edge-cloud environments with the Actor-Critic algorithm called MCWT-AC. First, each MD is modeled as an agent and independently makes offloading decisions based on local information. Next, each MD’s workflow task offloading decision model is obtained through the Actor-Critic algorithm. At runtime, an effective workflow task offloading plan can be gradually developed through multi-agent collaboration. Extensive simulation results demonstrate that the MCWT-AC exhibits superior adaptability and scalability. Moreover, the MCWT-AC outperforms the state-of-art methods and can quickly achieve optimal/near-optimal performance. © 1990-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2314.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
