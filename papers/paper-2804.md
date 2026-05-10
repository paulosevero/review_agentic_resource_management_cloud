---
id: paper-2804
title: A Co-Designed KubeEdge-SDN Multi-Agent Framework for Secure and Predictable IIoT Manufacturing
authors:
- Tshakwanda, Petro M.
- Tsegaye, Henok B.
- Karukutla, Ashok
- Almaayn, Raddad
- Kumar, Harsh
- Devetsikiotis, Michael
venue: 2026 International Conference on Computing, Networking and Communications, ICNC 2026
venue_type: conference
year: 2026
doi: 10.1109/ICNC68183.2026.11416915
url: https://www.scopus.com/pages/publications/105035738444?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 328--332
keywords:
- Anomaly Detection
- Edge Computing
- Industrial IoT (IIoT)
- IoT Manufacturing
- KubeEdge
- Kubernetes
- Multi-Agent Systems
- Ray
- Software-Defined Networking (SDN)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2804 — A Co-Designed KubeEdge-SDN Multi-Agent Framework for Secure and Predictable IIoT Manufacturing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Industrial IoT (IIoT) networks increasingly rely on cloud-edge computing, but many deployments still struggle to meet tight latency, resilience, and security requirements in intelligent manufacturing. We present a co-designed KubeEdge-SDN-multi-agent framework that unifies Kubernetesbased orchestration, Ryu/OVS software-defined flow control, and Ray-based distributed agents into a single secure edge fabric. The framework enables low-latency anomaly detection, resilient failover, and SDN micro-segmentation for additive manufacturing workloads while keeping predictable performance at the Operational Technology (OT) edge. On a repeatable testbed, it sustains sub-100 ms anomaly-detection latency with high availability and keeps nearly all control events below 500 ms. Compared with EWMA, CUSUM, and Isolation-Forest baselines, our agents improve detection accuracy while respecting ISA-95 Level-2 timing constraints. The stack scales to 64 coordinated agents under adversarial load and provides a practical blueprint for secure, predictable Industry 4.0 deployments in additive manufacturing (AM). © 2026 IEEE.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2804.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
