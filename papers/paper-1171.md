---
id: paper-1171
title: Sustainability of Data Center Digital Twins with Reinforcement Learning
authors:
- Sarkar, Soumyendu
- Naug, Avisek
- Guillen, Antonio
- Luna, Ricardo
- Gundecha, Vineet
- Babu, Ashwin Ramesh
- Mousavi, Sajad
venue: Proceedings of the AAAI Conference on Artificial Intelligence
venue_type: conference
year: 2024
doi: 10.1609/aaai.v38i21.30580
url: https://www.scopus.com/pages/publications/85189630566?origin=resultslist
publisher: Association for the Advancement of Artificial Intelligence
pages: 23832--23834
keywords:
- Carbon footprint
- Climate control
- Digital storage
- E-learning
- Energy utilization
- Green computing
- Multi agent systems
- Sustainable development
- Carbon emissions
- Computational power
- Datacenter
- High energy consumption
- Intelligent designs
- Large data
- Machine-learning
- Multi-agent reinforcement learning
- Rapid growth
- Reinforcement learnings
- Reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1171 — Sustainability of Data Center Digital Twins with Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid growth of machine learning (ML) has led to an increased demand for computational power, resulting in larger data centers (DCs) and higher energy consumption. To address this issue and reduce carbon emissions, intelligent design and control of DC components such as IT servers, cabinets, HVAC cooling, flexible load shifting, and battery energy storage are essential. However, the complexity of designing and controlling them in tandem presents a significant challenge. While some individual components like CFD-based design and Reinforcement Learning (RL) based HVAC control have been researched, there's a gap in the holistic design and optimization covering all elements simultaneously. To tackle this, we've developed DCRL-Green, a multi-agent RL environment that empowers the ML community to design data centers and research, develop, and refine RL controllers for carbon footprint reduction in DCs. It is a flexible, modular, scalable, and configurable platform that can handle large High Performance Computing (HPC) clusters. Furthermore, in its default setup, DCRL-Green provides a benchmark for evaluating single as well as multi-agent RL algorithms. It easily allows users to subclass the default implementations and design their own control approaches, encouraging community development for sustainable data centers. Open Source Link: https://github.com/HewlettPackard/dc-rl. Copyright © 2024, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1171.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
