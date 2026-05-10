---
id: paper-1569
title: Distributed Inference Optimization for Large Language Model in Edge-Cloud Collaborative Networks
authors:
- Feng, Zideng
- Lu, Lu
- Li, Qin
- Chai, Yuhao
- Zhang, Zhenyu
- Zhang, Yong
- Teng, Yinglei
- Guo, Da
venue: IEEE International Conference on Communications
venue_type: conference
year: 2025
doi: 10.1109/ICC52391.2025.11160773
url: https://www.scopus.com/pages/publications/105018456705?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6161--6166
keywords:
- deep reinforcement learning
- edge-cloud computing
- Large language model
- model partition
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1569 — Distributed Inference Optimization for Large Language Model in Edge-Cloud Collaborative Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the progressive evolution of large language models (LLMs) and the increasing need of computing for 6G, it becomes crucial for multiple network nodes with limited computing resources to share the need for large model inference. Model partition methods have been proposed to enable computation-intensive artificial intelligence (AI) services by splitting an AI model across multi-edge and cloud nodes. In this paper, a distributed inference optimization framework for transformer decoder-only based LLMs (DIO-LLMs) is proposed in edge-cloud collaborative networks. The partitioning and offloading strategy is determined based on the computing workload and network status. DIO-LLMs specifically accounts for the parallel execution capabilities of the transformer architecture. It employs a two-phase model partitioning strategy, comprising inter-layer and intra-layer partitions, to effectively distribute LLMs across edge and cloud nodes. Additionally, to mitigate inference latency under resource limitations, a Greedy Proximal Policy Optimization (GPPO) based algorithm has been developed to devise optimal strategies. Simulation results indicate that under memory constraints, the proposed algorithm can reduce inference latency more effectively than other baseline algorithms.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1569.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
