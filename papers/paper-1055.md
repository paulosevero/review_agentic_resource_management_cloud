---
id: paper-1055
title: 'Computation Rate Maximization for SCMA-Aided Edge Computing in IoT Networks: A Multi-Agent Reinforcement Learning Approach'
authors:
- Liu, Pengtao
- An, Kang
- Lei, Jing
- Sun, Yifu
- Liu, Wei
- Chatzinotas, Symeon
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2024
doi: 10.1109/TWC.2024.3371791
url: https://www.scopus.com/pages/publications/85187973785?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10414--10429
keywords:
- computation offloading
- IoT
- MEC
- multi-agent reinforcement learning
- resource allocation
- SCMA
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
    my_justification: RL
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

# paper-1055 — Computation Rate Maximization for SCMA-Aided Edge Computing in IoT Networks: A Multi-Agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Integrating sparse code multiple access (SCMA) and mobile edge computing (MEC) into the Internet of Things (IoT) networks can enable efficient connectivity and timely computation for resource-limited IoT users. This paper studies the computation rate maximization problem under task deadline constraints in dynamic SCMA-MEC networks. Specifically, we propose a predictive deep Q-network for SCMA resource allocation and computation offloading (PQ-RACO) algorithm for single-cell scenarios, where IoT devices use long short-term memory (LSTM) networks to predict the states and actions of other agents. However, the PQ-RACO algorithm is not scalable for increasing numbers of IoT devices. To address this issue, an improved multi-agent deep Q-network for SCMA resource allocation and computation offloading algorithm (MQ-RACO) is proposed for multi-cell scenarios. The algorithm is a centralized training and decentralized execution (CTDE) multi-agent reinforcement learning (MARL) algorithm with explicit rewards, which is tailored to the special structure of joint rewards. Simulation results demonstrate that the proposed algorithm outperforms several state-of-the-art MARL algorithms and other benchmark schemes in terms of convergence speed and computation rate.  © 2024 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1055.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
