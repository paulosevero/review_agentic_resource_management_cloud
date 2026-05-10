---
id: paper-1885
title: Generative AI-Driven Robust Service Fault-Tolerant Migration under Dynamic Edge Networks
authors:
- Liu, Jice
- Fang, Honglin
- Yu, Peng
- Li, Wenjing
- Chen, Xu
- Liao, Dingshi
venue: Proceedings of the IEEE World Forum on Internet of Things, WF-IoT
venue_type: conference
year: 2025
doi: 10.1109/WF-IoT64238.2025.11270645
url: https://www.scopus.com/pages/publications/105032635174?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Dynamic Edge Network
- Generative Diffusion Models
- Preemptive Fault Prediction
- Service Fault Tolerant Migration
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1885 — Generative AI-Driven Robust Service Fault-Tolerant Migration under Dynamic Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Dynamic edge networks enhance service delivery by decentralizing resources, but challenges like network topology changes and heterogeneous node limitations hinder existing methods. To address this, this paper proposes PreDiffusion, a Diffusion-Based Service Fault-Tolerant Migration Algorithm, leveraging Generative Diffusion Models (GDMs) for stable and efficient preemptive migration decisions. The approach combines spatiotemporal network modeling, a fault prototype encoder, and a diffusion-based decision generator optimized for fast inference, achieving robust fault detection (99.07% accuracy) and classification (93.06% accuracy) while outperforming GAN-based methods in training stability and decision quality.Simulations on an edge heterogeneous cluster demonstrate PreDiffusion's superiority over baseline algorithms, significantly reducing energy consumption, service latency, and improving load balancing. By integrating an online fine-tuning mechanism, the algorithm adapts to dynamic environments, ensuring service continuity and higher resource utilization efficiency. The results validate PreDiffusion as an effective solution for intelligent fault-tolerant migration in edge computing. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "Generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_generative_diffusion, matched_substring: "Generative Diffusion" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_diffusion_model, matched_substring: "Diffusion Models" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1885.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
