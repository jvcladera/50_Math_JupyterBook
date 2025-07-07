## 41 Advanced counting

**Advanced counting, often referred to as combinatorics, is a branch of mathematics concerned with counting, both the number of ways to arrange or select objects, and the properties of these arrangements and selections. It provides powerful tools for solving problems in probability, computer science, and various other fields where discrete structures are involved.**

### Fundamental Principles

*   **The Multiplication Principle:** If there are `m` ways to do one thing and `n` ways to do another, then there are `m × n` ways to do both.
*   **The Addition Principle:** If there are `m` ways to do one thing and `n` ways to do another, and these two things cannot be done at the same time, then there are `m + n` ways to do either.

### Permutations

A permutation is an arrangement of objects in a specific order. The order of selection matters.

*   **Permutations of n objects taken r at a time (P(n, r)):** The number of ways to arrange `r` objects from a set of `n` distinct objects.
    `P(n, r) = n! / (n - r)!`

*   **Permutations with Repetition:** When objects can be repeated.

### Combinations

A combination is a selection of objects where the order of selection does not matter.

*   **Combinations of n objects taken r at a time (C(n, r) or "n choose r"):** The number of ways to choose `r` objects from a set of `n` distinct objects without regard to the order.
    `C(n, r) = n! / (r! * (n - r)!)`

### Other Advanced Counting Techniques

*   **Inclusion-Exclusion Principle:** Used to count the number of elements in the union of multiple sets.
*   **Generating Functions:** Power series used to encode sequences of numbers, often used to solve recurrence relations.
*   **Recurrence Relations:** Equations that define a sequence where each term is a function of preceding terms (e.g., Fibonacci sequence).

### Applications of Combinatorics

Combinatorics has wide-ranging applications:

*   **Probability:** Calculating the likelihood of events in complex scenarios.
*   **Computer Science:** Algorithm analysis, network design, cryptography, data structures.
*   **Statistics:** Sampling techniques, experimental design.
*   **Operations Research:** Optimization problems, scheduling.
*   **Biology:** Analyzing DNA sequences, protein structures.

# the condensed idea

# The art of counting

```python
# Python demo: Calculating Permutations and Combinations

import math

def permutations(n, r):
    if r < 0 or r > n:
        return 0
    return math.factorial(n) // math.factorial(n - r)

def combinations(n, r):
    if r < 0 or r > n:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Example usage:

# Permutations: How many ways to arrange 3 out of 5 distinct items?
n_perm = 5
r_perm = 3
result_perm = permutations(n_perm, r_perm)
print(f"Number of permutations of {n_perm} items taken {r_perm} at a time: {result_perm}")

# Combinations: How many ways to choose 3 out of 5 distinct items?
n_comb = 5
r_comb = 3
result_comb = combinations(n_comb, r_comb)
print(f"Number of combinations of {n_comb} items taken {r_comb} at a time: {result_comb}")

# Another example: Choosing a committee of 4 from 10 people
print(f"\nNumber of ways to choose a committee of 4 from 10 people: {combinations(10, 4)}")

# Another example: Arranging 7 different books on a shelf
print(f"Number of ways to arrange 7 different books on a shelf: {permutations(7, 7)}")
```