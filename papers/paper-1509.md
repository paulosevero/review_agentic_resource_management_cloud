---
id: "paper-1509"
title: "Ephemeral Kubernetes: dynamically deleting and recreating clusters using Warewulf"
authors: ["Decker, Jonathan", "Kunkel, Julian"]
year: 2025
venue: "Journal of Supercomputing"
venue_type: "journal"
doi: "10.1007/s11227-025-07668-y"
url: "https://www.scopus.com/pages/publications/105019525815?origin=resultslist"
publisher: "Springer"
pages: ""
keywords: ["HPC", "Kubernetes", "Scheduling", "Security", "Service", "Warewulf"]
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

# paper-1509 — Ephemeral Kubernetes: dynamically deleting and recreating clusters using Warewulf

## Metadata

- **Authors:** Decker, Jonathan and Kunkel, Julian
- **Year:** 2025
- **Venue:** Journal of Supercomputing
- **DOI:** 10.1007/s11227-025-07668-y
- **URL:** https://www.scopus.com/pages/publications/105019525815?origin=resultslist
- **Publisher:** Springer
- **Pages:** 
- **Language:** English
- **Keywords:** HPC; Kubernetes; Scheduling; Security; Service; Warewulf

### Abstract

With the rise of LLMs, GPU acceleration has become essential for both training and serving AI models. This requires HPC systems to be highly flexible with assigning multi-GPU nodes while also maintaining high security standards. Existing approaches involve utilizing nodes with batch and service schedulers, e.g., Slurm and Kubernetes, by dynamically moving nodes between the schedulers either through negotiation between the systems or via an external system. However, such a multi-use approach also increases the attack surface as more scheduling components operate with root permission. Moreover, it becomes increasingly difficult to recover from a security incident as attackers might have infected parts of either scheduling system. In this work, we present Ephemeral Kubernetes as a way to dynamically deploy and remove Kubernetes clusters in Warewulf managed environments such that nodes can be booted to be either part of a Slurm or Kubernetes cluster while being wiped at shutdown. © The Author(s) 2025.

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
