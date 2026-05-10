---
id: paper-0893
title: 'Online two-timescale service placement for time-sensitive applications in MEC-assisted network: A TMAGRL approach'
authors:
- Du, An
- Jia, Jie
- Chen, Jian
- Guo, Liang
- Wang, Xingwei
venue: Computer Networks
venue_type: journal
year: 2024
doi: 10.1016/j.comnet.2024.110339
url: https://www.scopus.com/pages/publications/85189026226?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Mobile edge computing
- Proactive replicas pre-deployment
- Reactive service migration
- Reinforcement learning algorithm
- Time-sensitive
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

# paper-0893 — Online two-timescale service placement for time-sensitive applications in MEC-assisted network: A TMAGRL approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) integrated with the Network Functions Virtualization (NFV) technique has been regarded as a promising solution for flexible services provision and user service experience improvement. However, existing service placement in such systems still faces the challenge of satisfying computing tasks with strict latency requirements, especially when massive mobile users roam around different coverage areas of edge servers. For this purpose, we first adopt a novel service placement framework that combines proactive replicas pre-deployment and reactive service migration. Based on this, we investigate the dynamic placement problem of multiple types of services achieved by the various virtualized network functions (VNFs) to minimize long-term redeployment costs in MEC-assisted systems, subject to the completion deadline of tasks and limited computing resources of edge servers. Considering that the update timescale of VNF replicas pre-deployment is different, we design a novel two-timescale multi-agent graph convolutional network-based reinforcement learning algorithm (TMAGRL) by invoking a long-timescale training layer for proactive VNF replicas placement and a short-timescale training layer for reactive VNF migration. Extensive numerical results reveal that TMAGRL, based on the designed hybrid framework, can learn a VNF placement strategy to adapt to the dynamics of the system without any prior information. Moreover, we verify its superior performance in terms of average service response latency and overall redeployment cost by comparing it with baselines. © 2024

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0893.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
