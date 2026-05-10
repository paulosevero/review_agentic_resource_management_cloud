---
id: paper-1793
title: Edge Computing-Enabled Peer-to-Peer Energy Trading in a Local Energy Community
authors:
- Li, Yehui
- Deng, Haoyuan
- Wang, Yi
venue: IEEE Transactions on Smart Grid
venue_type: journal
year: 2025
doi: 10.1109/TSG.2025.3574721
url: https://www.scopus.com/pages/publications/105007302762?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4058--4072
keywords:
- distributed energy resources
- edge computing
- edge intelligence
- Local energy community
- multi-agent reinforcement learning
- peer-to-peer energy trading
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

# paper-1793 — Edge Computing-Enabled Peer-to-Peer Energy Trading in a Local Energy Community

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Local energy communities establish a platform for prosumers and consumers to share surplus generation via peer-to-peer (P2P) energy trading. Traditional optimization techniques for energy management problems necessitate precise models and accurate predictions. In contrast, reinforcement learning has gained widespread attention as it can handle system uncertainties without relying on models. However, multi-agent reinforcement learning (MARL) approaches for P2P energy trading involve a large volume of communications and computations, hindering the practical deployment of decision-making algorithms on edge devices whose communication and computation resources are very limited. To this end, this paper proposes an efficient and privacy-preserving MARL approach for edge computing-enabled P2P energy trading. Specifically, we design an information interaction framework that shares representations rather than sensitive observations to protect the privacy of various agents. In addition, we develop an event-triggered communication approach that controls the frequency of interactions through a gating mechanism to reduce communication overhead among agents. To save the memory footprint of each agent, we investigate an evolutionary training method that updates the networks using perturbation without backward gradient computation. Case studies on a real-world dataset demonstrate that our proposed method yields significant efficiency improvements while maintaining high decision-making performance.  © IEEE. 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1793.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
