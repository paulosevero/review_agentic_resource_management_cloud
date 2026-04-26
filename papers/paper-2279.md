---
id: "paper-2279"
title: "Reductive Analysis with Compiler-Guided Large Language Models for Input-Centric Code Optimizations"
authors: ["Wang, Xiangwei", "Hui, Xinning", "Liao, Chunhua", "Shen, Xipeng"]
year: 2025
venue: "Proceedings of the ACM on Programming Languages"
venue_type: "journal"
doi: "10.1145/3729282"
url: "https://www.scopus.com/pages/publications/105008278705?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: ""
keywords: ["Input-Centric Optimization", "Large Language Models", "Predictive Modeling", "Program Optimization", "Seminal Behavior Identification"]
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

# paper-2279 — Reductive Analysis with Compiler-Guided Large Language Models for Input-Centric Code Optimizations

## Metadata

- **Authors:** Wang, Xiangwei and Hui, Xinning and Liao, Chunhua and Shen, Xipeng
- **Year:** 2025
- **Venue:** Proceedings of the ACM on Programming Languages
- **DOI:** 10.1145/3729282
- **URL:** https://www.scopus.com/pages/publications/105008278705?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 
- **Language:** English
- **Keywords:** Input-Centric Optimization; Large Language Models; Predictive Modeling; Program Optimization; Seminal Behavior Identification

### Abstract

Input-centric program optimization aims to optimize code by considering the relations between program inputs and program behaviors. Despite its promise, a long-standing barrier for its adoption is the difficulty of automatically identifying critical features of complex inputs. This paper introduces a novel technique, reductive analysis through compiler-guided Large Language Models (LLMs), to solve the problem through a synergy between compilers and LLMs. It uses a reductive approach to overcome the scalability and other limitations of LLMs in program code analysis. The solution, for the first time, automates the identification of critical input features without heavy instrumentation or profiling, cutting the time needed for input identification by 44× (or 450× for local LLMs), reduced from 9.6 hours to 13 minutes (with remote LLMs) or 77 seconds (with local LLMs) on average, making input characterization possible to be integrated into the workflow of program compilations. Optimizations on those identified input features show similar or even better results than those identified by previous profiling-based methods, leading to optimizations that yield 92.6% accuracy in selecting the appropriate adaptive OpenMP parallelization decisions, and 20-30% performance improvement of serverless computing while reducing resource usage by 50-60%. © 2025 Owner/Author.

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
