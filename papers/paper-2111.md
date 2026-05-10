---
id: paper-2111
title: 'Blockchain-Empowered Multi-Domain Resource Trading in TN-NTN 6G Networks: A Hierarchical Multi-Agent DRL Approach'
authors:
- Seid, Abegaz Mohammed
- Abishu, Hayla Nahom
- Rathore, Rajkumar Singh
- Erbad, Aiman
- Jhaveri, Rutvij H.
- Lu, Jianfeng
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2025
doi: 10.1109/TCE.2024.3512581
url: https://www.scopus.com/pages/publications/85212054283?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3874--3889
keywords:
- Aerial-MEC
- consortium blockchain
- HMADRL
- metaverse
- network slicing
- resource trading
- Stackelberg game
- TN-NTN
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2111 — Blockchain-Empowered Multi-Domain Resource Trading in TN-NTN 6G Networks: A Hierarchical Multi-Agent DRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The advent of 6G networks promises transformative advances in communication technologies, ushering in an era of unprecedented connectivity, low-latency communication, and ubiquitous computing. However, one of the key challenges in realizing the full potential of 6G lies in efficiently managing and trading resources across diverse domains in terrestrial and non-terrestrial integrated networks (TN-NTN). In this paper, we introduce a novel multi-domain resource trading approach that integrates blockchain technology, hierarchical multi-agent deep reinforcement learning (HMADRL), and multi-leader multi-follower (MLMF) Stackelberg games to address this challenge. HMADRL provides an intelligent and adaptable framework for resource requesters and provider agents to learn optimal resource allocation methods in multiple domains. The MLMF Stackelberg game framework represents the strategic interactions between virtual service providers (SPs), network operators, and computing resource providers to enable them to make dynamic resource allocation and pricing decisions. This hierarchical decision-making strategy ensures a structured bargaining mechanism where leaders optimize their revenue by setting resource pricing and followers strategically decide on their resource-buying strategies. In the proposed scheme, the blockchain includes smart contracts that autonomously execute resource trading agreements, ensuring that transactions are tamper-proof and executed according to predefined rules. The proposed method optimizes the system’s utility by dynamically adjusting the pricing strategy to changing resource demands. The simulation results show that our proposed HMADRL algorithm increases the utility by 19.645%, 33.018%, and 48.791% compared to the modified multi-agent deep deterministic policy gradient (MADDPG), MADDPG, and DDPG algorithms, respectively. © 1975-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2111.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
