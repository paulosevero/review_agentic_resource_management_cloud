---
id: paper-1683
title: Game-Theoretic-GAI Approach for Computation Offloading and Resource Management
  for Mobile Edge Collaborative Vehicular Networks
authors:
- Jahan, Nusrat
- Hasan, Mohammad Kamrul
- Islam, Shayla
- Nazri, Mohd Zakree Ahmad
- Ariffin, Khairul Akram Zainol
- Abbas, Huda Saleh
- Alqahtani, Ali
- Gohel, Hardik
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2025
doi: 10.1109/TITS.2025.3577673
url: https://www.scopus.com/pages/publications/105008658152?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- computation offloading
- Game-theoretic frameworks
- generative AI
- mobile edge computing (MEC)
- next-generation ITS applications
- vehicular networks
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
  06-full-text-screening: exclude
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management
      signal); C3=1.0 (infra/cloud-edge signal)
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
    - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_with_llm
    - ovr_using_llm
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: "Escopo V2X/vehicular networks. Per Gate A (Boundary C estrito), V2X é tratado como adjacente a Orbital Edge Computing e fora do escopo de RM em cloud/edge/fog/continuum."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1683 — Game-Theoretic-GAI Approach for Computation Offloading and Resource Management for Mobile Edge Collaborative Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To counter challenges posed by emerging service needs, limited resources, and the imperative of real-time flexibility, the present research synthesizes game theory and Generative Artificial Intelligence (GAI). The designed architecture supports discreet and scalable resource allocation by combining a Stackelberg game framework with GAI-driven simulation and decision-support mechanisms. The algorithmic methodology of two stages allocates resources among vehicles and Mobile Edge Computing (MEC) servers in an efficient manner, optimizing the offloading ratio. The architecture dynamically adapts by changing network environments using GAI’s ability to simulate complex vehicular scenarios and weight trade-offs concerning latency, energy consumption, and computation efficiency. The resource allocation process is supported by an intelligent offloading decision-support module powered by GAI, complementing parameter optimization using Lagrangian optimization and Karush-Kuhn-Tucker (KKT) conditions. The performance of the designed framework is validated using extensive simulations. The results show the reductions in computational overhead, energy consumption, and latency compared to conventional methods, especially in cases of dynamic job intensity and communication scenarios. The Generative AI can improve the system scalability by allowing task offloading in resource-scarce cases. The result demonstrates the synergistic effectiveness of GAI and game-theoretical approaches in resolving real-time resource allocation challenges in vehicle-to-everything networks. © 2000-2011 IEEE.

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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative Artificial Intellig" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative Artificial Intellig" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "Generative Artificial Intellig" }`
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_with_llm', 'ovr_using_llm', 'ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Generative AI have addressed privacy concerns by enabling decentralized training and inference" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "The exponential rise of Intelligent Transportation Systems (ITS) and autonomous vehicles has greatly" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: mas_llm_based, pattern_id: mas_llm_combo, matched_substring: "The exponential rise of Intelligent Transportation Systems (ITS) and autonomous vehicles has greatly" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** Escopo V2X/vehicular networks. Per Gate A (Boundary C estrito), V2X é tratado como adjacente a Orbital Edge Computing e fora do escopo de RM em cloud/edge/fog/continuum.
- **agrees_with_regex:** True
- **addressed_hint:** Paper propõe multi-agent RL-based system, não clássico RL/MARL sem LLM; GAI layer essencial para context-aware strategy derivation.
- **evidence_sections:** ['III. GAI-BASED COMPUTATION OFFLOADING', 'III-A. GenAI-Based Offloading and Resource Management', 'III-C. System model (3-layer architecture)', 'III-D. Decision-Making Algorithm', 'IV. RESULTS AND DISCUSSION']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
