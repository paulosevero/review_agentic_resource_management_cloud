---
id: paper-1603
title: 'Integrating Generative AI with Network Digital Twin for 6G: An Edge-Cloud Collaborative Approach'
authors:
- Guan, Wanqing
- Li, Peichun
- Zhang, Haijun
- Wu, Yuan
venue: IEEE Communications Magazine
venue_type: journal
year: 2025
doi: 10.1109/MCOM.001.2500002
url: https://www.scopus.com/pages/publications/105018065627?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 181--187
keywords:
- Artificial intelligence
- Behavioral research
- Decision making
- Digital twin
- Internet of things
- Mobile edge computing
- Mobile telecommunication systems
- User experience
- Wireless networks
- Accurate modeling
- Collaborative approach
- Content services
- Deployment architecture
- Edge clouds
- Intelligence models
- Networks management
- Physical network
- User requirements
- Wireless systems
- Life cycle
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1603 — Integrating Generative AI with Network Digital Twin for 6G: An Edge-Cloud Collaborative Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The sixth-generation (6G) of wireless systems aim to support the emerging Internet of Everything (IoE) applications and provide Artificial Intelligence-Generated Content (AIGC) services to diverse mobile devices. The strict communication requirements of various IoE applications and the personalized user requirements of mobile AIGC services pose great challenges to the 6G network management. Creating a digital twin (DT) to represent the wireless networks can facilitate the achievement of zero-touch and autonomous wireless network management with accurate modeling of the physical network and proactive analysis of its behavior. In this article, a hybrid deployment architecture of a joint DT for 6G network is introduced, integrating with the generative artificial intelligence (GenAI) models which are trained and deployed in an edge-cloud collaborative way. A integration framework between GenAI and network DT is presented to realize a cycle of benefits. GenAI models offer efficient solutions for ubiquitous intelligent decision-making during the life cycle of DT while the joint DT provides assistance in mobile AIGC services provisioning to reduce the resource consumption and improve user experience. A case study is presented for illustrating how to utilize DT capabilities to enhance the computing resource allocation for fine-tuning and inference, providing personalized AIGC services. © 1979-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative artificial intellig" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GenAI" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1603.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
