---
id: paper-2585
title: Pose-Free Radiance Reconstruction with Depth and Exposure Priors on a Cloud-Native Hybrid KAN Framework
authors:
- Gong, Zhuohao
- Guo, Xinyang
- Hu, Wenxin
- Li, Yanjie
- Liu, Weichu
- Hu, Xiping
venue: IEEE Transactions on Cloud Computing
venue_type: journal
year: 2026
doi: 10.1109/TCC.2026.3670345
url: https://www.scopus.com/pages/publications/105032420992?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 3D Deep Learning
- Cloud Computing
- Scene Representation
- View Synthesis
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2585 — Pose-Free Radiance Reconstruction with Depth and Exposure Priors on a Cloud-Native Hybrid KAN Framework

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Training neural radiance fields without pre-estimated camera poses remains challenging, particularly in the presence of complex illumination and large inter-frame motion. This work presents a self-calibrating radiance-field framework designed to address these difficulties through a unified optimization strategy. Reliable monocular depth priors from the Depth Anything V2 model are incorporated to provide stable geometric constraints, and multiview point-cloud alignment is enforced to prevent pose drift under wide baselines. Illumination-induced photometric inconsistencies are handled by a jointly optimized exposure-compensation module that separates transient brightness variations from the underlying scene radiance. To enhance the representational capacity beyond that of standard multilayer perceptrons, a Kolmogorov-Arnold Network is adopted as the radiance-field backbone, enabling improved recovery of fine geometric and appearance details. The complete pipeline is deployed on a cloud-native infrastructure that supports scalable optimization and interactive access through an LLM-assisted interface. Experiments on indoor and outdoor datasets demonstrate that the proposed method consistently improves pose accuracy and novel-view synthesis quality over existing self-calibrating approaches. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2585.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
