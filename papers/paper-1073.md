---
id: "paper-1073"
title: "Repairing Infrastructure-as-Code using Large Language Models"
authors: ["Low, En", "Cheh, Carmen", "Chen, Binbin"]
year: 2024
venue: "Proceedings - 2024 IEEE Secure Development Conference, SecDev 2024"
venue_type: "conference"
doi: "10.1109/SecDev61143.2024.00008"
url: "https://www.scopus.com/pages/publications/85210555721?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "20--27"
keywords: ["automatic program repair", "infrastructure as code", "large language model"]
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

# paper-1073 — Repairing Infrastructure-as-Code using Large Language Models

## Metadata

- **Authors:** Low, En and Cheh, Carmen and Chen, Binbin
- **Year:** 2024
- **Venue:** Proceedings - 2024 IEEE Secure Development Conference, SecDev 2024
- **DOI:** 10.1109/SecDev61143.2024.00008
- **URL:** https://www.scopus.com/pages/publications/85210555721?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 20--27
- **Language:** English
- **Keywords:** automatic program repair; infrastructure as code; large language model

### Abstract

Infrastructure-as-Code (IaC) is the practice of provisioning and managing cloud resources using machine-readable code. IaC is seeing increased adoption because it enhances transparency and reliability of infrastructure operations. However, as any software code, IaC can also contain misconfigurations, which can lead to insecure infrastructure, which may result in data breaches. Existing IaC scanning tools are able to detect common misconfigurations in IaC but they require IaC developers to manually repair the code. Recent advances in Large Language Models (LLMs) have led to promising results in applying LLMs to Automatic Program Repair (APR) tasks for code written in different languages. In this work, we propose an LLM-based approach to fix misconfigurations in IaC code. After misconfigurations in IaC code are identified by scanning tools, we feed the LLMs with the IaC code, details about the misconfigurations, and additional context provided by a human-in-the-loop and prompt the LLM to generate the repaired IaC code. We tested our approach on several vulnerable IaC repositories and found that the GPT-4 model from OpenAI suggests fixes that reduce up to 84.7% of the misconfiguration alarms produced by the scanners and our two-pass solution significantly improves the performance over a one-pass only approach. However, of the fixes suggested, we manually determined that only 79.6% actually solve the problem, while the remaining 20.4% are hallucinated fixes. Specifically, LLM hallucinations in the generated outputs pass checks for misconfigurations but fail other syntax and schema validation checks or do not address the underlying security issue. We propose a few potential approaches to tackle this challenge.  © 2024 IEEE.

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
