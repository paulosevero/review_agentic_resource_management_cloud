---
id: paper-2677
title: 'ACL: Adaptive Chunking of Large Language Models for Efficient Inference on Automotive Edge Devices'
authors:
- Lin, Yufei
- Xu, Tianxiang
- Ye, Chengwei
- Zhang, Huanzhen
- Wang, Kangsheng
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-981-95-3055-7_1
url: https://www.scopus.com/pages/publications/105023163358?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 1--11
keywords:
- Adaptive Partitioning
- Automotive Edge Devices
- Inference Optimization
- Large Language Models
- Latency Reduction
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

# paper-2677 — ACL: Adaptive Chunking of Large Language Models for Efficient Inference on Automotive Edge Devices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large language models (LLMs) increasingly drive intelligent services within automotive edge computing. However, deploying these models efficiently remains challenging due to diverse hardware setups and limited computational resources typical of automotive edge environments. Existing deployment strategies often disregard hardware diversity, resulting in suboptimal resource use and compromised performance, particularly under peak inference workloads. Consequently, computing elements like CPUs and integrated GPUs are frequently idle, with tasks excessively dependent on discrete GPUs. To address this, we propose a dynamic inference partitioning strategy named Hardware-Aware Dynamic Scheduling (ACL), tailored specifically for automotive edge computing. Our approach leverages the inherent distinction between initial token-processing phases (prefill) and subsequent token generation phases (decode) within LLM inference. By adaptively distributing these phases across heterogeneous hardware units, ACL maximizes resource utilization and balances workloads effectively. Empirical evaluations indicate that ACL significantly enhances inference performance. Furthermore, our framework demonstrates robust efficiency improvements consistently across various LLM architectures, highlighting its adaptability and effectiveness in heterogeneous automotive computing scenarios. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2677.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
