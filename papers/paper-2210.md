---
id: paper-2210
title: 'Coordinating Artificial Intelligence and Bitcoin Mining Workloads: A Risk-Aware Distributional Multi-Agent Reinforcement Learning Approach'
authors:
- Thomaidis, Ioannis T.
- Giannopoulos, Panagiotis G.
- Dasaklis, Thomas K.
venue: 16th International Conference on Information, Intelligence, Systems and Applications, IISA 2025
venue_type: conference
year: 2025
doi: 10.1109/IISA66859.2025.11311340
url: https://www.scopus.com/pages/publications/105031893048?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Agents
- Balance
- Bitcoin mining
- Energy
- Grid
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

# paper-2210 — Coordinating Artificial Intelligence and Bitcoin Mining Workloads: A Risk-Aware Distributional Multi-Agent Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid expansion of Artificial Intelligence (AI) workloads has created substantial energy requirements for contemporary data centers, which generate worries about infrastructure expansion and operational expenses and environmental sustainability. The worldwide shift toward renewable energy creates uncertainties in power supply that lead to grid instability and energy curtailment problems. This paper explores the synergistic convergence of AI compute infrastructure and Bitcoin (BTC) mining as a novel, energy-aware co-optimization framework. We propose a Distributional Multi-Agent Reinforcement Learning (MARL) system that dynamically allocates surplus energy between latency-sensitive AI jobs and highly flexible BTC mining operations. The proposed solution includes essential participants like renewable energy producers, energy management agents, AI clusters and BTC miners operating within a centralized training and decentralized execution paradigm. The simulation demonstrates that our MARL-driven methodology reduces the reduction in renewable energy by up to 65 % while maintaining high BTC mining profitability and stable grid demand and ensuring AI service level compliance. These findings suggest a path toward sustainable, intelligent energy computation ecosystems where AI and blockchain technologies operate not as competitors, but as complementary agents within a unified infrastructure.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2210.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
