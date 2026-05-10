---
id: paper-1622
title: Energy-efficient cloud-edge collaborative model integrating digital twins and machine learning for scalable and adaptive distributed networks
authors:
- Han, Lei
- Lei, Min
- He, Guilin
- Li, Yangyang
- Zhao, Yaopeng
venue: 'Sustainable Computing: Informatics and Systems'
venue_type: journal
year: 2025
doi: 10.1016/j.suscom.2025.101157
url: https://www.scopus.com/pages/publications/105008806864?origin=resultslist
publisher: Elsevier Inc.
pages: ''
keywords:
- Cloud-edge collaboration
- Digital twins
- Distributed networks
- Machine learning
- Network optimization
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1622 — Energy-efficient cloud-edge collaborative model integrating digital twins and machine learning for scalable and adaptive distributed networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The exponential growth of distributed networks, as seen in smart grids, IoT, and industrial automation, have added to the demands for effective and adaptive optimization systems. Traditional cloud solutions, while successful in providing global insights and scalability, often suffer from high latency and limited responsiveness, whereas edge-based models excel at instant decision making but lack global synergy and scale. In an effort to overcome these constraints, this paper proposes a novel Cloud-Edge Collaborative Optimization Framework, which leverages the latest machine learning and digital twin algorithms, to scale up distribution networks. The model relies on Long Short-Term Memory (LSTM) networks at the edge layer to forecast traffic in real time and make local decisions, and Multi-Agent Reinforcement Learning (MARL) at the cloud layer to coordinate resources across the globe. Digital twins facilitate real-time flexibility, dynamic simulation and feedback for continuous improvement. This proposed model was extensively tested against actual network datasets. We noted a 50 % reduction in latency compared to cloud-only architectures, with latency on average, baselined at 35.34 ms, reduced to 17.67 ms; additionally, we noted 23 % more resource utilization compared to edge-only setups based on the average of 10 simulation runs. We had real world IoT traffic data for the experimentation with throughput of 50–100 Mbps and PDR greater than 90 % (consistently), which demonstrates that the network operated robustly under changing conditions; we averaged the results for reliability and significance. This study provides an ideal foundation for future work on digital-twin-enhanced cloud-edge architectures. © 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1622.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
