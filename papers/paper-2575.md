---
id: paper-2575
title: 'NOMA-Assisted Mobile Edge Generation (MEG): Enabling Mobile Access to Large Models'
authors:
- Gan, Deqiao
- Xu, Xiaoxia
- Ge, Xiaohu
- Liu, Yuanwei
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2026
doi: 10.1109/TWC.2025.3648836
url: https://www.scopus.com/pages/publications/105028067030?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10002--10017
keywords:
- Artificial intelligence generated content (AIGC)
- large language model (LLM)
- mobile edge generation (MEG)
- non-orthogonal multiple access (NOMA)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2575 — NOMA-Assisted Mobile Edge Generation (MEG): Enabling Mobile Access to Large Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The popularity of artificial intelligence generated content (AIGC) is prompting the deployment of large language model (LLM) from cloud to edge networks, leading to mobile edge generation (MEG). Due to high latency and limited computational capabilities of mobile devices, personalized image generation for mobile healthcare and education requires edge-mobile generation paradigm. In this paper, a novel non-orthogonal multiple access (NOMA) assisted multi-user MEG framework is proposed for text-guided mobile image generation. NOMA enables concurrent access from multiple user equipments (UEs) to the edge-deployed large model, facilitating adjustable generation splitting. Specifically, the edge server (ES) partially generates the image and transmits it via downlink NOMA, while UEs complete the remaining parts using lightweight models. Both unlimited and limited energy budget scenarios are considered. 1) For unlimited energy budget, a joint generation splitting ratio and NOMA power allocation optimization problem is formulated, which minimizes the maximum (min-max) latency of UEs to ensure fairness. The closed-form globally optimal solutions based on Karush-Kuhn-Tucker (KKT) and Lambert-W theory are derived. Moreover, the superiority of MEG-NOMA over conventional MEG-orthogonal multiple access (OMA) is mathematically proved. 2) For limited energy budget, a multi-objective programming problem is formulated to minimize the latency of each UE, which leads to a user-centric latency minimization problem. The closed-form solutions of generation splitting ratio and power allocation are derived. Simulation results illustrate that the proposed MEG-NOMA outperforms the MEG-OMA in both two-user and multi-user cases. Compared to conventional MEG-OMA, the MEG-NOMA framework reduces the min-max latency and the user-centric latency by 33.01% and 9.86%, respectively. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2575.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
