---
id: paper-0830
title: Building Communication Efficient Asynchronous Peer-to-Peer Federated LLMs with Blockchain
authors:
- Balija, Sree Bhargavi
- Nanda, Amitash
- Sahoo, Debashis
venue: AAAI Spring Symposium - Technical Report
venue_type: conference
year: 2024
doi: 10.1609/aaaiss.v3i1.31212
url: https://www.scopus.com/pages/publications/105016581851?origin=resultslist
publisher: Association for the Advancement of Artificial Intelligence
pages: 288--292
keywords:
- Artificial intelligence
- Collaborative learning
- Computer aided instruction
- Copyrights
- Distributed computer systems
- Federated learning
- Peer to peer networks
- Privacy-preserving techniques
- Block-chain
- Collaborative training
- Communication efficiency
- Data scarcity
- Decentralised
- Heterogeneous data
- Language model
- Peer to peer
- Privacy concerns
- Real-world
- Economic and social effects
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0830 — Building Communication Efficient Asynchronous Peer-to-Peer Federated LLMs with Blockchain

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLM) have gathered attention with the advent of ChatGPT. However, developing personalized LLM models faces challenges in real-world applications due to data scarcity and privacy concerns. Federated learning addresses these issues, providing collaborative training while preserving the client's data. Although it has made significant progress, federated learning still faces ongoing challenges, such as communication efficiency, heterogeneous data, and privacy-preserving methods. This paper presents a novel, fully decentralized federated learning framework for LLMs to address these challenges. We utilize different blockchain-federated LLM (BC-FL) algorithms, effectively balancing the trade-off between latency and accuracy in a decentralized-federated learning environment. Additionally, we address the challenge of communication overhead in peer-to-peer networks by optimizing the path for weight transfer and mitigating node anomalies. We conducted experiments to evaluate memory usage and latency in server and serverless environments. Our results demonstrate a decrease in latency by 5X and a 13% increase in accuracy for serverless cases. Comparisons between synchronous and asynchronous scenarios revealed a 76% reduction in information passing time for the latter. The PageRank method is most efficient in eliminating anomalous nodes for better performance of the global federated LLM model. The code is available on GitHub (https://github.com/Sreebhargavibalijaa/Federated_finetuning_LLM-s_p2p_environment). Copyright © 2024, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0830.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
