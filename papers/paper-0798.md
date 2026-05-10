---
id: paper-0798
title: Task Offloading Based on Application Hit Ratio
authors:
- Zhang, Junna
- Wang, Xinxin
- Ding, Chuntao
- Zhao, Xiaoyan
- Wang, Shangguang
venue: Proceedings - 2023 IEEE International Conference on Web Services, ICWS 2023
venue_type: conference
year: 2023
doi: 10.1109/ICWS60048.2023.00017
url: https://www.scopus.com/pages/publications/85173851360?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 36--42
keywords:
- Application Hit Ratio
- Edge Computing
- Improved Multi-Agent Q-Learning Algorithm
- Load Balancing
- Multi-Task Offloading
- Service Placement
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0798 — Task Offloading Based on Application Hit Ratio

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> It has become mainstream for mobile devices to offload latency-sensitive applications to edge servers for execution to meet low-latency requirements. However, the existing related studies lack the consideration of application hit ratio, which makes them unable to meet the increasingly complex offloading of multi-applications including multi-tasks. To this end, this paper proposes a Multi-task offloading and Service placement optimization (MSO) method with the goal of maximizing the application hit ratio to provide high-quality service. The proposed MSO is constructed with Improved Multi-Agent Q-Learning (IMAQL) and load-balancing algorithms. IMAQL aims to learn an optimal service placement policy by using Q-learning techniques. Next, the load-balancing algorithm is designed to offload tasks according to the service placement policy. To verify the effectiveness of the MSO method, we conduct extensive experiments on a publicly available dataset. The experimental results show that the proposed method can improve the application hit ratio by appropriately 2.6% to 9% compared with other methods. © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0798.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
