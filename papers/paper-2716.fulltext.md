---
title: "A Trustworthy Hybrid ML-GenAI Architecture for Autonomous, Behavior-Aware Resource Allocation in Internet2 Traffic"
authors:
  - name: Shideh Yavary Mehr
    affiliation: "School of Cybersecurity, Old Dominion University"
    email: "syavarym@odu.edu"
  - name: Abhishek Phadke
    affiliation: "School of Engineering and Computing, Christopher Newport University"
    email: "abhishek.phadke@cnu.edu"
date: null
doi: null
venue: null
category: "Network Resource Management, Machine Learning, Generative AI"
keywords:
  - "Hybrid ML-GenAI"
  - "Resource Allocation"
  - "Internet2"
  - "Trustworthy AI"
  - "Autonomous Networks"
  - "Anomaly Detection"
  - "Network Traffic Prediction"
abstract: "Internet2 (I2), a high-performance research and education network, faces increasing pressure to allocate bandwidth and compute resources adaptively as traffic volumes and application behaviors evolve. Traditional static resource allocation strategies cannot meet the real-time demands of large-scale scientific workflows, distributed edge computing, and data-intensive academic environments. This paper introduces a trustworthy hybrid ML-GenAI architecture that autonomously predicts, explains, and optimizes I2 traffic resource allocation with high precision. The method integrates K-Nearest Neighbors (KNN) for fine-grained local pattern detection and Random Forest (RF) for robust global trend prediction with a Generative AI (Gen-AI) reasoning module that performs semantic flow characterization, anomaly explanation, and uncertainty justification. Trustworthiness is ensured through: (1) Model cross-validation and ensemble agreement between KNN and RF; (2) Gen-AI-based explanation synthesis for transparent decisions; and (3) Uncertainty-aware resource allocation with safe-fallback policies. Experimental results on a multi-terabyte Internet2 flow dataset (2021-2025) demonstrate 32% reduction in misallocation, 21% improvement in anomaly detection, and 89.7% prediction accuracy."
---

## A Trustworthy Hybrid ML-GenAI Architecture for Autonomous, Behavior-Aware Resource Allocation in Internet2 Traffic

Shideh Yavary Mehr School of Cybersecurity Old Dominion University Norfolk, Virginia, 23529 syavarym@odu.edu

Abstract -Internet2 (I2), a high-performance research and education network, faces increasing pressure to allocate bandwidth and compute resources adaptively as traffic volumes and application behaviors evolve. Traditional static resource allocation strategies cannot meet the real-time demands of largescale scientific workflows, distributed edge computing, and dataintensive academic environments. To address this challenge, this paper introduces a trustworthy hybrid ML-GenAI architecture that autonomously predicts, explains, and optimizes I2 traffic resource allocation with high precision. Our method integrates the two complementary machine learning models: K-Nearest Neighbors (KNN) for fine-grained local pattern detection and Random Forest (RF) for robust global trend prediction-\*\*to capture both micro-level traffic fluctuations and macro-level using a Generative AI (Gen-AI) reasoning module that performs semantic flow characterization, anomaly explanation, and uncertainty justification. The Gen-AI component provides naturallanguage rationales for model decisions, enabling transparent decision-making and enhanced operator trust. Trustworthiness is ensured through three mechanisms: (1) Model cross-validation and ensemble agreement between KNN and RF to reduce bias and improve reliability; (2) Gen-AI-based explanation synthesis that generates interpretable justifications for allocation decisions; and (3) Uncertainty-aware resource allocation, where Gen-AI flags high-risk predictions and triggers safe-fallback allocation policies. Experimental results on a multi-terabyte Internet 2 flow dataset (2021-2025) show that the proposed hybrid system reduces misallocation by 32%, improves anomaly detection by 21%, and enables auditable, behavior-aware decisions that outperform traditional ML-only baselines. This work represents one of the first trustworthy hybrid ML-GenAI approaches for next-generation autonomous network resource management.

## I. INTRODUCTION

The rapid growth of high-performance research and education networks, exemplified by Internet2 (I2), has created unprecedented demands on network infrastructure. Traditional static resource allocation methods, which pre-assign bandwidth and compute resources based on anticipated peak loads, fail to adapt to the dynamic, data-intensive traffic patterns characteristic of modern academic and scientific workflows. Such static approaches lead to resource underutilization, potential bottlenecks, and reduced overall network performance [1], [2].

Abhishek Phadke School of Engineering and Computing Christopher Newport University Newport News, Virginia, 23606 abhishek.phadke@cnu.edu

To overcome these limitations, dynamic resource allocation strategies leveraging machine learning (ML) have emerged as promising solutions. ML models can analyze historical and real-time traffic to predict future resource requirements, enabling more efficient, adaptive, and proactive network management. While conventional ML approaches, such as KNearest Neighbors (KNN) or Random Forest (RF), are effective for specific prediction tasks, they often lack interpretability, semantic reasoning, and confidence-awareness, which are essential for trustworthy network operations in large-scale, mission-critical environments like I2 [3], [4].

In this work, we propose a trustworthy hybrid ML-Generative AI (GenAI) architecture for autonomous, behavior-aware resource allocation in I2. Our system combines the complementary strengths of two ML models, KNN for fine-grained local traffic pattern detection and RF for robust global trend prediction-with a GenAI reasoning module that provides semantic flow analysis, interpretable explanations, and uncertainty-aware recommendations. By integrating GenAI, our framework ensures that network operators can audit, understand, and trust allocation decisions, effectively bridging the gap between predictive performance and operational transparency [5]-[7].

Key contributions of this paper include:

- Hybrid ML-GenAI framework: Combines KNN, RF, and GenAI to predict, explain, and optimize resource allocation in real time.
- Behavior-aware prediction: Analyzes user and application-level traffic patterns to allocate resources dynamically, minimizing congestion and maximizing utilization.
- Trustworthy AI mechanisms: Ensemble agreement, GenAI-driven explanations, and uncertainty-aware fallback policies ensure reliability, interpretability, and safety.
- Empirical validation: Experiments on a multi-terabyte I2 flow dataset (2021-2025) demonstrate significant improvements over traditional ML-only methods, including a 32% reduction in misallocation and 21% improvement

in anomaly detection.

By integrating predictive ML models with GenAI reasoning, this approach not only enhances the efficiency, responsiveness, and robustness of I2 traffic management but also establishes a transparent and auditable framework for autonomous network resource allocation. This represents one of the first attempts to leverage a trustworthy hybrid ML-GenAI paradigm in nextgeneration high-performance networking environments.

## II. RELATED WORK

Research on autonomous network resource management has progressed significantly in recent years, driven by the growth of data-intensive scientific workflows, real-time interactive applications, and large-scale distributed computing systems. This section reviews three relevant areas: (1) machine learning for traffic prediction, (2) AI-enhanced network management, and (3) trustworthiness and explainability in networked systems [8], [9].

## A. Machine Learning for Network Traffic Prediction

Classical ML methods such as KNN, SVMs, ARIMA, and Random Forest have been applied extensively to predict traffic load, classify flows, and detect anomalies in backbone and datacenter networks. KNN has shown effectiveness for capturing short-term micro-level fluctuations due to its instancebased nature, while Random Forest models provide robustness to noise and capture non-linear feature interactions associated with broader temporal trends. However, prior work typically focuses on a single model or a small ensemble, lacking mechanisms to reconcile local vs. global behavioral patterns, and providing limited interpretability for operators [10], [11].

## B. AI-Assisted and GenAI-Driven Network Management

Recent efforts in network automation have begun to explore integrating deep learning with semantic reasoning and large language models (LLMs). These works demonstrate the potential of generative models for internt prediction, policy synthesis, anomaly interpretation, and natural-language advisory systems. However, most existing architectures treat GenAI as an external assistive component rather than a firstclass decision element. Moreover, current LLM-based systems rarely incorporate real-time traffic telemetry or quantitative ML signals, limiting their reliability when used in autonomous environments such as Internet 2 [1], [11].

## C. Trustworthiness, Explainability, and Safe Autonomy

As networks evolve toward self-driving architectures, trustworthiness has become a central requirement. Trustworthy networking research has emphasized explainable ML, uncertainty quantification, and safe fallback mechanisms for autonomous control loops. Despite these advances, few solutions integrate numerical prediction with semantic explanation in a unified framework. Even fewer support ensemble agreement validation or per-decision uncertainty justification. Capabilities essential for operator trust in national-scale backbone networks [11], [12].

## D. Summary and Gap Analysis

Across these domains, two gaps emerge:

- The lack of hybrid frameworks that merge micro-level ML prediction with macro-level semantic reasoning, enabling behavior-aware decision-making.
- The absence of trustworthy mechanisms, including explanation synthesis, cross-model agreement, and uncertaintyaware fallback strategies, required for safe deployment in large research networks like Internet 2.

The proposed hybrid ML-GenAI architecture directly addresses these gaps by combining fine-grained KNN and robust RF predictions with GenAI-based semantic reasoning, enabling transparent, auditable, and adaptive resource allocation.

The authors in [2] propose an approach for enhancing network efficiency and managing distributed digital content through the I2 Distributed Storage Infrastructure (I2-DSI). This system leverages a network of replicated servers to optimize content delivery across academic and research networks. By employing a strategic placement of content within various geographic locations, I2-DSI aims to reduce latency and bandwidth usage while ensuring that data remains readily accessible to users across different regions. The methodology centers on the intelligent redirection of service requests to the closest or most suitable server replica, based on network dynamics and user demand, thus improving overall service quality and access speed.

The authors in [3] explore the application of data mining techniques to the Internet of Things (IoT), a network where everyday objects are connected to the Internet, allowing them to send and receive data. The IoT is set to transform our daily lives by making many previously impossible tasks possible, such as refrigerators that automatically order groceries, and lamps that adjust their brightness. With the vast amounts of data generated by these connected devices, data mining becomes crucial for extracting valuable insights to enhance system operations and service delivery. The paper discusses the unique challenges associated with IoT data, including its volume, variety, and velocity, as well as how data mining can address these by applying techniques like classification, clustering, and pattern recognition. These methods help in predicting device behavior, managing resources efficiently, and enhancing security through anomaly detection. The paper also highlights future trends and potential issues, emphasizing the need for improved device intelligence, and autonomous decision-making capabilities, and addressing significant privacy and security concerns. As IoT devices become more integrated into our lives, leveraging data mining effectively is key to unlocking their full potential, ensuring they contribute to a smarter, more efficient environment [12], [1].

## III. IMPLEMENTATION

This section describes the practical realization of the proposed Hybrid ML-GenAI architecture for dynamic, trustworthy resource allocation in Internet2 (I2). The implementation emphasizes the integration of multiple machine learning models with generative AI reasoning, and mechanisms to ensure trustworthy, behavior-aware network management [12].

## A. Methodology

The implementation follows a data-driven, predictive, and adaptive approach:

## Data Collection

- Multi-terabyte Internet2 flow dataset (2021-2025) that includes features such as source/destination IP addresses, ports, protocol numbers, packet counts, and timestamps.
- Traffic categorized by application type, user group, and priority level to support behavior-aware resource allocation.

## Preprocessing

- Handling missing values through mean/mode imputation.
- Standardization of numerical features for distance-based algorithms (e.g., KNN).
- Feature selection to include variables most predictive of network load (e.g., srcport, proto, inpackets, user/application type).

## Model Training

- KNN: Captures local, fine-grained traffic patterns for short-term, micro-level predictions.
- Random Forest (RF): Captures global trends and longterm traffic patterns to complement KNN predictions.
- Training split: 70% training, 30% testing, with crossvalidation for robustness.

## Evaluation Metrics

- Confusion matrix, accuracy, precision, recall, and error rate vs. K value for KNN.
- Ensemble agreement metrics to evaluate consistency between KNN and RF.

## B. Hybrid ML + GenAI Workflow

The hybrid workflow integrates predictive ML with Generative AI reasoning to enhance trustworthiness, interpretability, and adaptive resource allocation:

## 1) Prediction Phase:

- KNN generates fine-grained predictions for short-term, local traffic fluctuations.
- RF predicts global, long-term traffic trends.
- Ensemble agreement checks ensure consistency between KNN and RF outputs, flagging discrepancies for review.

## 2) GenAI Reasoning:

- Takes ML predictions as input along with network context (application type, user group, priority).
- Performs semantic flow characterization, explaining unusual traffic patterns or anomalies in natural language.
- Generates confidence scores and uncertainty justifications for flagged or high-risk predictions.

## 3) Decision & Allocation:

- Combines ML predictions with GenAI explanations to determine optimal bandwidth and compute allocations.
- Incorporates uncertainty-aware fallback policies when predictions are uncertain or conflicting.
- Allocations are behavior-aware, dynamically adapting to both micro-level fluctuations and macro-level trends.
- 4. Auditability & Feedback:
- All allocation decisions, ML predictions, GenAI explanations, and uncertainty flags are recorded.
- Network operators can review and validate the rationale behind each decision, ensuring transparency and trust.

## C. Implementation Considerations

Scalability: Parallel processing and streaming analytics allow real-time handling of multi-terabyte datasets.

Extensibility: The architecture can incorporate additional ML models or updated LLMs for improved prediction and reasoning.

Safety Mechanisms: Fallback policies prevent resource starvation or over-allocation during model uncertainty.

## D. Data mining

The data mining module provides the foundation for feature extraction, pattern discovery, and traffic behavior classification in Internet2. It operates before predictive modeling, converting raw multi-terabyte flow data into structured representations that the ML and GenAI modules can interpret.

- 1. Flow-Level Feature Engineering: The system performs:
- Aggregation: flow merging per 1-second or 5-second windows.
- Behavior tagging: scientific workflows, cloud services, HPC jobs, user groups.
- Derived metrics: burstiness index, flow entropy, interarrival variance, port/protocol .

These engineered features significantly improved the predictive performance of both KNN and RF models.

2. Traffic Pattern Discovery: Unsupervised mining is used to identify meaningful traffic classes.

- k-Means clustering detects typical usage modes
- DBSCAN identifies dense scientific transfer periods
- Sequential pattern mining extracts recurring workflow behaviors

The patterns discovered here are fed into the GenAI module to assist in semantic explanation and interpretation of anomalies.

- 3. Anomaly Candidate Extraction: The module flags suspicious or high-variance flows using
- Z-score thresholding
- Entropy deviation
- Port/protocol irregularity
- Edge-case clustering residuals

These flagged flows are passed to both ML models and GenAI for deeper analysis.

Figure 1: Resource Allocation Engine (RAE)

<!-- image -->

## E. Resource Allocation

The Resource Allocation Engine (RAE) translates predictions and GenAI reasoning into dynamic bandwidth and compute allocations in Internet2. The algorithm for resource allocation is showing in figure1.

1. Allocation Inputs : The RAE uses three data streams:

- KNN short-term micro predictions
- RF long-term macro predictions
- GenAI uncertainty and natural-language rationale
- 2. Allocation Policies : Three core allocation policies are implemented:

## Predictive Allocation:

Uses ensemble ML predictions to allocate bandwidth proportionally to expected demand.

## Behavior-Aware Allocation:

Traffic identified as HPC, urgent scientific workload, or timesensitive services receives priority.

Uncertainty-Aware Safe Mode: Triggered when:

- KNN and RF disagree strongly,
- GenAI flags high semantic uncertainty, or
- anomaly likelihood rises.

In this mode, a conservative fallback rule ensures no resource starvation or over-allocation.

3. Real-Time Adaptation Loop : The engine updates allocations every 1-10 seconds depending on traffic volatility. Operators receive ML predictions, GenAI explanations, and an uncertainty score for each allocation decision.

## IV. SIMULATION RESULTS

This section evaluates the performance of the proposed Hybrid ML-GenAI architecture using a full-scale simulation of Internet2 traffic conditions. To present the results clearly, Figures 2, 3, 4, and Tables I,II,III summarize prediction accuracy, anomaly detection improvements, and the trustworthiness of generated explanations.

## A. Experimental Setup

Simulations are executed using:

- 4 years (2021-2025) of Internet2 traffic
- Flow dataset exceeding multiple terabytes
- Mixed applications: scientific workflows, cloud transfers, IoT telemetry, HPC flows
- Baseline comparisons:
  - Static peak-based allocation
  - Standalone KNN
  - Standalone RF

## B. Traffic Prediction Accuracy

The hybrid KNN+RF ensemble outperformed all standalone models. Figure 2 (bar chart) shows a clear accuracy improvement from 78-82% (single models) to almost 90% for the hybrid.

Figure 2: Prediction accuracy comparison between KNN, RF, and Hybrid model.

<!-- image -->

Table I: Traffic Prediction Accuracy Across Models

| Model                  | Accuracy | Error Rate | Misallocation Reduction |
| ---------------------- | -------- | ---------- | ----------------------- |
| KNN (baseline)         | 78.4%    | 21.6%      | 8%                      |
| Random Forest (RF)     | 82.9%    | 17.1%      | 14%                     |
| Hybrid KNN + RF (Ours) | 89.7%    | 10.3%      | 32%                     |

## C. Anomaly Detection Improvements

Figure 3 visualizes precision, recall, and F1 metrics for three anomaly detection methods. The Hybrid ML-GenAI system significantly outperforms static thresholding and standalone ML.

Figure 3: Anomaly detection performance improvements across models.

<!-- image -->

Table II: Anomaly Detection Performance

| Model                    | Precision | Recall | F1 Score |
| ------------------------ | --------- | ------ | -------- |
| Static Thresholding      | 63.2%     | 58.9%  | 61.0%    |
| Random Forest Only       | 72.5%     | 70.8%  | 71.6%    |
| Hybrid ML + GenAI (Ours) | 84.1%     | 79.3%  | 81.6%    |

## D. Misallocation Reduction

Figure 4 shows how the hybrid model reduces resource misallocation by 32%, the largest improvement across all baselines. This enables more efficient real-time resource distribution

## E. Trustworthiness and Interpretability

Operators rated GenAI explanations highly in clarity and correctness. Table III shows the trustworthiness and explanation Quality. Nearly 87% agreement between human operators and GenAI justifications demonstrates strong interpretability.

The summary of Simulation Results are as follow:

- 32% reduction in misallocation
- 21% improvement in anomaly detection
- 89.% prediction accuracy, highest among all models
- 87% explanation alignment, supporting trustworthy autonomous control

Figure 4: Misallocation reduction for different methods.

<!-- image -->

Table III: Trustworthiness and Explanation Quality

| Metric                              | Baseline | Our Method |
| ----------------------------------- | -------- | ---------- |
| Explanation Alignment               | 41%      | 87%        |
| Uncertainty Calibration Error (UCE) | 0.19     | 0.08       |
| Risky Allocation Frequency          | 18%      | 10.6%      |
| Fallback Trigger Accuracy           | 61%      | 92%        |

Strong generalization across diverse application and traffic types

These results confirm that integrating ML predictions with GenAI reasoning substantially improves performance, interpretability, and safety in autonomous network resource allocation.

## V. CONCLUSION

This work introduced a trustworthy Hybrid ML-GenAI architecture for autonomous, behavior-aware resource allocation in Internet 2. By combining the fine-grained local sensitivity of KNN, the global trend robustness of Random Forest, and the semantic reasoning capability of Generative AI, the proposed system provides highly accurate, transparent, and safe allocation decisions. The integration of GenAI enables operators to understand the rationale behind predictions while uncertaintyaware fallback policies ensure trustworthy deployment in highstakes network environments.

Through extensive simulations on a multi-terabyte, fouryear Internet 2 dataset, the hybrid system demonstrated substantial improvements over traditional ML-only and static allocation methods. Notably, the framework reduced misallocation by 32%, improved anomaly detection by 21%, and achieved an 89.% traffic prediction accuracy. Additionally, the system's transparent explanations, with an 87% operator alignment score, confirmed that hybrid ML-GenAI methods can bridge the gap between automation performance and human trust.

Overall, this work represents one of the first complete implementations of a trustworthy hybrid ML-GenAI paradigm for next-generation backbone networks, offering a strong foundation for self-driving, auditable Internet 2 operations.

## VI. FUTURE WORK

Although the proposed architecture shows strong performance and trustworthiness, several avenues for advancement remain.

- Real-Time Streaming Deployment work will focus on building fully streaming versions of the ML and GenAI modules to support sub-second decision loops suitable for ultra-high-speed transfers and interactive scientific workloads.
- Multi-Domain and Cross-Backbone Coordination Expanding the architecture to federated deployments across ESnet, G ´ EANT, and campus networks would support coordinated resource allocation for multi-domain workflows.
- Integration with SDN Controllers Future research will explore embedding the RAE directly into SDN controllers (e.g., OpenDaylight or ONOS) to enable closed-loop, programmable network automation.
- Safety-Critical Validation Framework Developing formal verification tools for ML+GenAI network controllers would ensure reliable behavior under edge-case traffic conditions and prevent unintended allocation actions.

## ACKNOWLEDGMENTS

The authors would like to express their sincere gratitude to Dr. Saltuk B. Karahan, Deputy director of the School of Cybersecurity at Old Dominion University, for his invaluable support and guidance throughout the development of this research. His expertise, constructive feedback, and continual encouragement greatly contributed to the quality and completion of this work.

## REFERENCES

- [1] S. Y. Mehr and B. Ramamurthy, 'An svm based ddos attack detection method for ryu sdn controller,' in Proceedings of the 15th international conference on emerging networking experiments and technologies , 2019, pp. 72-73.
- [2] A. K. Rastogi, S. Taterh, and B. S. Kumar, 'Internet of things enabled machine learning-based smart systems: A bird's eye view,' Engineering Proceedings , vol. 59, no. 1, p. 36, 2023.
- [3] T. M. Micah Beck, 'The i2 distributed storage infrastructure project: an architecture for internet content channels,' Engineering Proceedings , vol. 30, no. 23, p. 8, 1999.
- [4] O. Salman, I. H. Elhajj, A. Kayssi, and A. Chehab, 'A review on machine learning-based approaches for internet traffic classification,' Annals of Telecommunications , vol. 75, no. 11, pp. 673-710, 2020.
- [5] C.-W. Tsai, C.-F. Lai, M.-C. Chiang, and L. T. Yang, 'Data mining for internet of things: A survey,' IEEE Communications Surveys & Tutorials , vol. 16, no. 1, pp. 77-97, 2013.
- [6] T. T. Nguyen and G. Armitage, 'A survey of techniques for internet traffic classification using machine learning,' IEEE communications surveys & tutorials , vol. 10, no. 4, pp. 56-76, 2008.
- [7] A. Vlădutescu, D. Comaneci, and C. Dobre, 'Internet traffic classification based on flows' statistical properties with machine learning,' International Journal of Network Management , vol. 27, no. 3, p. e1929, 2017.
- [8] --, 'Internet traffic classification based on flows' statistical properties with machine learning,' International Journal of Network Management , vol. 27, no. 3, p. e1929, 2017.
- [9] G. Chatzigeorgakidis, S. Karagiorgou, S. Athanasiou, and S. Skiadopoulos, 'Fml-knn: scalable machine learning on big data using k-nearest neighbor joins,' Journal of Big Data , vol. 5, pp. 1-27, 2018.
- [10] I. Triguero, D. García-Gil, J. Maillo, J. Luengo, S. García, and F. Herrera, 'Transforming big data into smart data: An insight on the use of the k-nearest neighbors algorithm to obtain quality data,' Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery , vol. 9, no. 2, p. e1289, 2019.
- [11] S. Y. Mehr and B. Ramamurthy, 'Protection techniques for wavelength division multiplexing networks using resource delayed release strategy,' in 2021 International Conference on Computer Communications and Networks (ICCCN) . IEEE, 2021, pp. 1-6.
- [12] Mehr, Shideh Yavary and Ramamurthy, Byrav, 'Hierarchical classic controllers (HCC) with an enhanced svm method for ddos attack detection in sdn,' in 2022 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS) . IEEE, 2022, pp. 381-386.
