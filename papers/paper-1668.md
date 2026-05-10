---
id: paper-1668
title: 'Dynamic Model Deployment, Batch Scheduling and Resource Allocation in MLLM-enabled Edge-Cloud Networks: A Multi-Agent Two-Timescale DRL Approach'
authors:
- Huang, Hualong
- Du, Yongkang
- Zhan, Wenhan
- Duan, Hancong
- Peng, Kai
- Cheng, Yamin
- Ye, Yalan
- Zhao, Zitian
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3611003
url: https://www.scopus.com/pages/publications/105016601032?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- batch processing
- computation offloading
- deep reinforcement learning
- Edge-Cloud collaboration
- MLLM inference
- resource allocation
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

# paper-1668 — Dynamic Model Deployment, Batch Scheduling and Resource Allocation in MLLM-enabled Edge-Cloud Networks: A Multi-Agent Two-Timescale DRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The deployment of multimodal large language models (MLLMs) on resource-constrained mobile devices poses significant challenges due to their high computational demands. This paper introduces a novel two-timescale optimization framework for efficient MLLM inference in Edge-Cloud networks, addressing the problem of multi-timescale resource management by jointly optimizing slow-timescale MLLMs deployment decisions and fast-timescale batch scheduling, GPU resource allocation, and bandwidth allocation under dynamic network conditions and spatiotemporal request heterogeneity. Our key innovation is a hierarchical twin delayed deep deterministic policy gradient (HALTD3) algorithm that integrates attention mechanisms and long short-term memory networks to optimize slow-timescale MLLMs deployment and fast-timescale resource allocation, minimizing weighted system costs including deployment cost, end-to-end latency, and energy consumption, while meeting stringent quality-of-service requirements. Extensive experiments demonstrate that the HALTD3 algorithm substantially outperforms baseline methods in reducing system costs across diverse MLLM workloads and dynamic network scenarios, validating its effectiveness for practical edge-cloud collaborative inference. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1668.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
