---
id: paper-2544
title: 'Bifröst: Peer-to-Peer Load-Balancing for Function Execution in Agentic AI Systems'
authors:
- Coviello, Giuseppe
- Rao, Kunal
- Khojastepour, Mohammad A.
- Chakradhar, Srimat
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-3-031-99854-6_19
url: https://www.scopus.com/pages/publications/105015502014?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 279--291
keywords:
- Agentic AI systems
- Distributed systems
- Function as a Service
- Load balancing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Load-balancing P2P para execução de funções em sistemas agentic AI — agentic AI como workload servido (Boundary B).
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

# paper-2544 — Bifröst: Peer-to-Peer Load-Balancing for Function Execution in Agentic AI Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Agentic AI systems rely on Large Language Models (LLMs) to execute complex tasks by invoking external functions. The efficiency of these systems depends on how well function execution is managed, especially under heterogeneous and high-variance workloads, where function execution times can range from milliseconds to several seconds. Traditional load-balancing techniques, such as round-robin, least-loaded, and Peak-EWMA (used in Linkerd), struggle in such settings: round-robin ignores load imbalance, least-loaded reacts slowly to rapid workload shifts, and Peak-EWMA relies on latency tracking, which is ineffective for workloads with high execution time variability. In this paper, we introduce Bifröst, a peer-to-peer load-balancing mechanism that distributes function requests based on real-time active request count rather than latency estimates. Instead of relying on centralized load-balancers or client-side decisions, Bifröst enables function-serving pods to dynamically distribute load by comparing queue lengths and offloading requests accordingly. This avoids unnecessary overhead while ensuring better responsiveness under high-variance workloads. Our evaluation on open-vocabulary object detection, multi-modal understanding, and code generation workloads shows that Bifröst improves function completion time by up to 20% when processing 13,700 requests from 137 AI agents on a 32-node Kubernetes cluster, outperforming both OpenFaaS and OpenFaaS with Linkerd. In an AI-driven insurance claims processing workflow, Bifröst achieves up to 25% faster execution.   © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI agents" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Load-balancing P2P para execução de funções em sistemas agentic AI — agentic AI como workload servido (Boundary B)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2544.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
