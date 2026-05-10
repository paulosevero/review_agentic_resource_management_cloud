---
id: paper-2938
title: Enhancing Metaverse Fidelity and Freshness via GAI-aided Semantic Communication in Low-Altitude IoT Networks
authors:
- Zhou, Xiaoyi
- Guo, Hongzhi
- Xun, Yijie
- Mao, Bomin
- Mu, Dejun
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2026.3665270
url: https://www.scopus.com/pages/publications/105030708149?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- edge computing
- generative AI (GAI)
- Metaverse
- Multi-UAV
- parametrized deep Q-network (PDQN)
- semantic communication (SemCom)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2938 — Enhancing Metaverse Fidelity and Freshness via GAI-aided Semantic Communication in Low-Altitude IoT Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid iteration of artificial intelligence (AI) and 5G technologies has created essential foundations for Metaverse, easing bottlenecks in content generation, real-time interaction, and large-scale deployment. Integrating unmanned aerial vehicle (UAV) with semantic communication (SemCom) further provides a lightweight sensing and uplink solution, but semantic compression and bias may degrade fidelity. Generative AI (GAI), with powerful contextual modeling and generation capabilities, helps mitigate these issues. Based on this, this paper proposes a GAI-aided SemCom architecture and evaluates the feasibility of applying it to low-altitude internet of things (IoT) networks. We build evaluation models for representative image compression and GAI-aided SemCom techniques, replacing traditional task assumptions with realistic cases. Then, taking UAV networks as an example, we design a path planning and two task allocation schemes. Specifically, the UAV path planning strategy together with a greedy task allocation scheme improves the Metaverse update frequency and ensures the data freshness, while a parametrized deep Q-network (PDQN) task allocation scheme jointly optimizes Metaverse fidelity and freshness through mixed action selection, i.e., preprocessing methods (discrete) and compression size (continuous). Extensive analysis and numerical results corroborate that GAI-aided SemCom technology has practical significance in low-altitude IoT networks. Through the collaboration of multiple data processing schemes and the rational resource allocation, the fidelity and freshness of Metaverse can be greatly improved.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "Generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_gai, matched_substring: "GAI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_gai, matched_substring: "GAI" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2938.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
