---
id: paper-0842
title: Multi-Agent DRL for task offloading with delay reliability assurances in ris-aided MEC in UDN
authors:
- Cai, Yunlong
- Dong, Chongwu
- Qiao, Cheng
- Wen, Wushao
venue: 'Journal of Physics: Conference Series'
venue_type: conference
year: 2024
doi: 10.1088/1742-6596/2807/1/012034
url: https://www.scopus.com/pages/publications/85201300705?origin=resultslist
publisher: Institute of Physics
pages: ''
keywords:
- Computation offloading
- Mobile edge computing
- Queueing networks
- Queueing theory
- Reliability theory
- Delay violation
- Dense network
- Edge computing
- Multi agent
- Probability bound
- Reconfigurable
- Reliability assurance
- Task offloading
- Transmission performance
- Violation probability
- Resource allocation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0842 — Multi-Agent DRL for task offloading with delay reliability assurances in ris-aided MEC in UDN

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper focuses on the scenario where Reconfigurable Intelligent Surfaces (RISs) are introduced in ultra-dense networks (UDN) to guarantee the transmission performance of task offloading of users in Mobile Edge Computing (MEC). Considering users' task arrival and wireless channel stochasticity, we analyze the delay violation probability bound for each user's two-hop tandem queueing system with the Martingale theory, i.e., the task offloading and edge computing queues. By taking the delay violation probability bounds as the service reliability constraint, we further propose a MADRL-based algorithm, which co-trains each user and BS as independent and heterogeneous agents and maximizes the total energy efficiency of the system by jointly optimizing the users' offloading ratio, the RISs' phase-shift, and the BSs' resource allocation policy. Experimental results show that our algorithm can improve the EE by about 17.9% compared to other alternative methods under different reliability requirements. © Published under licence by IOP Publishing Ltd.

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
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0842.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
