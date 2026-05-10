---
id: paper-2300
title: Resource Management for Low-Latency Cooperative Fine-Tuning of Foundation Models at the Network Edge
authors:
- Wu, Hai
- Chen, Xu
- Huang, Kaibin
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2025
doi: 10.1109/TWC.2025.3544333
url: https://www.scopus.com/pages/publications/85219583356?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4839--4852
keywords:
- edge computing
- fine-tuning
- Foundation models (FoMo's)
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

# paper-2300 — Resource Management for Low-Latency Cooperative Fine-Tuning of Foundation Models at the Network Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of large-scale foundation models (FoMo's) that can perform human-like intelligence motivates their deployment at the network edge for devices to access state-of-the-art artificial intelligence (AI). For better user experiences, the pre-trained FoMo's need to be adapted to specialized downstream tasks through fine-tuning techniques. To transcend a single device's memory and computation limitations, we advocate multi-device cooperation within the device-edge cooperative fine-tuning (DEFT) paradigm, where edge devices cooperate to simultaneously optimize different parts of fine-tuning parameters within a FoMo. The edge server is responsible for coordination and gradient aggregation. However, the parameter blocks reside at different depths within a FoMo architecture, leading to varied computation latency-and-memory cost due to gradient backpropagation-based calculations. The heterogeneous on-device computation and memory capacities and channel conditions necessitate an integrated communication-and-computation (C2) allocation of local computation loads and uplink communication resources to achieve low-latency (LoLa) DEFT. To this end, we consider the depth-ware DEFT block allocation problem. The involved optimal block-device matching is tackled by the proposed low-complexity Cutting-RecoUNting-CHecking (CRUNCH) algorithm, which is designed by exploiting the monotone-increasing property between block depth and computation latency-and-memory cost. Next, the joint bandwidth-and-block allocation (JBBA) makes the problem more sophisticated, i.e., mathematically NP-hard. We observe a splittable Lagrangian expression through the transformation and analysis of the original problem, where the variables indicating device involvement are introduced to decouple the block and bandwidth allocation. Then, the dual ascent method is employed to tackle the JBBA problem iteratively. Within each iteration, block allocation and bandwidth allocation are optimized concurrently. The optimal block allocation sub-problem is solved efficiently by applying the Hungarian method facilitated by the proposed CRUNCH algorithm. On the other hand, the bandwidth allocation sub-problem is solved in closed form, shedding light on favorable allocations to resource-limited devices. Through extensive experiments conducted on the GLUE benchmark, our results demonstrate significant latency reduction achievable by LoLa DEFT for fine-tuning a RoBERTa model.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2300.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
