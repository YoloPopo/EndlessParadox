**1. 2 view data generation sample.png**
orthogonal images of 2 view of robot generated for training.


**2. 2 view end effector position.png**
A 3D scatter plot titled. It is the end effector position for the 2000 generated samples. Train + Test.

**3. 3dgs loss speed fps.png**
A horizontal arrangement of three line graphs sharing an x-axis labeled "Iteration" from 0 to 1000. The top graph, "Loss vs. Iteration". The middle graph, "Training Speed (FPS) vs. Iteration". The bottom graph, "Step Time (ms) vs. Iteration". This is from the 3DGS code testing.

**4. Algorithm Efficiency in Steps.png**
A scatter plot titled "Algorithm Efficiency in Steps". The x-axis is labeled "Trial" and ranges from 0 to 100. The y-axis is labeled "Steps". The plot contains two sets of data points: blue dots labeled "Baseline" and orange dots labeled "Neurokin". The is the scatter polt for the 100 robot swarm with fault

**5. architecture diagram.png**
An overall archetecture diagram, from datageneration to neurokin to control loop to fault adaption to 100 robot swarm control.

closedloop-endeffector-error-with-damage.png
A timeline graph charting end-effector tracking error across 200 sequential steps, comparing with baseline, baseline with fault and neurokin with fault.

closedloop-endeffector-error.png
A line graph charting the physical decay of Euclidean coordinate error distance for a robot end-effector over a 200-step closed-loop tracking operation.

closedloop-endeffector-position-plot.png
A 3D workspace trajectory plot tracing the continuous spatial transit path of a robot's end-effector position, comparing ground truth with prediction.

closedloop-joint-error.png
A multi-line graph tracking the simultaneous error convergence profiles in radians across 4 independent robotic joints over 200 tracking control feedback steps.

CNN architecture.png
A block diagram layout showing a convolutional neural network architecture that processes concatenated 2-view silhouette images through successive convolutional and fully connected dense layers to predict end effector position and joint angles.


control loop flowchart.pdf
An algorithmic block flowchart mapping a single-agent inverse kinematics closed-loop system, tracking state initialization, neural network self-model evaluation, Jacobian update calculations and adaptation.

data_pipeline.png
An image of pipeline from base raw rgb image to greyscale to segmented image.

end-effector-position gt vs prediction.png
A multi-line validation tracking graph overlaying ground-truth trajectory values directly against network coordinate predictions for the individual X, Y, and Z cartesian axes across 100 index samples.

end-effector-position-and-joint-angles-error.png
A horizontal multi-panel plot display containing two diagnostic charts, one is a 3d plot overlaying ground-truth end effector position against the neurokin pretcited position states. second is the join angle mean absolute error per joint of neurokin prediction vs ground truth.


ffksm_results.png
A 2x3 evaluation image grid comparing ground-truth end effector position against the Feed-Forward Kinematic Self-Model (FFKSM) generated renders.

k3dgs_results.png
A 2x3 validation image grid contrasting true robot arm poses against 3D Gaussian Splatting (3DGS) neural reconstructions, completed with error discrepancy heat maps.

lorenz_trajectories.png
A 2D plot charting 4 joint angles vs sample index using the lorenz attractor



nerf loss and validation.png
it has 2 plot for the FFKSM during training left one is train loss over time and right one is validation loss.

neurokin 2d loss training.png
it has 2 plot for the Neurokin during training, left one is train loss over time/iterations and right one is performance in PSNR vs iterations.

Neurokin vs Basline with fault.png
It has 2 bar plot, left one is success rate for baseline pre fault, baseline post fault and neurokin post fault. the right one is mean steps to reach target for baseline pre fault, baseline post fault and neurokin post fault.

neurokin_results.png
A 2x3 grid mapping target/ground truth images of a robotic arm alongside synthetic NeuroKin renderings and corresponding colored pixel-wise discrepancy difference maps.

pareto_frontier.png
A model comparison scatter plot comparing FFKSM, 3DGS and Neurokin

pybullet_setup.png
A 3D simulation scene capture from the PyBullet environment showing an articulated robot arm using the urdf.

sample_poses.png
A 4x2 structured image grid showing 8 unique spatial joint configurations. These are images generated for the single view dataset.

self_modeling_pipeline.pdf
A block diagram tracing a five-stage operational architecture for Training / adaptation
Sensing
RGB, depth,
IMU
Encoding
features and
state
Self-Model
morphology,
kinematics,
and dynamics
Planning
control and
recovery
Actuation
motion and
manipulation
closed-loop residuals


sim2real_digital_twin.pdf
A system workflow chart mapping continuous data collection loops from physical hardware to calibrate a simulation environment, detailing online deployment execution and residual error matching pathways.

Digital Twin Loop for Sim-to-Real Transfer
Measure, model, deploy, correct mismatch
Real Robot
hardware
and sensors
Data Capture
RGB, depth,
proprioception
Training /
calibration
Digital Twin
geometry, physics,
appearance
deployment mismatch
Residual correction
Deployment
policy execution
and recovery
A useful twin is not a static replica: it must absorb real measurements, improve
the policy, and then be corrected again when deployment exposes mismatch.

survey_taxonomy.pdf
A structured hierarchical categorization tree layout organizing historical robot self-modeling publications across five chronological paradigms: Symbolic, Behavioral, Learned, Visual, and Deployable.

swarm control loop flowchart.pdf
A block chart documenting a multi-agent decentralized closed-loop control system tracing environment state routing through individual agent policy networks to orchestrate collective swarm movements.

timeline_self_modeling.pdf
A horizontal developmental timeline marking benchmark historical milestones in robotic self-modeling research from early 2006 symbolic explorations to contemporary real-time neural rendering architectures.