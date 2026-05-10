---
id: paper-0217
title: Scalable knowledge-defined orchestration for hybrid optical-electrical datacenter networks [Invited]
authors:
- Li, Qinhezi
- Fang, Hongqiang
- Li, Deyun
- Peng, Jianquan
- Kong, Jiawei
- Lu, Wei
- Zhu, Zuqing
venue: Journal of Optical Communications and Networking
venue_type: journal
year: 2020
doi: 10.1364/JOCN.12.00A113
url: https://www.scopus.com/pages/publications/85074968548?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: A113 - A122
keywords:
- Benchmarking
- Deep learning
- Multi agent systems
- Quality of service
- Reinforcement learning
- Bandwidth resource
- Convergence performance
- Data center networks
- Delay-sensitive applications
- Delay-tolerant applications
- Differentiated Services
- Network applications
- Residual resource
- Delay tolerant networks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0217 — Scalable knowledge-defined orchestration for hybrid optical-electrical datacenter networks [Invited]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To better provision fast-emerging network applications with various quality-of-service demands, datacenter network (DCN) operators need an effective network orchestration scheme that can coordinate IT and bandwidth resources for differentiated services in a timely manner. In this work, we consider a hybrid optical-electrical DCN (HOE-DCN) and study how to achieve scalable knowledge-defined network orchestration (KD-NO) for managing the delay-sensitive and delay-tolerant applications in it. For delay-sensitive applications, we leverage a multi-agent scheme to distribute the tasks of placing virtual machines (VMs) in server racks and routing VM traffic in electrical-optical inter-rack clouds to two cooperative deep reinforcement learning modules, respectively. Then, we utilize a classic-algorithm-based module to provision delay-tolerant applications with the residual resources in the HOE-DCN. We design the operation and coordination procedure of the KD-NO system and build a small HOE-DCN testbed that consists of four server racks to demonstrate its performance experimentally. Experimental results indicate that our KD-NO system can make timely and correct network orchestration decisions and have better convergence performance compared with the existing benchmark. © 2019 OSA.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0217.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
