---
id: paper-1382
title: Efficient Delay-Sensitive Task Offloading to Fog Computing with Multi-Agent Twin Delayed Deep Deterministic Policy Gradient
authors:
- Ali, Endris Mohammed
- Lemma, Frezewd
- Srinivasagan, Ramasamy
- Abawajy, Jemal
venue: Electronics (Switzerland)
venue_type: journal
year: 2025
doi: 10.3390/electronics14112169
url: https://www.scopus.com/pages/publications/105008496125?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- deep reinforcement learning (DRL)
- fog computing
- Internet of Things (IoT)
- multi-agent
- task offloading
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

# paper-1382 — Efficient Delay-Sensitive Task Offloading to Fog Computing with Multi-Agent Twin Delayed Deep Deterministic Policy Gradient

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog computing presents a significant paradigm for extending the computational capabilities of resource-constrained devices executing increasingly complex applications. However, effectively leveraging this potential critically depends on the implementation of efficient task offloading mechanisms to proximal fog nodes, particularly under conditions of high resource contention. To address this challenge, we introduce MAFCPTORA (multi-agent fully cooperative partial task offloading and resource allocation), a decentralized multi-agent deep reinforcement learning algorithm for cooperative task offloading and resource allocation. We evaluated the performance of MAFCPTORA and compared it against recent approaches. MAFCPTORA demonstrated superior performance compared to recent methods, achieving a significantly higher average reward (0.36 ± 0.01), substantially lower average latency (0.08 ± 0.01), and reduced energy consumption (0.76 ± 0.14). © 2025 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1382.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
