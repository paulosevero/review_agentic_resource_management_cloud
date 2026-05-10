---
id: paper-2887
title: Resource-Efficient Personal Large Language Models Fine-Tuning With Collaborative Edge Computing
authors:
- Ye, Shengyuan
- Ouyang, Bei
- Qian, Tianyi
- Zeng, Liekang
- Li, Jingyi
- Du, Jiangsu
- Chu, Xiaowen
- Xing, Guoliang
- Chen, Xu
venue: IEEE Transactions on Parallel and Distributed Systems
venue_type: journal
year: 2026
doi: 10.1109/TPDS.2026.3654957
url: https://www.scopus.com/pages/publications/105027963136?origin=resultslist
publisher: IEEE Computer Society
pages: 680--696
keywords:
- collaborative edge computing
- distributed training
- Edge intelligence
- personal LLM fine-tuning
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

# paper-2887 — Resource-Efficient Personal Large Language Models Fine-Tuning With Collaborative Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) have enabled transformative applications at the network edge, such as intelligent personal assistants. However, data privacy and security concerns necessitate a shift from cloud-centric paradigms to edge-based fine-tuning for personal LLMs. This transition is significantly hindered by intensive computational requirements and inherent resource scarcity, creating a “resource wall” that compromises training efficiency and feasibility. While current parameter-efficient fine-tuning (PEFT) and resource management strategies attempt to mitigate these constraints, they remain insufficient for the limited capacities of individual edge devices. To address these challenges, we propose PAC+, a resourceefficient collaborative edge AI framework for in-situ personal LLM fine-tuning. PAC+ overcomes the resource bottlenecks through a sophisticated algorithm-system codesign: (1) Algorithmically, PAC+ introduces a fine-tuning technique optimized for parameters, time, and memory. It utilizes Parallel Adapters to circumvent the need for a full backward pass through the LLM backbone. Furthermore, an activation cache mechanism streamlines the process by negating redundant forward passes across multiple epochs. (2) Systematically, PAC+ aggregates proximate edge devices into a collective resource pool, employing hybrid data and pipeline parallelism to orchestrate distributed training. By leveraging the activation cache, PAC+ enables the exclusive fine-tuning of Parallel Adapters via data parallelism, effectively bypassing the backbone's constraints. Extensive evaluation of the prototype implementation demonstrates that PAC+ significantly outperforms existing collaborative edge training systems, achieving up to a 9.7× end-to-end speedup. Furthermore, compared to mainstream LLM fine-tuning algorithms, PAC+ reduces memory footprint by up to 88.16%. © 1990-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2887.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
