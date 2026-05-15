---
paper_id: "paper-1971"
source_pdf_sha: "ae596471bafdff58cf5641cf2397dc7416cc398805e9e673d00877deeecbcea8"
extraction_quality: medium
extraction_method: pypdf
extraction_flags:
  toc_detected: false
  headings_count: 2
  page_count: 9
  tables_preserved: false
  equations_preserved: false
manually_edited: false
---

# paper-1971 — fulltext
## §unknown-1

LiLM-RDB-SFC: Lightweight Language Model with
Relational Database-Guided DRL for Optimized
SFC Provisioning
Parisa Fard Moshiri 1, Xinyu Zhu 1, Poonam Lohan 1, Burak Kantarci 1, Emil Janulewicz 2,
1University of Ottawa, Ottawa, ON, Canada
2Ciena, 383 Terry F ox Dr , Kanata, ON K2K 2P5, Canada
1{parisa.fard.moshiri, xzhu095, ppoonam, burak.kantarci }@uottawa.ca, 2ejanulew@ciena.com
Abstract—Effective management of Service Function Chains
(SFCs) and optimal Virtual Network Function (VNF) placement
are critical challenges in modern Software-Defined Networking
(SDN) and Network Function Virtualization (NFV) environments.
Although Deep Reinforcement Learning (DRL) is widely adopted
for dynamic network decision-making, its inherent dependency on
structured data and fixed action rules often limits adaptability and
responsiveness, particularly under unpredictable network condi-
tions. This paper introduces LiLM-RDB-SFC, a novel approach
combining Lightweight Language Model (LiLM) with Relational
Database (RDB) to answer network state queries to guide DRL
model for efficient SFC provisioning. Our proposed approach
leverages two LiLMs, Bidirectional and Auto-Regressive Trans-
formers (BART) and the Fine-tuned Language Net T5 (FLAN-T5),
to interpret network data and support diverse query types related
to SFC demands, data center resources, and VNF availability.
Results demonstrate that FLAN-T5 outperforms BART with a
lower test loss (0.00161 compared to 0.00734), higher accuracy
(94.79% compared to 80.2%), and less processing time (2h 2min
compared to 2h 38min). Moreover, when compared to the large
language model SQLCoder, FLAN-T5 has almost same accuracy
while cutting processing time by 96 % (SQLCoder: 54 h 43 min;
FLAN-T5: 2 h 2 min).
Index Terms —SFC provisioning, VNF placement, DRL, Lan-
guage Model, FLAN-T5, BART, Network State Monitoring.
I. I NTRODUCTION
The advent of Software-Defined Networking (SDN) and
Network Function Virtualization (NFV) has altered network
management, allowing for greater flexibility and efficiency.
Service Function Chain (SFC) provisioning involves the se-
quential execution of different virtual network functions (VNF)
to support complex applications such as Cloud Gaming (CG),
Augmented Reality (AR), Video Streaming (VS), Massive IoT
(MIoT), V oice over Internet Protocol (V oIP), and Industry
4.0 (Ind 4.0) [1]. Satisfying these applications through SFC
provisioning presents substantial challenges, such as resource
allocation for VNFs placements, sequential VNF execution, and
meeting end-to-end (E2E) latency constraints.
Deep Reinforcement Learning (DRL) algorithms are fre-
quently employed for optimal VNF placement and SFC provi-
sioning due to their ability to handle complex network environ-
ments, make effective resource allocation decisions, and adapt
to varying service demands [2]. However, DRL techniques
often rely on structured numerical inputs, predetermined state-
action representations, and learned policies, restricting their
adaptability while encountering unexpected network states or
scenarios that significantly differ from their training phase. For
instance, when typical data flows are interrupted by unexpected
network outages or link failures, a DRL model trained on stable
and structured network conditions may struggle to swiftly
reroute traffic or reposition VNFs effectively in such a situation,
maintaining the placement decisions or routing paths learned
from regular operation. This could result in additional outages,
higher latency, and poor network performance [3].
In contrast, integrating Language Models (LMs) can signif-
icantly enhance decision-making by exploiting their abilities
to comprehend unstructured input, reason about context, and
quickly adapt to unexpected network scenarios [4]. LMs can
scan real-time textual descriptions or logs that specify the
nature of failures, allowing for faster contextual evaluation and
dynamic decision-making beyond the established numerical
metrics and structured state-action restrictions inherent in DRL
[5]. Specifically, LMs address this issue by immediately eval-
uating the severity of partial outages or link failures from un-
structured event data, allowing them to quickly inform the issue
and suggest alternative routing paths or ideal VNF relocation
strategies [3]. Thus, combining DRL and LMs enables more
informed, adaptive, and responsive SFC provisioning and VNF
placement decisions, minimizing the adverse effects caused by
unexpected network events.
In our previous work [6], VNF placement using DRL is
addressed, focusing on the optimal allocation of storage and
computational resources required by VNFs. The goal in [6]
is to maximize the efficient handling of SFC requests based
on resource constraints and VNF specifications. Initially, our
approach in [3] involves using a textual dataset to capture
network states information; however, in this work, we transition
to a relational SQL database due to its superior capability
for handling scalability and facilitating rapid reconfigurability
across diverse DCs, varied VNFs and SFC scenarios. After
storing network state information determined by DRL actions
in a relational database, the dataset is fed into a Lightweight
2025 16th International Conference on Network of the Future (NoF)
979-8-3315-8580-8/25/$31.00 ©2025 IEEE 28
2025 16th International Conference on Network of the Future (NoF) | 979-8-3315-8580-8/25/$31.00 ©2025 IEEE | DOI: 10.1109/NoF66640.2025.11223314
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 20:09:03 UTC from IEEE Xplore.  Restrictions apply. 
LM (LiLM) for comprehensive network state monitoring. This
integration offers deep and actionable insights into network
dynamics, allowing greater adaptability and decision-making
precision in DRL-based VNF placement. LiLMs require sub-
stantially fewer computational resources and less advanced
hardware compared to Large LMs (LLM), achieving com-
parable performance while significantly improving inference
speed and operational efficiency [7]. Their suitability for rapid,
cost-effective decision-making makes them highly valuable for
dynamic network optimization tasks [5].
In this paper, we employ both BART and FLAN-T5, two
lightweight yet powerful language models, to translate natural-
language (NL) query to SQL queries. BART is known for its
strong performance in sequence-to-sequence tasks, particularly
text generation and summarization, while FLAN-T5 stands out
for its instruction tuning and generalization capabilities across
diverse NL processing tasks. Both models are assessed across
diverse question types centered on Data Center (DC), VNF, and
SFC configurations. To benchmark the performance of LiLMs,
we also employ a state-of-the-art LLM, SQLCoder, which
is specifically designed for efficient SQL query generation.
The results highlight the LiLMs capability to detect resource
usage patterns, pinpoint performance bottlenecks, and extract
valuable insights for future network enhancements with lower
computational cost compared to the LLM. Consequently, the
system evolves to be more adaptive and intelligent, enabling
proactive handling of SFC provisioning in dynamic environ-
ments.
The main contributions of this paper are as follows:
1) We design and implement a structured relational SQL
database schema that captures essential network state
information, including storage and computational re-
sources of DCs, available idle VNFs, and current SFC
demands. Additionally, a custom dataset comprising
natural-language and SQL query pairs is curated to train
the proposed language models for SQL query generation.
2) Two LiLMs, BART and FLAN-T5, and a LLM, SQL-
Coder, are trained on the custom dataset to translate
diverse natural-language queries into corresponding SQL
queries. These SQL queries are executed over the re-
lational SQL database to retrieve accurate, real-time
network state information.
3) The proposed system demonstrates high scalability and
adaptability to dynamic network conditions. The rela-
tional database schema can be extended by adding new
rows, while the trained LiLMs generalize well to unseen
queries and scenarios without additional training.
Based on our findings, FLAN-T5 outperforms BART with
lower test loss, higher accuracy, higher number of correct
predictions, and less processing time. Compared to SQLCoder,
FLAN-T5 has almost same accuracy but with lower processing
time. The rest of the paper is organized as follows: Section
II provides a literature review, followed by the methodology
in Section III. Section IV discusses performance evaluation.
Section V concludes the paper.
II. R ELATED WORK
In NFV systems, deep learning methodologies have been
investigated to enhance predictive precision for VNF resource
management and service orchestration. Kim et al. [8] present a
sequence modeling framework for VNF resource prediction uti-
lizing LSTM (Long short-term memory) variations and atten-
tion processes. Their strategy enhances prediction accuracy and
convergence speed by utilizing the structural interdependence
inherent in SFCs. Nonetheless, these methodologies generally
depend on supervised training using structured time-series data
and exhibit limited adaptation to dynamic and unstructured
network contexts. Bunyakitanon et al. [9] introduce AREL3P, a
RL framework employing Q-learning to independently position
VNFs based on predictions of E2E performance. In contrast to
supervised learning methods, AREL3P interfaces with NFV or-
chestration platforms and facilitates online learning in dynamic
contexts. Yet, as a tabular RL method, it encounters scalability
constraints and lacks semantic interpretability. Although both
supervised and non-DRL approaches possess distinct advan-
tages, they are hindered by inflexible input representations
and exhibit restricted adaptability in managing unstructured or
dynamic network environments.
DRL has been extensively utilized to tackle dynamic SFC
provisioning and VNF placement. Fu et al. [10] present
a method based on DRL for the embedding of VNFs in
NFV-enabled IoT systems, disaggregating VNFs into granular
functional components to enhance flexibility. Their Deep Q-
Learning approach, augmented with experience replay and
target networks, proficiently tackles traffic fluctuation and
infrastructure heterogeneity. Jaumard et al. [11] integrate DRL
with Graph Neural Networks (GNN) to encapsulate topo-
logical and functional restrictions in SFC routing decisions.
While effective, these models rely on predetermined state-
action representations and provide limited interpretability in
the presence of unstructured or unforeseen network alterations.
Our methodology enhances DRL by incorporating a stream-
lined LM module that facilitates semantic querying of DRL-
generated judgments within a structured SQL framework.
Recent studies have investigated the application of LMs in
network design, forecasting, and decision-making support. Su
et al. [12] utilize pre-trained LLaMA2 models for zero-shot
prediction of VNF resource utilization. By tokenizing numeri-
cal resource measurements and utilizing the sequence modeling
capabilities of LMs, the model attains competitive accuracy
without the need for task-specific fine-tuning. Nonetheless, it
is constrained in organized reasoning and provides minimal
interpretability for decision-making in operational settings.
Nguyen et al. [13] provide NFV-Intent, a framework that uses
in-context learning to convert user intents into JSON-formatted
NFV configurations. Their technology attains excellent trans-
lation accuracy and seamlessly interacts with the complete
NFV lifecycle without necessitating fine-tuning. Li et al. [14]
introduce LM-NOS, utilizing LMs to enhance heuristic policy
code inside a multi-objective optimization framework for SFC
deployment. While these solutions utilize LMs for deployment
2025 16th International Conference on Network of the Future (NoF)
29
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 20:09:03 UTC from IEEE Xplore.  Restrictions apply. 
logic or configuration abstraction, they concentrate on pre-
deployment phases and lack support for real-time semantic
querying of dynamic network states. Conversely, our research
utilizes LiLM (FLAN-T5, BART) and an LLM (SQLCoder) to
convert NL queries into SQL queries about structured network
monitoring data, facilitating transparent and contextually aware
interpretation of judgments generated by DRL.
III. M ETHODOLOGY
In our previous work [6], DRL is utilized to maximize the
number of accepted SFC requests while considering infrastruc-
ture constraints. Given the diverse resource demands, latency
requirements, and unique VNF sequences of different SFC
requests, DRL effectively learned optimal placement policies
tailored to specific network conditions. However, DRL faces
challenges in quickly adapting to unforeseen changes or in-
correct decisions, often necessitating extensive retraining. To
address these limitations, we now incorporate LMs with an
SQL-based dataset for managing SFCs, DCs, and VNFs. The
types of SFCs and their VNF sequences used in this work
are provided in TABLE I. The primary VNFs of these SFCs
can be listed as Network Address Translation (NAT), Intrusion
Detection and Prevention System (IDPS), Video Optimization
Controller (VOC), Firewall (FW), Traffic Monitor (TM), and
W AN Optimizer (WO). The SQL dataset offers structured
data organization, efficient querying capabilities, and robust
relational integrity, enabling quick and precise access to rel-
evant network information. We store network state information
in SQL database following DRL actions at each time-step.
Then, LM is leveraged to convert NL query to SQL query
to monitor the network state, accessing the SQL database.
NL queries are fed into the LM to dynamically investigate
critical network state metrics such as minimum and maximum
E2E latency for specific SFC, the number of idle VNFs, and
available storage and computational power at a particular DC.
By deeply understanding network state information, LMs can
produce valuable inputs/recommendations for DC selection
function, the output of which provides inputs to the DRL model
for optimal VNF placements aligned with service requests
and real-time network status. These recommendations can be
provided either periodically or on demand.
As shown in Fig. 1, comprehensive network state informa-
tion is collected following the actions taken by the DRL model.
This data is then structured into a schema compatible with a
relational SQL database, which is provided in detail in Fig. 2.
The schema is fully dynamic, as individual rows can be updated
on-the-fly, enabling real-time modification of any table entry
without interrupting normal database operations. NL queries
are formulated to retrieve key network metrics, focusing on: (i)
the total number of idle VNFs, (ii) the minimum E2E latency
for a specific SFC type at a given DC, (iii) the maximum E2E
latency for a specific SFC type at a DC, (iv) available storage
at a DC, and (v) available computational capacity at a DC.
Furthermore, queries may involve combinations of two metrics
(e.g., available storage and minimum E2E latency) and three
TABLE I: SFC characteristics [15]
SFC Request VNF Sequence Bandwith
(Mbps)
E2E delay
(msec)
Request
Bundle
CG NAT-FW-VOC
-WO-IDPS
4 80 [40-55]
AR NAT-FW-TM
-VOC-IDPS
100 10 [1-4]
V oIP NAT-FW-TM
-FW-NAT
0.064 100 [100-200]
VS NAT-FW-TM
-VOC-IDPS
4 100 [50-100]
MIoT NAT-FW-IDPS [1-50] 5 [10-15]
Ind 4.0 NAT-FW 70 8 [1-4]
metrics (e.g., minimum and maximum E2E latency along with
the total number of idle VNFs), allowing for more detailed
network state analysis. These NL queries, along with the
generated schema, are used for LM training. The LM is trained
to translate NL queries into accurate SQL queries. When
executed, these SQL queries retrieve relevant information from
relational database, resulting in useful insights for network
monitoring and decision-making processes in response to future
network requests. Using this systematic technique, network
management’s responsiveness, accuracy, and adaptability can
be substantially improved, allowing for more efficient and
proactive resource allocation strategies tailored to dynamic
network conditions.
A. Integration of Language Models
T5, which stands for “Text-To-Text Transfer Transformer,” is
a flexible language model created by Google [16]. It efficiently
treats every natural-language processing task as a text-to-text
challenge [16]. During the pre-training phase, parts of the text
are hidden, and the T5 model learns to fill in the gaps, which
helps it develop a solid grasp of grammar, structure, and mean-
ing. Fine-tuned Language Net T5 (FLAN-T5) is an improved
version of T5 released by Google Research. It builds upon
the original T5 architecture and was trained to follow natural-
language instructions across a wide range of tasks, making
it more effective in generalization and zero-shot scenarios. In
this research, FLAN-T5 is utilized for text-to-SQL generation.
When given a natural-language query along with a description
of the database schema, LiLM learns to create the SQL query
that would provide the answer utilizing SQL database. Its
ability to comprehend both the question’s structure and the
schema’s relational format allows it to generate accurate SQL
statements.
BART (Bidirectional and Auto-Regressive Transformers) is
also utilized as a complementary LiLM. BART, developed
by Facebook AI, is a powerful sequence-to-sequence archi-
tecture that integrates the strengths of BERT (bidirectional
encoder) and GPT (autoregressive decoder) [17]. Similar to T5,
BART is pre-trained with a denoising autoencoder objective
and can be fine-tuned for tasks like text-to-SQL generation.
BART’s adaptability and robustness make it a viable option
for translating natural-language queries into executable SQL
statements in network management. While both methods are
effective for text-to-SQL creation, their relative efficacy may
2025 16th International Conference on Network of the Future (NoF)
30
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 20:09:03 UTC from IEEE Xplore.  Restrictions apply. 
Fig. 1: Framework Design for LiLM-RDB-SFC
Fig. 2: Schema for Relational Database
differ based on the dataset’s features and the specific query
patterns used. These patterns can include, but are not limited to,
queries requiring aggregations or joins, value comparisons, or
filtering based on certain attributes. Other significant linguistic
or structural changes in the query could also affect model
performance.
SQLCoder is an open-source LLM specifically designed
for translating natural language queries into SQL queries with
high fidelity. Developed by Defog.ai [18], SQLCoder builds
upon modern transformer architectures and is fine-tuned on
diverse datasets consisting of complex text-to-SQL datasets
[19]. Its core design adopts a decoder-only architecture, similar
to models like LLaMA and GPT, leveraging multi-head self-
attention and dense feedforward layers to capture intricate
relationships between natural language input and SQL output
[20]. To further enhance its adaptability and reduce fine-
tuning resource requirements, SQLCoder can be updated using
parameter-efficient techniques such as Low-Rank Adaptation
(LoRA), which injects small, trainable rank-decomposition
matrices into each attention and feed-forward block. This
enables efficient domain adaptation without retraining the full
model [3]. To enable the efficient deployment of LLMs such
as SQLCoder on resource-constrained hardware, quantization
techniques are commonly applied. 4-bit and 8-bit quantization
reduce the precision of the model weights from 16 or 32-bit
floating point values to lower-bit integer representations. This
2025 16th International Conference on Network of the Future (NoF)
31
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 20:09:03 UTC from IEEE Xplore.  Restrictions apply. 
TABLE II: Notation Table
Parameter Description Eq.
i Each individual example in a batch (1) - (4)
N The total number of examples in batch (3), (4)
P (i)
s Binary penalty function defined for the i-
th example in the batch for SFC identifiers
(1), (3)
P (i)
v Binary penalty function defined for the i-
th example in the batch for idle VNFs
identifiers
(2), (4)
si Expected SFC identifier for the i-th exam-
ple
(1)
ˆsi Predicted SFC identifier for the i-th exam-
ple
(1)
vi Expected Idle VNFs identifier for the i-th
example
(2)
ˆvi Predicted Idle VNFs identifier for the i-th
example
(2)
PS Average penalty regarding SFC identifiers (3), (6)
PV Average penalty regarding idle VNFs
identifiers
(4), (6)
λce Penalty weight for cross-entropy loss (5), (6)
λs Penalty weight for SFCs mismatch (5), (6)
λv Penalty weight for idle VNFs mismatch (5), (6)
Lce Cross-entropy loss (6)
L Total loss (6)
substantially decreases both the memory footprint and com-
putational requirements, enabling faster inference and lower
power consumption. In practice, 8-bit quantization preserves
much of the model’s original accuracy while offering notable
efficiency gains, making it a standard choice for practical
deployments. 4-bit quantization provides even greater compres-
sion and acceleration, allowing SQLCoder models to fit into de-
vices with limited RAM and further reducing inference latency.
Recent research and open-source libraries, such as bitsandbytes
[21], have demonstrated that SQLCoder and similar LLMs can
operate with minimal performance degradation when quantized
to 4 or 8 bits, making advanced natural language-to-SQL
capabilities accessible on a wide range of hardware platforms.
B. Loss Function
In order to improve the ability of LiLMs to capture the SFC
and idle VNF identifiers correctly, additional penalty terms are
introduced to the loss function. The standard cross-entropy
loss may not explicitly enforce the correct identification of
these important components. By incorporating binary penalty
functions for mismatches in predicting SFC and idle VNFs’
identifiers, we can guide the model to focus on these details.
For a batch of N examples, si is the expected SFC identifier
and ˆsi is the predicted SFC identifier for the i-th example. In
addition, vi is the expected idle VNF identifier and ˆvi is the
predicted idle VNFs identifier for the i-th example. The binary
penalty functions P (i)
s and P (i)
v for SFC and VNF identifier,
respectively, are defined as follows:
TABLE III: Configuration Parameters for LiLMs
Parameter Value
Learning Rate 4e-5
Batch Size 2
Max Length of Tokens 512
Epochs 10
λce 0.1
λv 0.3
λs 0.6
P (i)
s =
(
1 if si ̸= ˆsi
0 if si = ˆsi
(1)
P (i)
v =
(
1 if vi ̸= ˆvi
0 if vi = ˆvi
(2)
The average penalties PS and PV for SFC and VNF identifier,
respectively, are calculated as follows:
PS = 1
N
NX
i=1
P (i)
s (3)
PV = 1
N
NX
i=1
P (i)
v (4)
λce, λs, and λv weights are utilized to emphasize/de-
emphasize the contribution of cross-entropy loss, SFC and VNF
identifier penality components, respectively, thereby controlling
their relative impact subject to:
λce + λs + λv = 1 (5)
The total loss L is then defined as follows:
L = λce Lce + λs PS + λv Pv (6)
Where Lce denotes the standard cross-entropy loss.
During the training phase, the combined loss function directs
the model to minimize the cross-entropy error and accurately
predict the SFC and Idle VNF IDs. The model’s ability to
capture these crucial elements is reinforced by this additional
supervision. Future extensions can include incorporation of dif-
ferent reward functions. All of the parameters in the formulas
are summarized in TABLE II.
IV. P ERFORMANCE ANALYSIS
The experiments were carried out on a system equipped
with NVIDIA A100-PCIE-40GB GPUs, each of which features
40GB of memory. The dataset includes schema, 16568 sets of
natural-language queries, equivalent SQL queries and ground-
truth answers of those queries, which are all manually crafted.
It is divided into three parts: 75% for training, 12.5% for
validation, and 12.5% for testing.
2025 16th International Conference on Network of the Future (NoF)
32
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 20:09:03 UTC from IEEE Xplore.  Restrictions apply. 
TABLE IV: Configuration Parameters for SQLCoder
Parameter Value
Learning Rate 1e-5
Batch Size 2
Max Length of Tokens 1024
r 16
α 32
Epochs 10
(a) Loss for FLAN-T5
(b) Loss for BART
(c) Loss for SQLCoder
Fig. 3: Training, testing, and validation loss for FLAN-T5,
BART, and SQLCoder
Other configuration parameters are summarized in TABLE
III, which are same for both LiLMs, thereby ensuring that
any observed performance differences stem exclusively from
their intrinsic architectural properties. In our experiments,
SQLCoder is deployed with 8-bit quantization for efficient
Fig. 4: Ground truth and correct predictions for LMs
2025 16th International Conference on Network of the Future (NoF)
33
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 20:09:03 UTC from IEEE Xplore.  Restrictions apply. 
TABLE V: Comparison of Metrics for BART, FLAN-T5, and SQLCoder
Metric BART FLAN-T5 SQLCoder
Accuracy (%) 80.2% 94.79% 94.54%
Correct / Total 1661 / 2071 1963 / 2071 1958 / 2071
Processing Time 2 h 38 min 2 h 2 min 54 h 43 min
Perplexity 1.0073 1.0016 1.03
memory usage and inference, and fine-tuned using LoRA. The
LoRA configuration utilizes a rank parameter of r=16, a scaling
factor α = 32, and a dropout rate of 0.05. All of the parameters
are summarized in TABLE IV All of these values in TABLE
III and TABLE IV were carefully chosen after multiple trial
runs.
We employ the BART-based model, which has a maximum
sequence length of 512 tokens. This model consists of 6
encoder and 6 decoder transformer blocks, each containing 768
hidden dimensions, for a total of around 139 million parameters
[17]. Additionally, we utilize the FLAN-T5-base model, which
has a maximum sequence length of 512 tokens. FLAN-T5-
base consists of 12 encoder and 12 decoder transformer blocks,
each with 768 hidden dimensions and 248 million parameters
[22]. We employ the SQLCoder model from Defog, which is
a 15 billion-parameter decoder-only transformer [19], which
is finetuned for our dataset by LoRA. To further reduce its
memory footprint and speed up inference, we quantize the
model to 8-bit precision using the bitsandbytes library, enabling
deployment with minimal impact on accuracy [21].
Given the maximum input sequence limitation of 512 tokens
for both FLAN-T5 and BART, a pre-processing step is utilized
to manage input length efficiently. In this step, based on
specific keywords identified in the user query, only the relevant
portions of the relational database schema are provided to the
LiLM. For instance, if the question includes keywords such
as ”idle VNFs”, the schema related to the idle VNFs table is
included. Similarly, if the question pertains to a specific type of
SFC, only the schema segments relevant to that SFC type are
selected. For combination queries involving multiple aspects,
the corresponding schema parts for all mentioned components
are included. In cases where no specific keywords are detected,
the full schema is presented to the LiLM. This targeted schema
selection strategy helps conserve input space, ensuring critical
information remains within the model’s token limit.
Fig.3a presents the training, validation, and test loss curves
for the FLAN-T5 model over ten epochs. Initially, all losses
start at relatively high values and quickly decreasing during
the initial epochs. Validation and test losses closely mir-
ror the training loss trend, stabilizing swiftly and indicating
the model’s strong generalization capabilities. Comparatively,
Fig.3b depicts the loss curves for the BART model. The initial
losses for BART are higher, but similarly experience rapid
decreases within the first few epochs. By the fourth epoch,
losses stabilize, with training loss showing the lowest values
followed by evaluation and test losses. This rapid and stable
convergence suggests effective training and generalization.
Fig.3c depicts the training and validation loss curves for the
SQLCoder model over ten epochs. The test loss is reported only
at epoch 10 due to GPU memory constraints. Similar to LiLMs,
training and validation loss of SQLCoder starts at high values
and drop during few first epochs before leveling off around
epoch 6. When comparing all three models, all exhibit efficient
convergence and robust generalization. However, FLAN-T5
achieves lower overall loss values.
TABLE V compares the performance of LiLMs and the
LLMs in terms of accuracy, correct predictions, and processing
time. The accuracy indicates the proportion of queries gener-
ated by the models that match exactly with the correct query
word-for-word, thereby retrieving the correct answer from the
relational database. FLAN-T5 achieved an accuracy of 94.79%,
resulting in 1963 correct predictions, and completed its com-
putations significantly faster. Conversely, BART reached an
accuracy of 80.2% with 1661 correct predictions but required
a considerably longer processing time. Moreover, SQLCoder
attains the accuracy of 94.54 % ( 1958 correct answers),
close to FLAN-T5, but with substantial computational cost
of 54 hours and 43 minutes of processing. These results
demonstrate FLAN-T5’s superior performance in both accuracy
and efficiency for our dataset, specifically in generating pre-
cise queries necessary for accurate information retrieval from
the relational database. Additionally, we calculated perplexity,
which measures the average number of choices the model is
confused between when predicting the next word/token, that is,
1.0073 for BART, and 1.03 for SQLCoder, compared to 1.0016
for FLAN-T5, meaning that FLAN-T5 is more confident in its
predictions.
Two illustrative examples of correct and incorrect predic-
tions for the LiLMs and the LLM are presented in Fig. 4
and Fig. 5. In the case of correct predictions, Fig. 4, all
models successfully generate accurate SQL queries, yielding
correct execution results. Conversely, in scenarios with incor-
rect predictions, Fig. 5, FLAN-T5 generates a SQL query
with correct results, albeit identifying an incorrect DC ID.
For the same question, BART not only predicts an incorrect
DC ID but also generates a SQL query that fails to generate
correct answer. In contrast, SQLCoder successfully generates
the correct SQL query. Moreover, as illustrated in Fig. 4 and
Fig. 5, without additional training, these models consistently
produce SQL queries that are syntactically incorrect and cannot
be executed on the database. This underscores the limitations
of their out-of-the-box capabilities and the necessity of fine-
tuning them on domain-specific data. The generated outputs
by SQLCoder are depicted in Fig. 6. As shown in Fig. 6,
SQLCoder sometimes outputs queries containing extra content,
such as repeated natural-language questions, answers, or other
text fragments. While training SQLCoder is computationally
intensive, it nevertheless produces semantically correct SQL
2025 16th International Conference on Network of the Future (NoF)
34
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 20:09:03 UTC from IEEE Xplore.  Restrictions apply. 
Fig. 5: Ground truth and incorrect predictions for LMs
 Fig. 6: Questions and generated SQL queries for SQLCoder
2025 16th International Conference on Network of the Future (NoF)
35
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 20:09:03 UTC from IEEE Xplore.  Restrictions apply. 
statements. By applying a lightweight post-processing step to
remove those extra parts, we can recover the correct SQL query
itself, resulting in an improvement in the SQLCoder accuracy
from 94.54% to 100%.
V. C ONCLUSION
In this paper, we have proposed LiLM-RDB-SFC, a novel
framework integrating a Light Language Model with Rela-
tional Database-guided DRL for optimized SFC provisioning.
Specifically, the network state information, including final VNF
allocations determined by the DRL model, SFC configurations,
and DC information, has been utilized by LMs to generate
precise SQL queries corresponding to natural-language queries.
Querying the current state of SFCs, DCs, and VNFs provides
critical insights into real-time resource utilization and potential
bottlenecks, significantly enhancing future resource allocation
strategies and responsiveness to dynamic network demands.
Our evaluations have shown that the FLAN-T5 model sig-
nificantly outperforms BART by achieving lower loss values
(0.00161 vs 0.00734), higher accuracy (94.79% vs 80.2%),
shorter processing time (2 h 2 min vs 2 h 38 min) with a
higher number of correct query predictions (1963 vs 1661).
Compared to SQLCoder, FLAN-T5 has similar accuracy of
94.79% compared to 94.54% for SQLCoder, but with 96%
lower processing time. In future work, we plan to explore
the use of alternative language models across varying demand
profiles to further enhance the system’s adaptability and per-
formance.

## § Acknowledgment

This work is supported by the Natural Sciences and En-
gineering Research Council of Canada (NSERC) Alliance
Program, MITACS Accelerate Program, and NSERC CREATE
TRA VERSAL program.

## § References

[1] Y . Han, W. Meng, and W. Fan, “SFC Placement and Dynamic Resource
Allocation Based on VNF Performance-Resource Function and Service
Requirement in Cloud-Edge Environment,” Journal of Systems Engineer-
ing and Electronics, vol. 35, no. 4, pp. 906–921, 2024.
[2] R. Mohamed, M. Avgeris, A. Leivadeas, and I. Lambadaris,
“Fragmentation-Aware VNF Placement: A Deep Reinforcement Learning
Approach,” in ICC 2024 - IEEE International Conference on Communi-
cations, 2024, pp. 5257–5262.
[3] P. F. Moshiri, M. A. Onsu, P. Lohan, B. Kantarci, and E. Janulewicz,
“Integrating Language Models for Enhanced Network State Monitoring in
DRL-Based SFC Provisioning,” arXiv preprint arXiv:2502.11298, 2025.
[4] D. T. Hoang, N. V . Huynh, D. N. Nguyen, E. Hossain, and D. Niyato,
DRL Challenges in Wireless Networks, 2023, pp. 213–240.
[5] G. O. Boateng, H. Sami, A. Alagha, H. Elmekki, A. Hammoud, R. Mi-
zouni, A. Mourad, H. Otrok, J. Bentahar, S. Muhaidat et al., “A Survey
on Large Language Models for Communication, Network, and Service
Management: Application Insights, Challenges, and Future Directions,”
arXiv preprint arXiv:2412.19823, 2024.
[6] M. Arda Onsu, P. Lohan, B. Kantarci, E. Janulewicz, and S. Slobodrian,
“Unlocking Reconfigurability for Deep Reinforcement Learning in SFC
Provisioning,” IEEE Networking Letters, vol. 6, no. 3, pp. 193–197, 2024.
[7] M. Hassid, T. Remez, J. Gehring, R. Schwartz, and Y . Adi, “The Larger
the Better? Improved LLM Code-Generation via Budget Reallocation,”
arXiv preprint arXiv:2404.00725, 2024.
[8] H.-G. Kim, S.-Y . Jeong, D.-Y . Lee, H. Choi, J.-H. Yoo, and J. W.-
K. Hong, “A Deep Learning Approach to VNF Resource Prediction
using Correlation between VNFs,” in 2019 IEEE Conference on Network
Softwarization (NetSoft), 2019, pp. 444–449.
[9] M. Bunyakitanon, X. Vasilakos, R. Nejabati, and D. Simeonidou, “End-
to-End Performance-Based Autonomous VNF Placement With Adopted
Reinforcement Learning,” IEEE Transactions on Cognitive Communica-
tions and Networking, vol. 6, no. 2, pp. 534–547, 2020.
[10] X. Fu, F. R. Yu, J. Wang, Q. Qi, and J. Liao, “Dynamic Service
Function Chain Embedding for NFV-Enabled IoT: A Deep Reinforcement
Learning Approach,” IEEE Transactions on Wireless Communications,
vol. 19, no. 1, pp. 507–519, 2020.
[11] B. Jaumard, C. Boudreau, and E. Janulewicz, “Dynamic Service
Function Chaining Provisioning with Reinforcement Learning Graph
Neural Networks,” in Proceedings of the 3rd GNNet Workshop on
Graph Neural Networking Workshop, ser. GNNet ’24. New York, NY ,
USA: Association for Computing Machinery, 2024, p. 53–58. [Online].
Available: https://doi.org/10.1145/3694811.3697824
[12] J. Su, S. Nair, and L. Popokh, “Leveraging Large Language Models for
VNF Resource Forecasting,” in 2024 IEEE 10th International Conference
on Network Softwarization (NetSoft), 2024, pp. 258–262.
[13] N. Van Tu, J.-H. Yoo, and J. W.-K. Hong, “Towards Intent-based Con-
figuration for Network Function Virtualization using In-context Learning
in Large Language Models,” in NOMS 2024-2024 IEEE Network Oper-
ations and Management Symposium, 2024, pp. 1–8.
[14] Y . Li, Q. Zhang, H. Yao, R. Gao, X. Xin, and M. Guizani, “Next-
Gen Service Function Chain Deployment: Combining Multi-Objective
Optimization with AI Large Language Models,” IEEE Network, 2025, to
appear.
[15] J. M. Ziazet, B. Jaumard, H. Duong, P. Khoshabi, and E. Janulewicz,
“A dynamic traffic generator for elastic 5G network slicing,” in 2022
IEEE International Symposium on Measurements & Networking (M&N).
IEEE, 2022, pp. 1–6.
[16] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena,
Y . Zhou, W. Li, and P. J. Liu, “Exploring the Limits of Transfer Learning
with a Unified Text-to-Text Transformer,” CoRR, vol. abs/1910.10683,
2019. [Online]. Available: http://arxiv.org/abs/1910.10683
[17] M. Lewis, Y . Liu, N. Goyal, M. Ghazvininejad, A. Mohamed, O. Levy,
V . Stoyanov, and L. Zettlemoyer, “BART: Denoising Sequence-to-
Sequence Pre-training for Natural Language Generation, Translation,
and Comprehension,” CoRR, vol. abs/1910.13461, 2019. [Online].
Available: http://arxiv.org/abs/1910.13461
[18] D. AI, “Sqlcoder: State-of-the-art llm for natural language to sql,” https:
//github.com/defog-ai/sqlcoder, 2024.
[19] R. Srivastava and W. Aw, “Open-sourcing sqlcoder: a state-of-the-art llm
for sql generation,” https://defog.ai/blog/open-sourcing-sqlcoder, 2023,
accessed: 2025-05-20.
[20] B. Zhang, Y . Ye, G. Du, X. Hu, Z. Li, S. Yang, C. H. Liu, R. Zhao, Z. Li,
and H. Mao, “Benchmarking the text-to-sql capability of large language
models: A comprehensive evaluation,” arXiv preprint arXiv:2403.02951,
2024.
[21] T. Dettmers, “bitsandbytes: 8-bit optimizers and quantization routines,”
https://github.com/bitsandbytes-foundation/bitsandbytes, 2023, accessed:
2025-05-20.
[22] H. W. Chung, L. Hou, S. Longpre, B. Zoph, Y . Tay, W. Fedus, E. Li,
X. Wang, M. Dehghani, Z. Dai et al., “Scaling Instruction-Finetuned
Language Models,” arXiv preprint arXiv:2210.11416, 2022.
2025 16th International Conference on Network of the Future (NoF)
36
Authorized licensed use limited to: Pontificia Universidade Catolica do Rio Grande do Sul (PUC/RS). Downloaded on May 10,2026 at 20:09:03 UTC from IEEE Xplore.  Restrictions apply.
