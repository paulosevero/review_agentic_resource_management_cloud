---
id: paper-1849
title: Fault-Tolerant Differential Privacy Routing of Human-Cyber-Physical Fusion Systems for Large Language Models Security
authors:
- Lin, Limei
- Huang, Yanze
- Wang, Xiaoding
- Garg, Sahil
- Moussa, Sherif
- Alrashoud, Mubarak
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3564766
url: https://www.scopus.com/pages/publications/105004052665?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 51821--51831
keywords:
- Completely independent spanning trees (CISTs)
- large language models security (LLM)
- privacy routing
- secure multiparty computing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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
    proposed_decision: Exclude
    proposed_justification: LLM as workload
    winning_category: llm_as_workload
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1849 — Fault-Tolerant Differential Privacy Routing of Human-Cyber-Physical Fusion Systems for Large Language Models Security

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid proliferation of Internet of Things (IoT) systems has introduced complex networks of interconnected devices, computational resources, and web-based communication infrastructure. Privacy protection in IoT data routing is critical to enabling secure deployment of large language models (LLMs) for processing distributed sensor data, user queries, and device-generated content. However, IoT environments inherently involve heterogeneous devices, dynamic network topologies, and resource-constrained nodes, complicating the design of privacy-preserving routing mechanisms that simultaneously ensure reliability across diverse communication layers. To address these challenges, we propose an innovative Fault-Tolerant Privacy Routing (FtPR) model based on secure multiparty computing mechanism, which enables secure and efficient data fusion and transmission in IoT networks. FtPR establishes a novel connection between IoT device clusters and data center network architecture AQDNn routers, leveraging the hierarchical architecture of AQDNn to construct completely independent spanning trees (CIST). By exploiting the nonoverlapping paths between nodes in distinct CISTs, FtPR achieves fault-tolerant routing while maintaining privacy guarantees. Building on this framework, we introduce a secure multiparty computing mechanism to perturb link weights in the AQDNn. This ensures that link weights across different CISTs adhere to constrained ranges, preventing adversarial inference of routing paths. Each node operates with localized knowledge of its connected link weights, eliminating the need for global network visibility. Consequently, even if malicious actors compromise one or multiple nodes, they cannot reconstruct end-to-end communication paths, thereby preserving route anonymity. Experimental results demonstrate that FtPR improves IoT network performance and security, reducing misclassification rates and marginal release score compared to state-of-the-art methods.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deployment of large language m" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Large Language Models" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1849.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
