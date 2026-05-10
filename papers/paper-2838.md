---
id: paper-2838
title: Towards a scalable reinforcement learning approach for fair service function chain partitioning in mobile edge computing
authors:
- Wang, Qiyu
- Zhang, Zilin
- Zhu, Qiang
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2026.112131
url: https://www.scopus.com/pages/publications/105031601143?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Fairness
- Network function parallelization
- Network function virtualization
- Reinforcement learning
- Scalability
- Service function chain
- SFC partitioning
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

# paper-2838 — Towards a scalable reinforcement learning approach for fair service function chain partitioning in mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Network Function Virtualization (NFV) enables flexible and dynamic network processing by decoupling network functions from dedicated hardware devices. However, the rapid expansion of NFV introduces new challenges in efficiently managing and deploying Service Function Chains (SFCs) within distributed Mobile Edge Computing (MEC) infrastructures. The inherent length of SFCs—comprising multiple interconnected Virtual Network Functions (VNFs)—often results in undesirable end-to-end latency. To address this issue, Network Function Parallelization (NFP) allows concurrent execution of multiple VNFs, thereby reducing service latency. A key challenge in NFP lies in partitioning SFCs into multiple sub-SFCs, where resource constraints make optimal partitioning difficult. Traditional SFC partitioning methods often suffer from high computational overhead and poor scalability, while existing reinforcement learning-based approaches struggle to capture interdependencies among VNFs. To bridge this gap, this paper introduces a Scalable Reinforcement Learning-based Fair SFC Partitioning framework (SRLFP) for NFP-oriented orchestration that jointly balances resource utilization and service latency. The SRLFP employs a multi-agent cooperative actor–critic architecture that enables efficient inter-agent communication and coordination. Furthermore, a self-attention mechanism is integrated to identify and model intricate dependencies among VNFs, enhancing decision accuracy. SRLFP incorporates a partial parallelization strategy to decompose SFC requests into multiple parallel partitions while mitigating excessive parallelization overhead. Extensive simulation results demonstrate that SRLFP significantly improves resource utilization efficiency and scalability, achieving lower service latency compared to state-of-the-art baseline methods. © 2026 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2838.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
