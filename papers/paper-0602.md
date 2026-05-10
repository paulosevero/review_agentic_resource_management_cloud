---
id: paper-0602
title: 'Multi-Agent Collaborative Inference via DNN Decoupling: Intermediate Feature Compression and Edge Learning'
authors:
- Hao, Zhiwei
- Xu, Guanyu
- Luo, Yong
- Hu, Han
- An, Jianping
- Mao, Shiwen
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2023
doi: 10.1109/TMC.2022.3183098
url: https://www.scopus.com/pages/publications/85132769851?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6041--6055
keywords:
- collaborative inference
- Deep reinforcement learning
- hybrid action space
- mobile edge computing
- multi-user
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0602 — Multi-Agent Collaborative Inference via DNN Decoupling: Intermediate Feature Compression and Edge Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, deploying deep neural network (DNN) models via collaborative inference, which splits a pre-trained model into two parts and executes them on user equipment (UE) and edge server respectively, becomes attractive. However, the large intermediate feature of DNN impedes flexible decoupling, and existing approaches either focus on the single UE scenario or simply define tasks considering the required CPU cycles, but ignore the indivisibility of a single DNN layer. In this article, we study the multi-agent collaborative inference scenario, where a single edge server coordinates the inference of multiple UEs. Our goal is to achieve fast and energy-efficient inference for all UEs. To achieve this goal, we design a lightweight autoencoder-based method to compress the large intermediate feature at first. Then we define tasks according to the inference overhead of DNNs and formulate the problem as a Markov decision process (MDP). Finally, we propose a multi-agent hybrid proximal policy optimization (MAHPPO) algorithm to solve the optimization problem with a hybrid action space. We conduct extensive experiments with different types of networks, and the results show that our method can reduce up to 56% of inference latency and save up to 72% of energy consumption. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0602.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
