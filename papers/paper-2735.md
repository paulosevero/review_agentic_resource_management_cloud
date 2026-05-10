---
id: paper-2735
title: 'Cloud-Native Generative AI for Automated Planogram Synthesis: A Diffusion Model Approach for Multi-store Retail Optimization'
authors:
- Pagidoju, Ravi Teja
- Agarwal, Shriya
venue: Communications in Computer and Information Science
venue_type: conference
year: 2026
doi: 10.1007/978-3-032-08649-5_10
url: https://www.scopus.com/pages/publications/105020241715?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 152--165
keywords:
- Cloud computing
- Diffusion models
- Edge deployment
- Generative AI
- Planogram generation
- Retail optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2735 — Cloud-Native Generative AI for Automated Planogram Synthesis: A Diffusion Model Approach for Multi-store Retail Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Planogram creation is a significant challenge for retail, requiring an average of 30 h per complex layout. This paper introduces a cloud-native architecture using diffusion models to automatically generate store-specific planograms. Unlike conventional optimization methods that reorganize existing layouts, our system learns from successful shelf arrangements across multiple retail locations to create new planogram configurations. The architecture combines cloud-based model training via AWS with edge deployment for real-time inference. The diffusion model integrates retail-specific constraints through a modified loss function. Simulation-based analysis demonstrates the system reduces planogram design time by 98.3% (from 30 to 0.5 h) while achieving 94.4% constraint satisfaction. Economic analysis reveals a 97.5% reduction in creation expenses with a 4.4-month break-even period. The cloud-native architecture scales linearly, supporting up to 10,000 concurrent store requests. This work demonstrates the viability of generative AI for automated retail space optimization. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

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

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2735.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
