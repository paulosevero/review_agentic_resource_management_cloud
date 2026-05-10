---
id: paper-2943
title: Desert power for the AI era
authors:
- Zhu, Ziheng
- Yu, Runxin
- Chen, Wei-Qiang
- Zhang, Da
venue: Nexus
venue_type: journal
year: 2026
doi: 10.1016/j.ynexs.2026.100121
url: https://www.scopus.com/pages/publications/105032834824?origin=resultslist
publisher: Cell Press
pages: ''
keywords:
- artificial intelligence
- data center
- desert
- renewable energy
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
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
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

# paper-2943 — Desert power for the AI era

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The surge in generative artificial intelligence (AI) may cause growing conflicts between securing electricity supplies and achieving sustainable development goals. Here, we propose off-grid hybrid wind-solar-storage (WSS) systems, which leverage the immense renewable resources in desert areas alongside relatively low-cost fiberoptic connectivity of data centers, to address this challenge. Using a global high-resolution techno-economic optimization model, we demonstrate that well-planned WSS systems can deliver cost-effective 24/7 uninterrupted power, primarily tailored for energy-intensive, latency-tolerant foundation model training. Furthermore, our analysis reveals that regions proximate to load centers can also support latency-sensitive inference tasks. This energy supply is capable of delivering 1 PWh globally in 2030 at levelized costs of around $39/MWh, meeting the forecasted electricity demand for AI by the International Energy Agency. Moreover, even if AI electricity demand increases 10-fold, reaching 10 PWh by 2030, the unit cost increment would be less than 20%. Further uncertainty analysis shows that under extreme investment (3.0×) and cooling (2.0×) cost assumptions for data centers operating with the desert WSS systems, this 10-PWh/yr demand could still be satisfied at competitive cost levels. The desert WSS systems could potentially align computational and clean energy infrastructure in the AI era, as well as simultaneously achieving decarbonization and ecological restoration. © 2026 The Author(s)

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2943.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
