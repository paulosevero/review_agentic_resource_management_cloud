---
id: paper-0399
title: Deep Coalitional Q-Learning for Dynamic Coalition Formation in Edge Computing
authors:
- Ding, Shiyao
- Lin, Donghui
venue: IEICE Transactions on Information and Systems
venue_type: journal
year: 2022
doi: 10.1587/transinf.2021KBP0007
url: https://www.scopus.com/pages/publications/85131224051?origin=resultslist
publisher: Institute of Electronics Information Communication Engineers
pages: 864--872
keywords:
- coalition structure generation
- deep Q-network
- edge computing
- internet of things
- MDP
- multi-agent systems
- reinforcement learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0399 — Deep Coalitional Q-Learning for Dynamic Coalition Formation in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the high development of computation requirements in Internet of Things, resource-limited edge servers usually require to cooperate to perform the tasks. Most related studies usually assume a static cooperation approach which might not suit the dynamic environment of edge computing. In this paper, we consider a dynamic cooperation approach by guiding edge servers to form coalitions dynamically. It raises two issues: 1) how to guide them to optimally form coalitions and 2) how to cope with the dynamic feature where server statuses dynamically change as the tasks are performed. The coalitional Markov decision process (CMDP) model proposed in our previous work can handle these issues well. However, its basic solution, coalitional Q-learning, cannot handle the large scale problem when the task number is large in edge computing. Our response is to propose a novel algorithm called deep coalitional Q-learning (DCQL) to solve it. To sum up, we first formulate the dynamic cooperation problem of edge servers as a CMDP: each edge server is regarded as an agent and the dynamic process is modeled as a MDP where the agents observe the current state to formulate several coalitions. Each coalition takes an action to impact the environment which correspondingly transfers to the next state to repeat the above process. Then, we propose DCQL which includes a deep neural network and so can well cope with large scale problem. DCQL can guide the edge servers to form coalitions dynamically with the target of optimizing some goal. Furthermore, we run experiments to verify our proposed algorithm’s effectiveness in different settings. Copyright © 2022 The Institute of Electronics, Information and Communication Engineers

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0399.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
