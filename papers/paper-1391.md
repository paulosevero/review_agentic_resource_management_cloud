---
id: paper-1391
title: FEDERATED LEARNING WITH TRANSFORMER-BASED REINFORCEMENT LEARNING FOR SMART CITY SECURITY
authors:
- Alterkawi, Laila
- Altarawneh, Mokhled
venue: Proceedings of the International Conferences on Big Data Analytics, Data Mining and Computational Intelligence 2025, BigDaCI 2025; Connected Smart Cities 2025 and e-Health 2025, EH 2025 - part of
  the Multi Conference on Computer Science and Information Systems 2025
venue_type: conference
year: 2025
doi: ''
url: https://www.scopus.com/pages/publications/105022102501?origin=resultslist
publisher: IADIS
pages: 119--127
keywords:
- Decision Transformer
- Federated Learning
- Internet of Things
- Mobile Edge Computing
- Multi-Agent Reinforcement Learning
- Smart Cities
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

# paper-1391 — FEDERATED LEARNING WITH TRANSFORMER-BASED REINFORCEMENT LEARNING FOR SMART CITY SECURITY

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The growing integration of devices from the Internet of Things (IoT) in smart city infrastructures creates new opportunities for autonomous decision-making but also introduces significant challenges related to scalability, coordination, and data privacy. Traditional reinforcement learning (RL) models, particularly Multi-Agent Actor-Critic (MAAC) frameworks, offer structured coordination but rely on centralized critics and recurrent networks, limiting their effectiveness in dynamic, large-scale environments. In this work, we propose a novel federated reinforcement learning framework that integrates Decision Transformers (DT) into a multi-agent federated learning (FL) paradigm. Our method replaces conventional policy gradient optimization with trajectory-based learning using self-attention mechanisms, enabling agents to model long-term dependencies without centralized value functions. By combining DT with FL, our framework supports decentralized training on IoT nodes, preserving privacy and reducing communication overhead. We benchmark our model against MAAC in a mobile edge computing (MEC) simulation environment, demonstrating that Transformer-based RL achieves higher reward efficiency, better scalability, and improved adaptability in non-stationary environments - although with slightly higher variance in early training. These results highlight the potential of Transformer-based RL as a robust alternative for decentralized, security-sensitive smart city applications. © 2025 IADIS Press All rights reserved.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1391.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
