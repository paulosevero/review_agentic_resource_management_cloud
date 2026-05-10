---
id: paper-2890
title: 'Distribution Network Optimization for Low-Carbon Energy Supply in Data Centers: A Boundary-Interpretable Feasible Region Method'
authors:
- Yin, Weihao
- Zhang, Tiance
- Li, Gengyin
- Wang, Jianxiao
- Zhou, Ming
- Guo, Qiang
venue: IEEE Transactions on Industry Applications
venue_type: journal
year: 2026
doi: 10.1109/TIA.2026.3677816
url: https://www.scopus.com/pages/publications/105034879958?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Boundary-Interpretable Feasible Region
- Coordinated Optimization Mechanism
- Data Center
- Low-Carbon Electricity Delivery
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2890 — Distribution Network Optimization for Low-Carbon Energy Supply in Data Centers: A Boundary-Interpretable Feasible Region Method

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the proliferation of lightweight generative artificial intelligence, data centers (DCs) are increasingly deployed within distribution networks (DNs). Their highly stochastic and high-power demands pose significant challenges to achieving low-carbon and secure power supply. Thus, coordinating the operation of DNs and DCs is critical for ensuring reliable low-carbon electricity delivery. However, significant barriers persist due to the integration of numerous distributed energy resources (DERs) and operational privacy requirements among stakeholders. To enable secure coordination while safeguarding model confidentiality, a boundary-interpretable feasible region (BIFR) method is proposed in this paper. This method can capture the intrinsic relationship between the controllable variables and the boundary responses that affect both carbon emissions and system safety performance. Based on the BIFR, a bidirectional coordinated optimization mechanism for DC-DN systems is established. The mechanism determines optimization strategies for low-carbon collaborative operation according to the coupled BIFR by iterative bidirectional adjustments until convergence. This mechanism achieves efficient DC-DN coordination through minimal information exchange while preventing privacy breaches. Case studies on modified IEEE 33-bus and Caracas 141-bus distribution networks validate the effectiveness and efficiency of the proposed method. © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2890.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
