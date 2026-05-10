---
id: paper-0760
title: Multi-agent deep reinforcement learning for task offloading in group distributed manufacturing systems
authors:
- Xiong, Jianyu
- Guo, Peng
- Wang, Yi
- Meng, Xiangyin
- Zhang, Jian
- Qian, Linmao
- Yu, Zhenglin
venue: Engineering Applications of Artificial Intelligence
venue_type: journal
year: 2023
doi: 10.1016/j.engappai.2022.105710
url: https://www.scopus.com/pages/publications/85144058485?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Cloud computing
- Group distributed manufacturing system
- Multi-agent deep reinforcement learning
- Near-real-time optimization
- Task offloading
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0760 — Multi-agent deep reinforcement learning for task offloading in group distributed manufacturing systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid development of cloud computing and the Internet of Things (IoT) have facilitated near real-time optimization of the group distributed manufacturing systems. Currently, the most common technique to accomplish near-real-time optimization is cloud–edge cooperation for offloading optimization tasks. The tasks are partially offloaded to the cloud to be completed, and the remaining are kept at the edge. Due to the complexity of task offloading, such as capacity restrictions of cloud and edge computing resources, or task deadlines, unbalanced or insufficient tasks are offloaded to cloud and edge, causing time delay. To address the imbalance and insufficiency in the task offloading process, a mixed-integer programming model was developed to reduce the latency of task calculation. The task offloading problem is decomposed into two sub-problems: 1) Defining priorities for the tasks in near real-time. 2) Determining if the task is offloaded to the cloud. A multi-agent deep reinforcement learning with attention mechanism (MaDRLAM) framework is proposed to solve the two-step decision problem. The MaDRLAM framework consists of two agents, and each agent corresponds to a sub-problem. Each agent comprises an encoder and a decoder, and the two agents cooperate in devising an offloading strategy for the tasks. The Encoder and Decoder built for each agent are based on the Transformer structure. Unlike the traditional Transformer, we added the Pointer networks to the Transformer to solve the proposed decision problem. Besides, an improved multi-actor and single-critic strategy based on the REINFORCE algorithm is designed to train the proposed MaDRLAM. Finally, Extensive computational experiments are conducted on instances with a varying number of tasks, different task data sizes, and different cloud computing capacities. Computational results show that the proposed framework can find a solution with a GAP value of less than 1% within 1 s for each instance. The proposed framework is competitive in both solution accuracy and solution time compared with other offloading strategies. © 2022 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0760.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
