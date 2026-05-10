---
id: paper-1253
title: Location-Privacy-Aware Service Migration Against Inference Attacks in Multiuser MEC Systems
authors:
- Wang, Weixu
- Zhou, Xiaobo
- Qiu, Tie
- He, Xin
- Ge, Shuxin
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3290145
url: https://www.scopus.com/pages/publications/85163541005?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1413--1426
keywords:
- Location privacy
- multiaccess edge computing (MEC)
- multiuser
- service migration
- soft actor-critic (SAC)
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

# paper-1253 — Location-Privacy-Aware Service Migration Against Inference Attacks in Multiuser MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In multiaccess edge computing (MEC) systems, service migration has been extensively applied to ensure service quality by migrating services to follow mobile users. The existing migration methods mainly focus on optimizing service response latency and migration costs by predicting user's movements. However, some malicious adversaries can learn auxiliary knowledge, i.e., users' mobility model and service migration trajectory, and launch location inference attacks to infer user locations. This leads to serious personal security threats, like malvertising, fraud and kidnapping. In this article, we propose a location privacy-aware service migration method to against adversaries' location inference attacks in multiuser MEC systems. First, we adopt an entropy-based location privacy metric to accurately measure user's location privacy leakage risk. Then, we formulate the service migration progress as a joint optimization problem that minimizes service response latency and location privacy leakage risk. To cope with interuser interference, we developed a multiagent soft actor-critic (MASAC) algorithm to help users collaboratively make service migration decisions. Finally, simulations based on real-world user movement trajectories were conducted to demonstrate the superiority of the proposed method. Evaluation and analysis results showed that our proposed method can effectively protect user location privacy while maintaining a low service response latency.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1253.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
