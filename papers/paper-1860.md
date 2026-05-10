---
id: paper-1860
title: Smart City Traffic Flow and Signal Optimization Using STGCN-LSTM and PPO Algorithms
authors:
- Lin, Tuxiang
- Lin, Rongliang
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2024.3519512
url: https://www.scopus.com/pages/publications/85212627245?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 15062--15078
keywords:
- intelligent transportation systems
- Long short-term memory (LSTM)
- proximal policy optimization (PPO)
- spatio-temporal graph convolutional networks (STGCN)
- traffic flow prediction
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-1860 — Smart City Traffic Flow and Signal Optimization Using STGCN-LSTM and PPO Algorithms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Urban traffic congestion remains a critical challenge for smart city development, necessitating innovative approaches to improve traffic flow and reduce delays. This study presents a novel framework that integrates the Spatiotemporal Graph Convolutional Network-Long Short-Term Memory (STGCN-LSTM) model for traffic flow prediction with the Proximal Policy Optimization (PPO) algorithm for dynamic traffic signal control. The STGCN-LSTM model captures complex spatiotemporal dependencies, achieving an R2 of 0.904 on the METR-LA dataset. Extensive experiments and ablation studies highlight the complementary strengths of STGCN and LSTM, with the hybrid model outperforming standalone variants. The PPO algorithm dynamically adjusts signal timings, reducing vehicle waiting times by 30% and increasing traffic throughput by 15%. Incorporating external factors, such as weather and holidays, enhances the framework's robustness in dynamic conditions, including adverse weather and traffic surges. GPU acceleration ensures scalability, enabling deployment in large-scale urban networks efficiently. This framework demonstrates significant potential to address urban congestion, reduce carbon emissions by 12%, and support sustainable urban development. Future research will explore edge computing, multi-agent reinforcement learning, and real-time data integration to further enhance scalability and adaptability.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1860.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
