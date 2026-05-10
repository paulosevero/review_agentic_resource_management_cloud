---
id: paper-2019
title: 'Beyond Terrestrial: LLM-Orchestrated DtS-IoT Networks for Ubiquitous Edge Intelligence'
authors:
- Pasandi, Hannaneh B.
- Rousseau, Franck
- Nadeem, Tamer
- Darabi, Sina
venue: ANAI 2025 - Proceedings of the 2025 ACM Workshop on Access Networks with Artificial Intelligence, Part of MobiCom 2025
venue_type: conference
year: 2025
doi: 10.1145/3737904.3768537
url: https://www.scopus.com/pages/publications/105026268635?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 41--45
keywords:
- Deep reinforcement learning
- Edge computing
- Federated learning
- Joint communication and sensing
- Large language models
- Satellite networks
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
  05-abstract-screening: include
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
    - ovr_llm_modifier
    - ovr_abs_llm_orchestrates
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
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

# paper-2019 — Beyond Terrestrial: LLM-Orchestrated DtS-IoT Networks for Ubiquitous Edge Intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents simulation-based insights into Joint Communication and Sensing (JCAS) optimization for direct-to-satellite access networks. We investigate three complementary approaches: (i) a hierarchical deep reinforcement learning framework for satellite beamforming, achieving an 18% throughput gain over heuristic baselines; (ii) a multi-modal federated learning architecture fusing 10 m Sentinel-1 SAR with terrestrial sensing, providing a ∼15% detection accuracy improvement under (ϵ, δ) = (1.2, 10<sup>-5</sup>) differential privacy guarantees; and (iii) a ground-based LLM-driven resource management system that reduces handover latency by 25% in vehicular mobility scenarios. Evaluations using NS-3, STK, TensorFlow, and OMNeT++ validate improvements with 95% confidence intervals across realistic traffic, IoT, and mobility settings. These results highlight opportunities and challenges for integrating AI techniques into satellite-terrestrial access networks, with implications for next-generation intelligent connectivity.  © 2025 Copyright held by the owner/author(s).

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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_llm_modifier', 'ovr_abs_llm_orchestrates']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: llm_as_workload, pattern_id: ovr_llm_modifier, matched_substring: "LLM-driven" }`
  - `{ category: llm_as_workload, pattern_id: ovr_abs_llm_orchestrates, matched_substring: "LLM-Orchestrate" }`
  - `{ category: llm_as_workload, pattern_id: ovr_abs_llm_orchestrates, matched_substring: "LLM-driven resource manage" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2019.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
