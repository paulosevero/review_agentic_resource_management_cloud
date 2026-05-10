---
id: paper-1407
title: 'Active Prompt Caching in Edge Networks for Generative AI and LLMs: An RL-Based Approach'
authors:
- Baccour, Emna
- Erbad, Aiman
- Mohamed, Amr
- Hamdi, Mounir
- Guizani, Mohsen
venue: IEEE Wireless Communications and Networking Conference, WCNC
venue_type: conference
year: 2025
doi: 10.1109/WCNC61545.2025.10978306
url: https://www.scopus.com/pages/publications/105006470020?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- BSUM
- collaborative edge computing
- Generative AI
- LLM
- prompts caching
- RL
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL + LLM as workload
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

# paper-1407 — Active Prompt Caching in Edge Networks for Generative AI and LLMs: An RL-Based Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Generative AI (GAI) and Large Language Models (LLMs) have revolutionized natural language processing and content creation. However, their significant computational demands during inference often require cloud servers, which are currently the only viable option for handling complex multi-modal models like GPT-4. The inherent complexity of these models increases latency, posing challenges even within cloud environments. Furthermore, cloud reliance brings other challenges, including high bandwidth consumption to transfer diverse data types. Worse, in personalized GAI applications like virtual assistants, similar prompts frequently occur, causing redundant transmission and computation of replies, which further increases overhead. Accelerating the inference of multi-modal systems is, therefore, critical in artificial intelligence. In this paper, we aim to improve the inference efficiency through prompt caching; if a current prompt is semantically similar to a previous one, the system can reuse the earlier response without invoking the model again. We leverage collaborative edge computing to cache popular replies and store their request embeddings. New prompts are locally processed to extract embeddings, with their qualities determined by the resources available on edge servers. Our problem is formulated as an optimization to manage offloading decisions for GAI tasks, aiming to avoid cloud inferences and minimize latency while maximizing reply quality. Given its non-convex nature, we propose to solve it via Block Successive Upper Bound Minimization (BSUM). Reinforcement learning is employed to actively pre-cache prompts, tackling the complexity of unknown prompt popularity. Our approach demonstrates near-optimal performance, significantly outperforming cloud-only solutions. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL + LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1407.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
