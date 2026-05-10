---
id: paper-2656
title: Blockchain-Enabled Storage Resource Trading for Collaborative Edges
authors:
- Li, Weimin
- Yan, Zhengmao
- Li, Zitong
- Chen, Zeqiang
- Wu, Fan
- Chen, Wenxiong
- Liu, Jianxun
- Ren, Ju
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3672019
url: https://www.scopus.com/pages/publications/105032809677?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Collaborative storage
- Edge computing
- Game theory
- Reinforcement learning
- Resource trading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2656 — Blockchain-Enabled Storage Resource Trading for Collaborative Edges

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As edge devices grow smarter and application scenarios become more diverse, users' demands for lower latency and higher efficiency in data storage and processing have risen sharply. Individual edge devices and nodes are no longer sufficient to meet these expanding storage requirements. Consequently, developing efficient, low-latency, and cost-effective solutions for collaborative storage across edge devices and nodes has become a critical challenge. In this paper, we present a framework for the transaction and pricing of storage resources in an edge computing environment involving multiple edge service providers, to address trust and incentive issues in storage resource collaboration. Firstly, we propose a secure and decentralized storage resource trading mechanism by leveraging blockchain technology and smart contracts. We introduce Proof of Transaction Expectation (PoTE), an efficient, reliable, and lightweight consensus mechanism, to ensure transaction transparency, openness, and non-repudiation. Secondly, we introduce a game theory-based storage resource pricing model, where a leader interacts with multiple followers to optimize profits while maintaining service quality. To address dynamic pricing and storage resource allocation problems under incomplete information, we propose the Stackelberg Game Approach based on Multi-Agent Reinforcement Learning (SGA-MARL), which formulates the optimal pricing and trading share decisions in the two-stage Stackelberg game as a stochastic Markov Decision Process (MDP). Simulations and prototype testing validate the effectiveness of the proposed system, with results showing that the PoTE consensus achieves up to 40% higher throughput than Proof-of-Work while reducing latency by over 50% compared to PBFT, and the SGA-MARL algorithm improves leader profit by approximately 30% and resource satisfaction rates by over 80% compared to baseline methods like MA-PPO and DQN. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2656.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
