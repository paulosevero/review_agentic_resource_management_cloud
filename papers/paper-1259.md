---
id: paper-1259
title: Offloading and Quality Control for AI Generated Content Services in 6G Mobile Edge Computing Networks
authors:
- Wang, Yitong
- Liu, Chang
- Zhao, Jun
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2024
doi: 10.1109/VTC2024-Spring62846.2024.10683477
url: https://www.scopus.com/pages/publications/85206145003?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AIGC
- diffusion model
- Edge computing
- generative AI
- resource allocation
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
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
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

# paper-1259 — Offloading and Quality Control for AI Generated Content Services in 6G Mobile Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> AI-Generated Content (AIGC), as a novel manner of providing Metaverse services in the forthcoming Internet paradigm, can resolve the obstacles of immersion requirements. Concurrently, edge computing, as an evolutionary paradigm of computing in communication systems, effectively augments real-time interactive services. In pursuit of enhancing the accessibility of AIGC services, the deployment of AIGC models (e.g., diffusion models) to edge servers and local devices has become a prevailing trend. Nevertheless, this approach faces constraints imposed by battery life and computational resources when tasks are offloaded to local devices, limiting the capacity to deliver high-quality content to users while adhering to stringent latency requirements. So there will be a tradeoff between the utility of AIGC models and offloading decisions in the edge computing paradigm. This paper presents a joint optimization scheme for offloading decisions, computation time, and diffusion steps of the diffusion models in the reverse diffusion stage. Moreover, we take the average error into consideration as the metric for evaluating the quality of the generated results. Experimental outcomes definitively show that the algorithm put forward outperforms baseline methods in terms of joint optimization performance. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1259.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
