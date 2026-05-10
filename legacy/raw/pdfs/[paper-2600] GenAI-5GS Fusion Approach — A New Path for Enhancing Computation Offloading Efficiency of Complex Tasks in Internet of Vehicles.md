---
title: "GenAI-5GS Fusion Approach: A New Path for Enhancing Computation Offloading Efficiency of Complex Tasks in Internet of Vehicles"
authors: "Chao He, Wenhui Jiang, Xing Wang, Wanting Wang, Hong Na, and Xin Xie"
abstract: "With the advancement of real-time communication and data interaction technologies in the Internet of Vehicles (IoV), the pivotal role of Mobile Edge Computing (MEC) in optimising vehicle service efficiency has become increasingly prominent. However, existing task offloading strategies still present significant room for improvement in handling complex tasks, delay control, and resource allocation for Roadside Units (RSUs). To reduce task offloading delay and enhance resource utilization, this paper proposes an offloading method integrating Generative Artificial Intelligence (GAI) with 5G Slicing."
keywords: "Internet of Vehicles, Mobile Edge Computing, Complex Task Offloading, Generative Adversarial Network, Graph Neural Network, 5G Slicing"
---

## GenAI-5GS Fusion Approach: A New Path for Enhancing Computation Offloading Efficiency of Complex Tasks in Internet of Vehicles

Chao He, Wenhui Jiang, Xing Wang, Wanting Wang, Hong Na, and Xin Xie

Abstract -With the advancement of real-time communication and data interaction technologies in the Internet of Vehicles (IoV), the pivotal role of Mobile Edge Computing (MEC) in optimising vehicle service efficiency has become increasingly prominent. However, existing task offloading strategies still present significant room for improvement in handling complex tasks, delay control, and resource allocation for Roadside Units (RSUs). To reduce task offloading delay and enhance resource utilization, this paper proposes an offloading method integrating Generative Artificial Intelligence (GAI) with 5G Slicing (GenAI5GS). First, a Graph-GAN-based vehicle trajectory prediction model is constructed. Operating with CPU/GPU utilization below 50% on resource-constrained RSUs, it enables precise prediction of vehicle movements to support proactive RSU deployment. Secondly, it innovatively integrates 5G slicing technology to dynamically allocate Resource Blocks (RB) within the dedicated 5.9GHz IoV band. By combining multiple Modulation and Coding Schemes (MCS) to accommodate tasks of varying priorities, which enables slicing-based management and flexible resource allocation for RSUs. Finally, research findings demonstrate that the proposed method enhances trajectory prediction accuracy and resource utilization while reducing offloading delay, all while safeguarding multi-dimensional Quality of Service (QoS) requirements. Furthermore, this approach significantly improves IoV complex task processing performance and system stability, delivering safer and more efficient service experiences for invehicle users, thereby possessing clear engineering deployment value.

Index Terms -Internet of Vehicles, Mobile Edge Computing, Complex Task Offloading, Generative Adversarial Network, Graph Neural Network, 5G Slicing

## I. INTRODUCTION

This work was supported by the Science and Technology Research Program of Chongqing Municipal Education Commission (Grant No. KJZDK202201203, KJQN202301258), the Doctoral 'Through Train' Scientific Research Project of Wanzhou (Grant No. wzstc20230418), the Foundation of Intelligent Ecotourism Subject Group of Chongqing Three Gorges University (Grant No. zhlv-20221004), the Natural Science Foundation of Chongqing, China(Grant No. CSTB2025NSCQ-GPX0246), and the Chongqing Graduate Research and Innovation Program (Grant No. CYS25843).

- C. He, W. Jiang, X. Wang, and W. Wang are with the School of Electronic and Information Engineering, Chongqing Three Gorges University, Chongqing, China (e-mail:hechao@sanxiau.edu.cn; jwh2445561061@163.com; 17338367980@163.com; wangwt201228@163.com).

H. Na is with the School of Electrical Engineering, Yunnan Water Resources and Hydropower Vocational College, Kunming, China(e-mail: nahong@ynwater.edu.cn).

- X. Xie is with the School of Automation, Chongqing University of Posts and Telecommunications, Chongqing, China(e-mail: xiexin@cqupt.edu.cn) Manuscript received XXX, XX, 2025; revised XXX, XX, 2025.

W ITH the deep integration of the Internet of Vehicles (IoV) and 6G communication technology, the intelligent transport system is rapidly evolving towards full-area sensing and real-time collaboration [1]. According to industry forecasts, the number of global intelligent vehicles will exceed 89 million units in 2026 [2], and emerging applications such as Autonomous Driving (AD) and vehicle-circuit collaboration have imposed stringent requirements on computing power, communication delay and reliability. Mobile Edge Computing (MEC) offers a promising solution to the challenges of limited in-vehicle computing capacity and inefficient task processing by enabling computation offloading to roadside infrastructure such as Roadside Unit (RSU) [3]. By July 2025, more than 8,700 RSUs have been deployed in China, laying the infrastructure foundation for the scaled application of the IoV.

However, the offloading of IoV complex tasks still faces two core challenges, one is the dynamic adaptation problem, high-speed vehicle movement leads to frequent changes in network topology and task demand [4], the traditional static resource allocation strategy is difficult to match the spatial and temporal distribution characteristics of the task, which is prone to triggering resource scrambling or idling [5]. The second is the delay control bottleneck. High priority tasks such as self-driving control commands have extremely stringent requirements for Ultra-reliable and Low-latency Communication (URLLC), while the existing offloading method lacks prospective prediction of the vehicle trajectory, making it difficult to achieve accurate pre-allocation of RSUs resources. For example, in the morning peak dense traffic scene [6] [7], the vehicle's sudden environment sensing data upload and AD decision instruction transmission concurrently, often due to the lag in resource allocation leads to task blockage, which directly threatens driving safety [8].

In the quest to address these challenges, Generative Artificial Intelligence (GAI) and 5G slice integrated techniques have emerged [9]. GAI, especially deep learning-based Generative Adversarial Networks (GAN), has demonstrated powerful data generation and pattern prediction capabilities in multiple domains [10] [11]. In IoV environment, vehicle movement behaviour models are constructed by integrating vehicle sensor data, road network information and historical trajectories to accurately predict vehicle trajectories and task demand trends, providing a forward-looking basis for resource allocation. Meanwhile, 5G slicing technology allows operators to create multiple logically isolated virtual network slices on a unified physical network infrastructure, each of which can be customised with network resources and Quality of Service (QoS) for specific service requirements [12] [13], effectively meeting the diverse needs of IoV services. Existing research has explored the application of GAI in trajectory prediction, such as the practice of Transformer-based vehicle behaviour modelling and 5G slicing technology in resource isolation and differentiated QoS guarantees, but there are still limitations in the integration of the two, with insufficient real-time and complex scene adaptability of the generative model and lack of deep coupling of the dynamic adjustment of the 5G slices with the vehicle movement trajectory [14], this leads to the resource allocation efficiency of multi-priority tasks and delay performance being difficult to be optimised in a synergistic manner.

In order to achieve a synergistic mechanism for accurate prediction and dynamic slicing, this paper proposes an enhancing computation offloading method that integrates GAI technology with 5G slicing technology (GenAI-5GS), and the main contributions of this work are summarised as follows.

- A Graph Neural Network (GNN) based on GAN (GraphGAN) vehicle trajectory prediction model is innovatively proposed to achieve high precision prediction of vehicle trajectories by capturing the social relationships between vehicles and environmental associations, providing data support for the prospective deployment of RSUs, and breaking through the limitations of the traditional trajectory prediction model that is insufficient in modelling dynamic interactions.
- Combining the trajectory prediction results with 5G slicing technology, a dynamic resource slicing model is designed to flexibly deploy Resource Blocks (RB) based on task priority and real-time demand, forming a closedloop management mechanism of 'Prediction-AllocationAdjustment-Recovery', which solves the problems of poor adaptability of the traditional resource allocation strategy in complex task environment, and the problem of resource wastage or scrambling.
- Through the collaborative framework of accurate prediction and dynamic slicing, the foresight of GAI and the differentiated service capability of 5G slicing are organically combined, which effectively improves the resource utilization rate, delay performance and system stability of complex task processing in IoV, and provides an innovative paradigm for RSUs resource management in dynamic environment.

The rest of this paper is structured as follows. Section II reviews relevant research and identifies existing limitations. Section III presents a system model consisting of communication and vehicle trajectory prediction models. Building upon this, Section IV describes the algorithm, integrating the model with 5G network slicing technology to optimise dynamic resource allocation. Section V analyses and discusses the experimental results, whilst Section VI summarises key findings and outlines future research directions.

## II. RELATED RESEARCH

With the rapid development of IoV technology, MEC has become the core support for improving vehicle service effi- ciency [15]. However, delay control in complex task offloading and RSUs resource allocation issues have always constrained the further improvement of IoV system performance. To comprehensively analyse the current state of research in this field, this paper provides an overview from three aspects: trajectory prediction, resource allocation management, and integrated technology research.

## A. Trajectory Prediction in Task Offloading

In their research on vehicle trajectory prediction, researchers have focused on vehicle interaction modelling and dynamic environment adaptation. Pazho et al. [16] proposed a VT-Former model that combines graph isomorphism and the Transformer architecture. Through the graph attentive tokenisation module, which captures complex interactions between vehicles and is used for vehicle trajectory prediction in highway monitoring scenarios. Experiments show that it achieves or approaches optimal performance on multiple benchmark datasets. Wang et al. [17] proposed a hybrid trajectory prediction framework combining attention mechanisms, which improves the trajectory prediction accuracy and long-term consistency of autonomous vehicles in complex traffic scenarios by integrating spatiotemporal feature modelling, vehicle interaction dynamic analysis, and multimodal data. He et al. [18] proposed a task offloading strategy based on RSUs fusion, combining DRL, CNN and other technologies to predict vehicle behaviour, and using the Nash Equilibrium Game (NEG) algorithm to optimise RSUs resource allocation. Wu et al. [19] proposed a multimodal, interaction-aware vehicle trajectory prediction model based on diffusion Graph Convolutional Network (GCN). By leveraging dynamic graph structures to capture spatiotemporal interactions among vehicles and incorporating multimodal sensory data, the approach enables accurate trajectory forecasting in complex traffic environments. Mistry et al. [20] proposed a hybrid framework that combines Long Short-Term Memory (LSTM) networks with GAN for trajectory prediction in connected and autonomous vehicles. By integrating spatio-temporal feature learning with adversarial training, the model effectively captures vehicle interaction dynamics in multimodal traffic scenarios, demonstrating strong accuracy and generalization in complex environments. Lu et al. [21] proposed a method based on a heterogeneous context-aware GNN for trajectory prediction in the context of the IoV. By integrating multi-source heterogeneous data to construct a dynamic heterogeneous graph, the method models the spatiotemporal interactions between vehicles and the contextual dependencies of the environment, enabling high-precision trajectory prediction in complex traffic scenarios.

The above research shows that traditional models are insufficient for modelling dynamic interactions between vehicles and cannot capture the social relationships between vehicles and their environmental connections. Some models also have limitations in terms of long-term dependency and dynamic interaction modelling, resulting in insufficient realism in the generated trajectories.

## B. Resource Allocation and Slicing Management in MEC

To optimise delay and energy consumption, researchers often use methods such as reinforcement learning and game theory. Cui et al. [22] proposed a mutual dependency calculation method for MEC-assisted robot teams based on multiagent Deep Reinforcement Learning (DRL), enabling robots to autonomously make task offloading and resource allocation decisions according to environmental and task requirements. Cao et al. [23] proposed a joint computing offloading solution for optimising edge computing in IoV to address the issue of task density in multi-vehicle RSUs systems. This solution aims to minimise energy consumption while ensuring task completion delay and limited RSUs computing resources. Chen et al. [24] proposed a federated learning framework based on riskaware reinforcement learning, applied to IoV scenarios, which uses hierarchical reinforcement learning to defend against selfish attacks, improving model accuracy while ensuring data privacy, and enhancing the security and adaptability of federated learning in the dynamic environment of Vehicle to Everything (V2X) networks. Wu et al. [25] focused on heterogeneous vehicular edge computing scenarios, addressed the requirements of URLLC, proposed a corresponding resource allocation scheme, and strived to meet the URLLC queue delay constraints while solving challenges such as the lack of global state information, to optimize system performance. Nezami et al. [26] employed a novel distributed optimization framework for mobile-aware edge-to-cloud resource allocation, service offloading, configuration, and load balancing, addressing the demands of emerging traffic patterns and large-scale realtime computing. Liu et al. [27] introduced an asynchronous DRL based approach for collaborative task computation and on-demand resource allocation in vehicular edge computing. This method enhances task offloading efficiency and resource utilization, thereby improving overall system performance in complex traffic environments. Meanwhile, research on 5G network slicing has primarily focused on dynamic resource management and ensuring service quality. Chekired et al. [28] proposed a scalable SDN core network solution based on 5G slicing, which meets the ultra-low delay requirements of AD services through customised network slicing, enabling flexible scheduling and isolation of network resources to improve the real-time performance and reliability of AD services. Cheng et al. [29] focused on the issue of network slicing resource allocation in Open Radio Access Networks (O-RAN) and proposed a solution using reinforcement learning to improve the throughput of target network slices.

The above studies lack deep coupling with vehicle trajectory prediction in terms of resource allocation and network slicing. Dynamic adjustments lag behind task changes brought about by high vehicle mobility, and overall adaptability and optimization effects are inferior to the methods proposed in this study.

## C. Cross-Domain Integration of GAI and Communication Technology

In applied research on GAI, scholars have focused on trajectory prediction and resource allocation optimization. Onim et al. [30] leveraged GAN in GAI. Through the powerful data augmentation capability of generative models, it broke through the limitation that traditional visual algorithms performed poorly under low-light conditions, and demonstrated the application value of GAI in visual perception tasks. Wang et al. [31] proposed a Unmanned Aerial Vehicles (UAV) assisted resource allocation and task offloading strategy to address the complexity of connected vehicle tasks and uneven resource distribution, and improved system performance by constructing a task dependency model. Fahime et al. [32] explored the application of GAI in the optimization of nextgeneration wireless networks, elaborated on GAI models and wireless network communication paradigms such as 6G, and studied their role in resource allocation and improving network performance. Shatnawi et al. [33] utilised a GAN model to generate new emergency vehicles, with the aim of introducing a comprehensive expanded dataset to assist in the emergency vehicle detection and classification process. Jiang et al. [34] proposed the concept of intelligent slicing and constructed a unified framework for integrating AI into 5G networks. By on-demand instantiation and deployment of AI modules to perform different intelligent tasks, and using neural network channel prediction and anomaly detection to ensure industrial network security as an example, he demonstrated the role of this framework in solving the diversification of 5G networks. Balevi et al. [35] proposed a method for accurately estimating frequency-selective channels with a small amount of pilot signals under low Signal-to-Noise Ratio (SNR) conditions using GAN. This method uses a generative network to learn and generate samples that conform to the distribution of real channels, demonstrating significant performance advantages under low SNR conditions. Zhuan et al. [36] proposed utilising GAI to assist MEC offloading solutions in the industrial Internet of Things (IoT) enabled by digital twins. Through generative models, task characteristics and resource status can be predicted to optimise computing offloading decisions, thereby improving edge computing efficiency and industrial IoT service quality.

The above papers have made some progress in the field of GAI, but they lack the 'Predict-Allocate-Adjust' closed loop of the IoV. Resource allocation often fails to keep pace with the rapid task dynamics caused by high vehicle mobility, while network slicing remains inadequately adaptive to complex and evolving traffic scenarios. In terms of the coordinated optimization of resource utilization and delay, they are inferior to the fusion method proposed in this paper.

To overcome the limitations of existing solutions, this paper proposes a GenAI-5GS fusion offloading method that addresses these challenges by constructing a Graph-GAN vehicle trajectory prediction model and a resource management mechanism based on 5G slicing technology. An intuitive comparison of the research content with existing solutions is shown in Table I.

## III. SYSTEM MODEL

## A. Communications Infrastructure

The role of V2X in RSUs deployment and optimization is crucial, which directly affects the performance and efficiency of IoV, Fig.1 shows the schematic diagram of IoV communication architecture. Among them, RSU is an important part of Vehicle-to-Infrastructure (V2I) communication, and RSUs deployment and optimization is the key to achieve efficient V2I collaboration. As the core communication node in IoV, RSU is not only responsible for collecting road conditions and traffic information, but also providing assisted driving decisions and safety through real-time communication with vehicles. Therefore, the reasonable layout of RSU is important for enhancing the reliability of data transmission, and reducing the communication delay.

TABLE I: Related research

| Research content                                             | Mistry et al. [20] | Cui et al. [22] | Onim et al. [30] | Zhuan et al. [36] | Ours |
| ------------------------------------------------------------ | ------------------ | --------------- | ---------------- | ----------------- | ---- |
| Integration of GAN and GNN                                   | #                  | #               | #                | #                 | !    |
| Prediction results combined with 5G slicing technology       | #                  | #               | #                | #                 | !    |
| 'Precise Prediction-Dynamic Slicing' collaborative framework | #                  | #               | #                | #                 | !    |
| Optimising resources using GAI technology                    | !                  | #               | !                | !                 | !    |
| Research related to resource allocation or network slicing   | #                  | !               | #                | !                 | !    |

Fig. 1: Schematic diagram of the proposed IoV communication.

<!-- image -->

The vehicle data in this study was collected from a section of road during the morning rush hour between 8:00 and 8:20. Due to the high vehicle density during this period, communication for autonomous vehicles and resource allocation at the RSUs may be significantly impacted. Moreover, Vehicleto-Vehicle (V2V) and V2I communications become more complex compared to normal traffic conditions. Therefore, this road segment is selected as the study area to represent a source of complex and demanding tasks. As shown in Fig.1, when vehicles drive into a dense area, the network load is increased, which is prone to triggering conditions such as offloading delays or communication blockage. In view of this, we deployed RSUs block [ Z 1 , Z 2 , ..., Z n ] . RSUs provides offloading service precisely for vehicles in a specific area. In this way, the disordered vehicle tasks in complex road environment are disassembled into multiple sub-tasks for offloading in an orderly manner. This not only greatly improves the offloading efficiency, but also effectively alleviates a series of trafficrelated problems such as traffic congestion and poor data transmission.

During the offloading process, the coverage and signal strength of the RSUs play a decisive role in the quality of the offloading service. In this study, the Friis transmission formula is used to describe the signal strength of the RSUs received by the vehicle, which is also known as the received power of the vehicle, and the formula is expressed as follows:

<!-- formula-not-decoded -->

where P r is the received signal power-higher values indicate stronger signal quality, which enhances data transmission reliability and facilitates efficient task offloading. P t represents the transmission power of the RSUs. G t and G r are the gains of the transmitting and receiving antennas, respectively. Higher antenna gains lead to more directional signal propagation and improved transmission efficiency. The parameter λ is the signal wavelength, and d shows the distance between the RSUs and the vehicle. In practical IoV environments, the effective coverage of an RSU can be extended by optimizing the relationships among these parameters.

Similarly, the data transfer rate is a key metric of communication performance, directly influencing task offloading efficiency and the responsiveness of various vehicular applications. According to the Shannon-Hartley theorem, the actual data transfer rate R d between the vehicle and the RSUs can be calculated using the following formula:

<!-- formula-not-decoded -->

where B denotes the communication bandwidth and N 0 represents the noise power spectral density. When a vehicle is within the RSU's coverage range and the received signal power is strong, the system can allocate additional RB to increase the effective bandwidth, thereby significantly boosting the data transmission rate to meet the stringent real-time demands of high priority tasks, such as AD control commands. Conversely, when the vehicle moves farther from the RSUs and the received power diminishes, the system dynamically adjusts RB allocation based on current conditions, achieving an optimal trade-off between bandwidth and SNR to ensure reliable, albeit lower-rate, data transmission.

In addition, the figure clearly shows the layered architecture in the IoV environment. In the vehicle layer, V2I and V2V communication technologies are used to achieve information interaction with each other and with RSUs. The edge layer, with the RSUs and the edge server as the core, processes vehicle data in situ at the edge of the network, and through the task offloading mechanism, each layer has a clear division of labour and operates in concert to jointly build an efficient and intelligent IoV communication system, which builds a solid foundation for applications such as AD and intelligent traffic management.

## B. Graph-GAN Vehicle Trajectory Prediction Model

In addition to enhancing the communication between RSUs and vehicles, reasonable RSU deployment is also crucial to better reduce the delay of vehicle task offloading, so we design a Graph-GAN vehicle trajectory prediction model graph for prospective RSUs deployment, as shown in Fig.2.

Fig. 2: Graph-GAN vehicle trajectory prediction model.

<!-- image -->

As can be seen in Fig.2, the model utilises generative and adversarial networks along with GNN to process the vehicle trajectory data. The main steps are as follows:

- 1. Input historical data: In the model input section, we organise the vehicle's historical trajectory, current position information and surrounding environment data into the form of a GNN-processable adjacency matrix, which is used as input data to provide support for subsequent trajectory prediction. In this matrix, the vehicle's historical trajectory data set is H = { h 1 , h 2 , ..., h n } , where h n denotes the n -th historical trajectory sequence, the current position information is denoted as P = ( p x , p y ) , and the surrounding environment information is denoted as e = ( e 1 , e 2 , ..., e m ) . We integrate these data into an adjacency matrix A , where the element A ij shows the degree of association between node i and node j . The main consideration is the combination of trajectory similarity, positional distance and environmental factors, and the formula is expressed as follows:

<!-- formula-not-decoded -->

where S ( h i , h j ) is a similarity measure between trajectories h i and h j , d ( P i , P j ) is the Euclidean distance between positions P i and P j , v is a very small integer to avoid a zero denominator, C ( e i , e j ) is a correlation measure between environmental data e i and e j , α , β , γ are weight coefficients, and α + β + γ = 1 . After constructing the adjacency matrix, normalization is applied to enhance the model's training performance. This process ensures a consistent scale across different dimensions, preventing features with extreme values from disproportionately influencing the learning process. In this study, Laplacian normalization is employed, which is defined by the following formula:

<!-- formula-not-decoded -->

where D is the degree matrix, whose elements are D ii = ∑ n j =1 A ij . The degree matrix D records the number of connections for each node. Through this normalisation operation, the impact of different node connection strengths on model training can be effectively balanced.

- 2. GAN-based trajectory prediction: In this model, the Generator's role is to generate fake vehicle trajectory samples based on the input data. By learning the distribution patterns of real data, it generates samples similar to real trajectories. The Generator continuously optimises its parameters to make the generated fake samples as convincing as possible to the Discriminator. Let the Generator be denoted by G , which takes as input a random noise vector z and an adjacency matrix A , and outputs a generated trajectory sample ˆ t = G ( z, A ) . Discriminator is D , the Discriminator network is responsible for distinguishing between real samples and fake samples generated by the Generator. It evaluates the input samples and outputs a probability value indicating whether the sample is real. Let the Discriminator be recorded as D . For the real trajectory sample t and the generated trajectory sample ˆ t , the Discriminator's outputs are D ( t, A ) and D ( ˆ t, A ) , respectively. During training, the Generator and Discriminator compete against each other, and their adversarial loss function is expressed as follows:

<!-- formula-not-decoded -->

where p data ( t ) represents the distribution of real trajectory samples, and p z ( z ) is the distribution of random noise vectors. The objective of the Generator is to minimise the second term in L GAN, that is min Gz ∼ p z ( z ) [log (1 -D ( G ( z, A ) , A ))] , while the objective of the Discriminator is to maximise the entire L GAN, that is max D L GAN.

- 3. Graph-GAN model implementation: GNN plays a key role in the model, as it can mine spatial and temporal relationships in vehicle trajectory data. By learning the adjacency matrix, GNN can capture the mutual influence between vehicles and the relationship between vehicles and their surrounding environment. By analysing the trajectory changes of different vehicles in similar time and space, it can predict the possible driving direction and position of a vehicle at the next moment. In this model, the node feature update formula for the l -th layer is expressed as follows:

<!-- formula-not-decoded -->

where h ( l ) i denotes the feature vector of node i at the l -th layer, N ( i ) represents the set of its neighboring nodes, and d i and d j are the degrees of nodes i and j , respectively, W ( l ) is the learnable weight matrix, and b ( l ) is the bias vector at the l -th layer, with σ denoting the activation function. Through multiple layers of CNN convolutional operations, the final node feature representations are obtained in the last layer. These feature vectors contain rich vehicle trajectory, location, and environmental information. To convert these feature vectors into specific information that can be used for trajectory prediction, a fully connected layer will be used for processing. The predicted trajectory feature vectors are obtained by multiplying the node feature vectors from the final layer with the weight matrix of the fully connected layer and then adding a bias vector, as expressed by the following formula:

<!-- formula-not-decoded -->

where H la = [ h ( L ) 1 , h ( L ) 2 , ..., h ( L ) n ] is the matrix composed of the feature vectors of all nodes in the last layer (layer L ), W fc shows the weight matrix of the fully connected layer, b fc is the bias vector of the fully connected layer, and t pre means the predicted trajectory feature vector.

However, the predicted trajectory feature vectors obtained are typically represented in a high-dimensional abstract space. To obtain meaningful vehicle trajectory coordinates, further transformation is required. We use a mapping function f to perform this transformation, which can be learned by training an additional regression model. Let the transformed trajectory coordinates be P pre = [ x pre , y pre ] , then we have:

<!-- formula-not-decoded -->

In practice, to optimize the mapping function, we employ the Mean Squared Error (MSE) loss to quantify the discrepancy between the predicted trajectory coordinates and the ground-truth coordinates P tr = [ x t r, y t r ] . The objective function is formulated as:

<!-- formula-not-decoded -->

where N is the number of training samples.

To enhance the model's generalization capability and mitigate overfitting, a regularization term is incorporated during training. Specifically, an L 2 regularization term is added to the loss functions of both the generator and the Discriminator. The updated loss functions for the generator L G and discriminator L D are as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where W G,k and W D,k express the k -th learnable parameter matrices in the Generator and Discriminator, respectively, and λ G and λ D are regularisation coefficients, which are adjusted by delay to balance the effects of the loss function and regularisation.

During training, Stochastic Gradient Descent (SGD) and its Adam algorithm are used to update the model parameters. In each iteration, the Discriminator parameters are first fixed, and the Generator parameters are updated to minimise the Generator's loss function. The Generator parameters are then held constant, while the Discriminator parameters are updated to maximize its loss function. After multiple iterations of training, the Generator is able to generate more realistic vehicle trajectories, and the Discriminator can accurately distinguish between real trajectories and generated trajectories, ultimately improving the accuracy and reliability of the entire GraphGAN model for vehicle trajectory prediction.

## C. RSUs Resource Slicing Model

In IoV environment, RSUs must simultaneously handle multiple types of tasks, including AD, environmental perception, and task scheduling. Different tasks have significantly different requirements for delay, bandwidth, and reliability. Traditional resource allocation methods employ a 'one-size-fits-all' strategy, which struggles to meet the dynamic resource demands of complex tasks. To address this, this study combines 5G slicing technology with Graph-GAN trajectory prediction results, as shown in Fig.3. Based on vehicle trajectory prediction results, traffic hotspots are identified, and independent resource slices are dynamically allocated to different task types. Through a dynamic resource slicing model, RSUs resources are managed with precision.

Fig. 3: 5G slicing technology for RSUs resource traffic management.

<!-- image -->

Assume that the total resource pool of the RSU is represented by R = { R 1 , R 2 , ..., R I } available frequency domain RB, where I is the total number of RB, to meet the differentiated needs of different priority task classes. The system divides the total resource pool into three priority slices: high, medium, and low. Each slice class adopts a differentiated resource allocation strategy with the following constraints:

<!-- formula-not-decoded -->

where R k ( t ) denotes the number of RB allocated to priority k at time t . R to represents the total RB resources, adjusted according to the actual deployed frequency band. The frequency band used in this experiment is the dedicated 5.9GHz band for IoV communications, with a channel bandwidth of 20MHz. Calculated based on each RB having a bandwidth of 180kHz, the total number of RB is 110. However, an additional 5% of QoS-guaranteed redundant RB must be reserved within the total resource pool, exclusively for retransmission and emergency requirements of high priority tasks to ensure reliability compliance. R min = 10 signifies the minimum RB quota guaranteed for each slice.

The dynamic allocation algorithm uses a three-layer decision-making mechanism, with static weight allocation set at the initial stage: high:medium:low=60:25:15. The quota is adjusted during operation through a prediction model. The prediction model generates estimates of future time slot task requirements based on vehicle movement characteristics and historical task data, as shown below:

<!-- formula-not-decoded -->

where T k ( t -1) indicates the actual task volume in the previous time slot, P v,k ( t ) shows the predicted probability of vehicle v generating k types of tasks, and the smoothing coefficient ε = 0 . 7 . Resource adjustment uses a progressive update strategy:

<!-- formula-not-decoded -->

where ω k represents the QoS weighting factor, with high priority tasks assigned ω 0 = 1 . 5 , medium priority tasks ω 1 = 1 . 0 , and low priority tasks ω 2 = 0 . 8 , ensuring high-QoS demand tasks receive resources preferentially. This strategy maintains system stability by adjusting the step size θ = 0 . 3 . To further safeguard transmission reliability for high priority tasks, this study introduces a channel quality-resource binding mechanism. RB are dynamically allocated based on the SNR received by vehicles. High priority tasks are prioritised for RB with superior channel quality, thereby reducing transmission error rates. The final allocation outcome undergoes normalisation processing to satisfy overall resource constraints.

Assume that the resource requirement for task type m -th denotes r m and the delay constraint is τ m . Define the binary allocation matrix as follows:

<!-- formula-not-decoded -->

where x m,n = 1 indicates that the n -th RB is allocated to the m -th task type, otherwise it is 0 .

Although this model preliminarily correlates Graph-GAN trajectory prediction results through a 'Predict-Allocate' logic, two key limitations remain: firstly, it passively receives prediction outcomes without accounting for how prediction accuracy fluctuations impact resource allocation, potentially causing high priority tasks to suffer resource shortages due to prediction bias. Secondly, it lacks feedback regulation of the prediction model based on resource utilization status. In low dynamic scenarios, this may generate redundant GraphGAN computations, increasing computational overhead at edge nodes. These limitations provide optimization directions for subsequent fusion mechanism design.

The RSUs resource slicing model constructed in this study achieves fine-grained resource management through a threelayer decision-making mechanism, in the initial stage, it ensures the basic resource requirements of core tasks based on a fixed proportion. During runtime, it dynamically adjusts quotas in conjunction with Graph-GAN trajectory prediction results, and it balances the flexibility and stability of resource allocation through smoothing coefficients and incremental update strategies. The binary allocation matrix and minimum resource quota constraints further ensure resource isolation and task reliability, laying the groundwork for subsequent delay optimization and hotspot area adaptation. They also reserve technical interfaces for the design of subsequent fusion mechanisms.

## D. Bidirectional Feedback Fusion Mechanism between Graph-GAN and 5G Slicing

To address the limitations of the RSUs resource slicing model, this section proposes a bidirectional feedback fusion mechanism integrating Graph-GAN with 5G slicing. By dynamically correlating prediction accuracy with resource elasticity, implementing inverse feedback between resource efficiency and prediction frequency, and employing spatiotemporal coordinated preactivation strategies, it achieves deep coupling between the two technologies. This overcomes the bottlenecks of the traditional 'Predict-Allocate' unidirectional workflow. This addresses resource wastage, high priority task blocking, and computational redundancy stemming from prediction accuracy fluctuations.

Based on the trajectory prediction error output by GraphGAN, prediction accuracy is categorised into high, medium, and low tiers. Correspondingly, the proportion of emergency resource pools for 5G slices and high priority slice quotas are adjusted to ensure resource supply aligns with prediction reliability. The emergency resource pool is reserved from the total RB to address resource shortfalls caused by prediction deviations: when MSE &lt; 0.6 m, the emergency resource pool is reduced to 5%, releasing resources to medium and low priority slices. When 0.6 m ≤ MSE ≤ 1.2 m, the emergency resource pool is maintained at 10%; when MSE &gt; 1.2 m, the emergency resource pool is expanded to 15%. Concurrently, high priority slice quotas adjust synchronously with the emergency resource pool, quantified by the formula:

<!-- formula-not-decoded -->

where R em represents the proportion of emergency resources, ensuring high priority tasks still receive adequate resources when prediction errors are significant.

To avoid redundant computations in Graph-GAN, a resource utilization efficiency metric is introduced to optimise the prediction update frequency of Graph-GAN. This efficiency is defined as η use, expressed by the following formula:

<!-- formula-not-decoded -->

where R ac denotes the actual number of RB occupied by the task, and R al represents the number of RB allocated to the slice. When η use &gt; 90% , the Graph-GAN update frequency decreases from 10 Hz to 5 Hz, reducing edge computing power consumption. When η use &lt; 70% , the update frequency increases to 15 Hz while simultaneously triggering emergency resource pool expansion. When 70% ≤ η use ≤ 90% , the baseline frequency of 10 Hz is maintained. This feedback mechanism dynamically aligns Graph-GAN's computational overhead with resource demands. During off-peak periods with sparse traffic, it reduces computational delay by 30%, thereby preventing computational resource wastage.

To address the switching lag issue of slice models during high speed vehicle movement, a strategy was devised by integrating Graph-GAN trajectory prediction capabilities. On the temporal dimension, based on the Graph-GAN predicted sequence of the vehicle's future positions over the next 5 seconds, the estimated time T en for the vehicle to enter the next RSU coverage area is derived using the vehicle's current speed and the distance to the RSUs. The formula is expressed as follows:

<!-- formula-not-decoded -->

where d R represents the deployment spacing between RSUs, d cu represents the vehicle's current distance to the next RSU, and v cu indicates the vehicle's current speed. When T en ≤ 200 ms, the high priority slice configuration of the current RSU is synchronised in advance to the target RSUs, reducing handover delay to 18 ± 3 ms. In the spatial dimension, when GraphGAN predicts vehicle density in a region will exceed 120 vehicles/km, it dispatches low priority redundant RB from two neighbouring RSUs to supplement the high priority slices of the hotspot RSU, thereby preventing task blocking.

The bidirectional feedback fusion mechanism between Graph-GAN and 5G slicing overcomes the limitations of the RSUs resource slicing model through three core design elements. This reduces slicing handover delay from 50 ms to below 18 ms, thereby overcoming resource scheduling delays during high speed vehicle movement. This establishes the foundational architecture for subsequent experimental validation, enabling enhanced resource utilization and reduced delay.

## IV. PROBLEM DESCRIPTION

After clarifying the infrastructure and allocation mechanism of the RSUs resource slicing model, to further achieve dynamic resource scheduling and precise optimization of task delay, practical algorithmic processes must be designed based on specific scenarios. This section will focus on the practical application of 5G slicing technology in delay control and resource efficiency improvement to meet the differentiated needs of complex tasks in the IoV.

In the context of the IoV communication, there are various types of tasks, and different tasks have significantly different requirements for resources and delay. To achieve refined resource allocation, this study categorises tasks into the following three priority levels and clarifies their characteristics:

- 1. High priority tasks: These include AD control commands and emergency avoidance signals, which require URLLC, which must meet URLLC requirements. Data volume is L &lt; 10 KB, with a delay constraint of T &lt; 50 ms, delay jitter of T ji &lt; 5 ms, and a task completion rate of 100%. Transmission reliability must be greater than or equal to 99.999%. Employing QPSK modulation with a hybrid automatic repeat request mechanism, the maximum retransmission count is less than or equal to 3.
- 2. Medium priority tasks: These include environmental perception data and vehicle-to-infrastructure information exchange, the system must meet the following

requirements, low delay of T &lt; 100 ms, data volume of 10 KB &lt; L &lt; 1 MB, task completion rate greater than or equal to 95%, and bandwidth fluctuation tolerance of ± 10%. Dynamic bandwidth adjustment is supported to prevent data transmission interruptions caused by channel fluctuations.

- 3. Low priority tasks: These include in-vehicle entertainment streaming and software OTA updates, with a delay tolerance of T &gt; 500 ms, data volume of L &gt; 1 MB, and a task completion rate requirement of greater than or equal to 90%. Non-real-time transmission is permissible, with temporary caching of files during network congestion.

To ensure communication quality, RB for similar tasks must be allocated consecutively, namely, for the m -th type of task, there are start block s m and end block e m , such that x m,n = 1 , with the following constraints:

<!-- formula-not-decoded -->

When there are insufficient available contiguous RB, the dynamic borrowing mechanism is triggered, allowing high priority tasks to temporarily occupy non-guaranteed RB of low priority tasks and automatically return them when the resources become available, thereby preventing low priority tasks from experiencing prolonged starvation.

It is assumed that the processing delay of the m -th task T m not only needs to consider transmission delay and processing delay, but also for handover delays when vehicles transition between RSUs coverage areas, queuing delays, and retransmission delays. The delay model is expressed as follows:

<!-- formula-not-decoded -->

where max Re = 3 is the maximum retransmission count, T so =1ms represents the TDMA slot duration, and P er signifies the bit error rate, ensuring 1 -P er ≥ 99.999%. If retransmissions attempts exceed the threshold without success, emergency resource allocation is triggered, utilising reserved redundant RB. L m means the task data volume, B m represents the bandwidth allocated to this task, and η SNR signifies the channel quality factor. This factor describes the impact of SNR on transmission rates and is a non-constant value, with its values expressed as follows:

<!-- formula-not-decoded -->

where SNR= P r N 0 · B + I MUI , I MUI=5 dBm shows neighbouring vehicle interference power, and N 0 = -174 dBm/Hz represents the thermal noise power spectral density. t d =5 ms is the fixed RSU processing delay, τ s =2 ms denotes the handover delay, and when the vehicle does not switch RSUs, τ s = 0 . B m is positively correlated with the number of RB r m , expressed as follows:

<!-- formula-not-decoded -->

where k indicates the bandwidth per RB, set at 180 kHz. At this point, the delay model must satisfy T m ≤ τ m , where τ m represents the maximum tolerable delay for the m -th task category.

Different Modulation and Coding Schemes (MCS) are employed for tasks of varying priority levels. High priority tasks utilise QPSK modulation with a data transmission rate of:

<!-- formula-not-decoded -->

where R c = 0 . 8 expresses the coding rate. Medium priority tasks employ 16QAM modulation with M m = 16 and a coding rate R c = 0 . 7 . Low priority tasks utilise 64QAM modulation with M l = 64 and a coding rate R c = 0 . 6 .

Additionally, the high priority task category employs QPSK modulation, with the bit error rate expressed by the following formula:

<!-- formula-not-decoded -->

where M h = 4 denotes the number of QPSK symbols, and erfc represents the complementary error function. Must ensure P er &lt; 10 -5 , should the threshold not be met, retransmission shall be triggered, with the retransmission delay factored into the total delay.

After the algorithm delay study is completed, this study will continue to investigate the RSUs resource situation. Using the Graph-GAN model to predict the location distribution of vehicles in the future time period t as P ( t ) = { p 1 ( t ) , p 2 ( t ) , ..., p K ( t ) } ( K is the number of vehicles), the task density of each region can be calculated as follows:

<!-- formula-not-decoded -->

where N t is the number of regional tasks, and a shows the regional area. Based on density, the RSUs coverage area is divided into Q hotspot regions Ω q ( q = 1 , 2 , ..., Q ) , with each region corresponding to a set of task type distributions { λ q,m } , where λ q,m represents the proportion of the m -th task type in the region Ω q .

On this basis, the goal of dynamically adjusting resource slices is to maximise global resource utilization η , that is:

<!-- formula-not-decoded -->

where r al q,m is the number of RB allocated to the m -th type of task in region Ω q , and r ac q,m represents the actual number of RB required. The Lagrange Multiplier method is introduced to solve this optimization problem, transforming the global resource utilization maximisation problem into a local optimization problem of resource allocation in each region, ensuring that resource idleness or insufficiency is minimised as much as possible while satisfying regional resource constraints. The Lagrange function is constructed as follows:

<!-- formula-not-decoded -->

where R t q denotes the total number of RB allocated to region Ω q , and µ q is the Lagrange multiplier. By taking the partial derivative of r al q,m and setting it to zero, the optimal allocation strategy can be obtained as follows:

<!-- formula-not-decoded -->

where through iterative updating of µ q , resources can be dynamically balanced across regions to avoid overloading resources in hotspot areas.

Considering that vehicle movement may cause the RSUs slice in a certain area to be unable to process the corresponding tasks in a timely manner, a task change rate threshold δ ( δ =30%) is set for each area. When vehicle movement causes the task density in the area to exceed the threshold, the slice switching mechanism is triggered.

Based on the future ∆ T -period trajectory distribution generated by the Graph-GAN model, the task density variation rate for each region is computed as follows:

<!-- formula-not-decoded -->

where ρ p represents the predicted task density for the region, and ρ c shows the current task density for the region. When ρ d ≥ δ/ 2 , the pre-allocation process is initiated to reserve 20% of emergency RB for the target region in advance, as shown below:

<!-- formula-not-decoded -->

When ρ d ≥ δ , trigger formal slice switching. We set a resource difference to indicate the degree of current RSUs slice resource shortage or excess. When ∆ R q &gt; 0 , request new resources. When ∆ R q &lt; 0 , release redundant resources, as shown below:

<!-- formula-not-decoded -->

where R o q represents the currently allocated resources, and R n q denotes calculated based on the predicted task density ρ p q , reflecting the resource requirements for future periods, as shown below:

<!-- formula-not-decoded -->

where r u is the number of RB corresponding to the unit density.

To clearly illustrate the implementation logic of the aforementioned 5G slice dynamic resource allocation mechanism, particularly the differences between the 'Predict-AllocateAdjust' closed-loop process in the GenAI-5GS method and traditional methods, the following provides its core pseudocode to visually demonstrate the dynamic adjustment process of the GenAI-5GS method.

Through the above mechanism, the delay of slice switching can be controlled within 50 ms, and resource recovery efficiency can be improved to over 95%, effectively solving the problem of resource fragmentation in dynamic scenarios in IoV. Combined with the predictive capabilities of Graph-GAN, a closed-loop management system of 'Prediction-AllocationAdjustment-Recovery' is formed, providing a solid foundation for the efficient offloading of complex tasks.

## Algorithm 1 Implementation process of the GenAI-5GS method

Require: Vehicle trajectory dataset H , simulation duration T , total RSUs RB I

Ensure: Resource utilization η , average task delay T m initializeHistory()

- 1: Initialize RSUs with I RB, coverage radius 300m
- 2: Load vehicles V from H ; initialize predictor P
- 3: Set initial slices: High=60, Medium=25, Low=15, adjustment factor=0.3
- 4: for t = 1 to T do
- 5: Update vehicle positions/speeds from H
- 6: Generate tasks for vehicles in RSUs range (probability ∝ speed)
- 7: if method = 'GenAI-5GS' then
- 8: predicted tasks = P .predict( V, t )
- 9: ideal alloc = proportional allocation(predicted tasks, I )
- 10: slices [ τ ] += 0 . 3 × ( ideal alloc [ τ ] -slices [ τ ]) 11: Ensure ∑ slices = I
- 12: else if method = 'Dynamic' then
- 13: alloc = proportional allocation(RSUs.queue, I )
- 14: else
- 15: alloc: High=50, Medium=30, Low=20
- 16: end if
- 17: Process tasks:
- 18: Compute delay as:
- 19: (task.size × 8 × 10 3 ) / (alloc[task.type] × 180 × 10 3 ) +5 ms
- 20: Record delay if task completes
- 21: Record utilization = ∑ alloc I
- 22: end for
- 23: Return η = avg ( utilization history ) , T m = avg ( recorded delays )

## V. RESULTS AND DISCUSSION

## A. Experimental Setup

In this experiment, we selected a section of complex road conditions for study, which includes a multi-lane lane change scenario in a highway intersection area. Vehicle density during the morning peak period (8:00-8:20) can reach two highdensity gradients of 80 vehicles/km and 120 vehicles/km., with 70% being small passenger cars, 20% being trucks, and 10% being emergency vehicles. The average vehicle speed ranges is 40-80 km/h, the acceleration values is -3-2 m/s 2 , exhibiting typical characteristics of dynamic dense traffic. RSUs are deployed every 500 m and 300 m along the road, with a coverage radius of 300 m, a transmission power of 23 dBm, an antenna gain of 2 dBi, and operating on the 5.9GHz frequency band (dedicated to IoV communication). This deployment complies with the design specifications for road-vehicle coordination facilities, they support V2I/V2V communication.

The experiment utilised the V2I communication channel defined in 3GPP TR 36.885, pecifically incorporating Rayleigh Fading, multipath number is set to 6, and Log-Normal Shad- owing Fading, spatial correlation distance set to 50 m, whilst incorporating multi-user interference correction for SNR calculation. The Media Access Control (MAC) layer employs a TDMA scheduling mechanism with a 1 ms timeslot duration and 0.5 ms scheduling delay, supporting high priority tasks preempting non-guaranteed RB from low priority tasks. The network layer incorporates an M/M/1 queueing model to compute queueing delay, with high priority task jitter required to satisfy T ji &lt; 5 ms to meet URLLC standards.

The experimental data comes from public datasets, including fusion perception data from roadside lidar, millimeter-wave radar, and on-board unit devices, collected at a frequency of 10 Hz. And data covers the historical trajectories, realtime locations, and environmental parameters of 2000 test vehicles. This experiment employs the NVIDIA Jetson Xavier NX, a typical hardware platform for resource-constrained RSUs, to simulate real deployment environments. Testing was conducted using Python, with PyTorch 2.0 serving as the deep learning framework. Each test was repeated 30 times, with averages taken to mitigate random variation. By comparing the delay distribution with publicly available IoV test datasets from NGSIM and ApolloScape, the error was controlled within 10%, thereby validating the model's effectiveness. The specific simulation parameter settings are shown in Table II.

## B. Results Analysis

## 1) Trajectory Prediction

This experiment is divided into model trajectory prediction simulation and RSUs resource allocation simulation based on 5G slicing technology on the Graph-GAN model. The effectiveness of the Graph-GAN model is evaluated based on the trajectory prediction losses in both the Generator and Discriminator, as well as the accuracy of the model's output. Additionally, the rationality and applicability of 5G network slicing in RSUs resource allocation are also assessed.

This experiment compares the Generator and Discriminator losses of the CNN-GAI vehicle trajectory prediction model and the proposed Graph-GAN model during trajectory prediction, as illustrated in Fig.4. The comparison aims to provide a preliminary assessment of the Graph-GAN model's superior performance in trajectory prediction.

As evident from the two plots in Fig.4, the Generator Loss of the CNN-GAI model exhibits significant fluctuations in the early stages and remains markedly higher than the Discriminator Loss in the later stages. Furthermore, the error bars corresponding to the Generator Loss are consistently longer than those for the Discriminator Loss. This indicates that the Generator's capabilities are weaker than those of the Discriminator, resulting in insufficient training stability and an inadequate learning of the true trajectory distribution. In contrast, the loss curve for the Graph-GAN model demonstrates that both Generator and Discriminator losses decline rapidly in the early stages before stabilising throughout the remainder of training. The gap between Generator and Discriminator losses remains narrow, and the corresponding error bars for both are compact. This indicates that the Generator and Discriminator have achieved a favourable equilibrium in their competitive interaction, with robust training stability. The Generator has successfully produced trajectories approximating the true distribution, rendering the Discriminator unable to accurately distinguish between real and generated trajectories. This arises because graph neural networks effectively capture complex vehicle interactions, while GAN continuously optimise Generator and Discriminator performance through their adversarial mechanism. This accelerates convergence and enhances stability during training, thereby improving trajectory prediction quality and reliability.

TABLE II: Experimental Parameters

| Symbol                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |        |                 |       |       |       |     |     |     |              |     |     |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | --------------- | ----- | ----- | ----- | --- | --- | --- | ------------ | --- | --- |
| Z n P P                                                     | RSUs block deployment Power of the vehicle receiving the RSUs signal and the                                                                                                                                                                                                                                                                                                                                                                                                                                                   |        | r ,             |       | t     |       |     |     |     |              |     |     |
| G t , G r λ R d                                             | RSUs transmitting the signal antenna and receiving antenna benefits wavelength data transmission rate between vehicles and RSU domain bandwidth and communication band-                                                                                                                                                                                                                                                                                                                                                        |        |                 |       |       |       |     |     |     |              |     |     |
| B m , B                                                     | Transmitting Signal Actual Frequency of each RSUs RB are both 180 KHz                                                                                                                                                                                                                                                                                                                                                                                                                                                          |        |                 |       |       |       |     |     |     |              |     |     |
| r m N 0 α , β , γ P , P pre , P tr                          | width Number of allocated RB Noise power spectral density Weighting factor, and α + β + γ = 1 Vehicle's current location information, predicted trajectory trajectory information                                                                                                                                                                                                                                                                                                                                              | actual |                 |       |       |       |     |     | and | information, |     |     |
| λ P v,k ( t ) ρ ( t ) λ q,m al q,m , r ac q,m R t q f d f c | Regularisation coefficient Number of RB allocated to priority k at time t Global resource utilization rate, with the research objective of maximising it Vehicle-mounted transmit power, set to 20dBm Vehicle-mounted receiving antenna gain, rated at 2dBi Smoothness coefficient,and ε = 0 . 7 Processing delay for m -th class tasks, and T m ≤ τ m , τ m is the maximum tolerable delay Predicted probability of vehicle v generating k types of tasks Task density in each region Proportion of task type m in region Ω q |        | G G , k η G ε T | v,t m | D t ) | ( v,r | P   | R   |     |              | λ   | D   |
| I MUI                                                       | Doppler shift, expressed by the formula: d c Operating frequency band, set to 5.9GHz Standard deviation of the Rayleigh Fading coefficient and the Log-Normal Shadowing Fading coefficient are 0.1dB and 8dB respectively                                                                                                                                                                                                                                                                                                      |        |                 |       |       |       |     |     |     |              |     |     |
| SNR                                                         | Multi-user interference, value of 5dBm Signal interference Thermal noise power spectral density, value of Thermal                                                                                                                                                                                                                                                                                                                                                                                                              |        |                 |       |       |       |     |     |     |              |     |     |
| N 0                                                         | noise power spectral density, value of -174dBm/Hz                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |        |                 |       |       |       |     |     |     |              |     |     |
| T q                                                         | the formula: T q = ρ µ · (1 - ρ ) Queue utilization rate, formula: ρ = λ µ                                                                                                                                                                                                                                                                                                                                                                                                                                                     |        |                 |       |       |       |     |     |     |              |     |     |
| ρ                                                           | Arrival rate of tasks with different priorities, λ h = 100 /s                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |        |                 |       |       |       |     |     |     |              |     |     |
| λ                                                           | λ m = 50/s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |        |                 |       |       |       |     |     |     |              |     |     |
|                                                             | Service rate, formula: µ = k · r m , where k = 180KHz/RB                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |        | µ               |       |       |       |     |     |     |              |     |     |
|                                                             | M/M/1 queueing model calculates queueing delay using                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |        |                 |       |       |       |     |     |     |              |     |     |
|                                                             | Ω q and actual number of RB required Total number of RB allocated to region Ω q f = v · f c                                                                                                                                                                                                                                                                                                                                                                                                                                    |        |                 |       |       |       |     |     |     |              |     |     |
| r                                                           | Number of RB allocated for the m -th type of task in region                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |        |                 |       |       |       |     |     |     |              |     |     |
| , σ                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |        |                 |       |       |       |     |     |     |              |     |     |
| R                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |        |                 |       |       |       |     |     |     |              |     |     |
| S                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |        |                 |       |       |       |     |     |     |              |     |     |
| σ                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |        |                 |       |       |       |     |     |     |              |     |     |
|                                                             | ,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |        |                 |       |       |       |     |     |     |              |     |     |

As we can see, Fig.4 shows that the Graph-GAN model is more stable in training. Next, we will discuss the trajectory prediction results. We selected five groups of vehicle samples on the road, with each group containing 100 vehicle trajectories. By calculating the average of the 100 trajectory positions, this paper compares the prediction results of the Graph-GAN vehicle trajectory prediction model, the CNN-GAI [37], the CNN [38], and the Particle Swarm Optimization (PSO) [39], as shown in Fig.5.

<!-- image -->

(b) Graph-GAN trajectory model

Fig. 4: Trajectory prediction model of different strategy.

As shown in Fig.5, the Graph-GAN model exhibits the highest degree of alignment between its predicted trajectories and actual trajectories, with an average positional error of just 0.85 m and a standard deviation of 0.32 m, demonstrating strong predictive accuracy and stability. In contrast, the CNNGAI model has an average error of 1.52 m and a standard deviation of 0.48 m. While its prediction results are close to the actual trajectory, the deviation increases in dynamic scenarios such as turns. The error of the CNN model further increases to 2.37 m with a standard deviation of 0.76 m, while the PSO algorithm model performs the worst, with an average error of 3.14 m and a standard deviation of 1.05 m, showing significant trajectory fluctuations and severe deviations. These quantitative data further validate the superiority of the GraphGAN model. By synergistically optimising GAN and GNN, which significantly improves trajectory prediction accuracy in complex scenarios while maintaining a low standard deviation, providing a more reliable data foundation for subsequent RSUs resource scheduling.

Fig. 5: Trajectories comparison of different prediction model.

<!-- image -->

## 2) Resource Allocation

To validate the practical effectiveness of the proposed GenAI-5GS integrated offloading method, this experiment further combined the trajectory prediction results of GraphGAN to conduct a simulation analysis of the performance of 5G slicing technology in RSUs resource allocation. The experiment covered the entire morning rush hour simulation cycle using 100 time steps, focusing on evaluating two key metrics, resource utilization rate and task offloading delay. These metrics were compared with those of traditional Static Resource Allocation (Static-RA) [40] methods and Dynamic Resource Allocation (Dynamic-RA) [41] methods.

Resource utilization serves as a key metric for evaluating the efficiency of resource allocation within the RSUs. In this paper, resource utilization specifically denotes the RB utilization rate of the RSUs, defined as the ratio of the actual number of RB allocated to tasks to the total number of available RB within the RSUs. The RB actually allocated must satisfy two conditions. Firstly, they must be assigned to high, medium, or low priority task slices. Secondly, they must be actively occupied by tasks within the time step. The dynamic resource allocation across high, medium, and low priority tasks based on 5G slicing technology is illustrated in Fig.6. This diagram depicts the dynamic resource allocation process within the proposed method, where the initial allocation ratio of the three priority levels is set at 60:25:15. Using this baseline, the allocation quotas are adjusted during runtime through a predictive model, enabling dynamic resource allocation and management.

As shown in Fig.6, high priority tasks initially occupy approximately 60% of the resource quota. When a surge in high priority tasks is predicted, such as during the morning rush hour from 8:10 to 8:15 (step length 40-60), vehicles merge from ramps onto the main road, Graph-GAN anticipates high-density areas and shifts 5% of resource slices toward high priority tasks, maintaining a utilization rate of 98%, thereby validating the accuracy of prediction-driven adjustments. The medium priority quota ensures basic requirements while dynamically adapting to changes in high priority tasks. Low priority tasks are always guaranteed a minimum threshold of 10 RB, with only minor adjustments made when system resources are surplus or scarce, ensuring the continuous processing of non-real-time tasks. Following task prioritisation, resource utilization is analysed as illustrated in Fig.7. The resource utilization data is calculated based on actual RB occupancy within each time step, with averages taken every 10 time steps.

Fig. 6: Time variation between different task priorities in GenAI-5GS resource allocation methods.

<!-- image -->

Fig. 7: Comparison chart of resource utilization rates for different resource allocation methods.

<!-- image -->

As shown in Fig.7, the Static-RA method achieves 100% utilization because it allocates all RB statically. However, approximately 25% of RB remain idle resources occupied by low priority tasks, resulting in an actual effective utilization rate of only 75% ± 3%. This may cause high priority tasks to become blocked due to resources being permanently occupied by low priority tasks. The Dynamic-RA method dynamically adjusts resources based on real-time task queues, demonstrating responsiveness to task variations. However, relying solely on current queue information without forward-looking prediction introduces allocation lag during high-speed vehicle movement or sudden task surges, resulting in resource idleness. The GenAI-5GS approach integrates Graph-GAN trajectory prediction with 5G slice dynamic management, achieving near 100% utilization with idle RB accounting for less than 1%. This closed-loop mechanism of 'Predict-Allocate-Adjust-Recover' pre-allocates resource slices for forecasted vehicle trajectories in hotspot areas, ensuring precise resource matching during traffic fluctuations. This integrated technology demonstrates significant advantages in balancing resource utilisation efficiency with dynamic adaptability.

As we can see, Fig.6 and Fig.7 clearly illustrates the dynamic resource allocation logic between tasks of different priorities in the GenAI-5GS method based on 5G slicing technology, validating the effectiveness of the baseline quota and predictive adjustment mechanism in fine-grained resource management. Next, we will further analyse the differences in delay control between the GenAI-5GS method and traditional Static-RA and Dynamic-RA methods, as shown in Fig.8, thereby providing direct evidence for evaluating the optimization effect of integrated technology on the real-time performance of complex tasks.

Fig. 8: Task offloading delay comparison.

<!-- image -->

As shown in Fig.8, the Dynamic-RA method exhibits the greatest delay fluctuations and the highest number of extreme spikes. This stems from its reliance solely on real-time task queues for resource adjustment, resulting in pronounced lag and difficulty in handling sudden task surges. The Static-RA method exhibits fluctuating but milder delay, stemming from certain high priority tasks failing outright due to resource shortages under fixed allocation, thus not being included in delay statistics. The GenAI-5GS approach demonstrated optimal performance, owing to the synergistic collaboration between Graph-GAN prediction and 5G slicing. Proactive resource allocation prevents queuing, while dynamic adjustment mechanisms ensure stable delay. Furthermore, to further validate the stability of the GenAI-5GS approach, we conducted comparative experiments on high priority tasks under varying SNR conditions, as illustrated in Fig.9. The SNR range for this experiment was set from 5 dB to 30 dB, with delay statistics calculated using the same methodology as in Fig.8.

Fig. 9: Comparison of average delay for high priority tasks under different SNR.

<!-- image -->

As shown in Fig.9, the delay of all three methods decreases with increasing SNR. However, the GenAI-5GS method consistently maintains optimal performance, with significantly lower delay fluctuations than traditional approaches. At SNR=5dB, GenAI-5GS achieves an average delay reduction of 28.2% compared to Dynamic-RA and 41.0% compared to Static-RA. This advantage stems from Graph-GAN trajectory prediction proactively identifying low quality channel regions. Through a bidirectional feedback mechanism, it expands the emergency resource pool by 15%, prioritising retransmission resources for critical tasks and mitigating retransmission congestion caused by poor channel conditions. As SNR increased to 20 dB, transmission delay decreased significantly. The dynamic resource allocation of the 5G slice precisely matched the predicted task demands, reducing the proportion of queueing delay from 21.7% at SNR=5dB to 8.4%. As SNR further increases to 30 dB, GenAI-5GS maintains stable delay, with bit error rate approaching the URLLC requirement of 10 -5 and retransmission delay becoming negligible. The GenAI5GS approach's advantage lies in its precise resource matching through 'Prediction-Slicing' synergy. By using Graph-GAN to pre-allocate RB to high SNR zones where vehicles are about to enter, it effectively avoids the real-time adjustment lag of Dynamic-RA and the fixed resource wastage of Static-RA.

## C. QoS Multi-dimensional Performance Analysis

To further validate the GenAI-5GS method's capability in safeguarding multi-dimensional QoS requirements, rather than relying solely on radio block count to measure service quality, this experiment introduces three core QoS metrics: transmission reliability, delay jitter, and bandwidth stability. The performance differences between GenAI-5GS and traditional methods Static-RA and Dynamic-RA are compared, with results shown in Fig.10.

As shown in Fig.10, GenAI-5GS delivers optimal performance across all QoS dimensions. For high priority URLLC

<!-- image -->

(a) Transmission reliability (high priority)

<!-- image -->

- (c) Bandwidth stability (medium priority)

<!-- image -->

(b) Time delay jitter (high priority)

<!-- image -->

(d) Task completion rate (low priority)

Fig. 10: Multidimensional performance comparison of different QoS methods.

tasks, its transmission reliability reaches 99.9995%, surpassing Dynamic-RA by 0.0495 percentage points and Static-RA by 0.0795 percentage points. This advantage stems from the model's allocation of 5% QoS-guaranteed redundant RB for high priority tasks. When the channel bit error rate approaches the 10 -5 threshold, these redundant RB rapidly trigger HARQ retransmissions, preventing task failure. Regarding delay jitter, GenAI-5GS exhibits a high priority task delay fluctuation of 3.2 ± 0.5 ms, representing merely 36.8% of Static-RA and 50.8% of Dynamic-RA. This is because Graph-GAN proactively predicts vehicle channel quality changes, prioritising high priority tasks for scheduling onto high quality RB with SNR &gt; 20 dB, thereby mitigating delay jitter caused by channel fluctuations.

For medium priority tasks, GenAI-5GS exhibits bandwidth stability of less than or equal to 8%, meeting the industry tolerance threshold of ± 0.5 ms. In contrast, Dynamic-RA experiences bandwidth fluctuations of 15.2% due to lag in realtime adjustments, while Static-RA, with its fixed allocation, demonstrates lower volatility but incurs 25% idle resources. Regarding task completion rates for low priority tasks, GenAI5GS achieved 92.3%, slightly outperforming both DynamicRA and Static-RA. It further supports temporary buffering during network congestion, thereby preventing frequent task discards.

In summary, the Graph-GAN model reduces vehicle trajectory prediction errors by 44% compared to the CNN-GAI model, providing a high precision foundation for resource scheduling. Furthermore, the GenAI-5GS fusion algorithm achieves synergistic optimization in both resource utilization and task delay dimensions. Compared to conventional approaches, resource utilisation improved by 14.9%, while baseline delay decreased by 16% relative to Static-RA and by 22% relative to Dynamic-RA. Delay performance across varying SNR conditions also demonstrated optimality for the GenAI-5GS fusion algorithm. Furthermore, the GenAI-5GS approach achieves optimization from single RB quantity to multi-dimensional QoS assurance through redundant resource reservation, combined with channel quality binding and QoS weight allocation. This fully demonstrates the effectiveness of generative AI and 5G slicing fusion technology in offloading complex IoV tasks, providing a viable paradigm for refined RSUs resource management in dynamic scenarios.

When considering overall metrics, GenAI-5GS demonstrates a 14.9% improvement in resource utilization compared to Dynamic-RA, a 16% reduction in task delay relative to Static-RA, and 22% lower than Dynamic-RA. This synergistic optimization with QoS guarantees demonstrates that the deep integration of generative AI with 5G slicing can effectively adapt to complex task demands in dynamic IoV scenarios, providing a practical technical paradigm for refined RSUs resource management.

## VI. CONCLUSION

The proposed GenAI-5GS integrated offloading approach effectively resolves the challenges of dynamic adaptation and latency control in complex IoV task offloading through the deep coupling of Graph-GAN and 5G slicing technology, with simulation experiments demonstrating significant efficacy. The Graph-GAN vehicle trajectory prediction model, leveraging synergistic optimization of GAN and GNN, achieves an average positional error of 0.85 m, single-prediction processing time of 12.3 ± 1.5 milliseconds, and a parameter count of 1.2 × 10 6 while maintaining CPU/GPU utilisation below 50% on resource-constrained RSUs. This not only provides high precision support for resource pre-allocation but also guides RSUs forward-looking deployment through the mapping logic of 'Tier-1 hotspots 300 m, Secondary Hotspot 500 m' mapping logic to guide proactive RSUs deployment. The GenAI-5GS approach dynamically calculates resource blocks within the dedicated 5.9GHz V2X band, adapts to multiple modulation coding schemes, and establishes a 'Predict-AllocationAdjustment-Recovery' closed-loop mechanism. This achieves near 100% resource utilization, reduces task offloading latency by 16% compared to Static-RA, and 22% lower than DynamicRA. It simultaneously guarantees 99.9995% transmission reliability for high priority URLLC tasks, 3.2 ± 0.5 ms delay jitter, and less than or equal to 8% bandwidth stability for medium priority tasks. The innovative 'Prediction Accuracy-Resource Elasticity' bidirectional feedback mechanism overcomes limitations of single-technology approaches. However, research shortcomings remain, the model has not been validated in real extreme scenarios such as heavy rain or dense fog, GraphGAN's real-time performance requires enhancement in scenarios exceeding 120 vehicles/km, and its adaptability for multiRSUs collaborative scheduling warrants further exploration. Future work will involve field testing to optimise robustness in non-ideal environments, lightweight Graph-GAN architectures to accelerate response times, and integration with 6G technology to expand multi-RSUs collaborative scenarios. This will provide more robust support for the large-scale deployment of intelligent transport systems.

## ACKNOWLEDGMENT

The authors gratefully acknowledge the insightful comments from the anonymous reviewers.

## REFERENCES

- [1] GSM Association, 'Global Mobile Economy Development 2022 report,' 2022.
- [2] F. Tang, B. Mao, N. Kato et al., 'Comprehensive Survey on Machine Learning in Vehicular Network: Technology, Applications and Challenges,' IEEE Commun. Surv. Tutorials. , vol. 23, no. 3, pp. 2027-2057, 2021, doi:10.1109/COMST.2021.3089688.
- [3] Y. Lu, X. Huang, K. Zhang et al., 'Blockchain Empowered Asynchronous Federated Learning for Secure Data Sharing in Internet of Vehicles,' IEEE Trans. Veh. Technol. , vol. 69, no. 4, pp. 4298-4311, 2020, doi:10.1109/TVT.2020.2973651.
- [4] T. Deng, Y. Chen, G. Chen et al., 'Task Offloading Based on edge Collaboration in MEC-Enabled IoV Networks,' ACM Trans. Internet Technol. , vol. 25, no. 2, pp. 197-207, 2023, doi:10.23919/JCN.2023.000004.
- [5] Y. -J. Ku, S. Baidya and S. Dey, 'Uncertainty-Aware Task Offloading for Multi-Vehicle Perception Fusion Over Vehicular Edge Computing,' IEEE Trans. Veh. Technol. , vol. 72, no. 11, pp. 14906-14923, 2023, doi:10.1109/TVT.2023.3284369.
- [6] W. Zhao, Y. Cheng and Z. Liu, 'Advancing RSU-assisted Automated Vehicle Networks: A DRL Empowered Distributed Task Offloading Framework,' IEEE Network. , vol. 39, no. 2, pp. 242-249, 2025, doi:10.1109/MNET.2024.3449851.
- [7] M. Khabbaz, 'Deadline-Constrained RSU-to-Vehicle Task Offloading Scheme for Vehicular Fog Networks,' IEEE Trans. Veh. Technol. , vol. 72, no. 11, pp. 14955-14961, 2023, doi:10.1109/TVT.2023.3285255.
- [8] B. Ko, S. Liu, S. Son et al., 'RSU-Assisted Adaptive Scheduling for Vehicle-to-Vehicle Data Sharing in Bidirectional Road Scenarios,' IEEE Trans. Intell. Transp. Syst. , vol. 22, no. 2, pp. 977-989, 2021, doi:10.1109/TITS.2019.2961705.
- [9] K. Moghaddasi, S. Rajabi, F. S. Gharehchopogh, 'An advanced deep reinforcement learning algorithm for three-layer D2D-edgecloud computing architecture for efficient task offloading in the Internet of Things,' Sustainable Comput. Inf. Syst. , vol. 43, 2024, doi:10.1016/j.suscom.2024.100992.
- [10] K. Asghari, M. Masdari, F. S. Gharehchopogh, 'Multi-swarm and chaotic whale-particle swarm optimization algorithm with a selection method based on roulette wheel,' Expert Syst. , vol. 38, no. 8, 2021, doi:10.1111/exsy.12779.
- [11] M. Yan, H. Guo, C. A. Chan et al., 'Semantic Communication-Enabled Multi-Access Edge Computing Network Resource Optimization in the 6G Era,' IEEE Wireless Commun. , 2025, doi:10.1109/MWC.2025.3600791.
- [12] Y. Guo, Y. Zhang, L. Niu et al., 'Conflict Probability based Path Planning Algorithm for Internet of Vehicles,' IAEAC. , 2021, doi:10.1109/IAEAC50856.2021.9390979.
- [13] M. Yan, R. Xiong, Y. Wang et al., 'Edge Computing Task Offloading Optimization for a UAV-assisted Internet of Vehicles via Deep Reinforcement Learning,' IEEE Trans. Veh. Technol. , vol. 73, no. 4, pp. 5647-5658, 2024, doi:10.1109/TVT.2023.3331363.
- [14] T. Z. H. Ernest and A. S. Madhukumar, 'Computation Offloading in MEC-Enabled IoV Networks: Average Energy Efficiency Analysis and Learning-Based Maximization,' IEEE Trans. Mob. Comput. , vol. 23, no. 5, pp. 6074-6087, 2024, doi:10.1109/TMC.2023.3315275.
- [15] F. S. Gharehchopogh, S. Ghafouri, M. Namazi et al., 'Advances in Manta Ray Foraging Optimization: A Comprehensive Survey,' J Bionic Eng. , vol. 21, pp. 953-990, 2024, doi:10.1007/s42235-024-00481-y.
- [16] A. D. Pazho, G. A. Noghre, V. Katariya et al., 'VT-Former: An Exploratory Study on Vehicle Trajectory Prediction for Highway Surveillance through Graph Isomorphism and Transformer,' CVPRW. , 2024, doi:10.1109/CVPRW63382.2024.00574.
- [17] M. Wang, L. Zhang, J. Chen et al., 'A Hybrid Trajectory Prediction Framework for Automated Vehicles With Attention Mechanisms,' IEEE Trans. Transp. Electrif. , vol. 10, no. 3, pp. 6178-6194, 2024, doi:10.1109/TTE.2023.3346668.
- [18] C. He, W. Jiang, X. Wang et al., 'Deep Reinforcement Learning and Nash Equilibrium Game-Based Task Offloading Optimization Strategy for the IoV,' IEEE Sens. J. , vol. 25, no. 10, pp. 18384-18393, 2025, doi:10.1109/JSEN.2025.3558228.
- [19] K. Wu, H. Shi, X. Li et al., 'Graph-Based Interaction-Aware Multimodal 2D Vehicle Trajectory Prediction Using Diffusion Graph Convolutional Networks,' IEEE Trans. Intell. Veh. , vol. 9, no. 2, pp. 3630-3643, 2024, doi:10.1109/TIV.2023.3341071.
- [20] V. Mistry, B. Vaidya and H. T. Mouftah, 'Evaluation of LSTM GAN for Trajectory Prediction in Connected and Autonomous Vehicles,' IWCMC. , 2024, doi:10.1109/IWCMC61514.2024.10592580.
- [21] Y. Lu, W. Wang, X. Hu et al., 'Vehicle Trajectory Prediction in Connected Environments via Heterogeneous Context-Aware Graph Convolutional Networks,' IEEE Trans. Intell. Transp. Syst. , vol. 24, no. 8, pp. 8452-8464, 2023, doi:10.1109/TITS.2022.3173944.
- [22] Q. Cui, X. Zhao, W. Ni et al., 'Multi-Agent Deep Reinforcement Learning-Based Interdependent Computing for Mobile Edge ComputingAssisted Robot Teams,' IEEE Trans. Veh. Technol. , vol. 72, no. 5, pp. 6599-6610, 2023, doi:10.1109/TVT.2022.3232806.
- [23] D. Cao, N. Gu, R. S. Sherratt et al., 'Energy-Efficient MultiVehicle Edge Networks: A Joint Optimization Algorithm for Task Splitting Offloading and Resource Allocation,' SmartIoT. , 2023, doi:10.1109/SmartIoT58732.2023.00021.
- [24] Y. Chen, Z. Liu, X. Lu et al., 'Risk-Aware Reinforcement Learning Based Federated Learning Framework for IoV,' WCNC. , 2024, doi:10.1109/WCNC57260.2024.10571032.
- [25] Q. Wu, W. Wang, P. Fan et al., 'URLLC-Awared Resource Allocation for Heterogeneous Vehicular Edge Computing,' IEEE Trans. Veh. Technol. , vol. 73, no. 8, pp. 11789-11805, 2024, doi:10.1109/TVT.2024.3370196.
- [26] Z. Nezami , E. Chaniotakis and E. Pournaras, 'When Computing follows Vehicles: Decentralized Mobility-Aware Resource Allocation for Edge-toCloud Continuum,' IEEE Internet Things J. , vol. 12, no. 13, pp. 2332423340, 2025, doi:10.1109/JIOT.2025.3552504.
- [27] L. Liu, J. Feng, X. Mu et al., 'Asynchronous Deep Reinforcement Learning for Collaborative Task Computing and On-Demand Resource Allocation in Vehicular Edge Computing,' IEEE Trans. Intell. Transp. Syst. , vol. 24, no. 12, pp. 15513-15526, 2023, doi:10.1109/TITS.2023.3249745.
- [28] D. A. Chekired, M. A. Togou, L. Khoukhi, et al., '5G-Slicing-Enabled Scalable SDN Core Network: Toward an Ultra-Low Latency of Autonomous Driving Service,' IEEE J. Sel. Areas Commun. , vol. 37, no. 8, pp. 1769-1782, 2019, doi:10.1109/JSAC.2019.2927065.
- [29] N. Cheng, T. Pamukiu and E. Melike, 'Reinforcement Learning Based Resource Allocation for Network Slices in O-RAN Midhaul,' CCNC. , 2023, doi:10.1109/CCNC51644.2023.10059966.
- [30] M. S. Onim, H. Nyeem, H. Arnob et al., 'Unleashing the power of generative adversarial networks: A novel machine learning approach for vehicle detection and localisation in the dark,' Cognit. Comput. Syst. , vol. 5, no. 3, pp. 169-180, 2023, doi:10.1049/ccs2.12085.
- [31] X. Wang, C. He, W. Jiang et al., 'Generative AI-Based DependencyAware Task Offloading and Resource Allocation for UAV-Assisted IoV,' IEEE Open J. Commun. Soc. , vol. 6, pp. 3932-3949, 2025, doi:10.1109/OJCOMS.2025.3562720.
- [32] K. Fahime and H. Ekram, 'Generative AI for the Optimization of Next-Generation Wireless Networks: Basics, State-of-theArt, and Open Challenges,' IEEE Commun. Surv. Tutorials. , 2024, doi:10.1109/COMST.2025.3535554.
- [33] M. Shatnawi and M. Bani Younes, 'An Enhanced Model for Detecting and Classifying Emergency Vehicles Using a Generative Adversarial Network (GAN),' Vehicles. , vol. 6, no. 5, pp. 1114-1139, 2024, doi:10.3390/vehicles6030053.
- [34] W. Jiang, S. Anton and H. Schotten 'Intelligence Slicing: A Unified Framework to Integrate Artificial Intelligence into 5G Networks,' WMNC. , 2019, doi:10.23919/WMNC.2019.8881402.
- [35] E. Balevi and J. Andrewa 'Wideband Channel Estimation With a Generative Adversarial Network,' IEEE Trans. Wireless Commun. , vol. 20, no. 5, pp. 3049-3060, 2020, doi:10.1109/TWC.2020.3047100.
- [36] C. Zhuan, P. Li, Y. Liu et al., 'Generative AI-Assisted MobileEdge Computation Offloading in Digital-Twin-Enabled IIoT,' IEEE Internet Things J. , vol. 12, no. 10, pp. 13248-13258, 2025, doi:10.1109/JIOT.2025.3547370.
- [37] C. He, W. Jiang, X. Wang et al., 'Generative AI-Enhanced Task Offloading Strategy for the IoV: An RSU-RSU Load-Balancing Perspective,' IEEE Networking Lett. , vol. 7, no. 3, pp. 161-165, 2025, doi:10.1109/LNET.2025.3542094.
- [38] R. Izquierdo, A. Quintanar, D. F. Llorca et al., 'Vehicle trajectory prediction on highways using bird eye view representations and deep learning,' Appl Intell. , vol. 53, pp. 8370-8388, 2022, doi:10.1007/s10489022-03961-y.
- [39] Y. Jiang, B. Zhu, S. Yang et al., 'Vehicle Trajectory Prediction Considering Driver Uncertainty and Vehicle Dynamics Based on Dynamic Bayesian Network,' IEEE Trans. Syst. Man Cybern.: Syst. , vol. 53, no. 2, pp. 689-703, 2022, doi:10.1109/TSMC.2022.3186639.
- [40] Q. Gao, S. Lin and G, Zhu, 'Joint Vehicular and Static Users Multiplexing Transmission With Hierarchical Modulation for Throughput

Maximization in Vehicular Networks,' IEEE Trans. Intell. Transp. Syst. , vol. 21, no. 9, pp. 3835-3847, 2020, doi:10.1109/TITS.2019.2934597.

- [41] Y. Luo, Y. Wang, Y. Lei et al., 'Decentralized User Allocation and Dynamic Service for Multi-UAV-Enabled MEC System,' IEEE Trans. Veh. Technol. , vol. 73, no. 1, pp. 1306-1321, 2024, doi:10.1109/TVT.2023.3308589.

<!-- image -->

Chao He received the B.E. and M.E. degrees from School of Electronic and Information Engineering, Chongqing Three Gorges University, and the Ph.D. degree from School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications, in 2014 and 2017, respectively. Currently, he is a lecturer in the School of Electronic and Information Engineering, Chongqing Three Gorges University. His main research interests are in modern communication technology. He has published more than 10 papers in his research area,

including more than 5 papers in refereed journals.

<!-- image -->

Wenhui Jiang received the B.S. degree in computer science and Technology from Weifang University in 2023, and is currently pursuing for a master's degree in School of Telecommunications, Chongqing Three Gorges University. Her research direction is task offloading for IoV, and she has published 3 articles.

<!-- image -->

<!-- image -->

Xing Wang received the bachelor's degree from the School of Information Engineering, Chongqing Vocational and Technical University of Mechatronics, Chongqing, China, in 2023. She is currently pursuing for a master's degree in the School of Electronic and Information Engineering, Chongqing Three Gorges University. Her research focuses on task offloading in the IoV.

Wanting Wang received the bachelor's degree from the School of Electronic and Information Engineering, Hubei University of Automotive Technology, Hubei, China, in 2023. She is currently studying in School of Electronic and Information Engineering, Chongqing Three Gorges University, Chongqing, China.Her research interest is mainly IoV.

<!-- image -->

<!-- image -->

Hong Na is the Dean of the School of Electric Power Engineering at Yunnan Vocational College of Water Resources and Hydropower, Kunming, China. His research focuses on vehicle-to-grid (V2G) technology, smart grid integration, and the development of practical energy systems for vocational education. He has led several provincial-level research projects and actively promotes the application of intelligent energy technologies in the teaching and training process.

Xin Xie is a Lecturer/Postdoctoral Fellow with the School of Automation, Chongqing University of Posts and Telecommunications, Chongqing, China. He is mainly engaged in the research of Industrial Internet of Things, information age, real-time scheduling, edge computing, vision-assisted millimeterwave communication, and other directions. In recent years, he has presided over a number of scientific research projects. He has published eight academic articles, applied for seven invention patents, and published one textbook.
