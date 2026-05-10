---
id: paper-1753
title: GPT-Powered Virtual Assistants for Intelligent Cloud Service Management
authors:
- Kumar, Santosh
- Nutalapati, Pavan
- Vemuri, Srinikhil Saisatya
- Aida, Raviteja
- Salami, Zaeid Ajsan
- Boob, Nandini Shirish
venue: 2025 World Skills Conference on Universal Data Analytics and Sciences, WorldSUAS 2025
venue_type: conference
year: 2025
doi: 10.1109/WorldSUAS66815.2025.11198967
url: https://www.scopus.com/pages/publications/105022248624?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AI-driven automation
- cloud monitoring
- cloud service management
- conversational AI
- GPT-powered virtual assistants
- intelligent cloud computing
- IT service optimization
- machine learning
- natural language processing
- predictive analytics
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

# paper-1753 — GPT-Powered Virtual Assistants for Intelligent Cloud Service Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing has become highly adopted, which increased the demand for intelligent management solutions that can optimize the allocation of resources, as well as enhance security and improve overall service efficiency. One such solution comes from GPT-powered virtual assistants that harness the power of natural language processing (NLP) and machine learning (ML) to automate the day-to-day management of cloud services. Utilizing machine learning and natural language processing, AI-powered assistants analyze data and trends to offer actionable insights, making proactive suggestions to optimize maintenance schedules, allocate resources, and identify issues before they escalate. Organizations that combine GPT models with cloud platforms can accelerate workflows, reduce risks, and achieve cloud services' high availability. In addition, these virtual assistants allow for seamless user interactions, allowing IT teams to manage cloud environments via conversational AI interfaces. The versatility of GPT frameworks enables continuous learning and contextual alignment, leading to enhanced issue resolution capabilities and proactive incident management. In contrast, there are challenges such as data privacy, bias in AI responses, and issues around integration that need to be dealt with for reliable deployment. This explores on the design, functionality and impact of GPT-based virtual assistants in smart cloud service observer. Future research directions are also suggested, providing a glimpse into a potential future where end-to-end cloud operations are dynamically managed by AI agents. Enterprise can gain on efficiency, scalability, and cloud service reliability by leveraging on GPT-based AI.  © 2025 IEEE.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "natural language processing" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "NLP" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "natural language processing" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1753.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
