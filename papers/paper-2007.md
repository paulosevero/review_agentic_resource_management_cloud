---
id: paper-2007
title: Inter-AGV Scheduling and a Novel Multi-Agent Collaborative Protocol for Intra-AGV Resource Allocation in MEC-Enabled Multi-AGV Scenarios
authors:
- Palomares, Javier
- Carmona-Cejudo, Estela
- Cervelló-Pastor, Cristina
- Coronado, Estefanía
- Chergui, Hatim
- Shuaib Siddiqui, Muhammad
venue: IEEE Open Journal of the Communications Society
venue_type: journal
year: 2025
doi: 10.1109/OJCOMS.2025.3567585
url: https://www.scopus.com/pages/publications/105004775716?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4238--4259
keywords:
- MEC
- Multi-agent collaboration
- Multi-AGV
- Resource allocation
- Scheduling
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: RL
    winning_category: rl
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2007 — Inter-AGV Scheduling and a Novel Multi-Agent Collaborative Protocol for Intra-AGV Resource Allocation in MEC-Enabled Multi-AGV Scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In modern novel collaborative multi-Automated Guided Vehicle (AGV) systems, vehicles are responsible for executing both mission-critical process-related operations and purely computational tasks, such as collision avoidance. This work investigates the problem of joint inter-AGV task placement and intra-AGV computational resource allocation in MEC-enabled multi-AGV environments. To address this challenge, a two-step strategy is proposed to maximize the number of scheduled and completed tasks across multiple AGVs while ensuring fair and efficient resource use within each AGV. The problem of inter-AGV task placement is solved by dynamically applying a catalog of deep reinforcement learning (DRL) models for varying numbers of AGVs. Training time for these models is reduced threefold by using datasets from existing optimization solvers. Transfer learning further reduces training times by up to 51%. Second, a multi-agent deep reinforcement learning (MADRL)-based collaborative protocol for dynamic intra- AGV resource allocation (MACP-DRA) is proposed, allowing AGVs to adjust computational resources dynamically. It incorporates a minimum guaranteed share strategy to ensure fair resource distribution while optimizing performance under dynamic workloads. Compared to existing MADRL approaches, MACP-DRA enhances conflict resolution efficiency while maintaining low computational cost. Evaluation results demonstrate that the proposed inter-AGV scheduling strategy approaches optimal performance while achieving a superior trade-off between decision time and task completion rates. Compared to a multi-agent DRL baseline, the proposed MACP-DRA models reduced resource conflicts by 54.9%, task processing delays by 35.7%, and resource underutilization by 9.93%, while maintaining minimal computational and energy consumption overhead. © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "RL"
- **winning_category:** 'rl'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_madrl, matched_substring: "MADRL" }`
  - `{ category: rl, pattern_id: rl_madrl, matched_substring: "MADRL" }`
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "In modern novel collaborative" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2007.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
