# 33 The birthday problem

The **Birthday Problem**, or **Birthday Paradox**, is a classic **probability puzzle** that demonstrates how counter-intuitive probability can be. It asks: in a randomly selected group of *n* people, what is the probability that at least two people share the same birthday? The surprising answer is that this probability becomes quite high with a relatively small number of people.

## Understanding the Paradox

The paradox lies in the fact that most people underestimate how quickly the probability of a shared birthday increases as the group size grows. Intuitively, one might think you need a very large group, perhaps hundreds of people, to have a good chance of a match. However, the probability of *at least one* shared birthday is much higher than the probability of *your* birthday matching someone else's.

## Calculating the Probability

It's easier to calculate the **complementary probability**: the probability that *no two people* share the same birthday. If we have *n* people, and assuming *365 days* in a year (ignoring leap years):

*   The first person can have any of *365* birthdays.
*   The second person must have a different birthday (*364 options*).
*   The third person must have a different birthday from the first two (*363 options*).
*   And so on.

So, the probability that no two people share a birthday is:

`P(no shared birthday) = (365/365) * (364/365) * (363/365) * ... * ((365 - n + 1)/365)`

The probability of at least one shared birthday is then:

`P(at least one shared birthday) = 1 - P(no shared birthday)`

## Surprising Results

*   With just *23 people*, there's a greater than *50%* chance (approx. *50.7%*) that at least two people share a birthday.
*   With *50 people*, the probability jumps to over *97%*.
*   With *70 people*, the probability is over *99.9%*.

This phenomenon is not a true paradox in the logical sense, but rather a counter-intuitive result that highlights the power of compounding probabilities.

## Applications

The Birthday Problem has practical implications in various fields:

*   **Cryptography:** Understanding the likelihood of collisions in **hash functions** (where different inputs produce the same output).
*   **Computer Science:** Analyzing the performance of algorithms that rely on random assignments.
*   **Statistics:** Illustrating the importance of sample size in detecting patterns.

# the condensed idea

# The surprising power of probability

```python
# Python demo: Calculate the probability for the Birthday Problem

import math

def calculate_birthday_probability(num_people):
    if num_people > 365:
        return 1.0  # Certainty of a shared birthday if more people than days in a year

    # Calculate the probability that NO two people share a birthday
    prob_no_match = 1.0
    for i in range(num_people):
        prob_no_match *= (365 - i) / 365
    
    # The probability of at least one shared birthday is 1 - P(no shared birthday)
    prob_shared_birthday = 1 - prob_no_match
    return prob_shared_birthday

# Example usage:
people_count = 23
prob = calculate_birthday_probability(people_count)
print(f"With {people_count} people, the probability of a shared birthday is: {prob:.4f}")

people_count = 50
prob = calculate_birthday_probability(people_count)
print(f"With {people_count} people, the probability of a shared birthday is: {prob:.4f}")

people_count = 70
prob = calculate_birthday_probability(people_count)
print(f"With {people_count} people, the probability of a shared birthday is: {prob:.4f}")
```