---
id: paper-2090
title: GenAI for bottleneck Detection in Cloud Architecture
authors:
- Roy Choudhury, Sharod
- Chahal, Dheeraj
- Phalak, Chetan
- Ramesh, Manju
- Singhal, Rekha
venue: ICPE Companion 2025 - Companion of the 16th ACM/SPEC International Conference on Performance Engineering
venue_type: conference
year: 2025
doi: 10.1145/3680256.3721333
url: https://www.scopus.com/pages/publications/105007283237?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 154--161
keywords:
- cloud computing
- cloud service optimization
- editable cloud architecture
- optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    my_justification: GenAI para detecção de gargalos em arquitetura cloud — análise/detecção, não decisão de RM.
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

# paper-2090 — GenAI for bottleneck Detection in Cloud Architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid adoption of cloud computing, accelerated by the global pandemic, has increased the need for efficient cloud architecture that balances cost and performance. As organizations migrate applications to the cloud, cloud architects face challenges in managing an overwhelming number of services - often exceeding a thousand. This paper presents a novel tool designed for editable cloud architecture management that automates the optimization process. Our solution enables cloud architects to visually design and edit cloud architectures while utilizing a backend represented as a directed acyclic graph in an adjacency matrix. This structure allows for dynamic adjustments based on real-time workload predictions, moving from reactive to proactive resource management. Leveraging advanced Generative AI models, specifically Azure's GPT-4o [11], our tool identifies alternative services that can effectively replace or supplement existing ones based on functionality. By extracting relevant data from AWS documentation, we provide actionable insights on service performance and cost. We validate our approach through use cases, demonstrating the tool's effectiveness in detecting potential bottlenecks and recommending service adjustments to eliminate Service Level Agreement (SLA) violations. Our findings indicate that the tool enhances performance and reduces operational costs, empowering cloud architects to make informed, data-driven decisions. This innovative approach significantly streamlines cloud resource management, ensuring organizations can effectively navigate the complexities of their cloud environments and achieve sustained operational excellence.  © 2025 ACM.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GenAI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "GenAI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative AI" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "GenAI para detecção de gargalos em arquitetura cloud — análise/detecção, não decisão de RM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2090.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
