---
id: paper-1079
title: A Fault-Tolerant Mobility-Aware Caching Method in Edge Computing
authors:
- Ma, Yong
- Zhao, Han
- Guo, Kunyin
- Xia, Yunni
- Wang, Xu
- Niu, Xianhua
- Zhu, Dongge
- Dong, Yumin
venue: CMES - Computer Modeling in Engineering and Sciences
venue_type: journal
year: 2024
doi: 10.32604/cmes.2024.048759
url: https://www.scopus.com/pages/publications/85191083867?origin=resultslist
publisher: Tech Science Press
pages: 907--927
keywords:
- cooperative caching
- fault tolerance
- Mobile edge networks
- mobility
- multi-agent deep reinforcement learning
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

# paper-1079 — A Fault-Tolerant Mobility-Aware Caching Method in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) is a technology designed for the on-demand provisioning of computing and storage services, strategically positioned close to users. In the MEC environment, frequently accessed content can be deployed and cached on edge servers to optimize the efficiency of content delivery, ultimately enhancing the quality of the user experience. However, due to the typical placement of edge devices and nodes at the network’s periphery, these components may face various potential fault tolerance challenges, including network instability, device failures, and resource constraints. Considering the dynamic nature of MEC, making high-quality content caching decisions for real-time mobile applications, especially those sensitive to latency, by effectively utilizing mobility information, continues to be a significant challenge. In response to this challenge, this paper introduces FT-MAACC, a mobility-aware caching solution grounded in multi-agent deep reinforcement learning and equipped with fault tolerance mechanisms. This approach comprehensively integrates content adaptivity algorithms to evaluate the priority of highly user-adaptive cached content. Furthermore, it relies on collaborative caching strategies based on multi-agent deep reinforcement learning models and establishes a fault-tolerance model to ensure the system’s reliability, availability, and persistence. Empirical results unequivocally demonstrate that FT-MAACC outperforms its peer methods in cache hit rates and transmission latency. © 2024 Tech Science Press. All rights reserved.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1079.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
