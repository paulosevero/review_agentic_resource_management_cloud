---
id: paper-1808
title: 'Knowledge- and Model-Driven Deep Reinforcement Learning for Efficient Federated Edge Learning: Single- and Multi-Agent Frameworks'
authors:
- Li, Yangchen
- Zhao, Lingzhi
- Wang, Tianle
- Ding, Lianghui
- Yang, Feng
venue: IEEE Transactions on Machine Learning in Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TMLCN.2025.3534754
url: https://www.scopus.com/pages/publications/105027882275?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers
pages: 332--352
keywords:
- algorithm parameter configuration
- deep reinforcement learning
- edge computing
- Federated learning
- multi-agent reinforcement learning
- worker selection
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

# paper-1808 — Knowledge- and Model-Driven Deep Reinforcement Learning for Efficient Federated Edge Learning: Single- and Multi-Agent Frameworks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we investigate federated learning (FL) efficiency improvement in practical edge computing systems, where edge workers have non-independent and identically distributed (non-IID) local data, as well as dynamic and heterogeneous computing and communication capabilities. We consider a general FL algorithm with configurable parameters, including the number of local iterations, mini-batch sizes, step sizes, aggregation weights, and quantization parameters, and provide a rigorous convergence analysis. We formulate a joint optimization problem for FL worker selection and algorithm parameter configuration to minimize the final test loss subject to time and energy constraints. The resulting problem is a complicated stochastic sequential decision-making problem with an implicit objective function and unknown transition probabilities. To address these challenges, we propose knowledge/model-driven single-agent and multi-agent deep reinforcement learning (DRL) frameworks. We transform the primal problem into a Markov decision process (MDP) for the single-agent DRL framework and a decentralized partially-observable Markov decision process (Dec-POMDP) for the multi-agent DRL framework. We develop efficient single-agent and multi-agent asynchronous advantage actor-critic (A3C) approaches to solve the MDP and Dec-POMDP, respectively. In both frameworks, we design a knowledge-based reward to facilitate effective DRL and propose a model-based stochastic policy to tackle the mixed discrete-continuous actions and large action spaces. To reduce the computational complexities of policy learning and execution, we introduce a segmented actor-critic architecture for the single-agent DRL and a distributed actor-critic architecture for the multi-agent DRL. Numerical results demonstrate the effectiveness and advantages of the proposed frameworks in enhancing FL efficiency.  © 2025 CCBY.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1808.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
