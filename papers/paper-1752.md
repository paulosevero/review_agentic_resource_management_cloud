---
id: paper-1752
title: 'Blockchain-Based Edge Computing: Joint Task Offloading And Mining With Multi-Agent Reinforcement Learning'
authors:
- Kumar, R. Anil
- Patchala, Sarala
- Pachala, Sunitha
- Atkar, Geeta Bhimrao
- Mahalaxmi, U.H.B.K.
- Satyam, Angara
venue: Journal of Theoretical and Applied Information Technology
venue_type: journal
year: 2025
doi: ''
url: https://www.scopus.com/pages/publications/105016876542?origin=resultslist
publisher: Little Lion Scientific
pages: 6414--6430
keywords:
- Blockchain Design
- MADDPG.
- MADRL
- MEC
- Task Offloading
- TOBM
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

# paper-1752 — Blockchain-Based Edge Computing: Joint Task Offloading And Mining With Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of mobile edge computing (MEC) and blockchain enhances computing efficiency and security. This paper presents a novel cooperative task offloading and block mining (TOBM) approach in blockchain-based MEC. The system enables edge devices to offload tasks and participate in mining operations. To handle blockchain latency, a novel Proof-of-Reputation (PoR) consensus mechanism is introduced. A multi-objective function is developed to optimize system utility by managing offloading, channel selection, power allocation and computational resources. A multi-agent deep deterministic policy gradient (MA-DDPG) algorithm is used for optimization. A game-theoretic approach is applied to model competition among edge devices and establish a Nash equilibrium. Simulations demonstrate improved system utility compared to traditional approaches. The proposed TOBM framework provides efficient task allocation and computational resource management. It dynamically adapts to network conditions, reducing computational delays and enhancing overall performance. Blockchain security mechanisms prevent unauthorized data modifications, promoting data integrity and trustworthiness. The PoR consensus mechanism minimizes the verification time required for block mining, allowing for faster transactions and reduced network congestion. The proposed method enables edge devices to make intelligent task offloading decisions, optimizing computational efficiency while maintaining low energy consumption. The MADDPG algorithm effectively learns from network interactions, continuously improving decision-making policies. The results indicate that the system significantly outperforms existing solutions in terms of latency reduction, resource utilization and security enhancements. Future research directions include enhancing the PoR mechanism and exploring additional consensus models to improve scalability and performance. © Little Lion Scientific

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1752.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
