---
id: paper-2612
title: Task placement and traffic interleaving for cross-datacenter LLM training over optical networks
authors:
- Hu, Qiaojun
- Wang, Wei
- Huang, Chongzhu
- Wang, Xiaoyu
- Li, Yajie
- Zhao, Yongli
- Zheng, Yanlei
- Tan, Yanxia
- Zhang, Jie
venue: Journal of Optical Communications and Networking
venue_type: journal
year: 2026
doi: 10.1364/JOCN.579324
url: https://www.scopus.com/pages/publications/105029741678?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 137--149
keywords:
- Adaptive optics
- Computational efficiency
- Fiber optic networks
- Light transmission
- Optical communication
- Program processors
- '''current'
- Data-transmission
- Datacenter
- Feasible solution
- Interleavings
- Language model
- Model size
- Model training
- Optical-
- Over provisioning
- Bandwidth
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

# paper-2612 — Task placement and traffic interleaving for cross-datacenter LLM training over optical networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the continuous growth of large language model (LLM) sizes, individual datacenters are increasingly insufficient to support LLM training. Cross-datacenter training has become a feasible solution, where optical networks play a crucial role in data transmission. However, current optical networks suffer from severe over-provisioning issues, primarily due to the conflict between the bursty nature of LLM traffic and the fixed bandwidth of optical network connections. Therefore, this paper presents CrossOptic, a novel, to our knowledge, framework for optimizing cross-datacenter LLM training over optical networks. The proposed solution addresses the critical challenges of bandwidth under-utilization in optical networks and excessive communication overhead in distributed LLM training. CrossOptic integrates two synergistic components: adaptive GPU resource orchestration (AGRO) for communication-minimizing task placement and traffic-interleaved connectivity provisioning (TICP) for bandwidth-efficient flow aggregation. Through comprehensive simulations using realistic GPT model workloads, CrossOptic outperforms conventional dedicated connection approaches by 38.1% in terms of optical resource utilization. For a GPT model with 529.6B parameters, compared with the training methods using data parallelism and pipeline parallelism between datacenters, CrossOptic reduces the iteration time by 55% and 14%, respectively. The framework achieves significant cost efficiency in the optical infrastructure while supporting the computational demands of LLM training. © 2009-2012 Optica Publishing Group.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2612.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
