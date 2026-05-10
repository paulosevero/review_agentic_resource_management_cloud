---
id: paper-0592
title: Large-Scale Computation Offloading Using a Multi-Agent Reinforcement Learning in Heterogeneous Multi-Access Edge Computing
authors:
- Gao, Zhen
- Yang, Lei
- Dai, Yu
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2023
doi: 10.1109/TMC.2022.3141080
url: https://www.scopus.com/pages/publications/85122867172?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3425--3443
keywords:
- attention mechanism
- Large-scale computation offloading
- multi-access edge computing
- multi-agent reinforcement learning (MARL)
- recurrent multi-agent actor-critic
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

# paper-0592 — Large-Scale Computation Offloading Using a Multi-Agent Reinforcement Learning in Heterogeneous Multi-Access Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, existing computation offloading methods have provided extremely low service latency for mobile users (MUs) in multi-access edge computing (MEC). However, this remains a challenge in large-scale mixed cooperative-competitive MUs heterogeneous MEC environments. Moreover, existing methods focus more on all offloaded tasks handled by static resource allocation MEC servers (ESs) within a time interval, ignoring on-demand requirements of heterogeneous tasks, resulting in many tasks being dropped or wasting resources, especially for latency-sensitive tasks. To address these issues, we present a decentralized computation offloading solution based on the Attention-weighted Recurrent Multi-Agent Actor-Critic (ARMAAC). First, we design a recurrent actor-critic framework to assist MU agents in remembering historical resource allocation information of ESs to better understand the future state of ESs, especially in dynamic resource allocation. Second, an attention mechanism is introduced to compress the joint observation space dimension of all MUs agent to adapt to large-scale MUs. Finally, the actor-critic framework with double centralized critics and Dueling network is redesigned considering the instability and convergence difficulties caused by the sensitive relationship between the actor and critic networks. The experiments show that ARMAAC improves task completion rates and reduces average system cost by 11.01∼14.03% and 10.45∼15.56% compared with baselines.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0592.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
