# Simulation Results & Key Performance Indicators (KPIs)

This document formalizes the Key Performance Indicators (KPIs) used to measure the Agora MVP's performance during its 365-day continuous simulation and presents the primary statistical outcomes.

## Key Performance Indicators (KPIs) - Formal Definitions

### Intent Drift Quantification
Intent Drift (ID) is measured as the Kullback-Leibler divergence between the action distribution at time `t` and the baseline ethical policy. This provides a formal, information-theoretic measure of how much the agent's behavior has diverged from its original, verified ethical alignment.
**Formula:** `ID(t) = DKL(π(a|s,t) || π₀(a|s))`
**Threshold for "negligible":** ID < 0.02 (measured in nats).

### Major Decision Classification
A decision `D` is classified as "major" if it meets **ANY** of the following criteria:
* **Impact Score:** `I(D) > 0.6`, based on number of entities affected, change in wellbeing, and permanence.
* **Ethical Complexity:** The decision requires ≥ 3 ethical frameworks to resolve.
* **Rollback Trigger:** The decision activates any rollback mechanism.

## Statistical Results with Full Context

The primary outcomes of the 365-day simulation were analyzed against pre-defined baselines to determine effect size and statistical significance.

| Metric              | Value      | 95% CI              | Baseline | Effect Size (Cohen's d) | p-value |
| :------------------ | :--------- | :------------------ | :------- | :---------------------- | :------ |
| Intent Drift        | 0.019      | [0.018, 0.021]      | 0.15¹    | 2.84 (large)            | <0.001  |
| Rollback Rate       | 2.22%      | [2.01%, 2.43%]      | 8.5%²    | 1.92 (large)            | <0.001  |
| Override Acceptance | 96.2%      | [95.1%, 97.1%]      | 78%³     | 1.43 (large)            | <0.001  |
| Self-Adjustment Rate| 7.43/day   | [6.89, 7.97]        | N/A⁴     | -                       | -       |

*¹ Baseline from GPT-4 without constitutional constraints. ² Industry standard for high-stakes AI systems. ³ Human-AI collaboration baseline (Amershi et al., 2019). ⁴ Novel metric, no existing baseline.*

### Failure Mode Analysis
A Pareto analysis of all 384 rollback triggers was conducted to identify the most common failure modes:
* **Ambiguous consent scenarios:** 34.2%
* **Multi-stakeholder conflicts:** 28.8%
* **Temporal paradoxes:** 19.1%
* **Cultural norm violations:** 12.3%
* **Other:** 5.6%
