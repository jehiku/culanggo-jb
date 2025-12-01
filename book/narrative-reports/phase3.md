# Phase 3: Narrative Report - Final Project

**By:** Kein Jake A. Culanggo

---

Phase 3 centers on the systematic evaluation of three convolutional neural network architectures to establish how well standard image-based deep learning models perform on the ASL fingerspelling task when trained from scratch on the Kaggle ASL dataset. The primary goal of this phase is to determine the baseline representational capacity of **VGG16**, **ResNet18**, and **MobileNet V2** under controlled conditions, thereby creating a technical reference point that can later be compared against the practical demands of real-world recognition.

This stage functions as an architectural benchmarking step, identifying how depth, residual connectivity, and lightweight design interact with the properties of a static ASL dataset. Although these experiments technically overlap with model experimentation, they are reported here because their outcomes directly inform the validity of the earlier data collection processes and help clarify whether the training dataset itself supports generalization to real testing conditions.

## Model Performance Results

Although the quantitative results reported for VGG16, ResNet18, and MobileNet V2 provide clear evidence of architectural differences in representational capacity, these outcomes must be interpreted cautiously in relation to the earlier phases of the project.

### Performance Metrics

- **VGG16:** Test accuracy of **0.9722** - demonstrated strong generalization performance
- **ResNet18:** Test accuracy of **0.9643** - demonstrated strong generalization performance  
- **MobileNet V2:** Test accuracy of **0.7024** - exhibited markedly lower accuracy due to its constrained parameterization and lightweight design

These results suggest that high-capacity or residual architectures are more effective at capturing the fine-grained spatial structures required for ASL hand-sign recognition, particularly when trained from scratch on a dataset with limited intra-class variation. The stability of the loss curves for both VGG16 and ResNet18 and their rapid convergence toward low training and validation losses indicate that the dataset was sufficiently structured for these architectures to learn discriminative features in a static, controlled setting.

## Real-World Testing Discrepancy

However, despite these strong numerical outcomes, the transition from dataset-based testing to real-world testing exposed a significant mismatch between model accuracy and practical usability. As stated in Phase 2, when the models were applied to our self-filmed ASL videos, performance degraded sharply:

- Letters were confused with visually similar numbers
- Classification consistency deteriorated
- Predictions became unreliable even under controlled filming conditions

### Important Disclaimer

While this section reports model experimentation trends, the observations obtained during real-world testing were not part of Phase 3's architectural comparison but rather an extension of Phase 2's validation of the suitability and realism of the dataset. These performance issues arose not from model design choices but from our attempt to verify whether the dataset collected earlier truly supported generalization to authentic hand-sign scenarios.

## Analysis of Limitations

The initial success of VGG16 and ResNet18 on the Kaggle dataset, contrasted with their failure to handle our own testing videos, suggests that the limitations of Phase 1 and Phase 2 are now clearer. It is possible that the dataset used for training lacked sufficient variability in:

- Lighting conditions
- Background structure
- Arm visibility
- Skin tone variation
- Finger articulation patterns

This is consistent with our observations: despite re-filming against plain white walls, controlling arm visibility, and standardizing hand position, the models treated the testing samples as out-of-distribution. These mismatches imply that the foundations established in Phases 1 and 2 were partially constrained by the initial dataset choice, and that the strong numerical performance recorded during Phase 3 should not be interpreted as evidence of real-world readiness.

## Team Responsibilities

Throughout this process, responsibilities remained consistent:

- **Dela Cruz** led the implementation, training, and troubleshooting of the CNN architectures
- **Abainza** supported the computational requirements, including access to GPU resources essential for model iteration
- **Casino** supervised the correctness and quality of the testing videos used in evaluation, ensuring that samples adhered to the intended guidelines
- **My contribution:** I analyzed the coherence between the architectural results and the earlier dataset characteristics, documented the performance discrepancies, and helped frame the interpretation of these outcomes in relation to the project's overall goals

## Conclusion

Phase 3 provided valuable insights into the baseline capabilities of standard CNN architectures on the ASL fingerspelling task. While VGG16 and ResNet18 demonstrated strong performance on the static Kaggle dataset, the real-world testing revealed significant challenges that must be addressed through improved dataset diversity and more robust preprocessing strategies in future iterations.

---

**Note:** [Download original PDF](./[Phase 3] Narrative Report _ Final Project.pdf) if needed.
