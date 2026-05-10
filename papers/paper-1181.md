---
id: paper-1181
title: 'Integrating Intelligent Chip Design with Agentic AI: Building the Future of Smart Wireless Communication Systems'
authors:
- Sheelam, Goutham Kumar
venue: MSW Management
venue_type: journal
year: 2024
doi: 10.7492/1x1v2c78
url: https://www.scopus.com/pages/publications/105018207138?origin=resultslist
publisher: Forester Communications Inc.
pages: 1380--1405
keywords:
- 6G Networks
- Agentic AI
- AI Hardware Integration
- AI-Driven Signal Processing
- Autonomous Systems
- Cognitive Radio
- Edge Computing
- Embedded AI
- Energy-Efficient Chips
- Intelligent Chip Design
- Intelligent Transceivers
- Low-Latency Processing
- Neural Accelerators
- Real-Time Data Processing
- Smart Wireless Communication
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1181 — Integrating Intelligent Chip Design with Agentic AI: Building the Future of Smart Wireless Communication Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recent breakthroughs in Artificial Intelligence (AI) are propelling society towards a new technological era, wherein intelligent systems can independently observe and interpret their environment, make optimal decisions, and act accordingly. Agentic AI is evolving from tool AI to an entity that operates without human involvement. Almost all aspects of society are now being impacted by this rapid proliferation of Agentic AI, such as the public sector, education, finance, healthcare, entertainment, media, and automotive. In parallel, composite intelligent chip design, encompassing chip architecture, chip implementation and chip manufacturing, is urgently needed amid soaring demand for computation and communication. Despite initial optimism about Moore’s law, the efficacy of silicon-based chips has seen degradation. One potential route for intelligent chip design is inspired by biological exploration, which could involve the evolution of chips along a co-developed path guided by environmental pressure. Chip designs with complex functionalities require optimization strategies that surpass the capabilities of current silicon-based chips. The realization of such a vision could result in completely new architectures using advanced materials and manufacturing techniques, as well as translating these designs into novel chip automatons. However, this path would involve fundamental breakthroughs over decades and would render legacy chips obsolete. A complementary route for rapid maturity involves applying agentic AI to intelligent chip design, resulting in new AI-native chips. These chips would come integrated with learned weights from training AI models, providing immediate acceleration to on-chip inference. In addition, agentic AI could dramatically speed up the training and design of intelligent chips for next-gen wireless systems. AI tools could be utilized to provide domain knowledge on chip design, chip operation, and workflow optimization. Agentic AI ridden with new challenges for regulation and safety concerns leads to the notion of regulatory compliance, which encompasses social norms, laws, regulations and standards. Such a deep embedding of regulatory compliance in agentic systems could enable compliance by design, imbuing them with performance enhancing abilities. Furthermore, any codes, tools and metrics devised by humans for regulation on agentic systems could be adopted as learning signal to pursue optimal policies for compliance, thus inheriting pre-existing processes. Looking ahead, the rapid proliferation of agentic AI is poised to alter the course of the next wireless communications revolution. © 2024 Forester Communications Inc.. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-native" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1181.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
