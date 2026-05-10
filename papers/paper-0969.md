---
id: paper-0969
title: Online delay optimization for MEC and RIS-assisted wireless VR networks
authors:
- Jia, Jie
- Yang, Leyou
- Chen, Jian
- Ma, Lidao
- Wang, Xingwei
venue: Wireless Networks
venue_type: journal
year: 2024
doi: 10.1007/s11276-024-03706-4
url: https://www.scopus.com/pages/publications/85188230732?origin=resultslist
publisher: Springer
pages: 2939--2959
keywords:
- Delay optimization
- MEC
- RIS
- VR
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0969 — Online delay optimization for MEC and RIS-assisted wireless VR networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As wireless networks continue to advance, virtual reality (VR) transmission over wireless connections is progressively transitioning from concept to practical application. Although this technology can significantly enhance the VR user experience, its development bottleneck lies in the computing capacity of devices and transmission latency. Considering the limited computational resources of VR devices for rendering tasks, multi-access edge computing (MEC) servers are introduced to provide powerful computing capabilities. To cope with transmission latency, reconfigurable intelligent surface (RIS) enhances links between base stations (BSs) and users. Based on these two technologies, we propose a RIS-assisted VR streaming model, where BSs are equipped with MEC servers to assist data rendering. Firstly, the user association, power control, and RIS phase shift optimization problems in the VR transmission system are jointly modeled and analyzed, establishing a long-term minimization of the interaction delay model. Secondly, by modeling the optimization problem as a Markov decision process (MDP), a joint optimization framework based on multi-agent deep reinforcement learning (MADRL) is proposed. In this framework, we have separately designed two dedicated algorithms for discrete and continuous variables. Furthermore, multiple agents can provide feedback based on user experience and cooperate with each other to improve the joint strategy. Finally, the performance and superiority of the proposed solution and algorithm are validated through simulation experiments in different application scenarios. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0969.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
