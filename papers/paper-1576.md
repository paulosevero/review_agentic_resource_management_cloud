---
id: paper-1576
title: 'BAAM: An Inferential Multi-agent Modeling for Energy-Optimized Job Scheduling in Green Data Centers'
authors:
- Gao, Mingxu
- Zhao, Yu
- Lin, Jianfeng
venue: Communications in Computer and Information Science
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-9986-5_42
url: https://www.scopus.com/pages/publications/105013055652?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 499--510
keywords:
- Energy Optimization
- Green Data Centers
- Job Scheduling
- Multi-Agent Reinforcement Learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1576 — BAAM: An Inferential Multi-agent Modeling for Energy-Optimized Job Scheduling in Green Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Under high load conditions, unreasonable scheduling strategies in distributed data centers will increase energy consumption and carbon emissions, which goes against the original intention of green data centers. Traditional static policies are difficult to adapt to dynamically changing environments. Even reinforcement learning methods struggle to infer the policies of other centers with limited observability, thus impeding cooperation. To address these challenges, we propose Belief and Attention-based Agent Modeling (BAAM), a novel multi-agent reinforcement learning framework for energy-optimized job scheduling in distributed data centers. BAAM integrates a fact-based belief reasoning module and self-attention mechanism, allowing each agent to infer the hidden strategy of its peers and predict its own future state changes using only local observations, actions, and rewards. We conducted extensive experiments using Alibaba's real dataset cluster-trace-v2018 to validate BAAM in a distributed data center scheduling scenario that simulates job dynamic arrival and virtual machine execution. Compared with traditional scheduling methods and MARL baselines, BAAM provides better coordinated scheduling policies among centers and substantially reduces energy consumption, ​achieving about 20% lower energy usage than commonly used advanced MARL approaches. Moreover, BAAM exhibits strong robustness and adaptability in different environments, demonstrating its practical potential for achieving green data center operations. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "Under high load conditions" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1576.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
