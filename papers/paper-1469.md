---
id: paper-1469
title: Exploring NetGPT-Enabled Dynamic Resource Management for Mobile D2D in Industrial IoT
authors:
- Chen, Baotong
- Liang, Haiquan
- Wan, Jiafu
- Wang, Chuangjian
- Yan, Xuguo
- Xia, Xuhui
- AlQahtani, Salman A.
venue: IEEE Network
venue_type: journal
year: 2025
doi: 10.1109/MNET.2025.3532655
url: https://www.scopus.com/pages/publications/85216386481?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 37--46
keywords:
- Co-offloading
- D2D
- GenAI
- Industrial IoT
- NetGPT
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope + RL
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

# paper-1469 — Exploring NetGPT-Enabled Dynamic Resource Management for Mobile D2D in Industrial IoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> AI large model-centered intelligent applications holds promises to revolutionize network quality of service (QoS). therefore, the deployment and utilization of such models in the Industrial Internet of Things (Industrial IoT) are considered as an increasingly pressing priority. In particular, the integration of Generative AI (GenAI) into Industrial IoT, with a focus on establishing a robust NetGPT network architecture that leverages Mobile Edge Computing (MEC) and Device-to-Device (D2D) collaboration has been subjected to significant academic attention. Accordingly, this paper explores the optimization of dynamic network resource management in mobile D2D networks through the innovative application of NetGPT. First, a NetGPT-based system architecture for network resource management is proposed. Thereafter, mobile D2D network model is established with a detailed account of NetGPT training and NetGPT fusion. Finally, the workload scheduling strategy in industrial IoT based on Stackelberg game model is formulated though multi-agent GenAI and present the NetGPT-based orchestration of task co-offloading for mobile network nodes. Deep reinforcement learning is implemented at the edge side to compete and cooperate in addressing complex network problems, which enabling GenAI nodes in a co-offloading and load balancing manner. The implementation of NetGPT-enhanced D2D networks has been conducted in a Mininet simulation environment. Compared to traditional network solutions, our findings show significant improvements in several key performance indicators, including network response latency, task processing capacity, and transmission power. © 1986-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "AI large model-centered intell" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "NetGPT" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GenAI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "NetGPT" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope + RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1469.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
