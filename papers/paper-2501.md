---
id: paper-2501
title: 'Sustainable autonomous multi-UAV edge computing: An energy-positive framework with hierarchical multi-timescale optimization'
authors:
- Al-Bakhrani, Ali A.
- Li, Mingchu
- Obaidat, Mohammad S.
- Manza, Ramesh R.
- Amran, Gehad Abdullah
- Tian, Jiyu
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2026.112254
url: https://www.scopus.com/pages/publications/105034733963?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Deep reinforcement learning
- Energy harvesting
- Energy-positive computing
- Hierarchical optimization
- Mobile edge computing
- Multi-UAV coordination
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2501 — Sustainable autonomous multi-UAV edge computing: An energy-positive framework with hierarchical multi-timescale optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> UAV-assisted mobile edge computing (MEC) enables flexible computational services for dynamic IoT environments, yet existing systems remain fundamentally constrained by energy limitations that prevent sustained autonomous operation. Current approaches universally adopt energy-minimization paradigms, treating UAV batteries as finite resources requiring periodic recharging precluding deployment in remote areas, disaster zones, and infrastructure-sparse environments where continuous coverage is most critical. This paper introduces a fundamental paradigm shift from energy-constrained to energy-positive UAV-MEC operation, where UAVs systematically harvest more energy than they consume through coordinated multi-source energy harvesting. We propose a hierarchical multi-timescale optimization framework integrating four specialized components: Enhanced Lyapunov Optimization (ELO) for millisecond-scale task offloading decisions, Adaptive Sequential Convex Optimization (ASCO) for second-scale energy-harvesting-aware trajectory planning, Context-Aware LSTM (CA-LSTM) for predictive mobility and workload management, and Multi-Agent Constrained Proximal Policy Optimization (MAC-PPO) for minute-scale multi-UAV coordination. This architecture aligns algorithmic decisions with natural system dynamics across distinct timescales. Rigorous theoretical analysis establishes convergence guarantees and performance bounds through six formal theorems. Comprehensive experiments with 30 IoT devices and 3 UAVs demonstrate transformative results: 94.80 ± 0.5% task completion rate, net energy accumulation of +1,462.7 ± 38.4 Joules compared to baseline deficits ranging from - 298 to - 684 Joules, and 40–50% reduction in required UAV fleet size. These results establish that energy-positive operation fundamentally transforms UAV-MEC from infrastructure-dependent platforms to truly autonomous systems capable of sustained operation. © 2026 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2501.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
