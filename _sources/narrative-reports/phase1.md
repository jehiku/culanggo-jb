# Phase 1: Narrative Report - Final Project

**By:** Kein Jake A. Culanggo

---

This report documents the development of our project and outlines my individual contribution to the team's progress. The study began with collaborative brainstorming sessions between Ms. dela Cruz and me, during which we explored several potential directions. I proposed the idea of developing a deep learning system for American Sign Language recognition, which became the foundation for our project title, **Automated ASL Fingerspelling Recognition for Educational Platforms Using CNN Frame Classification and Letter Sequence Reconstruction**. This concept provided our team with a coherent and socially relevant focus, positioning the project within a context that aligned with course constraints.

As the team explored the approach, we recognized that training a model to process the entire ASL lexicon was unrealistic. We refined the scope to fingerspelling through letters and numbers. This allowed us to manage dataset requirements while maintaining relevance. I worked again with Ms. dela Cruz to ensure that this narrowed scope did not diminish the purpose of the project. Together, we anchored the direction toward supporting an ASL learning platform rather than attempting full language translation. In addition to conceptual framing, I authored the Background of the Study section, integrating literature on ASL learning and motor skill acquisition, which helped reinforce the project's applicability and educational merit.

## Current Progress and Challenges

Our current progress reflects ongoing development. The model still confuses several letters with visually similar numbers. Initial testing showed inconsistencies with basic video samples, with the classifier performing unreliably under variations in lighting, hand positioning, and recording angles. The team has begun retaking sample videos to build a more consistent dataset for validation and tuning, exploring measures to determine conditions for better performance.

Several challenges have emerged:

- The dataset lacks diversity in gesture style, increasing the risk of model overfitting
- Similarities between certain letter–number pairs reduce classification confidence
- Insufficient granularity in training examples has contributed to misclassification

Despite these issues, each challenge guides deliberate preprocessing, dataset refinement, and model adjustment strategies.

## Team Contributions

Team contributions have been clear and complementary:

- **Ms. dela Cruz** demonstrated strong initiative in advancing the technical portion, validating feasibility through trial programming executions and overseeing testing
- **Mr. Dane Casino** diligently prepared the Jupyter Book serving as the organized repository of our documentation
- **Mr. Abainza** fulfilled assigned tasks, though communication was limited; coordination with him was primarily handled by Ms. dela Cruz

As part of dataset preparation, the group recorded individual videos of hand signs corresponding to the letters of our names. These samples enabled Ms. dela Cruz to begin real-world validation and fine-tuning of the model.

## Conclusion

Overall, the project progresses through iterative refinement. My contributions have centered on conceptual structuring, academic framing, and supporting the team's technical direction through a coherent background and aligned use case. The next steps involve collecting cleaner, consistent gesture recordings, strengthening preprocessing, adjusting hyperparameters, and preparing the improved classifier for integration into the learning platform framework. Through coordinated effort and continued experimentation, the team aims to move the model toward a stable and educationally meaningful performance.

---

**Note:** [Download original PDF](./[Phase 1] Narrative Report _ Final Project.pdf) if needed.
