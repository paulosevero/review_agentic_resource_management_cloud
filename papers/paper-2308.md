---
id: paper-2308
title: Enhancing IoT Applications' Placement in the Fog with Proactive Infeasibility Detection and Repair
authors:
- Xia, Ye
- Zhang, Xing
venue: 2025 10th International Conference on Fog and Mobile Edge Computing, FMEC 2025
venue_type: conference
year: 2025
doi: 10.1109/FMEC65595.2025.11119366
url: https://www.scopus.com/pages/publications/105016116627?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 74--80
keywords:
- Fog Computing
- Infeasibility Repairing
- Machine Learning
- Placement
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2308 — Enhancing IoT Applications' Placement in the Fog with Proactive Infeasibility Detection and Repair

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog computing extends processing and storage resources to the edge of the network by making use of heterogeneous devices. How to efficiently use resources in the fog remains a challenge not only because of the complexity of selecting appropriate hosts for distributed applications, but also due to the lack of guaranteed resource capacities to meet all applications’ deployment requests. Application host selection, which is also known as the placement problem, is typically modeled as an optimization problem with hard constraints, which is computationally expensive. Therefore, it is essential to ensure that valid solutions exist (i.e., the problem’s feasibility) before passing a placement problem to the optimization module. Otherwise, potential retries in placement decision making can degrade the responsiveness and reliability of the fog infrastructure. This paper presents an infeasibility repair approach to avoid inputting infeasible problems to placement optimization modules. The proposed approach integrates a Machine Learning-based infeasibility detection module with a heuristic algorithm to update the application set under consideration. Multiple datasets<sup>1</sup> representing diverse infrastructures are generated to train and evaluate the proposed model. Experiments show that our model achieves 86% infeasibility detection accuracy, outperforming the state-of-the-art Large Language Model with few-shot prompting. Furthermore, the model demonstrates strong generalizability—it has the capability to suit infrastructures that do not exist in its training data, making it a robust solution for dynamic fog environments. These results highlight the effectiveness of the proposed model in identifying infeasible problems without invoking computationally expensive optimization modules, which can significantly reduce computation time and ensure the system’s responsiveness. ©2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2308.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
