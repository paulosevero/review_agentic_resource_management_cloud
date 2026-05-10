---
id: paper-1913
title: Task Offloading in Dynamic Energy Splitting STAR-RIS Assisted NOMA-MEC Systems With Decomposition Based Multi-Agent DRL
authors:
- Lu, Baoshan
- Fang, Junli
- Hong, Xuemin
- Shi, Jianghong
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3557279
url: https://www.scopus.com/pages/publications/105002692920?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13091--13103
keywords:
- Mobile edge computing
- multi-agent deep reinforcement learning
- non-orthogonal multiple access
- simultaneously transmitting and reflecting reconfigurable intelligent surface
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

# paper-1913 — Task Offloading in Dynamic Energy Splitting STAR-RIS Assisted NOMA-MEC Systems With Decomposition Based Multi-Agent DRL

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper explores a system that integrates non-orthogonal multiple access (NOMA) with mobile edge computing (MEC), supported by a simultaneously transmitting and reflecting reconfigurable intelligent surface (STAR-RIS) in energy splitting (ES) mode. We aim to address the challenge of minimizing energy consumption over the long-term by modeling it as a non-convex optimization problem. To simplify the resolution of this complex issue, we introduce a decomposition approach using a multi-agent deep reinforcement learning (DRL) technique. Specifically, we decompose the problem into the sub-problems of computational resource and power allocation, and phase shifting, amplitude coefficient, offloading ratio, and time optimization. Based on theoretical derivations, we determine the optimal computational resource and power allocation for the given phase shifting, amplitude coefficient, offloading ratio, and time. Then, we propose a multi-agent twin delayed deep deterministic policy gradient (TD3) algorithm to jointly optimize phase shifting, amplitude coefficient, offloading ratio, and time for each time slot. Simulation outcomes demonstrate that the decomposition-based multi-agent TD3 (DB-MATD3) algorithm achieves faster convergence compared to conventional centralized DRL approaches. Compared with other existing methods, the proposed task offloading strategy, which employs the ES-based STAR-RIS, achieves energy savings of 28.7% to 40.8%. © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1913.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
