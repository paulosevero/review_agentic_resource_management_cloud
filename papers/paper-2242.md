---
id: paper-2242
title: 'Poster: Reconstructing LLM Training Workloads: A Topology- and Model-aware Network Tester'
authors:
- Vogt, Francisco Germano
- Yang, Zhiheng
- Lopes, Victor Hugo Schneider
- Rodríguez, Fabricio
- Luizelli, Marcelo Caggiani
- Rothenberg, Christian Esteve
- Papagianni, Chrysa
venue: CoNEXT 2025 - Proceedings of the 21st International Conference on Emerging Networking EXperiments and Technologies
venue_type: conference
year: 2025
doi: 10.1145/3765515.3771757
url: https://www.scopus.com/pages/publications/105023972677?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 41--42
keywords:
- llm workloads
- network testing
- p4
- programmable switches
- rdma emulation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2242 — Poster: Reconstructing LLM Training Workloads: A Topology- and Model-aware Network Tester

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Model (LLM) training generates synchronized Remote Direct Memory Access (RDMA) bursts that heavily stress datacenter fabrics and are highly sensitive to faults. However, access to full-scale training clusters is costly, and existing network testers fail to accurately reproduce such patterns. We introduce GPTraffic, a topology- and model-aware testing framework that predicts, emulates, and analyzes LLM training workloads on programmable hardware. By combining burst-accurate traffic generation, RDMA-aware semantics, and fine-grained fault injection, GPTraffic enables scalable, realistic, and reproducible experiments that faithfully reflect the dynamics of distributed LLM training. This allows researchers to explore performance bottlenecks, congestion behavior, and fault tolerance under conditions that closely mirror real-world AI training workloads. © 2025 Owner/Author.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2242.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
