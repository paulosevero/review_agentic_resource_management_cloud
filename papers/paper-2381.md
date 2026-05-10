---
id: paper-2381
title: 'Optimizing AIGC Services by Prompt Engineering and Edge Computing: A Generative Diffusion Model-Based Contract Theory Approach'
authors:
- Ye, Dongdong
- Cai, Shuting
- Du, Hongyang
- Kang, Jiawen
- Liu, Yinqiu
- Yu, Rong
- Niyato, Dusit
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2024.3463420
url: https://www.scopus.com/pages/publications/85207141783?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 571--586
keywords:
- AI-generated content
- contract theory
- Edge computing
- generative diffusion model
- prompt engineering
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
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
    my_justification: Otimização de serviços AIGC com prompt engineering — AIGC como workload servido, não agente de RM.
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

# paper-2381 — Optimizing AIGC Services by Prompt Engineering and Edge Computing: A Generative Diffusion Model-Based Contract Theory Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The development of Generative AI (GAI) and AI-generated content (AIGC) has been significantly improved by pretrained foundation models and prompt-based methods. To boost the quality and reduce the latency of AIGC generation, prompt engineering and edge computing are introduced, demanding a multi-dimensional resource allocation approach. Thus, we use the generative diffusion model (GDM) and contract theory to design a two-stage, multi-dimensional resource allocation framework. In the first stage, we employ an approximation approach to quantitatively assess the relationship between the level of prompt optimization, the number of diffusion denoising steps, and the quality of AIGC generation. Based on the quality function, we formulate models for the utilities of an AI-generated content Service Provider (ASP) and users, leading to a non-convex quality-based contract problem optimizing the level of prompt optimization and the number of diffusion denoising steps. To address the time-consuming process of solving the non-convex problem due to variable cost of the ASP and gain preferences of the users, a GDM-based scheme is proposed to optimize quality-based contract items. In the second stage, for each group of users who choose the same quality-based contract items, a non-convex latency-based contract problem optimizing the CPU cycle frequency and network transmission rate is formulated, then the GDM-based scheme is also applied to find the optimal latency-based contract items. Numerical results show that the proposed GDM-based contract generation scheme is very advantageous in improving the quality of AIGC generation and decreasing the latency of AIGC generation, compared to other standard schemes.  © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Prompt Engineering" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AIGC" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "foundation models" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Otimização de serviços AIGC com prompt engineering — AIGC como workload servido, não agente de RM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2381.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
