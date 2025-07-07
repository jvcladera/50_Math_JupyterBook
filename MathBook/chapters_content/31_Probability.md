# 31 Probability

**Probability** is the mathematical framework for quantifying **uncertainty**. It provides a rigorous way to measure the likelihood of events occurring, enabling us to make informed decisions in the face of randomness. From games of chance to scientific experiments and financial markets, probability is an indispensable tool for understanding and predicting the world around us.

## Basic Concepts

*   **Experiment:** A process that leads to well-defined outcomes.
*   **Outcome:** A single possible result of an experiment.
*   **Sample Space (S):** The set of all possible outcomes of an experiment.
*   **Event (E):** A subset of the sample space, representing a collection of outcomes.
*   **Probability of an Event (P(E)):** The ratio of the number of favorable outcomes to the total number of possible outcomes, assuming all outcomes are equally likely.
    `P(E) = (Number of favorable outcomes) / (Total number of possible outcomes)`

## Rules of Probability

*   **Probability Range:** The probability of any event is a number between *0* and *1*, inclusive (*0 ≤ P(E) ≤ 1*).
*   **Sum of Probabilities:** The sum of the probabilities of all possible outcomes in a sample space is *1*.
*   **Complement Rule:** The probability that an event does not occur is *1 minus* the probability that it does occur: *P(E') = 1 - P(E)*.
*   **Addition Rule (for mutually exclusive events):** If two events *A* and *B* cannot occur at the same time (**mutually exclusive**), then *P(A or B) = P(A) + P(B)*.
*   **Multiplication Rule (for independent events):** If two events *A* and *B* do not affect each other (**independent**), then *P(A and B) = P(A) × P(B)*.

## Conditional Probability

**Conditional probability** is the probability of an event occurring given that another event has already occurred. It is denoted as *P(A|B)*, the probability of *A* given *B*.

## Applications of Probability

Probability theory has a vast array of applications:

*   **Gambling and Games:** Analyzing odds and strategies.
*   **Insurance:** Calculating risks and premiums.
*   **Quality Control:** Assessing the likelihood of defects in manufacturing.
*   **Medical Diagnosis:** Estimating the probability of a disease given certain symptoms.
*   **Finance:** Modeling stock market behavior and risk assessment.
*   **Science:** Designing experiments, analyzing data, and drawing conclusions.

# the condensed idea

# Quantifying uncertainty

```python
# Python demo: Simulating Coin Flips and Calculating Probability

import random

def simulate_coin_flips(num_flips):
    heads = 0
    tails = 0
    results = []
    for _ in range(num_flips):
        outcome = random.choice(['Heads', 'Tails'])
        results.append(outcome)
        if outcome == 'Heads':
            heads += 1
        else:
            tails += 1
    return heads, tails, results

# Example usage:
num_simulations = 1000
heads_count, tails_count, _ = simulate_coin_flips(num_simulations)

print(f"After {num_simulations} coin flips:")
print(f"Heads: {heads_count} (Probability: {heads_count / num_simulations:.2f})")
print(f"Tails: {tails_count} (Probability: {tails_count / num_simulations:.2f})")

# Python demo: Calculating probability of rolling a specific sum with two dice
def probability_two_dice_sum(target_sum):
    sample_space_size = 6 * 6  # 36 possible outcomes
    favorable_outcomes = 0
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            if (die1 + die2) == target_sum:
                favorable_outcomes += 1
    return favorable_outcomes / sample_space_size

target = 7
prob_target = probability_two_dice_sum(target)
print(f"\nProbability of rolling a sum of {target} with two dice: {prob_target:.3f}")

target = 2
prob_target = probability_two_dice_sum(target)
print(f"Probability of rolling a sum of {target} with two dice: {prob_target:.3f}")
```