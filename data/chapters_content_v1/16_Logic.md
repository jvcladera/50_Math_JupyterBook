# 16 Logic

**Logic** is the foundation of mathematics and reasoning. It provides a systematic way to analyze arguments and determine their validity, moving from premises to conclusions through a series of well-defined rules. From ancient Greek philosophy to modern computer science, logic underpins how we structure thought and build reliable systems.

## Propositions and Truth Values

At its core, logic deals with **propositions**, which are statements that can be either *true* or *false*. For example, "*The sky is blue*" is a proposition. "*Is the sky blue?*" is not, as it's a question.

## Logical Connectives

Propositions can be combined using **logical connectives** to form more complex statements. The most common connectives are:
*   **AND (∧):** True only if both propositions are true.
*   **OR (∨):** True if at least one proposition is true.
*   **NOT (¬):** Reverses the truth value of a proposition.
*   **IMPLIES (→):** If P then Q. False only if P is true and Q is false.
*   **IF AND ONLY IF (↔):** True if both propositions have the same truth value.

## Truth Tables

**Truth tables** are a fundamental tool in logic to determine the truth value of a compound proposition for all possible truth values of its simple propositions.

| P     | Q     | P AND Q | P OR Q | NOT P |
|-------|-------|---------|--------|-------|
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |

## Deductive and Inductive Reasoning

Logic is broadly divided into:
*   **Deductive Reasoning:** Starts with general statements and moves to specific conclusions. If the premises are true, the conclusion must be true.
*   **Inductive Reasoning:** Starts with specific observations and moves to general conclusions. The conclusions are probable, not certain.

## History of Logic

Formal logic originated with **Aristotle** in ancient Greece, who developed **syllogistic logic**. Later, **Stoic philosophers** contributed to **propositional logic**. In the *19th* and *20th centuries*, mathematicians like **George Boole** and **Gottlob Frege** revolutionized logic, transforming it into a symbolic and mathematical discipline, which laid the groundwork for computer science and artificial intelligence.

# the condensed idea

# The rules of thought

```python
# Python demo: Basic Logical Operations

def logical_operations(p, q):
    print(f"P: {p}, Q: {q}")
    print(f"P AND Q: {p and q}")
    print(f"P OR Q: {p or q}")
    print(f"NOT P: {not p}")
    print(f"P IMPLIES Q (P -> Q): {not p or q}") # Equivalent to not P or Q
    print(f"P IFF Q (P <-> Q): {(p and q) or (not p and not q)}") # Equivalent to (P and Q) or (not P and not Q)
    print("---------------------")

# Example usage:
logical_operations(True, True)
logical_operations(True, False)
logical_operations(False, True)
logical_operations(False, False)
```