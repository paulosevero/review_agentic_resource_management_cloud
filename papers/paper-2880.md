---
id: paper-2880
title: DNN Inference Task Partitioning and Offloading Strategy for Cloud-Edge-End Collaborative Computing Environments; [面向云边端协同计算环境的 DNN 推理任务分割卸载策略]
authors:
- Yang, Yuhui
- Tang, Xiaoyong
venue: Computer Engineering and Applications
venue_type: journal
year: 2026
doi: 10.3778/j.issn.1002-8331.2501-0046
url: https://www.scopus.com/pages/publications/105034493665?origin=resultslist
publisher: Journal of Computer Engineering and Applications Beijing Co., Ltd.; Science Press
pages: 314--323
keywords:
- cloud-edge-end collaborative
- computation offloading
- deep reinforcement learning
- edge computing
- Internet of things
- 云-边-端协同
- 深度强化学习
- 物联网
- 计算卸载
- 边缘计算
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2880 — DNN Inference Task Partitioning and Offloading Strategy for Cloud-Edge-End Collaborative Computing Environments; [面向云边端协同计算环境的 DNN 推理任务分割卸载策略]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, deep neural networks (DNNs) have made significant breakthroughs in fields such as data processing, image recognition, and speech recognition, and have been extensively deployed on Internet of things (IoT) devices. However, IoT devices face limitations in computational performance and battery capacity, making it difficult to complete DNN inference tasks with low latency and energy consumption. To address this issue, a DNN inference task partitioning and offloading strategy based on cloud-edge-end collaborative computing is proposed. The computation and transmission load characteristics of DNN inference tasks are analyzed, and a delay and energy consumption model is established based on these characteristics. The delay and energy consumption in this model are normalized and weighted to compute a cost. A multi-agent deep reinforcement learning algorithm, MAPPO-MO (multi-agent proximal policy optimization multi-object), is proposed for DNN inference task partitioning and offloading in the cloud-edge-end collaborative computing framework. This method models the cloud- edge- end collaborative computing environment as a Markov decision process (MDP), and uses the processed cost as a reward signal to guide the algorithm training, thus enabling deep reinforcement learning for inference process optimization. To validate the effectiveness of the algorithm, simulation experiments are conducted. The results show that compared to the classic Local-Computing, Offloading-Computing, and QMIX algorithms, the proposed MAPPO-MO algorithm offers significant advantages in terms of cost.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2880.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
