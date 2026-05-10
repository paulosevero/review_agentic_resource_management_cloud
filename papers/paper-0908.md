---
id: paper-0908
title: 'Optimizing Microservice Deployment in Edge Computing with Large Language Models: Integrating Retrieval Augmented Generation and Chain of Thought Techniques'
authors:
- Feng, Kan
- Luo, Lijun
- Xia, Yongjun
- Luo, Bin
- He, Xingfeng
- Li, Kaihong
- Zha, Zhiyong
- Xu, Bo
- Peng, Kai
venue: Symmetry
venue_type: journal
year: 2024
doi: 10.3390/sym16111470
url: https://www.scopus.com/pages/publications/85210435496?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- large language models
- microservice deployment
- mobile edge computing
- retrieval augmented generation
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
  05-abstract-screening: include
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
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

# paper-0908 — Optimizing Microservice Deployment in Edge Computing with Large Language Models: Integrating Retrieval Augmented Generation and Chain of Thought Techniques

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) have demonstrated impressive capabilities in autogenerating code based on natural language instructions provided by humans. We observed that in the microservice models of edge computing, the problem of deployment latency optimization can be transformed into an NP-hard mathematical optimization problem. However, in the real world, deployment strategies at the edge often require immediate updates, while human-engineered code tends to be lagging. To bridge this gap, we innovatively integrated LLMs into the decision-making process for microservice deployment. Initially, we constructed a private Retrieval Augmented Generation (RAG) database containing prior knowledge. Subsequently, we employed meticulously designed step-by-step inductive instructions and used the chain of thought (CoT) technique to enable the LLM to learn, reason, reflect, and regenerate. We decomposed the microservice deployment latency optimization problem into a collection of granular sub-problems (described in natural language), progressively providing instructions to the fine-tuned LLM to generate corresponding code blocks. The generated code blocks underwent integration and consistency assessment. Additionally, we prompted the LLM to generate code without the use of the RAG database for comparative analysis. We executed the aforementioned code and comparison algorithm under identical operational environments and simulation parameters, conducting rigorous result analysis. Our fine-tuned model significantly reduced latencies by 22.8% in handling surges in request flows, 37.8% in managing complex microservice types, and 39.5% in processing increased network nodes compared to traditional algorithms. Moreover, our approach demonstrated marked improvements in latency performance over LLMs not utilizing RAG technology and reinforcement learning algorithms reported in other literature. The use of LLMs also highlights the concept of symmetry, as the symmetrical structure of input-output relationships in microservice deployment models aligns with the LLM’s inherent ability to process and generate balanced and optimized code. Symmetry in this context allows for more efficient resource allocation and reduces redundant operations, further enhancing the model’s effectiveness. We believe that LLMs hold substantial potential in optimizing microservice deployment models. © 2024 by the authors.

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
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Retrieval Augmented Generation" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Chain of Thought" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0908.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
