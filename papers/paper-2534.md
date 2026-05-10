---
id: paper-2534
title: IRS-Assisted Secure Computation Offloading in Multi-Region Mobile Edge Computing via Multi-Agent Deep Reinforcement Learning
authors:
- Chen, Lingxiao
- Li, Xiuhua
- Sun, Chuan
- Li, Penghua
- Wang, Xiaofei
- Leung, Victor C.M.
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2026.3676421
url: https://www.scopus.com/pages/publications/105034064329?origin=resultslist
publisher: IEEE Computer Society
pages: 7931--7948
keywords:
- computation offloading
- intelligent reflecting surface
- Mobile edge computing
- multi-agent deep reinforcement learning
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

# paper-2534 — IRS-Assisted Secure Computation Offloading in Multi-Region Mobile Edge Computing via Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) offers an advanced solution to offload tasks from user devices (UDs) to the network edge, alleviating network congestion and reducing task execution latency. Nevertheless, current computation offloading still faces two critical challenges: high transmission latency due to poor wireless channel quality, and task privacy leakage due to the potential for eavesdropping. Intelligent reflecting surface (IRS) is a promising technique to enhance channel quality and security in MEC networks. In this paper, we consider a multi-region IRS-assisted MEC network that jointly optimizes computation offloading and IRS phase configuration to minimize the task execution latency for UDs. The optimization problem is NP-hard and requires distributed decision-making in multiple regions. Therefore, we propose a multi-agent deep reinforcement learning algorithm with an attention mechanism and Gumbel-Softmax. Specifically, the attention mechanism helps dynamically select key information and improve decision-making efficiency, while Gumbel-Softmax is used to solve the problem of the non-differentiable discrete action spaces. Simulation results demonstrate that the proposed algorithm outperforms baseline schemes by reducing the task execution latency and improving the offloading rate by 27.2% and 60.7% on average in the considered MEC networks. © 2013 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2534.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
