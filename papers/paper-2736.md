---
id: paper-2736
title: 'LAGTrust: Language-Augmented Graph Representation Learning for Trust Evaluation in Cloud-Network Convergence'
authors:
- Pan, Fan
- Cui, Pengshuai
- Zhang, Jiaqi
- Pei, Jinchuan
- Song, Xuanyan
- Hu, Yuxiang
- Long, Keping
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2026
doi: 10.1109/TNSE.2026.3680408
url: https://www.scopus.com/pages/publications/105034815478?origin=resultslist
publisher: IEEE Computer Society
pages: ''
keywords:
- Cloud-network Convergence
- Graph Representation Learning
- Large Language Models
- Trust Evaluation
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
    my_justification: Talvez o fato de ter um "language-augmented" indique uso de LLM+GNN
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
    my_final_decision: Exclude
    my_justification: LAGTrust gera scores de TRUST e explicações causais para entidades em cloud-network convergence; saída é avaliação interpretável de confiança, não ação de RM. Sistema downstream usaria
      a saída — closed loop de RM não demonstrado no paper.
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

# paper-2736 — LAGTrust: Language-Augmented Graph Representation Learning for Trust Evaluation in Cloud-Network Convergence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud-network convergence represents a pivotal architectural evolution in modern communication networks, enabling unified orchestration of computing, storage, and network resources. Within such environment, trust evaluation plays an essential role in ensuring secure resource scheduling and reliable service deployment. While graph representation learning (GRL) has emerged as a powerful paradigm for trust evaluation by capturing complex relational patterns among entities, existing approaches still face three fundamental challenges: resource heterogeneity, data sparsity, and insufficient interpretability. To address these challenges, we propose LAGTrust, a Language-Augmented Graph representation learning framework for trust evaluation in cloud-network convergence. LAGTrust integrates large language models (LLMs) with graph neural networks through three synergistic components: (i) a Heterogeneous Feature Representation module that leverages LLMs to project multi-dimensional resource attributes into a unified semantic space while employing spatio-temporal graph neural networks to capture structural and behavioral dynamics; (ii) an Adaptive Feature Enhancement module that performs hierarchical LLM-driven augmentation for semantic completion, relationship inference, and profile enrichment; and (iii) a Semantic Explanation Generation module that synthesizes multi-source evidence through causal reasoning to produce interpretable trust assessments. Extensive experiments on real-world and synthetic topologies demonstrate that LAGTrust consistently outperforms baseline methods across multiple evaluation metrics, particularly under cold-start scenarios, validating its superior accuracy, robustness, and interpretability for trust evaluation in cloud-network convergence environments. © 2013 IEEE.

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
- **my_justification:** "Talvez o fato de ter um "language-augmented" indique uso de LLM+GNN"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Language-Augmented" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Language-Augmented" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LAGTrust gera scores de TRUST e explicações causais para entidades em cloud-network convergence; saída é avaliação interpretável de confiança, não ação de RM. Sistema downstream usaria a saída — closed loop de RM não demonstrado no paper."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2736.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
