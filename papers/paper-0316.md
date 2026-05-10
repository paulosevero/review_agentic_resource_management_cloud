---
id: paper-0316
title: Multi-Agent Reinforcement Learning for Edge Resource Management with Reconstructed Environment
authors:
- Miao, Weiwei
- Zeng, Zeng
- Zhang, Mingxuan
- Quan, Siping
- Zhang, Zhen
- Li, Shihao
- Zhang, Li
- Sun, Qi
venue: 19th IEEE International Symposium on Parallel and Distributed Processing with Applications, 11th IEEE International Conference on Big Data and Cloud Computing, 14th IEEE International Conference
  on Social Computing and Networking and 11th IEEE International Conference on Sustainable Computing and Communications, ISPA/BDCloud/SocialCom/SustainCom 2021
venue_type: conference
year: 2021
doi: 10.1109/ISPA-BDCloud-SocialCom-SustainCom52081.2021.00233
url: https://www.scopus.com/pages/publications/85124121079?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1729--1736
keywords:
- Edge Computing
- Imitation Learning
- Multi-Agent Reinforcement Learning
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

# paper-0316 — Multi-Agent Reinforcement Learning for Edge Resource Management with Reconstructed Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In edge computing it is pivotal to automatically manage the resources to increase efficiency with limited resources. Deep reinforcement learning, which aims to maximize the long term cumulative reward, has recently been adopted in such scenarios. However, training the policy in real-world edge computing environment is challenging since arbitrary exploration in real world could drastically impair user utilities. In this paper, we propose a novel imitation learning approach to construct a virtual environment, in which the policy can be trained freely without additional costs. Under the virtual environment, we use a multi-agent reinforcement learning to manage the edge resources. Our method adopts a decentralized, sequential approach to deal with the uncertainties in the environment. Specifically, we decompose the target reward function into separated global part and local parts, where the global part is shared by all agents for cooperation, and the local parts are owned by each individual edge to accelerate the model learning. Extensive experimental results demonstrate that the constructed environment is very close to the real environment. In addition, the proposed multi agent reinforcement learning algorithm can converge very fast in the training phase and outperforms other state-of-art methods significantly in a variety of scenarios. © 2021 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0316.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
