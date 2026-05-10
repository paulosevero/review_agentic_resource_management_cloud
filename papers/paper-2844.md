---
id: paper-2844
title: HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks
authors:
- Wen, Jinbo
- Su, Cheng
- Kang, Jiawen
- Nie, Jiangtian
- Zhang, Yang
- Tang, Jianhang
- Niyato, Dusit
- Yuen, Chau
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2025.3637120
url: https://www.scopus.com/pages/publications/105023666575?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6547--6562
keywords:
- deep reinforcement learning
- HybridRAG
- LLMs
- Low-altitude economy
- low-carbon multi-UAV-assisted MEC networks
- regularization diffusion models
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2844 — HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Low-Altitude Economy Networks (LAENets) are emerging as a promising paradigm to support various low-altitude services through integrated air-ground infrastructure. To satisfy low-latency and high-computation demands, the integration of Unmanned Aerial Vehicles (UAVs) with Mobile Edge Computing (MEC) systems plays a vital role, which offloads computing tasks from terminal devices to nearby UAVs, enabling flexible and resilient service provisions for ground users. To promote the development of LAENets, it is significant to achieve low-carbon multi-UAV-assisted MEC networks. However, several challenges hinder this implementation, including the complexity of multidimensional UAV modeling and the difficulty of multi-objective coupled optimization. To this end, this paper proposes a novel Retrieval Augmented Generation (RAG)-based Large Language Model (LLM) agent framework for model formulation. Specifically, we develop HybridRAG by combining KeywordRAG, VectorRAG, and GraphRAG, empowering LLM agents to efficiently retrieve structural information from expert databases and generate more accurate optimization problems compared with traditional RAG-based LLM agents. After customizing carbon emission optimization problems for multi-UAV-assisted MEC networks, we propose a Double Regularization Diffusion-enhanced Soft Actor-Critic (R<sup>2</sup>DSAC) algorithm to solve the formulated multi-objective optimization problem. The R<sup>2</sup>DSAC algorithm incorporates diffusion entropy regularization and action entropy regularization to improve the performance of the diffusion policy. Furthermore, we dynamically mask unimportant neurons in the actor network to reduce the carbon emissions associated with model training. Simulation results demonstrate the reliability of the proposed HybridRAG-based LLM agent framework, which achieves a 6.6% improvement in F1 scores over traditional RAG, and validate the effectiveness of the R<sup>2</sup>DSAC algorithm, which outperforms the SAC algorithm by up to 64.17%. © 2025 IEEE. All rights reserved,

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Retrieval Augmented Generation" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "RAG" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2844.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
