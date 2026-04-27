---
id: "paper-2564"
title: "Protocol-Driven Agentic Integration of LLMs: A Multi-tool Use Case"
authors: ["Ersoy, P\u0131nar", "Er\u015fahin, Mustafa"]
year: 2026
venue: "Communications in Computer and Information Science"
venue_type: "conference"
doi: "10.1007/978-3-032-15632-7_8"
url: "https://www.scopus.com/pages/publications/105029083378?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "139--148"
keywords: ["Agentic AI", "Large Language Models (LLM)", "Model Context Protocol (MCP)"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2564 — Protocol-Driven Agentic Integration of LLMs: A Multi-tool Use Case

## Metadata

- **Authors:** Ersoy, Pınar and Erşahin, Mustafa
- **Year:** 2026
- **Venue:** Communications in Computer and Information Science
- **DOI:** 10.1007/978-3-032-15632-7_8
- **URL:** https://www.scopus.com/pages/publications/105029083378?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 139--148
- **Language:** English
- **Keywords:** Agentic AI; Large Language Models (LLM); Model Context Protocol (MCP)

### Abstract

Agentic architectures that ensemble specialized AI agents offer modularity, parallel throughput, and fault isolation for complex workflows yet demand rigorous integration layers to connect large-language-model (LLM) reasoning with external tools in a reproducible, auditable manner. We present a comprehensive integration of Anthropic’s Model Context Protocol (MCP)—a transport-agnostic JSON-RPC 2.0 framework whose machine-readable schemas advertise typed capabilities and unified error codes—with LangGraph. This state-preserving orchestrator models agent workflows as directed graphs of concurrent nodes. An industrial-grade MCP server implemented in Python 3.11 enforces strict JSON-Schema validation, cryptographic authentication, and exponential back-off retries. It is deployed as a Helm-packaged container for bit-for-bit reproducibility. The stack is evaluated in four production-realistic scenarios on a homogeneous Kubernetes cluster. First, an enterprise knowledge-base assistant couples an LLM planner with a vector-search MCP resource to sustain sub-second P95 responses in the documents while isolating schema violations. Second, an autonomous data-analysis pipeline interleaves sandboxed Python evaluation with on-the-fly SVG charting, generating FAIR-compliant provenance bundles that ensure data are findable, accessible, interoperable, and reusable. Third, a cross-agent scheduling workflow integrates Google Agent-to-Agent delegation with vertical MCP tool calls to Microsoft Graph, upholding ISO 27001 segregation of duties and sub-second end-to-end latency under continuous soak testing. Finally, an automated pharmacovigilance pipeline streams PubMed abstracts, extracts clinical metrics, and compiles Periodic Safety Update Reports whose SHA-256-backed audit trail meets EMA Good Pharmacovigilance Practice and CFR Part 11 electronic records requirements. Across these cases, MCP-enabled graphs scale linearly until external services saturate, degrade gracefully under injected faults, and retain end-to-end traceability. All code artifacts, container charts, and telemetry dashboards are released to foster replication, establishing the LangGraph and MCP stack as a robust foundation for compliant, high-throughput multi-agent systems. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

## 04 — Title Screening

**Title:** Protocol-Driven Agentic Integration of LLMs: A Multi-tool Use Case

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Protocol-Driven Agentic Integration of LLMs: A Multi-tool Use Case
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Protocol-Driven Agentic Integration of LLMs: A Multi-tool Use Case
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
