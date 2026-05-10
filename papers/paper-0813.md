---
id: paper-0813
title: Generalizable 5G RAN/MEC Slicing and Admission Control for Reliable Network Operation
authors:
- Ahmadi, Mahdieh
- Moayyedi, Arash
- Sulaiman, Muhammad
- Salahuddin, Mohammad A.
- Boutaba, Raouf
- Saleh, Aladdin
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2024
doi: 10.1109/TNSM.2024.3437217
url: https://www.scopus.com/pages/publications/85200262255?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5384--5399
keywords:
- 5G RAN
- deep reinforcement learning
- graph attention networks
- MEC
- network slicing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0813 — Generalizable 5G RAN/MEC Slicing and Admission Control for Reliable Network Operation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The virtualization and distribution of 5G Radio Access Network (RAN) functions across radio unit (RU), distributed unit (DU), and centralized unit (CU) in conjunction with multi-access edge computing (MEC) enable the creation of network slices tailored for various applications with distinct quality of service (QoS) demands. Nonetheless, given the dynamic nature of slice requests and limited network resources, optimizing long-term revenue for infrastructure providers (InPs) through real-time admission and embedding of slice requests poses a significant challenge. Prior works have employed Deep Reinforcement Learning (DRL) to address this issue, but these approaches require re-training with the slightest topology changes due to node/link failure or overlook the joint consideration of slice admission and embedding problems. This paper proposes a novel method, utilizing multi-agent DRL and Graph Attention Networks (GATs), to overcome these limitations. Specifically, we develop topology-independent admission and slicing agents that are scalable and generalizable across diverse metropolitan networks. Results demonstrate substantial revenue gains-up to 35.2% compared to heuristics and 19.5% when compared to other DRL-based methods. Moreover, our approach showcases robust performance in different network failure scenarios and substrate networks not seen during training without the need for re-training or re-tuning. Additionally, we bring interpretability by analyzing attention maps, which enables InPs to identify network bottlenecks, increase capacity at critical nodes, and gain a clear understanding of the model decision-making process.  © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0813.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
