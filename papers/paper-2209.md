---
id: paper-2209
title: Multigranularity Interleaved Reconfigurable Edge Data Center Network Architecture for Accelerated GAI Jobs
authors:
- Teng, Yun
- Yang, Hui
- Yao, Qiuyan
- Cheng, Wenlong
- Hao, Miao
- Zhang, Jie
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3531385
url: https://www.scopus.com/pages/publications/85217755481?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13222--13232
keywords:
- Demand-aware topology reconfiguration
- edge data centers
- hybrid electrical/optical switch
- multigranularity adaptive interleaving algorithm
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: sub-modo A] Arquitetura óptica/elétrica de edge data center para acelerar jobs GAI; GAI é o workload. RM decision é heurística multigranularity sobre topologia óptica, sem LLM agentic.
      | [3a-hardgate/keep] [sub-modo A / nota] O paper propõe um algoritmo clássico de scheduling para redes ópticas/elétricas em edge data centers, onde 'GAI jobs' são apenas o workload — não há LLM nem
      loop agentic no paper. Isso é sinal de Boundary A (escopo de sub-agente 1), não de hard gate documental (sub-modo A) nem de escopo de infraestrutura (sub-modo B). A infra (edge data center) está em
      escopo. Mantido como nota para sub-agente 1.
    agrees_with_regex: false
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

# paper-2209 — Multigranularity Interleaved Reconfigurable Edge Data Center Network Architecture for Accelerated GAI Jobs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The network has become a bottleneck for generative artificial intelligence (GAI) jobs. Accelerating GAI jobs in edge data centers using hybrid electrical/optical switch is considered a promising solution. This architecture optimizes bandwidth utilization by enabling demand-aware topology reconfiguration through flexible configuration of optical circuit switche optical circuit switches (OCS). However, frequent topology reconfiguration may increase latency. Therefore, there is a balanced relationship between latency and bandwidth utilization. In this article, we propose a multigranularity adaptive interleaved algorithm for service scheduling in edge data centers. First, different degrees of time slot shifts are introduced based on the latency sensitivity of jobs, where large bandwidth GAI jobs are transmitted in a single hop by configuring a demand-aware topology. Additionally, when the reconfiguration threshold is met, low-priority ports are prioritized for reconfiguration to ensure latency requirements are met. This approach effectively resolves the tradeoff between bandwidth utilization and latency by decoupling them from each other. Simulation results show that this approach can effectively reduce the latency and improve the network throughput.  © 2025 IEEE.

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
- **agrees_with_regex:** False
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative artificial intellig" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "generative artificial intellig" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "generative artificial intellig" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_gai, matched_substring: "GAI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_gai, matched_substring: "GAI" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "sub-modo A] Arquitetura óptica/elétrica de edge data center para acelerar jobs GAI; GAI é o workload. RM decision é heurística multigranularity sobre topologia óptica, sem LLM agentic. | [3a-hardgate/keep] [sub-modo A / nota] O paper propõe um algoritmo clássico de scheduling para redes ópticas/elétricas em edge data centers, onde 'GAI jobs' são apenas o workload — não há LLM nem loop agentic no paper. Isso é sinal de Boundary A (escopo de sub-agente 1), não de hard gate documental (sub-modo A) nem de escopo de infraestrutura (sub-modo B). A infra (edge data center) está em escopo. Mantido como nota para sub-agente 1."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2209.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
