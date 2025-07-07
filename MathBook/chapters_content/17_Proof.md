# 17 Proof

**Proof** is the bedrock of mathematics. Unlike other sciences where theories are supported by evidence and observation, mathematical truths are established through rigorous, logical deductions from axioms and previously proven theorems. A mathematical proof provides an **irrefutable demonstration** of a statement's validity.

## Types of Proof

There are several common methods of mathematical proof:

*   **Direct Proof:** Starts with known facts (axioms, definitions, theorems) and logically deduces the conclusion.

*   **Proof by Contradiction (Reductio ad Absurdum):** Assumes the negation of the statement to be proven is true, and then shows that this assumption leads to a logical contradiction. This implies the original statement must be true.

*   **Proof by Induction:** Used to prove statements about natural numbers. It involves two steps:
    1.  **Base Case:** Prove the statement is true for the first number (e.g., n=1).
    2.  **Inductive Step:** Assume the statement is true for an arbitrary natural number k (the inductive hypothesis) and then prove it must also be true for k+1.

*   **Proof by Contrapositive:** Proves a statement "If P, then Q" by proving its contrapositive "If not Q, then not P." These two statements are logically equivalent.

*   **Proof by Exhaustion (Case Analysis):** Divides the problem into a finite number of cases and proves the statement for each case individually. This method is only feasible when the number of cases is small.

## The Importance of Rigor

Mathematical proofs demand absolute rigor. Every step must be logically sound and justified. This strictness ensures that mathematical truths are universal and timeless, independent of empirical observation or personal belief.

## Famous Proofs

Throughout history, many groundbreaking mathematical proofs have shaped our understanding of the world. Examples include **Euclid's proof of the infinitude of prime numbers**, **Pythagoras's theorem**, and **Andrew Wiles's proof of Fermat's Last Theorem**.

# the condensed idea

# The ultimate validation

```python
# Python demo: Proof by Exhaustion (checking if a number is even or odd)

def is_even_or_odd(n):
    # This is a simple demonstration of checking cases
    if n % 2 == 0:
        return f"{n} is an even number."
    else:
        return f"{n} is an odd number."

# Example usage:
print(is_even_or_odd(4))
print(is_even_or_odd(7))
print(is_even_or_odd(0))
print(is_even_or_odd(-3))

# Python demo: Illustrating a simple direct proof concept
# Proof that the sum of two even numbers is even

def sum_of_two_evens(a, b):
    # Let a and b be even numbers.
    # By definition, an even number can be written as 2k for some integer k.
    # So, a = 2k1 and b = 2k2
    # Their sum is a + b = 2k1 + 2k2 = 2(k1 + k2)
    # Since (k1 + k2) is also an integer, 2(k1 + k2) is an even number.
    # This demonstrates that the sum of two even numbers is always even.
    return a + b

# Example usage:
num_even1 = 6
num_even2 = 10
sum_evens = sum_of_two_evens(num_even1, num_even2)
print(f"\nThe sum of {num_even1} and {num_even2} is {sum_evens}. This is an even number.")
```
