---
id: paper-2568
title: Graph-Aware Diffusion Policy for Fault-Tolerant Agentic AI Service Migration in Edge Computing Power Networks
authors:
- Fang, Honglin
- Yu, Peng
- Liu, Xinxiu
- Liu, Jice
- Qu, Zhaowei
- Wang, Ying
- Li, Wenjing
- Guo, Shaoyong
- Wu, Celimuge
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2025.3627391
url: https://www.scopus.com/pages/publications/105020698397?origin=resultslist
publisher: IEEE Computer Society
pages: 5992--6009
keywords:
- agentic AI service
- diffusion policy
- edge computing power network
- Fault-tolerant
- proactive migration
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: Migração de serviços agentic AI com diffusion policy — agentic AI como workload sendo gerenciado, não como agente que decide RM.
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

# paper-2568 — Graph-Aware Diffusion Policy for Fault-Tolerant Agentic AI Service Migration in Edge Computing Power Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In edge computing power network environments, there is a growing demand to support compute-intensive Agentic AI Services, which are composed of interdependent functions represented as Directed Acyclic Graphs (DAGs). Nevertheless, the challenges posed by dynamic resource volatility and potential node failures significantly impact reliable task execution. Existing solutions (often reactive heuristics or GAN-based models) struggle to anticipate risks and overlook DAG dependencies. This paper introduces GADP, a Graph-Aware Diffusion Policy framework designed to facilitate proactive fault-tolerant DAG workload migration in large-scale edge computing systems. This paper presents GADP, a Graph-Aware Diffusion Policy framework for proactive, fault-tolerant DAG workload migration in large-scale edge systems. GADP integrates three key modules: a Transformer-GAT fault predictor for failure probability and type estimation; a DAG encoder that learns structure-preserving task embeddings via multi-round attention; and a diffusion policy generator that refines placement strategies through conditional denoising. Experiments on dynamic simulations with real workload traces show that GADP achieves 99.6% fault detection accuracy, 95.4% diagnosis F1, and over 60% fewer SLO violations, while consuming the least energy among baselines. These results demonstrate GADP's robustness and effectiveness in anticipatory migration under volatile edge conditions. © 2013 IEEE.

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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Transformer" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Agentic" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Agentic" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Migração de serviços agentic AI com diffusion policy — agentic AI como workload sendo gerenciado, não como agente que decide RM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2568.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
