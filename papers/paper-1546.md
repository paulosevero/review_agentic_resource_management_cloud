---
id: paper-1546
title: Minimizing Economic Costs and Task Processing Fails in MEC-Enabled Satellite-Ground Integrated Networks With MADDPG and Fuzzy Logic
authors:
- Du, Jianbo
- Zhang, Jianjun
- Kong, Ziwen
- Yu, Zuting
- Hu, Bintao
- Jiang, Jing
- Lu, Guangyue
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2025
doi: 10.1109/TCE.2025.3574097
url: https://www.scopus.com/pages/publications/105006884201?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9021--9031
keywords:
- fuzzy logic
- multi-access edge computing (MEC)
- multi-agent deep deterministic policy gradient (MADDPG)
- Satellite-ground integrated networks
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

# paper-1546 — Minimizing Economic Costs and Task Processing Fails in MEC-Enabled Satellite-Ground Integrated Networks With MADDPG and Fuzzy Logic

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As the Internet of Things (IoT) continues to expand rapidly, traditional ground networks are increasingly unable to meet the growing demands for connectivity and coverage. To address these challenges, integrated satellite-ground networks have emerged as a vital solution, enhancing both coverage and reliability. At the same time, Multi-Access Edge Computing (MEC) enables intelligent task execution on IoT devices by deploying resources at the network edge. In this paper, we propose a joint optimization framework for task placement and removal, access control, business instance selection, and bandwidth allocation within MEC-enabled integrated satellite-ground IoT networks. To manage the inherent complexities and uncertainties in dynamic environments, we integrate fuzzy logic into the optimization process. Additionally, we introduce a deep reinforcement learning-based algorithm, specifically the Multi-Agent Deep Deterministic Policy Gradient (MADDPG), to effectively solve this problem. Experimental results demonstrate that the proposed algorithm outperforms benchmark methods in terms of convergence, while achieving minimized economic costs and reduced task processing failures. © 1975-2011 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1546.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
