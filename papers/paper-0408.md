---
id: paper-0408
title: A Multi-Agent Deep Reinforcement Learning Approach for Computation Offloading in 5G Mobile Edge Computing
authors:
- Gan, Zhaoyu
- Lin, Rongheng
- Zou, Hua
venue: Proceedings - 22nd IEEE/ACM International Symposium on Cluster, Cloud and Internet Computing, CCGrid 2022
venue_type: conference
year: 2022
doi: 10.1109/CCGrid54584.2022.00074
url: https://www.scopus.com/pages/publications/85135760356?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 645--654
keywords:
- 5G Network
- Mobile Edge Computing
- Multi-Agent Reinforcement Learning
- Offloading
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

# paper-0408 — A Multi-Agent Deep Reinforcement Learning Approach for Computation Offloading in 5G Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) in 5G networks has recently emerged as a promising paradigm to enhance the data processing capabilities of mobile devices. Due to portability and cost considerations, mobile devices usually have limited battery and computing resources. Through MEC technology, computing tasks can be offloaded to remote servers, which helps to reduce computing latency and energy consumption. However, an im-proper computing offloading may produce additional overheads such as waiting time and wireless transmission latency, because of the limited resources of remote servers and extra wireless transmissions. In this paper, we propose a multi-agent deep reinforcement learning (MADRL) based decentralized cooperative offloading decision algorithm, which determines whether the computing tasks are executed locally or placed on an appropriate edge node to minimize system costs. Our goal is to learn an optimal online policy from experiences to solve a combinatorial optimization problem at a lower computational complexity, and the factors such as computation delay, energy consumption, communication latency, and waiting time in remote servers are all considered. Experiment results show that our approach is able to reduce by an average of 5.4% execution latency than traditional methods, and outperforms single-agent D RL algorithms. © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0408.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
