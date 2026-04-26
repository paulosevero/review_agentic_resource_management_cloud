---
id: "paper-595"
title: "DiviML: A Module-based Heuristic for Mapping Neural Networks onto Heterogeneous Platforms"
authors: ["Ghannane, Yassine", "Abdelfattah, Mohamed S."]
year: 2023
venue: "IEEE/ACM International Conference on Computer-Aided Design, Digest of Technical Papers, ICCAD"
venue_type: "conference"
doi: "10.1109/ICCAD57390.2023.10323712"
url: "https://www.scopus.com/pages/publications/85181398739?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Computer hardware", "Integer programming", "Mapping", "Program processors", "Video signal processing", "Datacenter", "Heterogeneous platforms", "Heterogeneous servers", "Mixed integer linear", "Module-based", "Networking video", "Neural-networks", "Solution quality", "Specialized hardware", "Video processing", "Deep neural networks"]
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

# paper-595 — DiviML: A Module-based Heuristic for Mapping Neural Networks onto Heterogeneous Platforms

## Metadata

- **Authors:** Ghannane, Yassine and Abdelfattah, Mohamed S.
- **Year:** 2023
- **Venue:** IEEE/ACM International Conference on Computer-Aided Design, Digest of Technical Papers, ICCAD
- **DOI:** 10.1109/ICCAD57390.2023.10323712
- **URL:** https://www.scopus.com/pages/publications/85181398739?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Computer hardware; Integer programming; Mapping; Program processors; Video signal processing; Datacenter; Heterogeneous platforms; Heterogeneous servers; Mixed integer linear; Module-based; Networking video; Neural-networks; Solution quality; Specialized hardware; Video processing; Deep neural networks

### Abstract

Datacenters are increasingly becoming heterogeneous, and are starting to include specialized hardware for networking, video processing, and especially deep learning. To leverage the heterogeneous compute capability of modern datacenters, we develop an approach for compiler-level partitioning of deep neural networks (DNNs) onto multiple interconnected hardware devices. We present a general framework for heterogeneous DNN compilation, offering automatic partitioning and device mapping. Our scheduler integrates both an exact solver, through a mixed integer linear programming (MILP) formulation, and a modularity-based heuristic for scalability. Furthermore, we propose a theoretical lower bound formula for the optimal solution, which enables the assessment of the heuristic solutions' quality. We evaluate our scheduler in optimizing both conventional DNNs and randomly-wired neural networks, subject to latency and throughput constraints, on a heterogeneous system comprised of a CPU and two distinct GPUs. Compared to naively running DNNs on the fastest GPU, the proposed framework can achieve more than 3× lower latency and up to 2.9× higher throughput by automatically leveraging both data and model parallelism to deploy DNNs on our sample heterogeneous server node. Moreover, our modularity-based 'splitting' heuristic improves the solution runtime up to 395× without noticeably sacrificing solution quality compared to an exact MILP solution, and outperforms all other heuristics by 30-60% solution quality. Finally, our case study shows how we can extend our framework to schedule large language models across multiple heterogeneous servers by exploiting symmetry in the hardware setup. Our code can be easily plugged in to existing frameworks, and is available at https://github.com/abdelfattah-lab/diviml.  © 2023 IEEE.

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
