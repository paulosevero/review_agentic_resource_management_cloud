---
id: paper-1902
title: 'TickIt: Leveraging Large Language Models for Automated Ticket Escalation'
authors:
- Liu, Fengrui
- He, Xiao
- Zhang, Tieying
- Chen, Jianjun
- Li, Yi
- Yi, Lihua
- Zhang, Haipeng
- Wu, Gang
- Shi, Rui
venue: Proceedings of the ACM SIGSOFT Symposium on the Foundations of Software Engineering
venue_type: conference
year: 2025
doi: 10.1145/3696630.3728558
url: https://www.scopus.com/pages/publications/105013965244?origin=resultslist
publisher: Association for Computing Machinery
pages: 343--354
keywords:
- Cloud platform ticket
- Large language model
- Ticket escalation
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
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_leveraging_llm
    - ovr_modifier_by_llm
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-1902 — TickIt: Leveraging Large Language Models for Automated Ticket Escalation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In large-scale cloud service systems, support tickets serve as a critical mechanism for resolving customer issues and maintaining service quality. However, traditional manual ticket escalation processes encounter significant challenges, including inefficiency, inaccuracy, and difficulty in handling the high volume and complexity of tickets. While previous research has proposed various machine learning models for ticket classification, these approaches often overlook the practical demands of real-world escalations, such as dynamic ticket updates, topic-specific routing, and the analysis of ticket relationships. To bridge this gap, this paper introduces TickIt, an innovative online ticket escalation framework powered by Large Language Models. TickIt enables topic-aware, dynamic, and relationship-driven ticket escalations by continuously updating ticket states, assigning tickets to the most appropriate support teams, exploring ticket correlations, and leveraging category-guided supervised fine-tuning to continuously improve its performance. By deploying TickIt in ByteDance’s cloud service platform Volcano Engine, we validate its efficacy and practicality, marking a significant advancement in the field of automated ticket escalation for large-scale cloud service systems. © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_leveraging_llm', 'ovr_modifier_by_llm', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: llm_as_workload, pattern_id: ovr_leveraging_llm, matched_substring: "Leveraging Large Language" }`
  - `{ category: llm_as_workload, pattern_id: ovr_modifier_by_llm, matched_substring: "powered by Large Language" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Large Language Models" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1902.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
