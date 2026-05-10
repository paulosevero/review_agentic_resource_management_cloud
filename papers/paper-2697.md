---
id: paper-2697
title: 'BEST: Blockchain-Enabled Sustainable Task Scheduling for Optimizing Large AI Model Workloads at the Edge'
authors:
- Luo, Haoxiang
- Chen, Runhua
- Sun, Gang
- Yu, Hongfang
- Dustdar, Schahram
venue: IEEE Transactions on Artificial Intelligence
venue_type: journal
year: 2026
doi: 10.1109/TAI.2026.3669544
url: https://www.scopus.com/pages/publications/105032255697?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- blockchain
- edge Computing
- edge computing power network
- Real-World Asset (RWA)
- Sustainable Large AI Models (LAMs)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2697 — BEST: Blockchain-Enabled Sustainable Task Scheduling for Optimizing Large AI Model Workloads at the Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The proliferation of Large AI Models (LAMs) to the network edge promises unprecedented intelligence in real-time applications. It also introduces a critical sustainability challenge due to the immense energy footprint of model inference on resource-constrained devices. While model-level optimizations have made progress, they fail to address the systemic issue of aggregate energy consumption across a network. This paper introduces BEST (Blockchain-Enabled Sustainable Task Scheduling), a novel framework that reimagines edge resource management to explicitly tackle this sustainability crisis. BEST establishes a decentralized marketplace for underutilized edge resources by introducing a novel application of Real-World Asset (RWA) tokenization to abstract and commoditize computational capacity and battery power. These tokenized resources can be securely and transparently traded among peer devices via a blockchain-based infrastructure. To navigate this dynamic marketplace, we develop a cooperative multi-agent deep reinforcement learning (MADRL) algorithm based on Proximal Policy Optimization (PPO). The agents learn a sophisticated scheduling policy that dynamically balances task latency, system-wide energy consumption, and task success rate. Extensive simulations against compared baselines demonstrate BEST’s unique strengths. It reduces total energy consumption by up to 26% — 46% against other schemes, while maintaining a high task success rate and latency competitive with the state-of-the-art scheme. By creating a market-driven, collaborative ecosystem, BEST provides a scalable and effective pathway toward achieving truly sustainable LAM at the edge. © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2697.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
