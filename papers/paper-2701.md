---
id: "paper-2701"
title: "TiPE-SAM: Tiny and Parameter-Efficient SAM for Edge Medical Image Segmentation with Mixture-of-Shape-Experts Priors"
authors: ["Lv, Xingguo", "Li, Ningshu", "Zhao, Lei", "Xu, Kai", "Lin, Qika", "Zhu, Yifan", "Zhang, Chuan", "Pu, Bin"]
year: 2026
venue: "IEEE Transactions on Artificial Intelligence"
venue_type: "journal"
doi: "10.1109/TAI.2026.3665493"
url: "https://www.scopus.com/pages/publications/105030703364?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Edge computing", "Medical image segmentation", "Parameter-efficient fine-tuning", "Vision Foundation Model"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-2701 — TiPE-SAM: Tiny and Parameter-Efficient SAM for Edge Medical Image Segmentation with Mixture-of-Shape-Experts Priors

## Metadata

- **Authors:** Lv, Xingguo and Li, Ningshu and Zhao, Lei and Xu, Kai and Lin, Qika and Zhu, Yifan and Zhang, Chuan and Pu, Bin
- **Year:** 2026
- **Venue:** IEEE Transactions on Artificial Intelligence
- **DOI:** 10.1109/TAI.2026.3665493
- **URL:** https://www.scopus.com/pages/publications/105030703364?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge computing; Medical image segmentation; Parameter-efficient fine-tuning; Vision Foundation Model

### Abstract

Medical image segmentation is a foundational component of numerous clinical measurement and quantitative analysis pipelines. However, deploying foundation models such as the Segment Anything Model (SAM) on clinical edge devices is hindered by stringent computational and memory constraints: their large model size renders full fine-tuning impractical, and existing efficient variants rarely incorporate anatomical priors or optimize for device-level resource budgets. We propose TiPESAM (Tiny, Parameter-Efficient SAM for Edge Devices), which augments a frozen SAM encoder with a shape-based mixture-of-experts prior, low-rank adaptation, and resource-aware execution. A learned dictionary of shape experts and a pixelwise gating network reconstruct a low-resolution shape map that is re-encoded as a dense structural prompt and fused with encoder tokens for the SAM decoder. To satisfy edge constraints, we define multiple execution profiles with device-specific costs and train a cost-aware routing network that trades off segmentation accuracy and expected computation. On multicenter echocardiographic segmentation benchmarks, TiPE-SAM matches or surpasses SAM-based baselines with only ~0.5M trainable parameters (less than 1% of the ViT-B) and provides explicit control over parameter and inference budgets, enabling resource-efficient deployment of medical foundation models. © 2020 IEEE.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
