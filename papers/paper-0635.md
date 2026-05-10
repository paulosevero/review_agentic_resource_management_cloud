---
id: paper-0635
title: 'Causal Semantic Communication for Digital Twins: A Generalizable Imitation Learning Approach'
authors:
- Kurisummoottil Thomas, Christo
- Saad, Walid
- Xiao, Yong
venue: IEEE Journal on Selected Areas in Information Theory
venue_type: journal
year: 2023
doi: 10.1109/JSAIT.2023.3336538
url: https://www.scopus.com/pages/publications/85186498882?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 698--717
keywords:
- and causal inference
- imitation learning
- integrated information theory
- model-based reinforcement learning
- Semantic communication
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
    my_justification: '"Imitation Learning" talvez indique LLMs / Agents.'
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
    my_final_decision: Exclude
    my_justification: MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)
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

# paper-0635 — Causal Semantic Communication for Digital Twins: A Generalizable Imitation Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A digital twin (DT) leverages a virtual representation of the physical world, along with communication (e.g., 6G), computing (e.g., edge computing), and artificial intelligence (AI) technologies to enable many connected intelligence services. In order to handle the large amounts of network data based on digital twins (DTs), wireless systems can exploit the paradigm of semantic communication (SC) for facilitating informed decision-making under strict communication constraints by utilizing AI techniques such as causal reasoning. In this paper, a novel framework called causal semantic communication (CSC) is proposed for DT-based wireless systems. The CSC system is posed as an imitation learning (IL) problem, where the transmitter, with access to optimal network control policies using a DT, teaches the receiver using SC over a bandwidth-limited wireless channel how to improve its knowledge to perform optimal control actions. The causal structure in the transmitter's data is extracted using novel approaches from the framework of deep end-to-end causal inference, thereby enabling the creation of a semantic representation that is causally invariant, which in turn helps generalize the learned knowledge of the system to new and unseen situations. The CSC decoder at the receiver is designed to extract and estimate semantic information while ensuring high semantic reliability. The receiver control policies, semantic decoder, and causal inference are formulated as a bi-level optimization problem within a variational inference framework. This problem is solved using a novel concept called network state models, inspired from world models in generative AI, that faithfully represents the environment dynamics leading to data generation. Furthermore, the proposed framework includes an analytical characterization of the performance gap that results from employing a suboptimal policy learned by the receiver that uses the transmitted semantic information to construct a model of the physical environment. The CSC system utilizes two concepts, namely the integrated information theory principle in the theory of consciousness and the abstract cell complex concept in topology, to precisely express the information content conveyed by the causal states and their relationships. Through this analysis, novel formulations of semantic information, semantic reliability, distortion, and similarity metrics are proposed, which extend beyond Shannon's concept of uncertainty. Simulation results demonstrate that the proposed CSC system outperforms conventional wireless and state-of-the-art SC systems by achieving better semantic reliability with reduced bits and enabling better control policies over time thanks to the generative AI architecture.  © 2020 IEEE.

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
- **my_justification:** ""Imitation Learning" talvez indique LLMs / Agents."
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "generative AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "generative AI" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "MAS/Agent sem sinal de LLM no abstract (provável clássico ou MARL puro)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0635.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
