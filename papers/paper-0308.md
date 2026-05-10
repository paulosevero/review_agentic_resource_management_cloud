---
id: paper-0308
title: Deep Reinforcement Learning-Based MEC Offloading and Resource Allocation in Uplink NOMA Heterogeneous Network
authors:
- Liu, Wei
- He, Yejun
- Zhang, Jinfeng
- Qiao, Jian
venue: 2021 Computing, Communications and IoT Applications, ComComAp 2021
venue_type: conference
year: 2021
doi: 10.1109/ComComAp53641.2021.9653064
url: https://www.scopus.com/pages/publications/85124609077?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 144--149
keywords:
- deep Q network (DQN)
- Deep reinforcement learning (DRL)
- heterogeneous networks (HetNets)
- mobile edge computing (MEC)
- nonorthogonal multiple access (NOMA)
- resource allocation
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

# paper-0308 — Deep Reinforcement Learning-Based MEC Offloading and Resource Allocation in Uplink NOMA Heterogeneous Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the advancement of fifth generation(5G) technology, mobile edge computing (MEC) has been considered an effective solution to 5G technical problems. The applications of non-orthogonal multiple access (NOMA) in heterogeneous networks is gradually being considered as an method to increase network throughput and improve spectrum utilization. By assigning non-orthogonal communication resources to different users at the transmitting end, the utilization rate of the spectrum can be maximized. Based on these advantages, we analyze thoroughly the MEC based on NOMA in this paper. In the NOMA system, we focus on optimizing channel resources, user offloading pattern and transmit power. These all characteristics have major role in obtaining the optimized user energy consumption. In recent years, deep Q network (DQN) is considered to be an effective method to solve the model-free problems. Different from traditional heuristic algorithms, we design multi-agent DQN to solve resource allocation in NOMA system. Due to the strong coupling between multiple decisions and the large solution space in dynamic optimization, there are found great challenges to the optimization of resources allocations. According to the simulation results, we can see that the DQN method for multi-agents can allow each agent to find approximately the optimal solution.  © 2021 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0308.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
