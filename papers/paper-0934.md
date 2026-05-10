---
id: paper-0934
title: Computation and Privacy Protection for Satellite-Ground Digital Twin Networks
authors:
- Gong, Yongkang
- Yao, Haipeng
- Liu, Xiaonan
- Bennis, Mehdi
- Nallanathan, Arumugam
- Han, Zhu
venue: IEEE Transactions on Communications
venue_type: journal
year: 2024
doi: 10.1109/TCOMM.2024.3392795
url: https://www.scopus.com/pages/publications/85191336944?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5532--5546
keywords:
- blockchain-aided transaction verification
- model-agnostic meta-learning multi-agent deep federated reinforcement learning
- resource management
- Satellite-ground integrated digital twin networks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0934 — Computation and Privacy Protection for Satellite-Ground Digital Twin Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Satellite-ground integrated heterogeneous networks can relieve network congestion, release network resources and provide ubiquitous intelligence services for terrestrial users. Furthermore, digital twin technology can enable nearly-instant data mapping from the physical world to digital systems. The integration between satellite-ground integrated heterogeneous networks and digital twin alleviates the gap between data analyses and physical unities. However, the current challenges, such as the pricing policy, the stochastic task arrivals, the time-varying satellite locations, mutual channel interference, and resource scheduling mechanisms between the users and cloud servers, severely affect the improvement of quality of service. Hence, we establish a blockchain-aided Stackelberg game model for maximizing the pricing profits and network throughput in terms of minimizing privacy overhead, which is able to perform computation offloading, decrease channel interference, and improve privacy protection. Due to the long-term task queue in Stackelberg model, we propose a Lyapunov stability theory-based model-agnostic meta-learning aided multi-agent deep federated reinforcement learning framework to transfer the long-term task queue into the single time slot, and then optimize the central processing unit frequency, channel selection, task-offloading decision, block size, and cloud server price, which facilitate the integration of communication, computation, and block resources. Subsequently, several performance analyses show that the proposed learning framework can strengthen the privacy protection, approach the optimal time average function, and fulfill the long-term average queue size via lower computational complexity. Finally, our simulation results indicate that the proposed learning framework is superior to the existing baseline methods in terms of network throughput, channel interference, cloud server profits, and privacy overhead.  © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0934.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
