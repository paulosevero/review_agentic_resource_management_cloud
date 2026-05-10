---
id: paper-1935
title: 'MACU: A Multiagent Cache Updating Framework for IIoT Networks'
authors:
- Maiti, Ritabrata
- Madhukumar, A.S.
- Ernest, Tan Zheng Hui
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3487913
url: https://www.scopus.com/pages/publications/85208257061?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5219--5232
keywords:
- Age of Information (AoI)
- deep reinforcement learning (DRL)
- Internet of Things (IoT)
- multiagent DRL
- multiple access edge computing (MEC)
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
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: false
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

# paper-1935 — MACU: A Multiagent Cache Updating Framework for IIoT Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> An important role played by industrial Internet of Things (IIoTs) networks is supporting the operations of autonomous mobile robots (AMRs) by leveraging multiple-access edge caching servers. At the same time, judicious content caching strategies are essential for minimizing content retrieval delays and the costs associated with updating caches. In this study, a novel multiagent reinforcement learning (MARL)-based cache update strategy termed multiagent cache update (MACU) is proposed. MACU leverages the multiagent deep deterministic policy gradient (MADDPG) framework and aims to optimize cache updates to reduce Age of Information (AoI), minimize events where AoI exceeds acceptable levels, and ensure that the costs associated with performing cache updates are kept low. Furthermore, to mitigate the computational complexity of training agents with MACU, the MACU with global critic (MACU-GC) variant is introduced, which diverges from traditional MADDPG by employing a singular global critic for enhanced training efficiency. Extensive numerical evaluations showcase the proposed strategies' superiority over conventional deep reinforcement learning-based caching methods, achieving significant improvements in AoI costs, caching costs, and AoI violation costs, while effectively reducing content retrieval latency, enhancing hit rates, and optimizing AoI and link load metrics.  © 2014 IEEE.

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
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "An important role played by in" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multiagent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1935.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
