---
id: paper-1952
title: Harnessing pre-trained generalist agents for software engineering tasks
authors:
- Mindom, Paulina Stevia Nouwou
- Nikanjam, Amin
- Khomh, Foutse
venue: Empirical Software Engineering
venue_type: journal
year: 2025
doi: 10.1007/s10664-024-10597-8
url: https://www.scopus.com/pages/publications/85212077271?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Generalist agents
- Pre-training
- Reinforcement learning
- Software engineering
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent).
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1952 — Harnessing pre-trained generalist agents for software engineering tasks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Nowadays, we are witnessing an increasing adoption of Artificial Intelligence (AI) to develop techniques aimed at improving the reliability, effectiveness, and overall quality of software systems. Deep reinforcement learning (DRL) has recently been successfully used for automation in complex tasks such as game testing and solving the job-shop scheduling problem, as well as learning efficient and cost-effective behaviors in various environments. However, these specialized DRL agents, trained from scratch on specific tasks, suffer from a lack of generalizability to other tasks and they need substantial time to be developed and re-trained effectively. Recently, DRL researchers have begun to develop generalist agents, able to learn a policy from various environments (often Atari game environments) and capable of achieving performance similar to or better than specialist agents in new tasks. In the Natural Language Processing or Computer Vision domain, these generalist agents are showing promising adaptation capabilities to never-before-seen tasks after a light fine-tuning phase and achieving high performance. To the best of our knowledge, no study has investigated the applicability of these generalist agents to SE tasks. This paper investigates the potential of generalist agents for solving SE tasks. Specifically, we conduct on three increasingly used SE tasks: playtesting in games (for two games), bug localization in software projects (i.e., six software projects) and the minimization of makespan in task scheduling in cloud computing (for two instances). Our results show that the generalist agents outperform the specialist agents with very little effort for fine-tuning, achieving a 20% reduction of the makespan over specialized agent performance on task-based scheduling. In the context of game testing, some generalist agent configurations find bugs 3-8% faster than the specialist agents. Finally, in the context of bug localization, generalist agents perform at least 9% better than specialist agents in terms of Mean Reciprocal Rank. Building on our analysis, we provide recommendations for researchers and practitioners looking to select generalist agents for SE tasks, to ensure that they perform effectively. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2024.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Natural Language Processing" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1952.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
