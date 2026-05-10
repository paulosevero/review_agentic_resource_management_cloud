---
id: paper-2654
title: Multi-Agent Reinforcement Learning for Modeling, Simulating, and Optimizing Energy Markets
authors:
- Levy, Matan
- Segev, Itay
- Tuisov, Alexander
- Keren, Sarah
venue: Proceedings of the AAAI Conference on Artificial Intelligence
venue_type: conference
year: 2026
doi: 10.1609/aaai.v40i45.41229
url: https://www.scopus.com/pages/publications/105034604456?origin=resultslist
publisher: Association for the Advancement of Artificial Intelligence
pages: 38844--38852
keywords:
- Behavioral research
- Electric industry
- Electric load dispatching
- Intelligent agents
- Machine learning
- Marketing
- Power markets
- Renewable energy
- Centralized systems
- Demand pattern
- Energy markets
- Integration of renewable energies
- Market players
- Multi-agent reinforcement learning
- Optimisations
- Optimizing energy
- Public-private
- Renewable energy source
- Multi agent systems
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-2654 — Multi-Agent Reinforcement Learning for Modeling, Simulating, and Optimizing Energy Markets

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The objective of this study is to advance the optimization of hybrid electricity markets using multi-agent reinforcement learning (MARL). The transition from centralized systems to public–private models introduces significant challenges, including the emergence of independent market players and the increasing integration of renewable energy sources (RESs). These challenges are further intensified by rapidly shifting demand patterns, driven both by energy-intensive data centers and AI inference workloads, as well as by political and societal instabilities. To address these complexities, we develop a formal model of market participants’ behavior and propose a MARL-based framework for optimizing system operator strategies. This framework incorporates dynamic pricing and dispatch scheduling to minimize operational costs, maintain grid stability, and align market incentives. We also present a new, adaptable simulation environment compatible with state-of-the-art MARL methods. Empirical evaluations in increasingly complex scenarios demonstrate the effectiveness of our approach in capturing the dynamic and decentralized nature of modern electricity markets. © 2026, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2654.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
