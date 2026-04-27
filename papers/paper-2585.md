---
id: "paper-2585"
title: "Pose-Free Radiance Reconstruction with Depth and Exposure Priors on a Cloud-Native Hybrid KAN Framework"
authors: ["Gong, Zhuohao", "Guo, Xinyang", "Hu, Wenxin", "Li, Yanjie", "Liu, Weichu", "Hu, Xiping"]
year: 2026
venue: "IEEE Transactions on Cloud Computing"
venue_type: "journal"
doi: "10.1109/TCC.2026.3670345"
url: "https://www.scopus.com/pages/publications/105032420992?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["3D Deep Learning", "Cloud Computing", "Scene Representation", "View Synthesis"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2585 — Pose-Free Radiance Reconstruction with Depth and Exposure Priors on a Cloud-Native Hybrid KAN Framework

## Metadata

- **Authors:** Gong, Zhuohao and Guo, Xinyang and Hu, Wenxin and Li, Yanjie and Liu, Weichu and Hu, Xiping
- **Year:** 2026
- **Venue:** IEEE Transactions on Cloud Computing
- **DOI:** 10.1109/TCC.2026.3670345
- **URL:** https://www.scopus.com/pages/publications/105032420992?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** 3D Deep Learning; Cloud Computing; Scene Representation; View Synthesis

### Abstract

Training neural radiance fields without pre-estimated camera poses remains challenging, particularly in the presence of complex illumination and large inter-frame motion. This work presents a self-calibrating radiance-field framework designed to address these difficulties through a unified optimization strategy. Reliable monocular depth priors from the Depth Anything V2 model are incorporated to provide stable geometric constraints, and multiview point-cloud alignment is enforced to prevent pose drift under wide baselines. Illumination-induced photometric inconsistencies are handled by a jointly optimized exposure-compensation module that separates transient brightness variations from the underlying scene radiance. To enhance the representational capacity beyond that of standard multilayer perceptrons, a Kolmogorov-Arnold Network is adopted as the radiance-field backbone, enabling improved recovery of fine geometric and appearance details. The complete pipeline is deployed on a cloud-native infrastructure that supports scalable optimization and interactive access through an LLM-assisted interface. Experiments on indoor and outdoor datasets demonstrate that the proposed method consistently improves pose accuracy and novel-view synthesis quality over existing self-calibrating approaches. © 2013 IEEE.

## 04 — Title Screening

**Title:** Pose-Free Radiance Reconstruction with Depth and Exposure Priors on a Cloud-Native Hybrid KAN Framework

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Pose-Free Radiance Reconstruction with Depth and Exposure Priors on a Cloud-Native Hybrid KAN Framework
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Pose-Free Radiance Reconstruction with Depth and Exposure Priors on a Cloud-Native Hybrid KAN Framework
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
