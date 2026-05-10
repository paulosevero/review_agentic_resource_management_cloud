---
id: paper-0500
title: Dynamic Scheduling for Stochastic Edge-Cloud Computing Environments Using A3C Learning and Residual Recurrent Neural Networks
authors:
- Tuli, Shreshth
- Ilager, Shashikant
- Ramamohanarao, Kotagiri
- Buyya, Rajkumar
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2022
doi: 10.1109/TMC.2020.3017079
url: https://www.scopus.com/pages/publications/85124597565?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 940--954
keywords:
- asynchronous advantage actor-critic
- cloud computing
- deep reinforcement learning
- Edge computing
- recurrent neural network
- task scheduling
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
    my_justification: RL / RNN
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

# paper-0500 — Dynamic Scheduling for Stochastic Edge-Cloud Computing Environments Using A3C Learning and Residual Recurrent Neural Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The ubiquitous adoption of Internet-of-Things (IoT) based applications has resulted in the emergence of the Fog computing paradigm, which allows seamlessly harnessing both mobile-edge and cloud resources. Efficient scheduling of application tasks in such environments is challenging due to constrained resource capabilities, mobility factors in IoT, resource heterogeneity, network hierarchy, and stochastic behaviors. Existing heuristics and Reinforcement Learning based approaches lack generalizability and quick adaptability, thus failing to tackle this problem optimally. They are also unable to utilize the temporal workload patterns and are suitable only for centralized setups. However, asynchronous-advantage-actor-critic (A3C) learning is known to quickly adapt to dynamic scenarios with less data and residual recurrent neural network (R2N2) to quickly update model parameters. Thus, we propose an A3C based real-time scheduler for stochastic Edge-Cloud environments allowing decentralized learning, concurrently across multiple agents. We use the R2N2 architecture to capture a large number of host and task parameters together with temporal patterns to provide efficient scheduling decisions. The proposed model is adaptive and able to tune different hyper-parameters based on the application requirements. We explicate our choice of hyper-parameters through sensitivity analysis. The experiments conducted on real-world data set show a significant improvement in terms of energy consumption, response time, Service-Level-Agreement and running cost by 14.4, 7.74, 31.9, and 4.64 percent, respectively when compared to the state-of-the-art algorithms.  © 2002-2012 IEEE.

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
- **my_justification:** "RL / RNN"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0500.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
