---
id: "paper-1570"
title: "Toward Deterministic Path Placement in AI Backends: A Practical SRv6-Based Architecture"
authors: ["Filsfils, Clarence", "Camarillo, Pablo", "Abdelsalam, Ahmed", "Quinci, Arianna", "Tulumello, Angelo", "Mayer, Andrea", "Loreti, Pierpaolo", "Bracciale, Lorenzo", "Salsano, Stefano"]
year: 2025
venue: "Proceedings of the 2025 21st International Conference on Network and Service Management: AI and Sustainability in the Future of Network and Service Management, CNSM 2025"
venue_type: "conference"
doi: "10.23919/CNSM67658.2025.11297568"
url: "https://www.scopus.com/pages/publications/105032117663?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["AI workloads", "congestion control", "datacenter fabrics", "programmable networks", "RoCEv2", "SRv6", "traffic engineering"]
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

# paper-1570 — Toward Deterministic Path Placement in AI Backends: A Practical SRv6-Based Architecture

## Metadata

- **Authors:** Filsfils, Clarence and Camarillo, Pablo and Abdelsalam, Ahmed and Quinci, Arianna and Tulumello, Angelo and Mayer, Andrea and Loreti, Pierpaolo and Bracciale, Lorenzo and Salsano, Stefano
- **Year:** 2025
- **Venue:** Proceedings of the 2025 21st International Conference on Network and Service Management: AI and Sustainability in the Future of Network and Service Management, CNSM 2025
- **DOI:** 10.23919/CNSM67658.2025.11297568
- **URL:** https://www.scopus.com/pages/publications/105032117663?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** AI workloads; congestion control; datacenter fabrics; programmable networks; RoCEv2; SRv6; traffic engineering

### Abstract

Distributed training of artificial intelligence models, such as Large Language Models (LLMs), generates highly structured and intense traffic patterns between GPUs, with synchronous and repetitive flows that can easily cause congestion and bottlenecks in data center networks. In this context, currently adopted protocols, such as RoCEv2, show significant limitations in the presence of bursty traffic and low entropy, compromising overall system efficiency. Segment Routing over IPv6 (SRv6) offers a programmable mechanism to steer AI workload traffic along explicitly chosen paths, enabling precise and congestion-aware routing under dynamic conditions. Lightweight monitoring modules can detect congestion conditions in real time and report them to the orchestrator or NICs, enabling dynamic rerouting decisions without requiring control-plane signaling or state in the fabric. SRv6 micro-segment (uSID) encoding allows the NIC to steer traffic along alternate, congestion-free paths simply by updating the IPv6 destination address, preserving RoCEv2 semantics while ensuring rapid adaptability. This work provides a practical implementation and experimental validation of the recent IETF Internet-Draft 'SRv6 for Deterministic Path Placement in AI Backends', demonstrating its feasibility and performance benefits in RoCEv2-based infrastructures. The results highlight the potential of SRv6 as a practical and vendor-agnostic solution to enhance networking efficiency in modern AI datacenters.  © 2025 IFIP.

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
