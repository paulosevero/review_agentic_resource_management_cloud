---
id: paper-1584
title: 'Towards Energy-Efficient Edge Inference in Radio Cpns: A Mixture-of-Depths Transformer Based Tri-Parallel Distributed Approach'
authors:
- Gao, Liu
- Gao, Dixiang
- Xia, Nian
- Peng, Mugen
- Wang, Dong
- Liu, Xiqing
venue: IEEE International Conference on Communications
venue_type: conference
year: 2025
doi: 10.1109/ICC52391.2025.11160774
url: https://www.scopus.com/pages/publications/105018467696?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1019--1024
keywords:
- energy efficient
- Large language models
- parallelism
- radio CPNs
- Transformer
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
    my_justification: LLM as workload
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

# paper-1584 — Towards Energy-Efficient Edge Inference in Radio Cpns: A Mixture-of-Depths Transformer Based Tri-Parallel Distributed Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) have shown remarkable abilities by significantly scaling up model size, but this has also greatly increased their computing overhead. Traditional solutions to reduce the overhead are offloading inference tasks to cloud servers. With the evolution of computing power networks, computing resources are increasingly distributed at the network edge, allowing inference tasks to be handled locally. This edge inference can reduce traffic stress on backbone networks from cloud offloading and improve the utilization of heterogeneous edge computing power. However, the challenge is how to balance the gigantic computing workloads of LLMs with the limited computing power at the edge. To overcome this, a mixture-of-depths (MoD) Transformer based tri-parallel distributed approach was introduced. By dynamically allocating computing power to specific positions in the Transformer and parallel computing, this approach maximizes the capabilities of heterogeneous edge nodes to achieve resource-efficient inference. Simulation results showed that the proposal performs best in various edge environments, reducing inference delay by up to 24.3% and energy consumption by up to 37.5%, respectively.  © 2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1584.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
