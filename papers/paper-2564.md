---
id: paper-2564
title: 'Protocol-Driven Agentic Integration of LLMs: A Multi-tool Use Case'
authors:
- Ersoy, Pınar
- Erşahin, Mustafa
venue: Communications in Computer and Information Science
venue_type: conference
year: 2026
doi: 10.1007/978-3-032-15632-7_8
url: https://www.scopus.com/pages/publications/105029083378?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 139--148
keywords:
- Agentic AI
- Large Language Models (LLM)
- Model Context Protocol (MCP)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2564 — Protocol-Driven Agentic Integration of LLMs: A Multi-tool Use Case

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Agentic architectures that ensemble specialized AI agents offer modularity, parallel throughput, and fault isolation for complex workflows yet demand rigorous integration layers to connect large-language-model (LLM) reasoning with external tools in a reproducible, auditable manner. We present a comprehensive integration of Anthropic’s Model Context Protocol (MCP)—a transport-agnostic JSON-RPC 2.0 framework whose machine-readable schemas advertise typed capabilities and unified error codes—with LangGraph. This state-preserving orchestrator models agent workflows as directed graphs of concurrent nodes. An industrial-grade MCP server implemented in Python 3.11 enforces strict JSON-Schema validation, cryptographic authentication, and exponential back-off retries. It is deployed as a Helm-packaged container for bit-for-bit reproducibility. The stack is evaluated in four production-realistic scenarios on a homogeneous Kubernetes cluster. First, an enterprise knowledge-base assistant couples an LLM planner with a vector-search MCP resource to sustain sub-second P95 responses in the documents while isolating schema violations. Second, an autonomous data-analysis pipeline interleaves sandboxed Python evaluation with on-the-fly SVG charting, generating FAIR-compliant provenance bundles that ensure data are findable, accessible, interoperable, and reusable. Third, a cross-agent scheduling workflow integrates Google Agent-to-Agent delegation with vertical MCP tool calls to Microsoft Graph, upholding ISO 27001 segregation of duties and sub-second end-to-end latency under continuous soak testing. Finally, an automated pharmacovigilance pipeline streams PubMed abstracts, extracts clinical metrics, and compiles Periodic Safety Update Reports whose SHA-256-backed audit trail meets EMA Good Pharmacovigilance Practice and CFR Part 11 electronic records requirements. Across these cases, MCP-enabled graphs scale linearly until external services saturate, degrade gracefully under injected faults, and retain end-to-end traceability. All code artifacts, container charts, and telemetry dashboards are released to foster replication, establishing the LangGraph and MCP stack as a robust foundation for compliant, high-throughput multi-agent systems. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI agents" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2564.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
