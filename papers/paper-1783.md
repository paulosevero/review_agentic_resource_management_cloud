---
id: paper-1783
title: Can LLMs only talk? Experimental studies on task scheduling with Large Language
  Models
authors:
- Li, Mengjuan
- Chen, Zhengguang
- Zhou, Huan
- Wang, Zhipeng
- Chen, Yingwen
- Zhao, Baokang
- Ouyang, Xue
- Su, Jinshu
venue: Proceedings - International Conference on Computer Communications and Networks,
  ICCCN
venue_type: conference
year: 2025
doi: 10.1109/ICCCN65249.2025.11133882
url: https://www.scopus.com/pages/publications/105016133227?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- experimental study
- LLMs
- prompt
- task scheduling
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource
      management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: Tarefa de DevOps/observabilidade (incident triage, RCA,
      geração de manifestos) — não é decisão de resource management.
    winning_category: D_devops_or_logs_not_rm
    overrides_applied: []
    my_final_decision: Include
    my_justification: "Escopo cloud computing task scheduling (Boundary C IN). LLMs são o decisor — geram diretamente decisões de scheduling a partir de prompts. RL aparece apenas como baseline para comparação (não combinado no pipeline). Inclusão."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1783 — Can LLMs only talk? Experimental studies on task scheduling with Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) have emerged as a disruptive technology for Natural Language Processing (NLP), achieving success in NLP-related generative applications. However, the potential capability of LLMs in other domains remains largely unexplored. To explore the potential of task scheduling with LLMs, we model a typical task scheduling scenario in cloud computing and transfer scheduling problems as natural language prompts. Afterward, the knowledge and reasoning abilities of LLMs are enabled to generate scheduling decisions. Six well-known and open-source LLMs are integrated into our framework to perform experimental studies, and the results are evaluated from multiple perspectives and compared with each other. Besides, traditional heuristic algorithms and a basic Reinforcement Learning (RL) method are all performed for comparison. Our results demonstrate: 1) compared to most heuristic methods, the decisions made by LLMs achieve better scheduling performance; 2) compared to the basic RL method, LLMs exhibit better generalization on various workload patterns; 3) the larger parameter size of the LLMs has, the better scheduling performance it achieves. To the best of our knowledge, our experimental study is the first exploration to apply LLMs in task scheduling. Our findings highlight the promising potential of LLMs as a novel approach to task scheduling, offering new avenues for research and practice. © 2025 IEEE.

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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Natural Language Processing" }`
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


### iter-0 (initial classification)

- **regex_decision:** Exclude
- **regex_justification:** "Tarefa de DevOps/observabilidade (incident triage, RCA, geração de manifestos) — não é decisão de resource management."
- **winning_category:** 'D_devops_or_logs_not_rm'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: D_devops_or_logs_not_rm, pattern_id: deployment_assistant_no_rm, matched_substring: "configuration generation" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Escopo cloud computing task scheduling (Boundary C IN). LLMs são o decisor — geram diretamente decisões de scheduling a partir de prompts. RL aparece apenas como baseline para comparação (não combinado no pipeline). Inclusão.
- **agrees_with_regex:** True
- **addressed_hint:** regex hint 'D_devops_or_logs_not_rm' é falso positivo; o problema é que não há loop agentic, não questão de DevOps.
- **evidence_sections:** ['Experiment Design § Model', 'Experiment Design § Scheduling with LLMs', 'Experimental Results and Analysis']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
