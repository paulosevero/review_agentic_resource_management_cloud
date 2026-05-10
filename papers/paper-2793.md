---
id: paper-2793
title: 'EdgePlus: A Multiagent Reinforcement Learning Framework for Dynamic Task Allocation in 6G Edge Computing'
authors:
- Taher, Bahaa Hussein
- Luo, Juan
- Ghrabat, Fadhil
- Qiao, Ying
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3656811
url: https://www.scopus.com/pages/publications/105028274819?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 15514--15532
keywords:
- Blockchain-lite security
- constrained reinforcement learning
- low-latency networks
- multiagent systems
- resource allocation
- sixth-generation (6G) edge computing
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

# paper-2793 — EdgePlus: A Multiagent Reinforcement Learning Framework for Dynamic Task Allocation in 6G Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In smart-city air-quality monitoring, millions of IoT sensors generate time-sensitive data that must be processed within strict end-to-end deadlines, under dynamic mobility conditions, and with strong security guarantees. In this study, we present EdgePlus, a unified sixth-generation (6G) framework that couples 1) masked cooperative PPO (CCPPO) enforcing feasibility at sampling time (routing order, slice quotas, resource limits), 2) a constricted particle swarm optimization (PSO) outer loop that escapes local optima under strict SLA gates, 3) a lightweight advisory layer (Nash sharing, Ziegler–Nichols-initialized PID, and leader election) that biases logits without breaking masks, and 4) a two-tier blockchain-lite ledger [edge proof-of-authority (PoA), cloud Byzantine fault-tolerant BFT)] whose reputation and debt signals feedback into state, reward, and masks. In a 100 km<sup>2</sup> city-scale simulator (ten clusters; three load regimes of 50 000, 100 000, and 150 000 tasks). Under light load, all methods reach 100% success with seconds-level latencies and no observable penalty from masking or security. At stress (150k), EdgePlus achieves the highest on-time completion rate (82.77%), highest throughput (206.93), lowest violation rate (17.23%), and lowest 15 percentile latency (L<sub>p</sub><sub>50</sub> of 53.23 s). Ablations confirmed that feasibility masks dominate performance: removing them increases violations by 5.5%–10.0% points and tail latency (L<sub>p</sub><sub>95</sub>) by 26–47 s, while advisory and PSO deliver smaller but consistent gains. The PID controller remains robust under ±20% gain drift (settling ≈ 2.7–2.9 s) by design-time Jury certification. In security experiments, baseline confidentiality, integrity, and availability (CIA)/auth attacks are mitigated at 98%–99% and advanced (nonphysical-layer) threats achieve 70%–83% defense with strong efficiency. Edge-tier PoA validation adds a median ≈ 0.39 ms per partial block for validator sets up to 10 and remains sub-ms with partitioned sub-quorums up to 30, while cloud BFT provides accountable finality off the critical path. In short, EdgePlus delivers a single, coherent scheduling–control–security stack for 6G edge computing, built on a feasibility-first design that preserves reliability, locality, and security at scale. © 2014 IEEE. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2793.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
