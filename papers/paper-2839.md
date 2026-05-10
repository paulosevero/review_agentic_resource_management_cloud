---
id: paper-2839
title: 'UAV-Assisted Task Offloading and Resource Allocation in Internet of Vehicles: An Integration of Digital Twin and Generative AI'
authors:
- Wang, Xing
- He, Chao
- Jiang, Wenhui
- Wang, Wanting
- Li, Leida
- Xie, Xin
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2025.3645844
url: https://www.scopus.com/pages/publications/105025717055?origin=resultslist
publisher: IEEE Computer Society
pages: 5038--5055
keywords:
- digital twin (DT)
- federated deep reinforcement learning (FDRL)
- generative adversarial network (GAN)
- Internet of Vehicles (IoV)
- multi-agent deep deterministic policy gradient (MADDPG)
- unmanned aerial vehicles (UAVs)
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
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: LLM as workload
    winning_category: llm_as_workload
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: 'UAV-IoV: GAN/FDRL-GAN para offloading; GAI ''predicts task demands'' como gerador dentro de FDRL. Decision-making é DRL/MADDPG; GAI é augmentação de geração, não agente LLM no loop.'
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-2839 — UAV-Assisted Task Offloading and Resource Allocation in Internet of Vehicles: An Integration of Digital Twin and Generative AI

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the increasing deployment of environment-aware services in the Internet of Vehicles (IoV), vehicles are required to execute multiple computational tasks in real time. However, resource allocation and task offloading in unmanned aerial vehicles (UAVs)-assisted IoV systems remain challenging due tothe growing number of vehicle terminals (VTs), potential privacy leakage, and resource-constrained edge devices. This paper proposes a digital twin (DT) and generative artificial intelligence (GAI)-powered hierarchical aerial-ground cooperative architecture (DTG-HACA) that achieves dynamic resource optimization through a three-layer framework. The DT layer enables real-time synchronization of vehicle/UAV states and simulated trajectory planning. The high altitude platforms (HAPs) layer provides low-latency offloading channels through stratospheric wide-area coverage and solar-powered endurance, while the physical entity layer executes energy-efficient edge computing via UAV-vehicle-roadside units (RSUs) collaboration. For UAV trajectory optimization, we introduce the multi-agent deep deterministic policy gradient (MADDPG)-improved prioritized experience replay (MADDPG-IPER) algorithm that minimizes communication overhead and energy consumption while integrating DT-simulated trajectory planning. For the joint challenge of edge caching and task offloading under privacy preservation constraints, we develop a federated deep reinforcement learning (FDRL) based generative adversarial network (FDRL-GAN) algorithm. This solution addresses critical challenges in dynamic task offloading and resource allocation for UAV-assisted IoV by leveraging GAI to predict task demands for cache hit rate optimization, while implementing FDRL for distributed privacy-preserving decision-making without raw data sharing, thereby achieving global resource allocation optimality. Extensive simulation experiments confirm that our proposed scheme demonstrates significant advantages over existing benchmark algorithms across five critical performance metrics, including training stability, computational capacity, task offloading efficiency, cache hit rate, and energy consumption. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "With the increasing deployment" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative artificial intellig" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "UAV-IoV: GAN/FDRL-GAN para offloading; GAI 'predicts task demands' como gerador dentro de FDRL. Decision-making é DRL/MADDPG; GAI é augmentação de geração, não agente LLM no loop."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2839.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
