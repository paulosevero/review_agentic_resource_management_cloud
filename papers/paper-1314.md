---
id: paper-1314
title: Generative AI-aided Reinforcement Learning for Computation Offloading and Privacy Protection in VR-based Multi-Access Edge Computing
authors:
- You, Feiran
- Du, Hongyang
- Kang, Jiawen
- Ni, Wei
- Niyato, Dusit
- Jamalipour, Abbas
venue: Proceedings - 2024 IEEE Smart World Congress, SWC 2024 - 2024 IEEE Ubiquitous Intelligence and Computing, Autonomous and Trusted Computing, Digital Twin, Metaverse, Privacy Computing and Data Security,
  Scalable Computing and Communications
venue_type: conference
year: 2024
doi: 10.1109/SWC62898.2024.00337
url: https://www.scopus.com/pages/publications/105002235341?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2209--2214
keywords:
- generative diffusion models
- Multi-access edge computing
- proximal policy optimization
- virtual reality
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
    my_justification: Tem RL, mas também menciona GenAI. Talvez tenha algo de LLM e/ou Agentic AI (MAS).
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

# paper-1314 — Generative AI-aided Reinforcement Learning for Computation Offloading and Privacy Protection in VR-based Multi-Access Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid growth of Artificial Intelligence-Generated Content (AIGC) services has led to increased mobile user participation in related computations and interactions. This development has enabled AI-generated characters to interact with Virtual Reality (VR) users in real time, making the VR experience more interactive and personalized. In this paper, we consider an MEC system where VR users engage in AIGC services, focusing on the Generative Diffusion Model (GDM)based image generation tasks. Specifically, VR users initiate requests for computing resources, while computation offloading distributes the processing load across the MEC system. To manage AIGC edge computation offloading and cloudlet-VR user connections jointly, a Data Center Operator (DCO) employs a centralized Proximal Policy Optimization (PPO) algorithm. To protect VR users' privacy while preserving PPO functionality, we employ the Generative Diffusion Model (GDM), specifically the Denoising Diffusion Implicit Model (DDIM), which first introduces noise to the PPO state, then conducts a denoising process to recover the state information. We further employ Inverse Reinforcement Learning (IRL) to infer rewards for the recovered states, using expert demonstrations trained by the PPO. The similarity between PPO-generated rewards and IRL-inferred rewards is then computed. Simulation results demonstrate that our proposed approach successfully achieves computation offloading while protecting VR users' privacy within the PPO centralized management framework.  © 2024 IEEE.

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
- **my_justification:** "Tem RL, mas também menciona GenAI. Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative AI" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1314.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
