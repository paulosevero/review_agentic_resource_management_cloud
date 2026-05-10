---
id: paper-2945
title: GAN-Enhanced Multi-Agent Deep Reinforcement Learning for Consumer-Centric Digital Twin Driven Urological Surgical Resource Optimization in Healthcare 5.0
authors:
- Zhu, Jiabao
- Khan, Shakir
- Agrawal, Seema
- Lyu, Jianhui
- Wang, Chao
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2026
doi: 10.1109/TCE.2026.3669398
url: https://www.scopus.com/pages/publications/105031927637?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Consumer-centric digital twin
- healthcare 5
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2945 — GAN-Enhanced Multi-Agent Deep Reinforcement Learning for Consumer-Centric Digital Twin Driven Urological Surgical Resource Optimization in Healthcare 5.0

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Urological cancer surgeries, including bladder tumor resections and kidney nephrectomies, require intensive computational resources for preoperative surgical planning, intraoperative navigation, and postoperative monitoring, straining hospital edge computing infrastructure in healthcare 5.0 ecosystems. Consumer-centric digital twin technology offers solutions through virtual patient replicas, enabling predictive resource allocation. However, existing approaches face limitations in medical training data availability, multi-agent coordination across heterogeneous patient populations, and privacy preservation for sensitive health information. This paper proposes UroTwin-MADRL, an integrated framework combining conditional generative adversarial networks with multi-agent deep deterministic policy gradient algorithms for intelligent surgical resource optimization. The system architecture establishes bidirectional mappings between physical healthcare infrastructure and digital twin virtual layers, enabling privacy-preserving knowledge sharing through federated learning mechanisms. Experiments on MedMNIST and MIMIC-IV datasets demonstrate that UroTwin-MADRL achieves 18.3% latency reduction and 27.6% energy savings compared to baselines. Deployment feasibility validation across hospital operational scales maintains stability indices above 0.85, while computational resource analysis confirms edge device compatibility with inference latency under 40 milliseconds. Privacy risk assessment reduces membership inference attack success rates below 19%, and ablation studies validate synergistic component contributions. © 1975-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2945.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
