---
id: paper-1852
title: Interactive Satellite Autonomous Data Analysis and Diagnosis via Low-Cost Reasoning Payload Enabled by DeepSeek Distillation Model
authors:
- Lin, Yinxiang
- Huang, Haishang
- Gong, Zeyu
- Chen, Pei
venue: Proceedings of the International Astronautical Congress, IAC
venue_type: conference
year: 2025
doi: 10.52202/083091-0016
url: https://www.scopus.com/pages/publications/105035996626?origin=resultslist
publisher: International Astronautical Federation, IAF
pages: 153--160
keywords:
- DeepSeek distillation model
- LLM
- Question answering
- Time series data
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1852 — Interactive Satellite Autonomous Data Analysis and Diagnosis via Low-Cost Reasoning Payload Enabled by DeepSeek Distillation Model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The advancement of commercial space technology has driven satellites toward higher functional density, with accelerated adoption of innovative hardware/software solutions. This rapid iteration, however, leads to insufficient reliability of long-term operational data, presenting new challenges for autonomous satellite management. This study proposes an embedded architecture for autonomous satellite data analysis and diagnosis employing a low-cost reasoning payload based on the DeepSeek distillation model. By integrating an onboard low-cost reasoning unit, the system aggregates extensive operational data aligned with autonomous objectives while sharing analytical outcomes with ground experts via structured sparse interactions. Experimental validation was conducted on an upcoming CubeSat mission: For novel on-orbit deployable payloads, the satellite captures multidimensional datasets including current, voltage, temperature, sensor readings, and continuous acceleration, exceeding conventional telemetry resolution thresholds. These datasets feed into the reasoning payload, which synergizes preloaded ground-test references to perform closed-loop orbital status diagnosis and generate actionable insights for optimizing subsequent ground tests to achieve full coverage of orbital operational regimes. Regarding satellite-level management, the reasoning payload processes fused datasets combining ground-uploaded mission plans with time-synchronized internal telemetry to identify dynamic efficiency bottlenecks in task execution. It further delivers prescriptive analytics for adaptive mission sequence optimization. This implementation utilizes an ARM processor (16GB RAM) hosting the distilled DeepSeek-R1-14b model, demonstrating a paradigm shift toward edge-computing-enabled satellite autonomy and establishing a resource-efficient human-AI co-evolution framework for space systems. Copyright ©2025 by the International Astronautical Federation (IAF). All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1852.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
