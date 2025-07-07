# 51 Glossary

This glossary provides definitions for key mathematical terms and concepts used throughout the book. Understanding these terms is essential for grasping the fundamental ideas presented in each chapter.

*   **Algebra:** A branch of mathematics that uses symbols to represent numbers and quantities in formulas and equations.
*   **Algorithm:** A step-by-step procedure for solving a problem or accomplishing a task.
*   **Calculus:** The mathematical study of change, divided into differential calculus (rates of change) and integral calculus (accumulation).
*   **Chaos Theory:** The study of dynamic systems whose behavior is highly sensitive to initial conditions.
*   **Combinatorics:** The branch of mathematics dealing with combinations and permutations of sets of elements.
*   **Complex Number:** A number that can be expressed in the form a + bi, where a and b are real numbers and i is the imaginary unit, satisfying i² = -1.
*   **Correlation:** A statistical measure that indicates the extent to which two or more variables fluctuate together.
*   **Curve:** A line that is not straight, or a continuous bending line.
*   **Dimension:** The number of independent coordinates needed to specify a point in a space.
*   **Distribution:** In statistics, a function that shows the possible values for a variable and how often they occur.
*   **Euclid's Algorithm:** An efficient method for computing the greatest common divisor (GCD) of two integers.
*   **Fermat's Last Theorem:** States that no three positive integers a, b, and c can satisfy the equation aⁿ + bⁿ = cⁿ for any integer value of n greater than 2.
*   **Fibonacci Numbers:** A sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1 (or 1 and 1).
*   **Fractal:** A complex geometric shape that exhibits self-similarity at different scales.
*   **Game Theory:** The mathematical study of strategic decision-making in situations of conflict and cooperation.
*   **Golden Ratio (Φ):** An irrational number, approximately 1.618, found when the ratio of two quantities is the same as the ratio of their sum to the larger of the two quantities.
*   **Graph Theory:** The study of graphs, which are mathematical structures used to model pairwise relations between objects.
*   **Group:** A set equipped with a binary operation that satisfies closure, associativity, identity, and inverse properties.
*   **Imaginary Number:** A number that, when squared, gives a negative result, typically expressed as a real number multiplied by the imaginary unit i (where i² = -1).
*   **Infinity (∞):** A concept describing something without any limit or end.
*   **Latin Square:** An n × n array filled with n different symbols, each occurring exactly once in each row and each column.
*   **Logic:** The study of reasoning and argumentation, providing rules for valid inference.
*   **Magic Square:** A square grid where the sum of numbers in each row, column, and main diagonals is the same.
*   **Matrices:** Rectangular arrays of numbers used to represent linear transformations and solve systems of equations.
*   **Normal Curve:** A bell-shaped probability distribution that is symmetric around its mean, also known as the Gaussian distribution.
*   **Number Systems:** Methods for representing and manipulating numbers.
*   **Pi (π):** The ratio of a circle's circumference to its diameter, approximately 3.14159.
*   **Prime Number:** A natural number greater than 1 that has no positive divisors other than 1 and itself.
*   **Probability:** The measure of the likelihood that an event will occur.
*   **Proof:** A rigorous, logical argument that establishes the truth of a mathematical statement.
*   **Relativity:** Albert Einstein's theories describing the relationship between space, time, gravity, and the universe.
*   **Riemann Hypothesis:** A conjecture about the distribution of the zeros of the Riemann zeta function, with profound implications for prime numbers.
*   **Set:** A well-defined collection of distinct objects.
*   **Square Root:** A number that, when multiplied by itself, gives the original number.
*   **Topology:** The study of properties of geometric objects that are preserved under continuous deformations.
*   **Travelling Salesperson Problem (TSP):** A classic optimization problem seeking the shortest route visiting a set of cities exactly once.
*   **Zero:** The additive identity, representing nothing or the absence of quantity.

```python
# Python demo: Simple Glossary Lookup

def get_definition(term, glossary):
    return glossary.get(term, "Term not found in glossary.")

# A very small, conceptual glossary
simple_glossary = {
    "Algebra": "A branch of mathematics that uses symbols to represent numbers.",
    "Calculus": "The mathematical study of change.",
    "Prime Number": "A natural number greater than 1 that has no positive divisors other than 1 and itself.",
    "Set": "A well-defined collection of distinct objects."
}

# Example usage:
term_to_lookup = "Prime Number"
definition = get_definition(term_to_lookup, simple_glossary)
print(f"Definition of '{term_to_lookup}': {definition}")

term_to_lookup = "Geometry"
definition = get_definition(term_to_lookup, simple_glossary)
print(f"Definition of '{term_to_lookup}': {definition}")
```