---
id: paper-1618
title: Comparative Analysis of GPT-2 and Gemini for Automated Generation of Dockerfiles and Docker Compose in DevOps Workflows
authors:
- Hamza, Laila
- Lachgar, Mohamed
- Errattahi, Rahhal
venue: Proceedings - 2025 8th International Conference on Networking, Intelligent Systems and Security, NISS 2025
venue_type: conference
year: 2025
doi: 10.1109/NISS66502.2025.00012
url: https://www.scopus.com/pages/publications/105035073604?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 16--23
keywords:
- DevOps
- Docker
- Gemini
- Generative AI
- GPT-2
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

# paper-1618 — Comparative Analysis of GPT-2 and Gemini for Automated Generation of Dockerfiles and Docker Compose in DevOps Workflows

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the growing complexity of containerized applications, ensuring efficient and error-free automation has become a critical challenge in modern software deployment workflows. This work compares GPT-2 and Gemini for Dockerfile and Docker Compose generation by examining three use cases of increasing complexity. The results demonstrat that although GPT-2 can produce valid configurations after fine-tuning, it often requires significant manual adjustments to meet specific requirements. On the other hand, Gemini demonstrated its abilty to generate complete and correct configurations with minimal or no human intervention. The quantitative scores obtained with BLEU and ROUGE-L also confirm that Gemini produces better quality results. Overall, the results of this study confirm Gemini's potential to change DevOps workflows, particularly for production environments requiring both reliability and efficiency. These results highlight Gemini's potential as a transformative tool in DevOps workflows, particularly for automating configuration generation in high-stakes environments. The study also highlights opportunities for future research, such as exploring the potential benefits of using Gemini for specialized tasks like Kubernetes orchestration.  © 2025 IEEE.

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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "GPT" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "GPT" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1618.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
