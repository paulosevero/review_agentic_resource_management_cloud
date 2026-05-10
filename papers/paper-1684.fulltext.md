---
title: "[paper-1684] GenAI Game Theory Analysis of Computational Offloading and Resource Management in Vehicular Networks"
authors:
  - name: "Selangor, Malaysia"
  - name: "Fig. 1. The VEC system follows a layered architecture."
keywords: []
abstract: ""
date_published: null
venue: "Unknown"
doi: null
arxiv_id: null
---

## GenAI Game Theory Analysis of Computational Offloading and Resource Management In Vehicular Networks

Nusrat Jahan Faculty of Information Science and Technology Universiti Kebangsaan Malaysia (UKM) Selangor, Malaysia

P128645@siswa.ukm.edu.my Mohammad Kamrul Hasan Faculty of Information Science and Technology Universiti Kebangsaan Malaysia

(UKM)

Selangor, Malaysia

mkhasan@ukm.edu.my

Abstract -This research introduces a framework that integrates Generative Artificial Intelligence (GAI) and gametheoretic models for enhancing computational offloading and resource allocation in vehicular edge computing (VEC) scenarios. The proposed three-layer architecture-Input, Augmented Intelligence, and Decision layers-enables intelligent and timely decision-making for dynamic task distribution with minimal latency and optimal energy efficiency. The framework leverages a Transformer-based GAI model with Retrieval-Augmented Generation (RAG) to adaptively learn from distributed vehicular environments, supported by federated learning to ensure privacy-preserving training across edge and cloud servers. Simulation outcomes demonstrate that the GAI-based solution achieves 25-35% lower task latency, 20-30% reduced energy consumption, and 30-40% faster convergence to the Nash equilibrium compared with traditional game-theoretic methods. These findings highlight the potential of combining GAI and game-theoretic mechanisms to provide scalable, energy-efficient, and latency-aware offloading strategies for future vehicular networks.

Keywords-Generative Artificial intelligence (GenAI), Game theory, Computation Offloading, Artificial intelligence technology, Nash Equilibrium, Energy consumption, Vehicular Networks.

## I. INTRODUCTION

The rapid advancements in edge intelligence and AIdriven offloading highlight the growing need for dynamic resource allocation strategies that can scale efficiently. Future research should focus on developing AI-driven adaptive offloading policies that optimize performance based on realtime workload variations. By integrating advanced learning models, intelligent network prediction, and decentralized AI training, future GenAI architectures can achieve optimal performance while reducing computational overhead and improving energy efficiency.

Generative AI introduces significant computational challenges, requiring innovative offloading strategies and optimized resource allocation. Edge-cloud computing provides an effective solution by dynamically distributing computational workloads, ensuring scalability, reduced latency, and enhanced privacy. Integrating adaptive learning techniques, decentralized AI models, and hybrid offloading strategies will be pivotal in enabling real-time, large-scale Generative AI applications. By leveraging intelligent task scheduling and efficient data distribution, future GenAI architectures can deliver high-performance, resource-efficient Mohd Zakree Ahmad Nazri Faculty of Information Science and Technology Universiti Kebangsaan Malaysia (UKM) Selangor, Malaysia zakree@ukm.edu.my AI services in increasingly complex network environments. [1]

Early AI models lacked scalability, requiring centralized computing resources, whereas modern transformer-based architectures demand distributed processing approaches.[2] A scalable GenAI system must maintain consistent response times despite increasing workloads, necessitating adaptive computation offloading [3]. Edge-cloud computing provides an ideal hybrid approach by distributing AI inference and training workloads dynamically based on available resources. For example, high-intensity processing is better suited for cloud servers, while real-time inference tasks, such as AIpowered metaverse interactions, require edge-based computation to minimize latency.

Fig. 1. The VEC system follows a layered architecture.

<!-- image -->

The architecture of the VEC system is a three-layered structure composed of the Cloud Layer, Edge Layer, and Intelligent Vehicle Layer, as shown in Fig. 1 adapted from [3]. Through this architecture, the resources are well managed, data are processed quickly, and real-time communication is achieved for different vehicle applications. The Cloud Layer provides the infrastructure for large-scale data storage, intense analytics, and complex computation not possible in lower layers to enable operations like traffic prediction and historical analysis that can tolerate more latency. [4] The Edge Layer is in between the vehicles and the cloud, leveraging edge servers, roadside units, and mobile base stations to support low-latency processing and real-time services such as real-time navigation, infotainment, emergency response, and cooperative computing via V2V and V2I connectivity. At the lowest level, the Intelligent Vehicle Layer consists of intelligent vehicles equipped with sensors, AI [5], and onboard computing systems to enable local data processing, situational awareness, and autonomous decision-making. These three layers combined form a strong system that allows for more efficient use of resources, minimizes delays, and offers seamless, reliable connections needed for tomorrow's autonomous and connected vehicle networks.

## A. Motivation:

Increasing computational requirements of Generative AI services and real-time auto offerings embody strict challenges in latency-critical settings. Conventional centralized cloudbased approaches are unsuitable due to high transmission latency and scalability issues, hence necessitating the implementation of a hybrid edge-cloud paradigm enabled by intelligent offloading techniques and adaptive resource provisioning.

## B. Objective:

The main objectives of this research work as follows:

1. To develop a GAI-integrated game-theoretic model that enables efficient, adaptive task offloading in VEC networks.
2. To minimize latency, reduce energy consumption, and optimize convergence speed while achieving a stable Nash equilibrium in dynamic vehicular environments.

The research paper begins with an Introduction, outlining the motivation behind addressing the computational challenges posed by real-time Generative AI (GenAI) applications in vehicular networks and emphasizing the need for dynamic, intelligent offloading strategies. It then defines the objectives of integrating GenAI with game-theoretic modeling to enhance resource allocation, minimize latency, and optimize system performance. The Literature Review surveys existing work on edge intelligence, GenAI deployment, and task offloading methodologies, highlighting gaps in energy efficiency, scalability, and real-world applicability. In Section 3, titled GAI-Based Computation Offloading and Resource Management, the paper discusses a detailed system model featuring layered decision-making and elaborates on performance metrics such as task completion time, energy consumption, and Nash equilibrium, followed by a visualization of the algorithmic steps used to evaluate and optimize the offloading process. Section 4 presents the Results and Discussion, showcasing simulation-based comparisons between traditional and GAI-driven methods in terms of latency, energy efficiency, and convergence speed. Finally, Section 5 concludes the study with insights into potential improvements, such as integrating blockchain for secure offloading and enhancing adaptability through real-time caching and mobility-aware strategies.

## II. LITERATURE REVIEW

Computation offloading has emerged as a critical solution to address the resource limitations of vehicular devices in dynamic and latency-sensitive environments. This section explores a variety of GAI offloading strategies, highlighting their methodologies, benefits, and challenges. Gong et al., reviewed Edge Intelligence (EI) applications in ITS, integrating AI with edge computing to reduce latency and improve security. [6] The paper highlighted recent advancements but emphasized the need for continuous updates and practical validation. Wan et al., used SPEA2 for multi-objective optimization in RSU offloading strategies, integrating TOPSIS and MCDM for selection.[7] While effective in simulations, the study neglected energy efficiency and privacy preservation considerations. [8] It aims to reduce delay and energy consumption in UAV-assisted MEC

environments, showing improvements in scalability and flexibility through comprehensive simulation evaluations. Hasan et al., introduces a federated learning (FL) framework for 6G-V2X, integrating DFedAvg for computation offloading and multi-objective optimization. [9]

This research [10] presents a Vehicular Edge Computing (VEC)-based IoV framework for efficient task offloading in Industry 4.0 environments. It focuses on resource-aware task scheduling by integrating edge computing with vehicular communication networks (V2V, V2I, and V2X) to reduce latency and enhance computational capabilities. Future work should focus on AI-driven prediction models for dynamic task scheduling and real-time QoS adaptation in VEC networks.

This paper [3] explores the deployment of Generative AI (GenAI) services in edge-cloud computing environments to address the computational and latency challenges posed by traditional cloud-based architectures. This study [11] extends the discussion on GenAI model deployment in edge-cloud computing by addressing challenges related to high transmission latency, energy inefficiency, and centralized cloud reliance. It proposes a hierarchical computation framework to efficiently distribute GenAI tasks across cloud, edge, and end-user devices. This paper [12] explores the integration of Generative AI (GenAI) and Big Data to enhance financial risk management. It emphasizes leveraging AI models such as GPT-4, Variational Autoencoders (VAE), and Generative Adversarial Networks (GANs) to improve workflow efficiency and reduce error margins in financial and enterprise systems. This paper [3] examines the deployment of Generative AI using an edge-cloud computing framework to address latency and resource constraints. Additionally, it presents two case studies-Metaverse and Artificial Intelligence of Things (AIoT)-to illustrate real-world applications. This research [16] proposes a two-stage gametheoretic framework enhanced with Generative AI (GAI) to optimize computation offloading and resource management in mobile edge collaborative vehicular networks. The key contribution lies in combining Stackelberg game modeling with GAI-driven simulation and KKT-based optimization, enabling adaptive offloading decisions that significantly reduce latency, energy consumption, and computational overhead while improving scalability and robustness in dynamic vehicular environments. [13] Dang et al., integrated task offloading, resource allocation, and pricing strategies using potential games and a hierarchical multi-tier scheme. While simulations validated the approach, scalability and computational overhead pose significant challenges. The study successfully optimized offloading but highlighted the need for empirical validation to address dynamic vehicular environments.

## III. GAI- BASED COMPUTATION OFFLOADING AND RESOURCE MANAGEMENT

## A. GenAI-Based Offloading and Resource Management

Figure 2, inspired by [3][14], illustrates a GenAI-based collaborative system where cloud and edge servers use AI models to optimize task offloading and resource management by synchronizing data and processing requests from distributed end devices and applications. AIoT leverages AIdriven intelligence in IoT systems, allowing end devices such as mobile phones, laptops, and autonomous vehicles to process and analyze data intelligently. In this framework, privacy, personalization, and data synchronization are key considerations for offloading. End devices collect and process local data, enabling lightweight GenAI model inference while offloading complex computations to edge servers. These edge servers act as intermediate processing nodes, handling midsized GenAI models and synchronizing data and models with cloud servers through a federated or split learning approach. The cloud server hosts large-scale GenAI models, aggregating model parameters from multiple users to enhance global model performance while preserving data privacy.

To ensure real-time updates and continuous learning, online optimization techniques support on-the-fly GenAI model training with streaming data. The sync request mechanism enables seamless communication between edge servers, optimizing computational efficiency and minimizing latency. Through knowledge distillation and model pruning, different versions of GenAI models are deployed at various hierarchical levels-lightweight models on user devices, midsize models at the edge, and large-scale models in the cloudensuring efficient task distribution and reducing computational overhead. The collaborative AI optimization for offloading component further enhances system performance by grouping users based on computation facilities, dynamically allocating resources, and fine-tuning models according to user behavior and device capabilities. This architecture supports scalable and adaptive AIoT applications such as autonomous driving, smart cities, and personalized voice assistants, making GenAI-powered services more responsive, privacy-preserving, and computationally efficient.

Fig 2. GenAI-Based Offloading and Resource Management.

<!-- image -->

Effective task scheduling systems play a critical role in the optimization of resource utilization and in the deployment of Generative AI services with minimal disruption. The users' shared and sensitive personal data interaction occurs in a hierarchical setup that incorporates both edge computing and cloud computing. Edge computing supports low-latency AI training and inference functions that utilize Green AI models to promote energy efficiency. Compressed pre-trained models are key edge functions for inference tasks, and cloud computing is responsible for centralized data processing as well as large-scale AI models. The edge-cloud collaboration layer encompasses key functions, including online optimization, knowledge distillation, collaborative learning, and federated learning. These processes facilitate dynamic adaptation of Generative AI services to varying workloads and network conditions, achieving high-performance AI application delivery efficiency.

Generative AI (GenAI) significantly enhances the resource management of many areas of technology with intelligent decision-making in real time. In telecommunication network operations, GenAI dynamically manages traffic control, prioritization of data flow, and resource allocation of bandwidth and processing capacity according to demand at the time. Its adaptive capability maximizes performance and efficiency. GenAI also automates network configuration by applying best settings and predictive maintenance principles to proactively identify potential failures, reducing downtime and ensuring consistent service quality.

Aside from telecommunications, GenAI is also a motive power in cloud-edge collaboration systems and mobile networks. It supports task offloading and resource allocation using game theory models for processing performance optimization with saved energy. GenAI-based models, such as Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG), enable the formulation and resolution of complex optimization problems in cellular networks, such as secure user assignment in UAV systems [15]. Most generally, GenAI automates routine administrative functions-such as scheduling and record-keeping-freeing up technical personnel to focus on more complex problem-solving and system refinements.

## B. Offloading processes delay, energy cost, and delivery

Figure 3 adapted from [14] illustrates various task offloading strategies in a Vehicular Edge Computing (VEC) network and their impact on task completion delay, energy cost, and payment requirements. When a vehicle generates a computational task, it has multiple execution options: holding the task, offloading to a VEC server, offloading to another vehicle, or executing locally. Each option has different consequences in terms of performance and resource consumption.

If a vehicle holds the task, it delays execution, leading to increased waiting time and a higher task completion delay, though it incurs minimal energy cost since no processing is done. When the task is offloaded to a VEC server, it undergoes data upload, computation, and download, taking advantage of the server's computational power. The implication of this is that it reduces the computation time but at the expense of high energy consumption in the form of data transmission and payment for using the VEC facilities. Offloading the task to another vehicle follows an analogous process in which computation is performed by a cooperative vehicle. This method can reduce the expenses compared to VEC offloading and smooth out energy usage, but at the expense of payment to the host vehicle and with potential delays in transmission.

On the other hand, local execution occurs when a vehicle uses its onboard resources to execute the task. While this approach eliminates dependence on external networks, it results in higher energy consumption and can introduce significant processing latency, especially for tasks that require large computational resources. The overall task completion delay in the system depends on multiple factors, including waiting time, transmission delay (for offloading methods), and computation time. The green bar in the figure represents this cumulative delay.

Among the different strategies, the optimal choice depends on the specific requirements. VEC offloading is ideal for minimizing delay, but it comes with high transmission energy costs and payment requirements. Offloading to another vehicle can be a cost-effective alternative with moderate energy consumption and delay. Local execution is feasible for lightweight tasks but is inefficient for complex computations due to high processing energy requirements. Ultimately, the best strategy should balance latency, energy efficiency, and cost, depending on network conditions and vehicle capabilities.

Fig 3. Offloading processes: delay, energy cost, and delivery.

<!-- image -->

## C. System model

The proposed framework aims to incorporate Generative Artificial Intelligence (GAI) into game theory models for evaluating the performance of computational offloading and resource allocation strategies in vehicular networks. The proposed framework employs a Transformer-based Generative AI model integrated with Retrieval-Augmented Generation (RAG) to support context-aware offloading and adaptive decision-making in vehicular edge computing (VEC). Lightweight compressed models are deployed on vehicles for real-time inference, mid-sized RAG-enhanced models operate on edge servers for localized optimization, and large-scale foundation models are hosted in the cloud for global policy refinement. Within the game-theoretic decision layer, vehicles act as strategic agents, and their offloading strategies iteratively converge toward a Nash equilibrium, balancing latency, energy consumption, and resource utilization. This hierarchical deployment of GAI across vehicles, edge, and cloud ensures scalability, responsiveness, and energy efficiency in dynamic vehicular environments. This framework architecture is designed based on three basic layers: the Input Layer, the Augmented Intelligence Layer, and the Decision Layer.

1. Input Layer of Data Acquisition and Preprocessing: The Input Layer systematically collects real-time information from various sensors and communication modules installed in vehicles in the dynamic vehicular environment. The collected information entails key parameters like channel quality, vehicle speed, energy levels, and the current computational load. Due to the heterogeneity of data and high volume of data, the utilization of effective preprocessing techniques such as normalization and feature extraction is imperative. The resultant processed data creates a solid basis for making sound decisions in matters of resource allocation and computing activity outsourcing.
2. Augmented Intelligence Layer for Integration of GAI and Retrieval-Augmented Generation: Augmented Intelligence Layer to Integrate Retrieval-Augmented Generation and Generative AI: At the core of the framework lies the Augmented Intelligence Layer that integrates Generative Artificial Intelligence and gametheoretic methods to enhance decision-making in dynamic network environments. The layer performs two primary tasks: it analyzes real-time network scenarios and
3. optimization needs and converts these into gametheoretic, structured models. [16] It leverages a database of game theory models, vehicular network performance metrics, and past simulation results, which collectively enable adaptive and context-aware strategy derivation.
4. Decision Layer of Game-Theoretic Modeling and Resource Allocation: Following data processing and enrichment by the GAI component, the Decision Layer uses game theory in modeling and analyzing vehicle-edge server interactions. Each vehicle is designed as a strategic agent whose offloading decisions significantly impact the overall network performance. Advanced learning techniques, specifically Multi-Agent Deep Reinforcement Learning (MADRL), are employed to iteratively converge towards a Nash equilibrium. At this point of equilibrium, critical system objectives-namely, latency reduction, energy savings, and improved resource allocation-are effectively balanced. In addition, the decision-making process remains responsive to real-time feedback, thus ensuring adaptiveness to incessant variations in the network.

## D. Performance Metrics for Comparative Evaluation

Overall Task Completion Time: Since the local and remote computations are carried out in parallel, [14] the total task completion time for user is given by the maximum of the two components:

<!-- formula-not-decoded -->

Total Energy Consumption: The total energy consumption for user includes contributions from both local computation and data transmission [17] (the energy cost of remote execution at the edge server is not typically abide by the user):

<!-- formula-not-decoded -->

Nash Equilibrium in the Offloading Game: The game formulation is non-cooperative; each user aiming to minimize its cost function &amp; , . A strategy profile ∗ ) ∗ # ∗ , … , + ∗ forms a Nash equilibrium if, for every user ,

Where is a constant, and $ is the transmission power.

<!-- formula-not-decoded -->

At the Nash equilibrium, no user can unilaterally reduce its cost by adjusting its offloading fraction. The cost function &amp; is inherently dependent on the offloading fractions chosen by other users. [16] For example, as more users increase their offloading fractions, the resulting interference degrades the transmission rates and thus influences the cost incurred by each user.

## E. The Decision-Making Algorithm

1. Measuring the transmission delay between vehicles and edge servers to minimize latency.
2. Evaluate the energy consumption involved in data transmission and processing to reduce overall energy usage.
3. Computing a utility function that integrates delay, energy consumption, and operational efficiency to maximize Convergence Speed.

4. Apply a gradient-based iterative update rule to adjust player strategies and achieve a unique Nash equilibrium.

<!-- formula-not-decoded -->

## IV. RESULTS AND DISCUSSION

The simulation results illustrate a comparison between a traditional method and a GAI-driven game theory approach for offloading, focusing on task latency, energy consumption, and convergence speed as the number of vehicles increases. In terms of task latency, the traditional method shows a consistently higher average task latency that increases linearly with the number of vehicles, while the GAI-driven approach demonstrates a significantly lower average task latency. The vehicle mobility patterns follow a Random Waypoint model with speeds ranging between 20-80 km/h. Workload characteristics are modeled using Poisson task arrivals with varying task sizes from 0.5-5 MB. The network topology assumes three edge servers placed along a 5 km urban road segment with vehicle densities ranging from 50-200.

Fig 4(a). Simulation of Traditional vs. GAI-Driven Game Theory Offloading: Latency vs. Number of Vehicles.

<!-- image -->

Regarding energy consumption, the traditional method exhibits a similar trend of increasing energy consumption as the number of vehicles grows, while the GAI-driven method maintains a considerably lower energy consumption, indicating better energy efficiency. This suggests that GAIdriven offloading can reduce processing delays in the network. Figure 4(a) compares the average task latency between traditional game-theoretic and GAI-driven offloading methods as the number of vehicles increases. GAI significantly reduces latency due to its adaptive optimization capabilities. Figure 4(b) shows the average energy consumption for data transmission and processing. The GAIbased method demonstrates better energy efficiency than the traditional approach across all vehicle counts.

Fig 4(b). Simulation of Traditional vs. GAI-Driven Game Theory Offloading: Energy Consumption vs. Number of Vehicles.

<!-- image -->

Fig 4(c). Simulation of Traditional vs. GAI-Driven Game Theory Offloading: Convergence Speed vs. Number of Vehicles.

<!-- image -->

Finally, the convergence speed, measured by convergence iterations, reveals that the traditional method requires a consistently higher number of iterations to reach a solution compared to the GAI-driven approach, which converges much faster.

Fig 5. Comparative Simulation of Vehicular Mobility, Network Conditions, and Latency in Highway and Urban Scenarios.

<!-- image -->

These results collectively highlight the superiority of the GAI-driven game theory model in achieving lower latency, reduced energy consumption, and faster convergence in VEC networks. The Fig 4(c) illustrates the number of iterations required to reach equilibrium. GAI-driven optimization converges much faster, highlighting its computational advantage in dynamic vehicular edge computing scenarios.

The simulation results in Figure 5 illustrate the performance differences between highway and urban vehicular scenarios, highlighting how mobility patterns directly influence network stability and latency. In the highway case, vehicles maintain nearly constant speeds with an average of 86.24 km/h, requiring only 13 handovers, with an average latency of 18.88 ms, packet loss rate of 0.064, and 44 link failures. This reflects more stable bandwidth, lower packet loss, and consistently low latency. By contrast, the urban scenario is characterized by frequent stop-and-go movement with an average speed of only 8.95 km/h, leading to 77 handovers, a slightly higher latency of 19.66 ms, packet loss rate of 0.062, and 53 link failures. These results confirm that urban conditions introduce numerous handovers, volatile bandwidth, higher packet loss, and frequent latency spikes, which degrade real-time communication quality. The main contribution of this simulation is the comprehensive evaluation of how distinct mobility profiles impact vehicular edge computing performance, demonstrating that highway scenarios enable predictable and stable offloading, while urban environments require mobility-aware and adaptive mechanisms to ensure reliable, low-latency service delivery.

## V. CONCLUSION

The proposed GAI-based game theory framework significantly improves the performance of vehicular edge computing by intelligently managing task offloading and resource allocation. Experimental findings confirm that it outperforms traditional methods of latency and energy reduction with quicker convergence. Future research on the next generation will investigate blockchain-based integration for secure offloading and adaptive caching, along with realtime user mobility management for enhancing system robustness and scalability.

Future work will target the enhancement of caching mechanisms at the Base Station (BS) levels to greatly advance performance metrics. Besides, the incorporation of blockchain technology is anticipated to increase the security of vehicular computation offloading procedures. Such incorporation aims to enhance cooperative interactions among stakeholders of the network and boost the effectiveness of services in dynamic vehicular environments. Future research can be engaged in the exploration of more realistic situations, including the adaptive evolution of network status and user requirements. In particular, researchers aim to break the constraint of the established Stackelberg game framework by embedding adaptive mechanisms capable of adapting to real-time network parameter changes. This effort encompasses investigating the influences of varying transmission rates and user mobility patterns on the computation offloading procedure.

## ACKNOWLEDGMENT

This research was conducted by the authors, with special appreciation extended to the main and co-supervisors for their invaluable guidance and support.

## REFERENCES

- [1] A. K. Budati, S. Islam, M. K. Hasan, N. Safie, N. Bahar, and T. M. Ghazal, 'Optimized Visual Internet of Things for Video Streaming Enhancement in 5G Sensor Network Devices,' Sensors , vol. 23, no. 11, 2023, doi: 10.3390/s23115072.
- [2] S. Islam, Z. A. Atallah, A. K. Budati, M. K. Hasan, R. Kolandaisamy, and
- S. Nurhizam, 'Mobile Networks Toward 5G/6G: Network Architecture, Opportunities and Challenges in Smart City,' IEEE Open J. Commun. Soc. , vol. PP, p. 1, 2024, doi: 10.1109/OJCOMS.2024.3419791.
- [3] Y. C. Wang, J. Xue, C. Wei, and C. C. J. Kuo, 'An Overview on Generative AI at Scale With Edge-Cloud Computing,' IEEE Open J. Commun. Soc. , vol. 4, no. October, pp. 2952-2971, 2023, doi: 10.1109/OJCOMS.2023.3320646.
- [4] T. R. Prathiba, S. B., Krishnamoorthy, S. R., Kannan, K. S., Selvaraj, A. K., Ranganayakulu, D., Fang, K., &amp; Gadekallu, 'Digital Twin-Enabled RealTime Optimization System for Traffic and Power Grid Management in 6GDriven Smart Cities,' IEEE Internet Things J. , 2025.
- [5] T. R. Verma, S., Kaur, S., Jhaveri, R. H., Zhu, Z., &amp; Gadekallu, 'TrustAware Social-System-Inspired Clustering for Large-Scale Knowledge Discovery in Wireless Sensor Networks,' IEEE Trans. Comput. Soc. Syst. , 2025.
- [6] T. Gong, L. Zhu, F. R. Yu, and T. Tang, 'Edge Intelligence in Intelligent Transportation Systems: A Survey,' IEEE Trans. Intell. Transp. Syst. , vol. 24, no. 9, pp. 8919-8944, 2023, doi: 10.1109/TITS.2023.3275741.
- [7] S. Wan, X. Li, Y. Xue, W. Lin, and X. Xu, 'Efficient computation offloading for Internet of Vehicles in edge computing-assisted 5G networks,' J. Supercomput. , vol. 76, no. 4, pp. 2518-2547, 2020, doi: 10.1007/s11227019-03011-4.
- [8] N. Agarwal and S. Joshi, 'Federated Learning-Based Task Offloading in a UAV-Aided Cloud Computing Mobile Network,' IEEE Trans. Veh. Technol. , vol. PP, pp. 1-6, 2024, doi: 10.1109/TVT.2024.3404223.
- [9] M. K. Hasan et al. , 'Federated Learning for Computational Offloading and Resource Management of Vehicular Edge Computing in 6G-V2X Network,' IEEE Trans. Consum. Electron. , vol. 70, no. 1, pp. 3827-3847, 2024, doi: 10.1109/TCE.2024.3357530.
- [10] M. Talebkhah, A. Sali, V. Khodamoradi, T. Khodadadi, and M. Gordan, 'Task offloading for edge-IoV networks in the industry 4.0 era and beyond: A high-level view,' Eng. Sci. Technol. an Int. J. , vol. 54, no. October 2023, p. 101699, 2024, doi: 10.1016/j.jestch.2024.101699.
- [11] Y. C. Wang, J. Xue, C. Wei, and C. C. J. Kuo, 'An Overview on Generative AI at Scale With Edge-Cloud Computing,' IEEE Open J. Commun. Soc. , vol. 4, pp. 2952-2971, 2023, doi: 10.1109/OJCOMS.2023.3320646.
- [12] S. Joshi, 'The Synergy of Generative AI and Big Data for Financial Risk : Review of Recent Developments,' vol. 7, no. 1, 2025.
- [13] Z. Sun, G. Sun, Y. Liu, J. Wang, and D. Cao, 'BARGAIN-MATCH: A Game Theoretical Approach for Resource Allocation and Task Offloading in Vehicular Edge Computing Networks,' IEEE Trans. Mob. Comput. , vol. 23, no. 2, pp. 1655-1673, 2024, doi: 10.1109/TMC.2023.3239339.
- [14] S. Chu, Z. Fang, S. Song, Z. Zhang, C. Gao, and C. Xu, 'Efficient MultiChannel Computation Offloading for Mobile Edge Computing: A GameTheoretic Approach,' IEEE Trans. Cloud Comput. , vol. 10, no. 3, pp. 17381750, 2022, doi: 10.1109/TCC.2020.2994145.
- [15] L. He et al. , 'Generative AI for Game Theory-based Mobile Networking,' pp. 1-10, 2024, doi: 10.1109/MWC.007.2400133.
- [16] N. Jahan et al. , 'Game-Theoretic-GAI Approach for Computation Offloading and Resource Management for Mobile Edge Collaborative Vehicular Networks,' IEEE Trans. Intell. Transp. Syst. , vol. PP, pp. 1-12, 2025, doi: 10.1109/TITS.2025.3577673.
- [17] J. Wang, D. Feng, S. Zhang, J. Tang, and T. Q. S. Quek, 'Computation Offloading for Mobile Edge Computing Enabled Vehicular Networks,' IEEE Access , vol. 7, pp. 62624-62632, 2019, doi: 10.1109/ACCESS.2019.2915959.
