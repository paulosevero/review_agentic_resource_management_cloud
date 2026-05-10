---
id: paper-0958
title: 'Request Dispatching Over Distributed SDN Control Plane: A Multiagent Approach'
authors:
- Huang, Victoria
- Chen, Gang
- Zuo, Xingquan
- Zomaya, Albert Y.
- Sohrabi, Nasrin
- Tari, Zahir
- Fu, Qiang
venue: IEEE Transactions on Cybernetics
venue_type: journal
year: 2024
doi: 10.1109/TCYB.2023.3266448
url: https://www.scopus.com/pages/publications/85159824039?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3211--3224
keywords:
- Distributed software-defined networking (SDN)controllers
- multiagent deep reinforcement learning (MA-DRL)
- request dispatching
- resource scheduling
- SDN
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0958 — Request Dispatching Over Distributed SDN Control Plane: A Multiagent Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Software-defined networking (SDN) allows flexible and centralized control in cloud data centers. An elastic set of distributed SDN controllers is often required to provide sufficient yet cost-effective processing capacity. However, this introduces a new challenge: Request Dispatching among the controllers by SDN switches. It is essential to design a dispatching policy for each switch to guide the request distribution. Existing policies are designed under certain assumptions, including a single centralized agent, global network knowledge, and a fixed number of controllers, which often cannot be satisfied in practice. This article proposes MADRina, Multiagent Deep Reinforcement Learning for request dispatching, to design policies with high dispatching adaptability and performance. First, we design a multiagent system to address the limitation of using a centralized agent with global network knowledge. Second, we propose a Deep Neural Network-based adaptive policy to enable request dispatching over an elastic set of controllers. Third, we develop a new algorithm to train the adaptive policies in a multiagent context. We prototype MADRina and build a simulation tool to evaluate its performance using real-world network data and topology. The results show that MADRina can significantly reduce response time by up to 30% compared to existing approaches.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "Software-defined networking (S" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multiagent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multiagent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0958.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
