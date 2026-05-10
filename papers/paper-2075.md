---
id: paper-2075
title: 'Circuit-AI: A Self-Hosted AI-Agent Language Model Framework for Control Loop Implementation and Simulation'
authors:
- Raval, Vishwam
- Zeid, Mohamed
- Enjeti, Prasad
venue: INTELEC, International Telecommunications Energy Conference (Proceedings)
venue_type: conference
year: 2025
doi: 10.1109/INTELEC63987.2025.11214739
url: https://www.scopus.com/pages/publications/105022436127?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 91--96
keywords:
- control systems
- digital twin
- generative AI
- intelligent design tools
- large language models
- Power electronics
- self-hosted AI
- simulation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2075 — Circuit-AI: A Self-Hosted AI-Agent Language Model Framework for Control Loop Implementation and Simulation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper presents an AI-Agent designed to assist with power electronics analysis, simulation, and interface with the hardware to optimize its operation employing LLaMA 3 language model, deployed locally on the NVIDIA Jetson Orin Nano Super. The system employs a self-hosted model to support simulation orchestration, control loop prototyping, and digital twin integration without requiring cloud connectivity. Modular APIs interface with simulation environments and hardware platforms, enabling more streamlined workflows. Engineers can interact with the system via natural language prompts to express design objectives, control strategies, and diagnostic tasks. This approach aims to simplify specific stages of the design process and reduce development overhead. The architecture represents a step toward evaluating the role of generative AI in power electronics workflows under resource-constrained, edge-computing conditions. The proposed system is designed to operate entirely on-device, without internet connectivity (air-gapped), making it especially well-suited for optimizing the performance of defense and industrial systems. Experimental results from the NVIDIA Jetson Orion Super hardware is discussed.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLaMA" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "language model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2075.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
