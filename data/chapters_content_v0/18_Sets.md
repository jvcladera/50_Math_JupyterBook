## 18 Sets

**Set theory is a fundamental branch of mathematics that deals with collections of objects. These collections, called sets, are ubiquitous in mathematics and provide a foundational language for defining and understanding various mathematical concepts, from numbers to functions and beyond.**

### What is a Set?

A set is a well-defined collection of distinct objects, considered as an object in its own right. The objects within a set are called its elements or members. Sets are typically denoted by capital letters, and their elements are enclosed in curly braces `{}`.

Examples:
*   The set of natural numbers: N = {1, 2, 3, ...}
*   The set of even numbers less than 10: E = {2, 4, 6, 8}
*   The set of primary colors: P = {red, yellow, blue}

### Set Operations

Several fundamental operations can be performed on sets:

*   **Union (∪):** The union of two sets A and B, denoted A ∪ B, is the set of all elements that are in A, or in B, or in both.
    Example: If A = {1, 2, 3} and B = {3, 4, 5}, then A ∪ B = {1, 2, 3, 4, 5}.

*   **Intersection (∩):** The intersection of two sets A and B, denoted A ∩ B, is the set of all elements that are common to both A and B.
    Example: If A = {1, 2, 3} and B = {3, 4, 5}, then A ∩ B = {3}.

*   **Difference (\ or -):** The difference of two sets A and B, denoted A \ B or A - B, is the set of all elements that are in A but not in B.
    Example: If A = {1, 2, 3} and B = {3, 4, 5}, then A - B = {1, 2}.

*   **Complement (A'):** The complement of a set A (relative to a universal set U) is the set of all elements in U that are not in A.

*   **Subset (⊆):** A set A is a subset of set B if every element in A is also in B.
    Example: {1, 2} is a subset of {1, 2, 3}.

### Venn Diagrams

Venn diagrams are visual representations of sets and their relationships. They use overlapping circles to show the commonalities and differences between sets.

### Importance of Set Theory

Set theory, largely developed by Georg Cantor in the late 19th century, revolutionized mathematics by providing a rigorous foundation for almost all mathematical concepts. It is essential in logic, computer science, and various other fields that deal with classification and relationships between data.

# the condensed idea

# Collections of objects

```python
# Python demo: Basic Set Operations

# Define two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union
union_set = set_a.union(set_b)
print(f"Union (A ∪ B): {union_set}")

# Intersection
intersection_set = set_a.intersection(set_b)
print(f"Intersection (A ∩ B): {intersection_set}")

# Difference (A - B)
difference_set_ab = set_a.difference(set_b)
print(f"Difference (A - B): {difference_set_ab}")

# Difference (B - A)
difference_set_ba = set_b.difference(set_a)
print(f"Difference (B - A): {difference_set_ba}")

# Check for subset
set_c = {1, 2}
print(f"Is {set_c} a subset of {set_a}? {set_c.issubset(set_a)}")
print(f"Is {set_a} a subset of {set_c}? {set_a.issubset(set_c)}")
```