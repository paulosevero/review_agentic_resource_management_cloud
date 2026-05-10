---
id: paper-1381
title: 'Think Fast, Infer Smart: A Hybrid Distributed LLMs Inference at the Wireless Edge'
authors:
- Albaseer, Abdullatif
- Bentafat, Elmahdi
- Hamood, Moqbel
- Abdallah, Mohamed
- Al-Fuqaha, Ala
- Hamdi, Mounir
venue: IEEE International Symposium on Personal, Indoor and Mobile Radio Communications, PIMRC
venue_type: conference
year: 2025
doi: 10.1109/PIMRC62392.2025.11274878
url: https://www.scopus.com/pages/publications/105030546202?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- and bandwidth optimization
- dynamic head-wise layer-wise partitioning
- Edge computing
- Large Language Models (LLMs)
- latency
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1381 — Think Fast, Infer Smart: A Hybrid Distributed LLMs Inference at the Wireless Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deploying large language models (LLMs) at the wireless edge is a promising solution to meet the low-latency, high-computation demands of next-generation AI applications. Although the existing literature has introduced approaches to enable distributed LLM inference, these methods largely overlook the distinct computational and communication characteristics of the two-phase LLM inference process - the pre-fill and decode phases. This oversight leads to suboptimal performance and limits scalability in real-world deployments. To address these issues, we propose a novel collaborative inference framework that strategically minimizes inference latency by optimally distributing computational loads across edge devices, the edge server, and the cloud. Our approach introduces a hybrid framework that combines head-wise parallel processing with layer-wise partitioning of LLM models, supported by a dual-phase optimization strategy. In the pre-fill phase, we optimize assigning attention heads to selected edge devices for parallel computation and efficient resource use. We then optimize for minimal latency by selecting participants, determining head assignments per device, and allocating bandwidth while meeting all constraints. In the de-code phase, our framework adaptively decides whether to execute computations locally on the edge server, offload them to the cloud, or redistribute tasks among edge devices, optimizing this decision based on the remaining latency budget and the sequential nature of the decode phase. The simulation results demonstrate that the proposed framework significantly outperforms the baseline methods, achieving a 56% reduction in inference latency, 40% improvement in bandwidth efficiency and 35% improvement in resource utilization.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1381.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
