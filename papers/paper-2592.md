---
id: paper-2592
title: Foundation Model Enhanced Joint Multi-Hop Task Offloading in Dynamic R2X/V2X-based Edge Computing Networks
authors:
- Han, Mingqi
- Sun, Xinghua
- Wang, Xijun
- Zhan, Wen
- Chen, Xiang
- Quek, Tony Q.S.
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3665406
url: https://www.scopus.com/pages/publications/105030680191?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Foundation Model
- Intelligent Transportation
- Joint R2X and V2X
- Multi-hop Transmission
- Reinforcement Learning
- Task Offloading
- Vehicular Edge Computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    - ovr_cls_llm_present
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

# paper-2592 — Foundation Model Enhanced Joint Multi-Hop Task Offloading in Dynamic R2X/V2X-based Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recent popularization of the Internet of Vehicles (IoVs) and vehicles-to-everything (V2X) enables the emergence of real-time vehicular applications, posing challenges to resourcelimited vehicles. Toward this end, vehicle edge computing (VEC) has been proposed to alleviate the computational burden on vehicles by leveraging resources from roadside units (RSUs) and VEC servers. While existing works mainly focus on the task requirement for either vehicles or RSUs, the joint task offloading for both V2X and RSUs-to-everything (R2X) has not been fully studied. In this paper, we aim at optimizing the task offloading strategies for both vehicles and RSUs, and adopt a multi-hop task offloading manner to fully utilize the VEC network resources. This problem introduces a severe state-action space shift issue with varying dimensions and representation, which poses challenges for conventional DRL approaches. To address it, we propose a Bidirectional Encoder Representations from Transformers (Bert)-based matching Q-network (BMQN) algorithm. First, we design the BMQN model to efficiently capture correlations among all vehicles and RSUs through bidirectional attention. Then, we propose type-embedded grouped attention and available action embedding to mitigate the overfitting sequence length issue, thereby enhancing generalization capacity. Moreover, we propose to address the state-action space shift issue through a matching-based manner, which can significantly enhance the task offloading ability by matching the states among devices. Simulation results demonstrate that: 1) the BMQN can achieve much better performance than other approaches in scenarios comprising various numbers of vehicles and RSUs as well as diverse road lengths; 2) the BMQN has sufficient generalization capacity to adapt to inexperienced scenarios through matching-based architecture and available action embedding. © 2002-2012 IEEE.

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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Foundation Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Transformers" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Bert" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Foundation Model" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Transformers" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2592.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
