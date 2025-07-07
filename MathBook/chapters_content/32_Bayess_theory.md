# 32 Bayes’s theory

**Bayes's Theorem** is a fundamental concept in **probability theory** that describes how to update the probability of a hypothesis based on new evidence. It provides a powerful framework for reasoning under uncertainty and is widely used in statistics, machine learning, medical diagnosis, and artificial intelligence.

## Understanding Bayes's Theorem

Bayes's Theorem is expressed as:

`P(H|E) = [P(E|H) * P(H)] / P(E)`

Where:
*   `P(H|E)` is the **posterior probability**: the probability of hypothesis H being true, given the evidence E.
*   `P(E|H)` is the **likelihood**: the probability of observing evidence E, given that hypothesis H is true.
*   `P(H)` is the **prior probability**: the initial probability of hypothesis H being true before observing any evidence.
*   `P(E)` is the **evidence probability**: the probability of observing evidence E, regardless of the hypothesis.

In simpler terms, Bayes's Theorem tells us how to revise our beliefs (prior probability) about an event when we encounter new information (evidence).

## Example: Medical Diagnosis

Consider a medical test for a rare disease. Bayes's Theorem can help us determine the actual probability of having the disease given a positive test result, taking into account the prevalence of the disease and the accuracy of the test.

## Applications

Bayes's Theorem has a wide range of applications:

*   **Spam Filtering:** Classifying emails as spam or not spam based on the words they contain.
*   **Medical Diagnosis:** Updating the probability of a disease based on symptoms and test results.
*   **Machine Learning:** Forming the basis of **Naive Bayes classifiers** and **Bayesian networks**.
*   **Financial Modeling:** Assessing risk and making investment decisions.
*   **Legal Reasoning:** Evaluating evidence in court cases.

## History

Bayes's Theorem is named after **Thomas Bayes**, an *18th-century British statistician* and philosopher. His work was published posthumously in *1763*. **Pierre-Simon Laplace** later independently rediscovered and popularized the theorem.

# the condensed idea

# Updating beliefs with evidence

```python
# Python demo: Bayes's Theorem for Medical Diagnosis

# Scenario:
# - Prevalence of a disease (P(Disease)) = 0.01 (1% of the population has the disease)
# - Test sensitivity (P(Positive | Disease)) = 0.95 (95% of people with the disease test positive)
# - Test specificity (P(Negative | No Disease)) = 0.90 (90% of people without the disease test negative)
#   Therefore, False Positive Rate (P(Positive | No Disease)) = 1 - 0.90 = 0.10

# We want to find P(Disease | Positive) - the probability of having the disease given a positive test result.

# 1. Define probabilities
P_Disease = 0.01
P_NoDisease = 1 - P_Disease # 0.99

P_Positive_given_Disease = 0.95
P_Positive_given_NoDisease = 0.10

# 2. Calculate P(Positive) - the probability of testing positive (evidence probability)
# P(Positive) = P(Positive | Disease) * P(Disease) + P(Positive | No Disease) * P(No Disease)
P_Positive = (P_Positive_given_Disease * P_Disease) + (P_Positive_given_NoDisease * P_NoDisease)

# 3. Apply Bayes's Theorem
# P(Disease | Positive) = [P(Positive | Disease) * P(Disease)] / P(Positive)
P_Disease_given_Positive = (P_Positive_given_Disease * P_Disease) / P_Positive

print(f"Prevalence of Disease: {P_Disease:.2%}")
print(f"Test Sensitivity (P(Positive | Disease)): {P_Positive_given_Disease:.2%}")
print(f"False Positive Rate (P(Positive | No Disease)): {P_Positive_given_NoDisease:.2%}")
print(f"\nProbability of testing positive (P(Positive)): {P_Positive:.4f}")
print(f"Probability of having the disease given a positive test (P(Disease | Positive)): {P_Disease_given_Positive:.2%}")

# This example shows that even with a seemingly accurate test, the probability of actually
# having a rare disease given a positive test can still be relatively low due to the low prior probability.
```
```