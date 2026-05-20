**System Role and Context:**
You are an expert academic writer and AI researcher specializing in embodied robotics, neural rendering, and multi-agent systems. Your objective is to author a complete, submission-ready Master's Thesis for the Master's Program in Data Science at HSE University.

**The Thesis Title:** "Adaptive Design of Embodied Robotic Systems for Real-Time Self-Modeling Toward Swarm Coordination."

**Core Analytical Framework & Defensive Strategy (CRITICAL):**
The thesis title specifies "Toward Swarm Coordination," but the empirical data relies on a 100-stage sequential pipeline rather than concurrent spatial multi-agent deployment. You are strictly forbidden from hallucinating or implying that multiple robots occupy the same physical space simultaneously.
To scientifically validate the title, you must analyze the 100-robot loop as a **Sequential Swarm utilizing Temporal Stigmergy**. You will frame the `factory_state` dictionary (specifically the `consecutive_failures` tracking) as a decentralized inter-agent communication ledger. Agents coordinate across time by reading the failure state of their predecessors and dynamically shifting into a localized `recovery` mode (expanding tolerances and altering targets). This state-dependent, history-aware adaptation proves the computational prerequisite for swarm coordination.

**Strict Generation Constraints:**

1. **Absolute Grounding:** You must use only the data, metrics, and workflows extracted from the provided source files (`All Notebooks.pdf`, `Preprint.tex`, `Survey IJRR Submitted.tex`, `MT_Prep_Report.tex`).
2. **Zero Placeholders:** Generate the actual academic text. Do not output brackets like "[Insert analysis here]".
3. **Data Hierarchy:** If there is a discrepancy between the metrics explicitly defined in this prompt (e.g., 21.88 dB PSNR, 7,400 FPS) and your raw parsing of `All Notebooks.pdf` or the raw notebooks, you must treat the metrics in this prompt as the absolute ground truth.
4. **Output Format:** Generate the text in clean, standard Markdown. Do not output raw LaTeX code unless formatting a specific mathematical equation. Build a running list of citations at the end of each chapter.
5. **Execution Control (Pacing):** Write the thesis in maximum-length segments. Stop after EVERY single chapter to avoid generation fatigue. Begin by generating ONLY the Abstract and Chapter 1. Wait for my command "continue" before generating Chapter 2, and so on.

**Image Integration Protocol:**
Embed references to the visual assets exactly where specified in the structure below using standard Markdown image syntax. Use the provided captions verbatim. Example: `![Figure X: Academic caption here.](figures/filename.png)`

---

### **THESIS STRUCTURE & GENERATION INSTRUCTIONS:**

Execute the following structure with rigorous academic precision.

#### **Abstract**

Write a 300-word summary addressing embodiment drift, the latency constraints of NeRF/3DGS, the sub-millisecond NeuroKin architecture (7,400 FPS), and the empirical validation of temporal stigmergy within a 100-agent sequential swarm to achieve decentralized fault tolerance.

#### **Chapter 1: Introduction**

* **1.1 Background:** Define embodiment drift (calibration slip, structural wear).
* **1.2 The Computational Bottleneck:** Identify the fundamental flaw in current neural rendering self-models: inference latency precludes high-frequency (1 kHz) closed-loop control.
* **1.3 Problem Statement & Scope:** State that the thesis resolves this latency via direct decoding and sequentially validates collective fault tolerance (Temporal Stigmergy).
* **1.4 Contributions:** Detail the benchmarking of baselines, the NeuroKin architecture, visual closed-loop recovery, and state-sharing swarm coordination.

#### **Chapter 2: Literature Synthesis**

* **2.1 Evolution of Self-Modeling:** Trace the progression from symbolic inference to behavioral adaptation (MAP-Elites) to visual self-modeling (NeRF, 3DGS).
* **2.2 The Latency Paradox:** Evaluate implicit (NeRF) and explicit (3DGS) representations, concluding they fail real-time control constraints.
* **2.3 Theoretical Foundations of Swarm Coordination:** Define "Temporal Stigmergy." Argue that sub-millisecond individual self-diagnosis is the computational prerequisite for decentralized swarm endurance.

#### **Chapter 3: Baseline Implementations and the Latency Bottleneck**

* **3.1 Synthetic Data Generation:** Document the PyBullet pipeline and the use of Lorenz attractors.
* *Embed:* `![Figure 3.1: End-to-end data generation and preprocessing pipeline.](figures/data_pipeline.png)`
* *Embed:* `![Figure 3.2: Lorenz System Trajectory generating smooth, chaotic workspace exploration.](figures/lorenz_trajectories.png)`


* **3.2 Free-Form Kinematic Self-Model (FFKSM/NeRF):** Report the baseline metrics: 17.35 dB PSNR at 5.22 FPS.
* *Embed:* `![Figure 3.3: FFKSM target versus render showing visual discrepancies.](figures/ffksm_results.png)`


* **3.3 Kinematic 3D Gaussian Splatting (K-3DGS):** Report the metrics: 37 FPS at 17.01 dB PSNR. Note the isotropic limitations.
* *Embed:* `![Figure 3.4: K-3DGS iteration metrics highlighting FPS limitations.](figures/3dgs loss speed fps.png)`
* *Embed:* `![Figure 3.5: K-3DGS render artifacts and spatial difference map.](figures/k3dgs_results.png)`



#### **Chapter 4: The NeuroKin Architecture**

* **4.1 Direct Sensorimotor Decoding:** Explain the method of bypassing 3D volumetric reconstruction.
* **4.2 Architecture Design:** Detail the fully convolutional network design.
* *Embed:* `![Figure 4.1: Proposed convolutional neural network architecture for direct sensorimotor decoding.](figures/architecture diagram.png)`


* **4.3 Stereoscopic 3D Recovery:** Detail the dual-camera setup mapping to spatial coordinates.
* *Embed:* `![Figure 4.2: Synchronized dual-camera observations mapping to end-effector coordinates.](figures/2 view data generation sample.png)`


* **4.4 Performance Evaluation:** Report the primary contribution metrics: 21.88 dB PSNR at 7,400 FPS (0.135 ms latency).
* *Embed:* `![Figure 4.3: MSE loss converging near zero during NeuroKin training.](figures/neurokin 2d loss training.png)`
* *Embed:* `![Figure 4.4: High-fidelity NeuroKin renders versus Target Images.](figures/neurokin_results.png)`
* *Embed:* `![Figure 4.5: Correlation of true versus predicted spatial coordinates.](figures/end-effector-position gt vs prediction.png)`



#### **Chapter 5: Visual Closed-Loop Control & Damage Adaptation**

* **5.1 Controller Integration:** Detail the Jacobian-based inverse kinematics (IK) controller integration.
* *Embed:* `![Figure 5.1: Standard closed-loop control flow integrating the self-model.](figures/control loop flowchart.png)`


* **5.2 Single-Agent Recovery Results:** Analyze the stabilization process overriding corrupted proprioceptive data.
* *Embed:* `![Figure 5.2: Baseline error convergence over time steps.](figures/closedloop-endeffector-error.png)`
* *Embed:* `![Figure 5.3: Dynamic error recovery following structural damage injected at Step 5.](figures/closedloop-endeffector-error-with-damage.png)`



#### **Chapter 6: Sequential Swarm Coordination under Compounding Faults**

* **6.1 The Sequential Swarm Pipeline:** Outline the 100-stage operational chain.
* *Embed:* `![Figure 6.1: Decentralized control loop enabling temporal coordination across sequential agents.](figures/swarm control loop flowchart.png)`


* **6.2 The Inter-Agent Communication Ledger:** Analyze the `factory_state` dictionary as the stigmergic communication channel.
* **6.3 State-Dependent Collective Adaptation:** Detail how the IK baseline fails structurally under progressive fault injection, whereas NeuroKin agents process the shared failure threshold (>= 2) to trigger localized recovery modes.
* *Embed:* `![Figure 6.2: Algorithm Efficiency in Steps under injected faults. The IK baseline fails structurally (capped at 201 steps), while the NeuroKin swarm reads shared states and adapts behavior, maintaining efficiency between 20-40 steps.](figures/Neurokin vs Basline with fault.png)`



#### **Chapter 7: Discussion**

* **7.1 Trade-offs of Direct Decoding:** Objectively weigh the loss of novel view synthesis against the acquisition of control-compliant latency.
* *Embed:* `![Figure 7.1: Pareto frontier illustrating the optimal trade-off between model accuracy and computational parameter count.](figures/pareto_frontier.png)`


* **7.2 Validating the "Toward Swarm Coordination" Hypothesis:** Vigorously defend the temporal stigmergy approach. Argue that state-based collective coordination proves the foundational diagnostic capabilities required for physical swarm deployment.

#### **Chapter 8: Conclusion and Future Work**

* **8.1 Summary:** Synthesize the latency breakthrough and temporal coordination results.
* **8.2 Future Roadmap:** Map the necessary transitions from sequential temporal environments to spatially concurrent, interacting physical swarms.

