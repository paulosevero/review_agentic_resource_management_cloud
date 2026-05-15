---
id: paper-1780
title: 'Agent-as-a-Service: An AI-Native Edge Computing Framework for 6G Networks'
authors:
- Li, Borui
- Liu, Tianen
- Wang, Weilong
- Zhao, Chengqing
- Wang, Shuai
venue: IEEE Network
venue_type: journal
year: 2025
doi: 10.1109/MNET.2024.3520987
url: https://www.scopus.com/pages/publications/105003036518?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 44--51
keywords:
- 6G network
- AI agents
- edge intelligence
- large language model
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource
      management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent).
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: Problema estritamente de RAN/5G/6G/spectrum sem substrato
      cloud/edge RM.
    winning_category: E_strict_telecom
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: 'Framework AaaS implementa lifecycle management de agentes LLM
      em edge (§ Introduction, Overview of AAAs). Porém, domínio é estritamente 6G
      RAN/spektrum, não cloud/edge/fog resource management. Case study foca latência
      de autonomous driving via RAN optimization, não placement/scheduling/scaling
      de recursos de infraestrutura. Out of scope: boundary C (infraestrutura) excludes
      strict telecom/spectrum sem substrato cloud-edge-fog RM.'
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1780 — Agent-as-a-Service: An AI-Native Edge Computing Framework for 6G Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> It has become a consensus that the integration of computing, sensing, and communication with ubiquitous intelligence will be the cornerstone of the sixth-generation (6G) network. The concept of edge computing and intelligence, which push the frontier of computation closer to the data source, is a suitable paradigm that aligns with these visions of 6G. In this article, we introduce Agent-as-a-Service (AaaS), an AI-native edge computing framework that leverages AI agents for both the control-plane operations and user-plane services of the 6G network. In the AaaS framework, agents can perform computing, sensing, and communicating tasks automatically by harnessing of the pervasive intelligence offered by 6G infrastructures. By AI-native, we refer to redesigning the whole lifecycle of an edge computing task to align with the prominent reasoning and planning ability of the generative AI. The lifecycle includes plan generation, execution orchestration, resource management, and long-term evolvement. The AaaS framework is built upon emerging techniques such as deviceless computing and WebAssembly to cope with the heterogeneous and geo-distributed 6G edge deployments. Based on the AaaS framework, we conduct a case study on autonomous driving in 6G edge computing to showcase the benefits in terms of overall latency reduction. Finally, we outline potential research directions to form a more efficient and integrated 6G edge computing with artificial intelligence. © 1986-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent)."
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-Native" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-native" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI agents" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-native" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening


### iter-0 (initial classification)

- **regex_decision:** Exclude
- **regex_justification:** "Problema estritamente de RAN/5G/6G/spectrum sem substrato cloud/edge RM."
- **winning_category:** 'E_strict_telecom'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: E_strict_telecom, pattern_id: strict_telecom_only, matched_substring: "6G network AI agents edge intelligence large language model 
 ---
title: Agent-as-a-Service: An AI-N" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** Framework AaaS implementa lifecycle management de agentes LLM em edge (§ Introduction, Overview of AAAs). Porém, domínio é estritamente 6G RAN/spektrum, não cloud/edge/fog resource management. Case study foca latência de autonomous driving via RAN optimization, não placement/scheduling/scaling de recursos de infraestrutura. Out of scope: boundary C (infraestrutura) excludes strict telecom/spectrum sem substrato cloud-edge-fog RM.
- **agrees_with_regex:** True
- **addressed_hint:** networks — confirmado: papel é estritamente telecom/6G, não RM de infraestrutura cloud/edge/fog
- **evidence_sections:** ['Introduction (2): Agents manage 6G edge computing (RAN-focused), not cloud/fog resource orchestration', 'Overview of AAAs framework: kernel-space agents manage user-space agents, but in 6G network context', 'Case study: autonomous driving latency via 6G agent coordination, not compute/storage placement']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
