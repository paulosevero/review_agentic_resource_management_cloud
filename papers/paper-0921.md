---
id: paper-0921
title: Large-Scale Cooperative Task Offloading and Resource Allocation in Heterogeneous MEC Systems via Multiagent Reinforcement Learning
authors:
- Gao, Zhen
- Yang, Lei
- Dai, Yu
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3292387
url: https://www.scopus.com/pages/publications/85164391192?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2303--2321
keywords:
- Curriculum learning
- multiaccess edge computing (MEC)
- reinforcement learning (RL)
- resource allocation
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

# paper-0921 — Large-Scale Cooperative Task Offloading and Resource Allocation in Heterogeneous MEC Systems via Multiagent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In multiaccess edge computing (MEC) systems, existing task offloading methods have provided ultrashort latency services for heterogeneous tasks on mobile devices (MDs). Nevertheless, the complexity of MEC systems grows exponentially with the number of MDs or edge servers (ESs), so learning a good offloading policy is a huge challenge when the number of MDs or ESs is large. Moreover, MDs are often unable to find optimal ESs for offloading since the restricted ESs infrastructures and the spatiotemporally imbalanced task offloading requirements. To solve these problems, we propose a curriculum spatiotemporal multiagent actor-critic (CSTMAAC)-based task offloading method. Each ES is regarded as an agent and the problem is formulated as a multiobjective optimization task. To adapt to the large-scale MEC systems, we first introduce an evolutionary curriculum learning by gradually raising the number of trained ES agents in a phased way. Second, to facilitate the coordination of the offloading policies among geographically distributed ESs, we design an attention-based centralized critic-network. Besides, a delayed access mechanism is introduced that uses information about future task processing competition to capture the impact of potential future task processing contention and help ES agents obtain a better offloading strategy. Finally, critic-network is expanded to multicritics and a dynamic weight mechanism is designed to adaptively optimize multiobjectives and obtain a good balance for multiple objectives. Real-world data sets used in experiments demonstrate that CSTMAAC raises task completion rates and total utility by 13.01%-15.21% and 16.89%-18.32% compared with the existing algorithms.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0921.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
