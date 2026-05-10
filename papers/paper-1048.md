---
id: paper-1048
title: Multi-objective cooling control optimization for air-liquid cooled data centers using TCN-BiGRU-Attention-based thermal prediction models
authors:
- Lin, Jianpeng
- Lin, Wenjun
- Lin, Weiwei
- Liu, Tianyi
- Wang, Jiangtao
- Jiang, Hongliang
venue: Building Simulation
venue_type: journal
year: 2024
doi: 10.1007/s12273-024-1185-7
url: https://www.scopus.com/pages/publications/85207009200?origin=resultslist
publisher: Tsinghua University
pages: 2145--2161
keywords:
- cooling control
- data center
- energy saving
- multi-objective optimization
- thermal prediction
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-1048 — Multi-objective cooling control optimization for air-liquid cooled data centers using TCN-BiGRU-Attention-based thermal prediction models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the breakthroughs in generative artificial intelligence (GAI) models, the vast computational demands are placing an unprecedented burden on the data center (DC) energy supply. The cooling system is the second major energy consumer in the DC, maintaining the safe and efficient operation of computing equipment. However, time-varying temperature gradients and power distribution pose a considerable challenge for efficient cooling management in DCs. For this problem, this work proposes a multi-objective cooling control optimization (MCCO) method to minimize cooling energy consumption while maximizing the rack cooling index (RCI) to ensure energy efficiency and security of hybrid-cooled DCs. The proposed method relies on high-fidelity models that characterize the dynamic thermal evolution and cooling power. Therefore, a novel network model (TCN-BiGRU-Attention) combining temporal convolutional network (TCN), bidirectional gated recurrent unit (BiGRU), and attention mechanism is designed to capture the features of multivariate time-series to predict temperature changes in thermal environments and cooling loops. Moreover, considering the complex heat transfer and operational characteristics of hybrid cooling systems, a machine learning (ML)-based power model is constructed to evaluate the holistic cooling power. Subsequently, the NSGA-II algorithm formulates the optimal cooling decision based on the predicted thermal distribution and cooling power, realizing the trade-off between energy consumption and cooling effectiveness. The results of numerical experiments using Marconi 100 data traces suggest that the proposed MCCO significantly reduces cooling energy consumption in summer and winter while maintaining the RCI above 95%. © Tsinghua University Press 2024.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1048.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
