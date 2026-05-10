---
id: paper-1231
title: A Cloud-Native Approach for Orchestrating 6G-Enabled Services at the Computing Continuum
authors:
- Tzanettis, Ioannis
- Kakkavas, Grigorios
- Stylos, Alexandros
- Zafeiropoulos, Anastasios
- Papavassiliou, Symeon
venue: IEEE International Workshop on Computer Aided Modeling and Design of Communication Links and Networks, CAMAD
venue_type: conference
year: 2024
doi: 10.1109/CAMAD62243.2024.10942907
url: https://www.scopus.com/pages/publications/105002867946?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 6G mobile communications
- autoscaling
- computing continuum
- migration
- offloading
- service orchestration
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1231 — A Cloud-Native Approach for Orchestrating 6G-Enabled Services at the Computing Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The cloudification of 6G services and the rise of edge and cloud computing have significantly increased the complexity of service lifecycle management, resulting in intricate networks deployed across interconnected infrastructures. The transition from traditional monitoring to modern cloud-native and network observability tools is crucial for providing a fine-grained view of application, infrastructure, and network performance. This paper proposes a novel orchestration methodology that enhances monitoring insights and effectively manages computing and network resources from the extreme edge to the cloud. Our approach encompasses synergetic orchestration mechanisms leveraging multi-agent systems, data fusion from various observability signals, and machine learning techniques wherever possible. Beyond conceptualizing and designing this methodology, we detail a tangible closed-loop architecture capable of supporting and realizing the proposed mechanisms. Finally, we validate a prototype implementation and evaluate its performance through a proof of concept involving realistic experimental trials, demonstrating our solution's effectiveness in orchestrating a 6G- enabled application with stringent latency requirements.  © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1231.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
