# Comprehensive List of Issues in d21.tex Requiring Correction

## CRITICAL ISSUE: FABRICATED ABLATION STUDIES

### Tables That Must Be REMOVED (No Supporting Evidence in Notebooks):

1. **Table 4.7** (lines ~1590-1605): "Ablation study: effect of noise augmentation"
   - Claims comparison of noise σ = 0, 0.005, 0.01, 0.02, 0.05
   - NOTEBOOK REALITY: Only σ=0.01 is used (ANGLE_NOISE_STD = 0.01)
   - No experiments with other noise levels exist
   - ACTION: REMOVE entire table and related claims

2. **Table 4.8** (lines ~1607-1621): "Ablation study: latent dimension"
   - Claims comparison of latent dims = 256, 512, 1024, 2048
   - NOTEBOOK REALITY: Only latent_dim=1024 is used
   - No experiments with other dimensions exist
   - ACTION: REMOVE entire table and related claims

3. **Table 4.9** (lines ~1623-1637): "Ablation study: decoder depth"
   - Claims comparison of 2, 3, 4, 5 transposed layers
   - NOTEBOOK REALITY: Fixed architecture with 4 layers
   - No experiments with different depths exist
   - ACTION: REMOVE entire table and related claims

### Text Claims That Must Be REMOVED or REVISED:

4. **Line 1224**: "The latent dimension of 1024 was chosen through systematic ablation. Lower dimensions (256, 512) lacked capacity... Higher dimensions (2048) overfit..."
   - FALSE: No ablation was performed
   - ACTION: Change to "The latent dimension of 1024 was selected as a design choice balancing representational capacity and computational efficiency."

5. **Section "Ablation Studies"** (starting line ~1588): Entire section must be removed or rewritten
   - ACTION: Replace with "Architecture Design Choices" discussing why specific parameters were chosen

## OTHER POTENTIAL ISSUES TO VERIFY:

### Performance Claims to Verify Against Notebooks:

6. **Line 77**: "7,400 FPS (0.135 ms latency)" - Verify this matches notebook measurements
7. **Line 77**: "21.88 dB PSNR" - Verify against notebook results
8. **Line 77**: "Training completes in 33.5 seconds on a Tesla T4 GPU" - Verify timing
9. **Line 77**: "ResNeuroKin-D... 2,500 FPS (0.400 ms latency)" - Verify

### Robot Experiment Claims:

10. **Line 79-80**: "baseline collapses from 100% pre-fault success to 13% post-fault success... NeuroKin-enabled agents... preserve 88% systemic success"
    - These numbers appear in Notebook 10 (100 Robots Fault Injection)
    - ACTION: Verify these match exactly

### Hardware/Simulation Claims:

11. **Throughout document**: Ensure it's clear all experiments are in SIMULATION (PyBullet)
    - Physical hardware deployment is NOT performed in this thesis
    - This is stated in Acknowledgements (line 98) but should be clearer in methodology

## RECOMMENDED ACTIONS:

1. **IMMEDIATE**: Remove Tables 4.7, 4.8, 4.9 entirely
2. **IMMEDIATE**: Remove or rewrite the "Ablation Studies" section heading and text
3. **IMMEDIATE**: Fix line 1224 claim about "systematic ablation"
4. **VERIFY**: All numerical results (FPS, PSNR, success rates) against notebooks
5. **CLARIFY**: Simulation-only nature throughout methodology sections
6. **ADD**: Limitations section acknowledging that hyperparameters were not systematically optimized

## ETHICAL NOTE:

These fabricated ablation studies constitute academic misconduct if submitted as-is. The actual work (single configuration training) is valid and valuable, but presenting it as systematic ablation studies is dishonest. The thesis should accurately report what was done:
- One NeuroKin model trained with fixed hyperparameters
- Noise augmentation at σ=0.01 only
- Latent dimension 1024 only  
- Fixed decoder architecture only

This is acceptable for a Master's thesis - not every parameter needs ablation. Just be honest about it.
