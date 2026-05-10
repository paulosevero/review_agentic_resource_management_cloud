---
id: paper-0476
title: 'Intelligent Blockchain-Based Edge Computing via Deep Reinforcement Learning: Solutions and Challenges'
authors:
- Nguyen, Dinh C.
- Nguyen, Van-Dinh
- Ding, Ming
- Chatzinotas, Symeon
- Pathirana, Pubudu N.
- Seneviratne, Aruna
- Dobre, Octavia
- Zomaya, Albert Y.
venue: IEEE Network
venue_type: journal
year: 2022
doi: 10.1109/MNET.002.2100188
url: https://www.scopus.com/pages/publications/85135739032?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 12--19
keywords:
- computation offloading
- Data mining
- Deep learning
- Information management
- Job analysis
- Mobile edge computing
- Multi agent systems
- Quality of service
- Reinforcement learning
- Block-chain
- Computing services
- Current computing
- Edge computing
- Optimisations
- Quality of experience
- Reinforcement learning solution
- Resource management
- Task analysis
- Task offloading
- Blockchain
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL + Review.
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

# paper-0476 — Intelligent Blockchain-Based Edge Computing via Deep Reinforcement Learning: Solutions and Challenges

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The convergence of mobile edge computing (MEC) and blockchain is transforming the current computing services in wireless Internet-of-Things (IoT) networks, enabling task offloading with security enhancement based on blockchain mining. Yet the existing approaches for these enabling technologies are isolated, providing only tailored solutions for specific services and scenarios. To fill this gap, we propose a novel cooperative task offloading and blockchain mining (TOBM) scheme for a blockchain-based MEC system, where each edge device not only handles computation tasks but also conducts block mining for improving system utility. To address the latency issues caused by the blockchain operation in MEC, we develop a new Proof-of-Reputation consensus mechanism based on a lightweight block verification strategy. To accommodate the highly dynamic environment and high-dimensional system state space, we apply a novel distributed deep reinforcement learning-based approach by using a multi-agent deep deterministic policy gradient algorithm. Experimental results demonstrate the superior performance of the proposed TOBM scheme in terms of enhanced system reward, improved offloading utility with lower blockchain mining latency, and better system utility, compared to the existing cooperative and non-cooperative schemes. The article concludes with key technical challenges and possible directions for future blockchain-based MEC research.  © 1986-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL + Review."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0476.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
