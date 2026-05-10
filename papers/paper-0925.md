---
id: paper-0925
title: Energy Cost Modelling for Optimizing Large Language Model Inference on Hardware Accelerators
authors:
- Geens, Robin
- Shi, Man
- Symons, Arne
- Fang, Chao
- Verhelst, Marian
venue: International System on Chip Conference
venue_type: conference
year: 2024
doi: 10.1109/SOCC62300.2024.10737844
url: https://www.scopus.com/pages/publications/85210589021?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- Computer graphics equipment
- Decoding
- Edge computing
- Graphics processing unit
- Photomapping
- Problem oriented languages
- Cloud-based
- Cost models
- Energy cost
- Energy efficient
- GPU computing
- Hardware accelerators
- Hardware architecture
- High energy consumption
- Language model
- Model inference
- Carbon footprint
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
    my_justification: LLM as workload
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

# paper-0925 — Energy Cost Modelling for Optimizing Large Language Model Inference on Hardware Accelerators

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rise of Large Language Models (LLMs) has significantly escalated the demand for efficient LLM inference, primarily fulfilled through cloud-based GPU computing. This approach, while effective, is associated with high energy consumption resulting in large operating expenses and considerable carbon footprints. In the meantime, growing privacy concerns advocate for inference on edge devices, which are constrained by a limited battery capacity. Both cloud and edge scenarios necessitate energy-efficient LLM inference strategies.This paper addresses the urgent need for energy-efficient inference by proposing an open-source framework designed to model LLM workloads on dedicated accelerators. Our framework facilitates early identification of energy bottlenecks through rapid modeling of the execution efficiency of a wide range of LLMs on diverse hardware architectures. Key innovations include a PyTorch-based generalized LLM template to easily generate custom workload graphs, extensions of the ZigZag design space exploration framework and techniques to significantly speed up simulation time at a negligible loss of accuracy. Using a representative hardware architecture, we conduct three case studies to reveal critical energy bottlenecks in Llama2-7B inference, revealing that 1) memory-bound computing in the decode stage is detrimental not only for the latency, but also for the energy cost; 2) aggressive weight-only quantization can reduce the energy cost by 4.6 × and shift the bottleneck from weight fetching to the attention mechanism; 3) in edge scenarios, the relative energy cost of the prefill stage is more significant, encouraging efforts to optimize both prefill and decode stage. Our framework is available open-source at github.com/KULeuven-MICAS/zigzag-llm.  © 2024 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0925.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
